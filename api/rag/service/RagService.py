from api.rag.core.VectorStoreIngestor import VectorStoreIngestor
from api.rag.service.AnsweringModel import AnsweringModel


class RAGService:
    def __init__(self):
        self.vectorstore = VectorStoreIngestor().load_vectorstore()
        self.answering_model = AnsweringModel()

    def ask(self, question: str):
        docs = self.vectorstore.similarity_search(question, k=3)
        context = "\n".join(d.page_content for d in docs)

        answer = self.answering_model.answer(question, context)

        print(context)
        print(answer)

        return {
            "question": question,
            "answer": answer,   
            "context_docs": docs
        }
