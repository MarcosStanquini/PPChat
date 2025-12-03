from api.rag.core.VectorStoreIngestor import VectorStoreIngestor
from api.rag.service.AnsweringModel import AnsweringModel
from api.config import settings


class RAGService:
    def __init__(self):
        self.ingestor = VectorStoreIngestor(
            persist_dir=settings.VECTOR_STORE_PATH,
            embedding_model_name=settings.EMBEDDING_MODEL,
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )
        self.vectorstore = self.ingestor.load_vectorstore()
        self.answering_model = AnsweringModel(
            model_id=settings.BEDROCK_MODEL_ID,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS,
            aws_region=settings.AWS_REGION
        )

    def ask(self, question: str):
        docs = self.vectorstore.similarity_search(question, k=3)

        context = "\n\n---\n\n".join([
            f"[Página {doc.metadata.get('page')}]\n{doc.page_content}"
            for doc in docs
        ])

        answer = self.answering_model.answer(question, context)

        print(context)
        print(answer)

        return {
            "question": question,
            "answer": answer,
            "context_docs": docs
        }
