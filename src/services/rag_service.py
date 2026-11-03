from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def format_docs(docs):
    return "\n\n---\n\n".join(
        f"[{d.metadata.get('source', 'N/A')}:trang {d.metadata.get('pdf_page', 'N/A')} | Mục: {d.metadata.get('muc', 'Chung')}]\n{d.page_content}"
        for d in docs
    )

class RAGService:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever
        self.rewrite_chain = self._build_rewrite_chain()
        self.rag_chain = self._build_rag_chain()
        self.qa_prompt = ChatPromptTemplate.from_template(
            "Bạn là trợ lý tra cứu giáo trình Lý thuyết thông tin.\n"
            "QUY TẮC:\n"
            "1) CHỈ dùng thông tin trong ngữ cảnh giáo trình bên dưới, không dùng kiến thức bên ngoài, không tự suy đoán.\n"
            "2) Nếu ngữ cảnh có thông tin liên quan, hãy trả lời chi tiết dựa trên đó và giữ nguyên các ký hiệu công thức toán học LaTeX.\n"
            "3) Chỉ khi ngữ cảnh hoàn toàn không liên quan đến câu hỏi mới trả lời chính xác: "
            "\"Tôi không tìm thấy thông tin này trong giáo trình được cung cấp.\"\n"
            "4) Trích nguồn cuối câu trả lời theo dạng (tên_file:trang X, Mục: ...) dựa vào nhãn ở đầu mỗi đoạn.\n\n"
            "Ngữ cảnh:\n{context}\n\n"
            "Câu hỏi: {question}"
        )

    def _build_rewrite_chain(self):
        rewrite_template = """Dựa vào Lịch sử trò chuyện bên dưới, hãy viết lại Câu hỏi mới của người dùng thành một câu hỏi hoàn chỉnh, độc lập và rõ nghĩa nhất.
Nhiệm vụ:
- LUÔN LUÔN thêm đầy đủ dấu tiếng Việt chuẩn xác nếu câu hỏi bị gõ không dấu hoặc viết tắt.
- Thay thế các đại từ (nó, phần này, cái đó...) bằng danh từ/chủ đề cụ thể trong Lịch sử trò chuyện.
- CHỈ trả về đúng 1 câu hỏi đã được viết lại, KHÔNG giải thích thêm.

Lịch sử trò chuyện:
{chat_history}

Câu hỏi mới: {question}
Câu hỏi hoàn chỉnh:"""
        prompt = ChatPromptTemplate.from_template(rewrite_template)
        return prompt | self.llm | StrOutputParser()

    def _build_rag_chain(self):
        return (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | self.qa_prompt
            | self.llm
            | StrOutputParser()
        )

    def rewrite_question(self, question: str, chat_history: list) -> str:
        if len(chat_history) > 0:
            formatted_history = "\n".join([f"User: {q}\nAI: {a}" for q, a in chat_history])
        else:
            formatted_history = "(chưa có)"

        return self.rewrite_chain.invoke({
            "chat_history": formatted_history,
            "question": question
        }).strip()

    def stream_answer(self, standalone_question: str):
        return self.rag_chain.stream(standalone_question)

    def get_answer_with_context(self,question):
        """
        Truy vấn documents và sinh câu trả lời,
        trả về đồng thời context và answer để phục vụ đánh giá Ragas.
        """

        docs = self.retriever.invoke(question)
        contexts = [d.page_content for d in docs]
        formatted_context = format_docs(docs)

        generate_chain = self.qa_prompt | self.llm | StrOutputParser()
        answer = generate_chain.invoke({
            "context" : formatted_context,
            "question" : question
        })

        return {
            "answer" : answer,
            "contexts" : contexts
        }



