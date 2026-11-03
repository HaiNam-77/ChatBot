from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from src import config
import sys
import langchain_google_vertexai
sys.modules["langchain_community.chat_models.vertexai"] = langchain_google_vertexai

from langchain_google_genai import ChatGoogleGenerativeAI
from src.core.ingestion import load_or_build_vectorstore
from src.core.retrieval import build_retriever_pipeline
from src.services.rag_service import RAGService
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
import json
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)





def run_benchmark():
    eval_dir = Path(__file__).resolve().parent
    dataset_path = eval_dir / "synthetic_testset.json"

    if not dataset_path.exists():
        print(f'Không tìm thấy file {dataset_path}, Bạn cần sinh ra bộ câu hỏi để đánh giá model')
        return

    embeddings = HuggingFaceEmbeddings(
        model_name = config.EMBEDDING_MODEL_NAME,
        model_kwargs = {'device' : 'cuda'},
        encode_kwargs = {'normalize_embeddings': True}
    )

    llm = ChatGoogleGenerativeAI(
        model = config.LLM_MODEL_NAME,
        temperature = 0.0
    )

    vectorstore = load_or_build_vectorstore(embeddings)
    retriever = build_retriever_pipeline(vectorstore)
    rag_service = RAGService(llm=llm, retriever = retriever)

    evaluator_llm = LangchainLLMWrapper(llm)
    evaluator_embeddings = LangchainEmbeddingsWrapper(embeddings)

    with open(dataset_path,"r",encoding = "utf-8") as f:
        synthetic_data = json.load(f)

    user_inputs = []
    retrieved_contexts = []
    generated_responses = []
    reference_answers = []


    for idx,item in enumerate(synthetic_data,start=1):
        question = item.get("user_input") or item.get("question") or ""
        reference = item.get("reference") or item.get("ground_truth") or ""

        if not question:
            continue

        result = rag_service.get_answer_with_context(question)


        user_inputs.append(question)
        retrieved_contexts.append(result["contexts"])
        generated_responses.append(result["answer"])
        reference_answers.append(reference)


    eval_dict = {
        "user_input": user_inputs,
        "retrieved_contexts": retrieved_contexts,
        "response": generated_responses,
        "reference": reference_answers,
    }

    hf_dataset = Dataset.from_dict(eval_dict)

    metrics = [
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,

    ]

    results = evaluate(
        dataset=hf_dataset,
        metrics=metrics,
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
    )

    output_excel = eval_dir/ "ragas_benchmark_report.xlsx"
    results.to_pandas().to_excel(str(output_excel), index=False)

if __name__ == "__main__":
    run_benchmark()

