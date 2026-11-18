import os
from concurrent.futures import ThreadPoolExecutor
from typing import Literal, Optional
from pydantic import BaseModel, Field
from exa_py import Exa

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda


# 1. SCHEMA ĐỊNH TUYẾN & PHÂN RÃ TRUY VẤN (Structured Output)
class QueryPlan(BaseModel):
    standalone_question: str = Field(
        description="Câu hỏi hoàn chỉnh, thêm đầy đủ dấu tiếng Việt và thay thế các đại từ dựa vào lịch sử trò chuyện."
    )
    route_mode: Literal["local_only", "web_only", "both"] = Field(
        description=(
            "Chọn 'local_only' nếu chỉ hỏi lý thuyết/công thức/bài tập trong giáo trình. "
            "Chọn 'web_only' nếu hỏi tin tức/công nghệ mới hoàn toàn ngoài giáo trình. "
            "Chọn 'both' nếu câu hỏi yêu cầu kết hợp/so sánh định nghĩa trong giáo trình với ứng dụng thực tế hiện nay (như 5G, 6G, AI hiện đại)."
        )
    )
    local_sub_query: Optional[str] = Field(
        default=None,
        description="Câu truy vấn con chỉ tập trung vào khái niệm, định lý, công thức để tìm trong giáo trình nội bộ."
    )
    web_sub_query: Optional[str] = Field(
        default=None,
        description="Câu truy vấn con tối ưu để tìm kiếm trên Internet về ứng dụng thực tế, công nghệ mới hiện nay."
    )


def format_docs(docs):
    if not docs:
        return ""
    return "\n\n---\n\n".join(
        f"[GIÁO TRÌNH | {d.metadata.get('source', 'N/A')}:trang {d.metadata.get('pdf_page', 'N/A')} | Mục: {d.metadata.get('muc', 'Chung')}]\n{d.page_content}"
        for d in docs
    )


def format_web_docs(web_results: list) -> str:
    if not web_results:
        return ""
    return "\n\n---\n\n".join(
        f"[WEB | Tiêu đề: {w['title']} | URL: {w['url']}]\n{w['content']}"
        for w in web_results
    )


class RAGService:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever

        # Khởi tạo Exa SDK chỉ cần API Key, không cần URL
        exa_api_key = os.getenv("EXA_API_KEY", "")
        self.exa = Exa(api_key=exa_api_key) if exa_api_key else None

        # Lưu kế hoạch truy vấn gần nhất từ bước rewrite_question để dùng ngay ở bước stream_answer
        self._last_plan: Optional[QueryPlan] = None

        self.rewrite_chain = self._build_rewrite_chain()
        self.qa_prompt = ChatPromptTemplate.from_messages([
            ("system",
             # 1. PERSONA PATTERN
             "Bạn là Trợ lý Học tập AI chuyên sâu môn Lý thuyết thông tin. "
             "Nhiệm vụ của bạn là giải đáp câu hỏi của sinh viên một cách chính xác tuyệt đối dựa trên ngữ cảnh được cung cấp (bao gồm Giáo trình nội bộ và Nguồn Web thực tế nếu có).\n\n"

             # 2. TREE-OF-THOUGHT (ToT) & COGNITIVE ROUTING
             "CHIẾN LƯỢC TƯ DUY & PHÂN NHÁNH (TREE-OF-THOUGHT):\n"
             "Trước khi sinh câu trả lời, hãy âm thầm đánh giá <context> và <question> theo cây quyết định 3 bước sau:\n"
             "- Bước 1 [Đánh giá độ phủ của Ngữ cảnh]:\n"
             "  + Nhánh 1A (Đầy đủ - Đơn nguồn hoặc Đa nguồn): <context> chứa trọn vẹn thông tin trả lời cho <question> (từ [GIÁO TRÌNH], từ [WEB], hoặc kết hợp cả hai) -> Chuyển sang Bước 2.\n"
             "  + Nhánh 1B (Một phần): <context> chỉ trả lời được một vế của <question> -> Chỉ trả lời vế có trong <context>, và ghi chú rõ vế còn lại không có trong dữ liệu truy xuất.\n"
             "  + Nhánh 1C (Không liên quan): <context> hoàn toàn không chứa thông tin cho <question> -> Dừng suy luận và chỉ xuất duy nhất câu: \"Tôi không tìm thấy thông tin này trong giáo trình được cung cấp.\" (Tuyệt đối không xuất phần Nguồn tham khảo).\n"
             "- Bước 2 [Phân loại Ý định Câu hỏi]:\n"
             "  + Nhánh 2A (Chỉ hỏi công thức): Đi thẳng vào phương trình toán học và giải thích ký hiệu đại lượng, bỏ qua phần định nghĩa chữ dài dòng.\n"
             "  + Nhánh 2B (Hỏi khái niệm / tính chất / chứng minh / so sánh thực tế): Tách thành các gạch đầu dòng súc tích accompanied bởi công thức minh họa (nếu có). Nếu câu hỏi kết hợp cả lý thuyết và thực tế, hãy chia rõ phần kiến thức từ Giáo trình và phần ứng dụng thực tế từ Web.\n"
             "- Bước 3 [Rà soát & Chuẩn hóa (Self-Verification)]:\n"
             "  + Khử nhiễu OCR: Tự động sửa các ký hiệu toán học bị vỡ font trong bản quét PDF về chuẩn LaTeX.\n"
             "  + Khử trùng lặp trích dẫn: Chỉ giữ lại các nguồn thực sự dùng để viết câu trả lời, phân biệt rõ nguồn Giáo trình và nguồn Web.\n\n"

             # 3. CONSTRAINTS & TEMPLATE PATTERN
             "QUY TẮC TRÌNH BÀY & ĐỊNH DẠNG (BẮT BUỘC):\n"
             "1) TRUNG THỰC TUYỆT ĐỐI: Chỉ dùng thông tin trong <context>, không tự suy diễn. Không lấy thông tin từ [WEB] để gán mác là định nghĩa của [GIÁO TRÌNH] và ngược lại.\n"
             "2) CẤU TRÚC DÒNG & MARKDOWN:\n"
             "   - Khi nêu nhiều ý, tính chất hoặc công thức: BẮT BUỘC dùng danh sách gạch đầu dòng (`- `) hoặc đánh số (`1.`, `2.`), mỗi ý nằm trên MỘT DÒNG RIÊNG BIỆT.\n"
             "   - In đậm (`**...**`) tên khái niệm, định lý hoặc đại lượng ở đầu mỗi ý.\n"
             "   - Giữa các đoạn văn, danh sách và khối công thức PHẢI cách nhau bằng một dòng trống (`\\n\\n`).\n"
             "3) CHUẨN LATEX TOÁN HỌC:\n"
             "   - Chỉ các công thức đại số chứa ký hiệu toán học (như $H(X)$, $p(x_i)$, $\\sum$, $\\log$) mới dùng LaTeX.\n"
             "   - Ký hiệu/biến số nằm trên cùng dòng chữ: bọc trong `$ ... $` (ví dụ: $H(X)$, $p(x_i)$).\n"
             "   - Phương trình đại số độc lập: tách thành khối riêng có dòng trống phía trên và phía dưới:\n"
             "     $$\n"
             "     <công_thức_LaTeX>\n"
             "     $$\n"
             "   - TUYỆT ĐỐI KHÔNG đưa câu chữ tiếng Việt hoặc công thức bằng lời vào khối $$...$$ (Ví dụ: 'Lượng thông tin = Độ bất định...' phải viết bằng văn bản thường căn đều lề trái, in đậm hoặc in nghiêng, KHÔNG bọc trong $$...$$).\n"
             "4) MẪU TRÍCH DẪN NGUỒN (Chỉ xuất khi Nhánh 1A hoặc 1B được kích hoạt):\n"
             "   > 📖 **Nguồn tham khảo:**\n"
             "   > - *[Giáo trình - Tên_file: trang X, Mục: ...]* (nếu dùng thông tin từ [GIÁO TRÌNH])\n"
             "   > - *[Web - Tiêu đề bài viết](URL)* (nếu dùng thông tin từ [WEB])\n\n"

             # 4. FEW-SHOT PROMPTING PATTERN (1-Shot chuẩn hóa định dạng)
             "VÍ DỤ MẪU (FEW-SHOT EXAMPLE):\n"
             "<example>\n"
             "Input Context:\n"
             "[GIÁO TRÌNH | giao_trinh_LTTT.pdf:trang 15 | Mục: 2.1: Lượng tin riêng] Lượng tin riêng của một biến cố ngẫu nhiên x_i xảy ra với xác suất p(x_i) được tính bằng công thức I(x_i) = -log_a p(x_i). Nếu cơ số a = 2 thì đơn vị là bit (hoặc shannon). Nếu a = e thì đơn vị là nat.\n\n"
             "Input Question:\n"
             "Cho biết công thức tính lượng tin riêng và các đơn vị đo?\n\n"
             "Output chuẩn:\n"
             "**Công thức tính lượng tin riêng** của một biến cố ngẫu nhiên $x_i$ là:\n\n"
             "$$\n"
             "I(x_i) = -\\log_a p(x_i)\n"
             "$$\n\n"
             "Trong đó các thành phần và đơn vị đo được xác định như sau:\n\n"
             "- **$p(x_i)$**: Xác suất xảy ra của biến cố ngẫu nhiên $x_i$.\n"
             "- **Đơn vị bit (hoặc shannon)**: Khi chọn cơ số logarit $a = 2$.\n"
             "- **Đơn vị nat**: Khi chọn cơ số logarit tự nhiên $a = e$.\n\n"
             "> 📖 **Nguồn tham khảo:**\n"
             "> - *[Giáo trình - giao_trinh_LTTT.pdf: trang 15, Mục 2.1: Lượng tin riêng]*\n"
             "</example>"
            ),
            ("human",
             # 5. DELIMITER PATTERN
             "Hãy áp dụng đúng quy trình tư duy và định dạng như ví dụ mẫu để trả lời câu hỏi dưới đây.\n\n"
             "<context>\n{context}\n</context>\n\n"
             "<question>\n{question}\n</question>")
        ])
        self.rag_chain = self._build_rag_chain()

    def _build_rewrite_chain(self):
        rewrite_template = """Dựa vào Lịch sử trò chuyện bên dưới, hãy viết lại Câu hỏi mới của người dùng và lập kế hoạch truy xuất dữ liệu.
Nhiệm vụ:
1. standalone_question: LUÔN LUÔN thêm đầy đủ dấu tiếng Việt chuẩn xác nếu câu hỏi bị gõ không dấu/viết tắt, và thay thế các đại từ (nó, phần này, cái đó...) bằng danh từ cụ thể trong Lịch sử trò chuyện.
2. route_mode:
   - Chọn 'local_only' nếu chỉ hỏi kiến thức lý thuyết, định nghĩa, công thức, bài tập trong môn Lý thuyết thông tin.
   - Chọn 'web_only' nếu hỏi sự kiện, công nghệ ngoài phạm vi giáo trình.
   - Chọn 'both' nếu câu hỏi yêu cầu kết hợp/so sánh lý thuyết trong giáo trình với ứng dụng thực tế hiện nay (ví dụ: trong 5G, 6G, chuẩn nén mới...).
3. local_sub_query & web_sub_query: Tách câu hỏi con tương ứng cho từng nguồn (để tối ưu độ chính xác khi tìm kiếm).

Lịch sử trò chuyện:
{chat_history}

Câu hỏi mới: {question}"""
        prompt = ChatPromptTemplate.from_template(rewrite_template)
        # Sử dụng Structured Output của LangChain để trả về thẳng đối tượng QueryPlan
        return prompt | self.llm.with_structured_output(QueryPlan)

    def _search_exa(self, query: str, num_results: int = 3) -> list:
        """Gọi Exa SDK tìm kiếm web và trích xuất highlights."""
        if not self.exa or not query:
            return []
        try:
            res = self.exa.search_and_contents(
                query,
                type="auto",
                num_results=num_results,
                highlights={"num_sentences": 4, "highlights_per_url": 2}
            )
            web_docs = []
            for item in res.results:
                content = "\n".join(item.highlights) if getattr(item, "highlights", None) else (item.text or "")
                if content.strip():
                    web_docs.append({
                        "title": item.title or "Tài liệu Web",
                        "url": item.url or "",
                        "content": content.strip()
                    })
            return web_docs
        except Exception as e:
            print(f"[Exa Search Warning] Lỗi khi tìm kiếm web: {e}")
            return []

    def _retrieve_hybrid_context(self, question: str) -> str:
        """Điều phối lấy dữ liệu từ Giáo trình, Web hoặc chạy song song cả hai."""
        plan = self._last_plan
        # Nếu gọi trực tiếp không qua rewrite_question (hoặc khác câu hỏi), tự động tạo plan mới
        if not plan or plan.standalone_question != question:
            plan = self.rewrite_chain.invoke({"chat_history": "(chưa có)", "question": question})

        mode = plan.route_mode
        local_q = plan.local_sub_query or question
        web_q = plan.web_sub_query or question

        local_docs, web_docs = [], []

        if mode == "local_only":
            local_docs = self.retriever.invoke(local_q)
        elif mode == "web_only":
            web_docs = self._search_exa(web_q)
        else:  # mode == "both": Chạy song song cả 2 nguồn bằng ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=2) as executor:
                future_local = executor.submit(self.retriever.invoke, local_q)
                future_web = executor.submit(self._search_exa, web_q)
                local_docs = future_local.result()
                web_docs = future_web.result()

        parts = []
        if local_docs:
            parts.append("### DỮ LIỆU TỪ GIÁO TRÌNH NỘI BỘ:\n" + format_docs(local_docs))
        if web_docs:
            parts.append("### DỮ LIỆU THỰC TẾ TỪ INTERNET (EXA WEB SEARCH):\n" + format_web_docs(web_docs))

        return "\n\n====================\n\n".join(parts)

    def _build_rag_chain(self):
        return (
            {
                "context": RunnableLambda(self._retrieve_hybrid_context),
                "question": RunnablePassthrough()
            }
            | self.qa_prompt
            | self.llm
            | StrOutputParser()
        )

    def rewrite_question(self, question: str, chat_history: list) -> str:
        if len(chat_history) > 0:
            formatted_history = "\n".join([f"User: {q}\nAI: {a}" for q, a in chat_history])
        else:
            formatted_history = "(chưa có)"

        # Chỉ 1 lần gọi LLM: vừa viết lại câu hỏi, vừa lên kế hoạch tìm kiếm (lưu vào self._last_plan)
        plan: QueryPlan = self.rewrite_chain.invoke({
            "chat_history": formatted_history,
            "question": question
        })
        self._last_plan = plan
        return plan.standalone_question.strip()

    def stream_answer(self, standalone_question: str):
        return self.rag_chain.stream(standalone_question)

    def get_answer_with_context(self, question: str):
        """
        Giữ nguyên hành vi cho bộ đánh giá Benchmark nội bộ.
        """
        docs = self.retriever.invoke(question)
        contexts = [d.page_content for d in docs]
        formatted_context = format_docs(docs)

        generate_chain = self.qa_prompt | self.llm | StrOutputParser()
        answer = generate_chain.invoke({
            "context": formatted_context,
            "question": question
        })

        return {
            "answer": answer,
            "contexts": contexts
        }