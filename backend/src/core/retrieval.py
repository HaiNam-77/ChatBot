from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever, ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from src import config
from src.utils.text_utils import bo_dau

def build_retriever_pipeline(vectorstore):

    hybrid_retriever = vectorstore.as_retriever(
        search_kwargs={"k": config.RETRIEVER_K}
    )

    reranker_model = HuggingFaceCrossEncoder(
        model_name=config.RERANKER_MODEL_NAME,
        model_kwargs={'device': config.DEVICE}
    )

    compressor = CrossEncoderReranker(
        model=reranker_model,
        top_n=config.RERANKER_TOP_N
    )

    final_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=hybrid_retriever
    )
    return final_retriever