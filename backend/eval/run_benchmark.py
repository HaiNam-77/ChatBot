from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from src import config
import sys
import time                                                      # THÊM
import langchain_google_vertexai
sys.modules["langchain_community.chat_models.vertexai"] = langchain_google_vertexai

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import os
from src.core.ingestion import load_or_build_vectorstore
from src.core.retrieval import build_retriever_pipeline
from src.services.rag_service import RAGService
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.run_config import RunConfig                           # THÊM
import json
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import Faithfulness, AnswerRelevancy, ContextPrecision, ContextRecall


def run_benchmark():
    eval_dir = Path(__file__).resolve().parent
    dataset_path = eval_dir / "synthetic_testset.json"

    if not dataset_path.exists():
        print(f'Không tìm thấy file {dataset_path}, Bạn cần sinh ra bộ câu hỏi để đánh giá model')
        return

    embeddings = HuggingFaceEmbeddings(
        model_name = config.EMBEDDING_MODEL_NAME,
        model_kwargs = {'device' : config.DEVICE},               # SỬA: dùng config.DEVICE thay cho 'cuda'
        encode_kwargs = {'normalize_embeddings': True}
    )

    # llm = ChatOpenAI(
    #     base_url=os.getenv("ROUTER_BASE_URL", "http://localhost:20128/v1"),
    #     api_key=os.getenv("ROUTER_API_KEY", "none"),
    #     model=os.getenv("JUDGE_MODEL_NAME", "rag-judge-combo"),
    #     temperature=0.0,
    #     max_retries=3
    # )
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL_NAME,
        temperature=0.0
    )
    vectorstore = load_or_build_vectorstore(embeddings)
    retriever = build_retriever_pipeline(vectorstore)
    rag_service = RAGService(llm=llm, retriever = retriever)

    evaluator_llm = LangchainLLMWrapper(llm, bypass_n=True)      # SỬA: thêm bypass_n=True
    evaluator_embeddings = LangchainEmbeddingsWrapper(embeddings)

    with open(dataset_path,"r",encoding = "utf-8") as f:
        synthetic_data = json.load(f)[:2]

    print("Số câu hỏi trong file:", len(synthetic_data))          # THÊM
                             # THÊM: chạy thử 10 câu trước

    user_inputs = []
    retrieved_contexts = []
    generated_responses = []
    reference_answers = []

    for idx,item in enumerate(synthetic_data,start=1):
        question = item.get("user_input") or item.get("question") or ""
        reference = item.get("reference") or item.get("ground_truth") or ""

        if not question:
            continue

        try:
            result = rag_service.get_answer_with_context(question)

            user_inputs.append(question)
            retrieved_contexts.append(result["contexts"])
            generated_responses.append(result["answer"])
            reference_answers.append(reference)
        except Exception as e:
            print(f"Lỗi ở câu {idx}: {e}")
            continue

        time.sleep(5)                                             # THÊM: nghỉ 5 giây giữa các câu

    if len(user_inputs) == 0:                                     # THÊM: chặn lỗi IndexError
        print("Không có câu hỏi hợp lệ. Kiểm tra lại file synthetic_testset.json (có rỗng không? tên khóa là gì?)")
        return

    eval_dict = {
        "user_input": user_inputs,
        "retrieved_contexts": retrieved_contexts,
        "response": generated_responses,
        "reference": reference_answers,
    }

    hf_dataset = Dataset.from_dict(eval_dict)

    metrics = [
        Faithfulness(llm=evaluator_llm),
        AnswerRelevancy(llm=evaluator_llm, embeddings=evaluator_embeddings),
        ContextPrecision(llm=evaluator_llm),
        ContextRecall(llm=evaluator_llm),
    ]

    results = evaluate(
        dataset=hf_dataset,
        metrics=metrics,
        run_config=RunConfig(
            max_workers=1, timeout=120
        ),  # Chạy tuần tự từng job, timeout 120s
        raise_exceptions=True,
    )

    df = results.to_pandas()                                      # SỬA: tách ra để lưu CSV trước
    df.to_csv(str(eval_dir / "ragas_benchmark_report.csv"), index=False, encoding="utf-8-sig")   # THÊM

    print(df.select_dtypes("number").mean())                      # THÊM: điểm trung bình
    print(df.select_dtypes("number").isna().sum())                # THÊM: số lượt chấm bị lỗi (NaN)

    output_excel = eval_dir/ "ragas_benchmark_report.xlsx"
    df.to_excel(str(output_excel), index=False)

if __name__ == "__main__":
    run_benchmark()