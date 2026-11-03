
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pprint import pprint
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

loader = DirectoryLoader(
    path ="../data",
    glob = "**/*.pdf",
    loader_cls = PyMuPDFLoader,
    show_progress = True,
    use_multithreading = True
)

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\\n",
    "\n---+\\n",
    "\n___+\\n",
    "\n\n",
    "\n",
    " ",
    "",
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    add_start_index = True,
    strip_whitespace = True,
    separators = MARKDOWN_SEPARATORS
)


embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={'device': 'cpu'}, # Ép mô hình chạy trên GPU NVIDIA để tăng tốc độ
    encode_kwargs={'normalize_embeddings': True}
)


docs = loader.load()
chunk = text_splitter.split_documents(docs)




vectorstore = FAISS.from_documents(
    documents = chunk,
    embedding = embeddings,
    distance_strategy = DistanceStrategy.COSINE

)

retriever = vectorstore.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k":5,}
)

template = (
    "Bạn là trợ lý tra cứu thông tin từ tài liệu nội bộ.\n"
    "QUY TẮC:\n"
    "1) CHỈ dùng thông tin trong ngữ cảnh bên dưới, không dùng kiến thức bên ngoài, không suy đoán.\n"
    "2) Nếu ngữ cảnh có thông tin liên quan (trực tiếp hoặc gián tiếp), hãy trả lời dựa trên đó. "
    "Nếu câu hỏi rộng hơn hoặc hơi khác so với nội dung tài liệu "
    "(ví dụ hỏi về \"trí tuệ nhân tạo\" nhưng tài liệu nói về \"trí tuệ nhân tạo sinh\"), "
    "hãy nói rõ tài liệu đề cập đến điều gì và trả lời trong phạm vi đó.\n"
    "3) Chỉ khi ngữ cảnh hoàn toàn không liên quan đến câu hỏi mới trả lời chính xác: "
    "\"Tôi không tìm thấy thông tin này trong tài liệu được cung cấp.\"\n"
    "4) Trích nguồn theo dạng (tên_file:trang) dựa vào nhãn [tên_file:trang] của từng đoạn.\n\n"
    "Ngữ cảnh:\n{context}\n\n"
    "Câu hỏi: {question}"
)


prompt = ChatPromptTemplate.from_template(template)

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature = 0.5
)



rag_chain = (
    {"context":retriever, "question": RunnablePassthrough()}
    |prompt
    |llm
    |StrOutputParser()
)


while True:

    question = input("Question: ")
    if question == "thoát":
        break

    answer = rag_chain.invoke(question)
    print(answer)


