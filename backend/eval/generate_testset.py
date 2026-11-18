import os
import sys
import types
from pathlib import Path
import langchain_google_vertexai
from ragas.run_config import RunConfig
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.testset.transforms import default_transforms
from langchain_google_genai import ChatGoogleGenerativeAI
from ragas.testset.synthesizers.single_hop.specific import SingleHopSpecificQuerySynthesizer
from ragas.testset import TestsetGenerator

from src import config
from src.core.ingestion import load_or_build_vectorstore


def generate_and_save():
    print("⏳ Đang tải embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={'device': config.DEVICE},
        encode_kwargs={'normalize_embeddings': True}
    )

    print("⏳ Đang tải LLM...")
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL_NAME,
        temperature=0.3
    )

    print("⏳ Đang lấy dữ liệu từ vectorstore...")
    vectorstore = load_or_build_vectorstore(embeddings)
    docs = list(vectorstore.docstore._dict.values())
    print(f"📄 Tổng số chunk: {len(docs)}")

    generator = TestsetGenerator.from_langchain(
        llm=llm,
        embedding_model=embeddings
    )

    test_size = 3
    sample_docs = docs[:25] if len(docs) > 25 else docs
    base_transforms = default_transforms(
        documents=sample_docs,
        llm=generator.llm,
        embedding_model=generator.embedding_model
    )

    filtered_transforms = [
        t for t in base_transforms
        if "Headline" not in t.__class__.__name__
    ]
    run_config = RunConfig(
        max_workers=2,
        timeout=60,
        max_retries=3
    )

    query_distribution = [
        (SingleHopSpecificQuerySynthesizer(llm=generator.llm), 1.0)
    ]
    print(f"🚀 Bắt đầu sinh {test_size} câu hỏi (Dữ liệu dự phòng)...")
    dataset = generator.generate_with_langchain_docs(
        documents=sample_docs,
        testset_size=test_size,
        transforms=filtered_transforms,
        run_config=run_config,
        query_distribution=query_distribution
    )

    current_dir = Path(__file__).resolve().parent

    # [QUAN TRỌNG] Đã đổi tên file đầu ra để KHÔNG ghi đè lên bộ Golden Dataset thủ công của bạn
    output_path = current_dir / "auto_generated_testset.json"

    dataset.to_pandas().to_json(
        str(output_path),
        orient="records",
        force_ascii=False,
        indent=2
    )
    print(f"✅ Đã tạo thành công file dự phòng: {output_path}")


if __name__ == "__main__":
    generate_and_save()