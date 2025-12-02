import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from api.rag.core.PdfProcessor import PdfProcessor

class VectorStoreIngestor:
    def __init__(
        self,
        embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        persist_dir: str = "api/rag/vector_store/db/chroma",
        collection_name: str = "pdf_documents",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        min_clean_length: int = 100
    ):
        self.embedding_model_name = embedding_model_name
        self.persist_dir = persist_dir
        self.collection_name = collection_name

        self.pdf_processor = PdfProcessor(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            min_clean_length=min_clean_length
        )

        self.embedding_function = HuggingFaceEmbeddings(
            model_name=embedding_model_name
        )

        os.makedirs(persist_dir, exist_ok=True)
        
    def ingest_pdf(self, pdf_path: str):
        print(f"Carregando: {pdf_path}")
        
        chunks = self.pdf_processor.process_pdf(pdf_path)
        print(f"Total de chunks gerados: {len(chunks)}")
        vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embedding_function,
            persist_directory=self.persist_dir
)
        print("Armazenando chunks no ChromaDB")
        vectorstore.add_documents(chunks)
        
        print(f"Ingestão concluída! Dados persistidos em: {self.persist_dir}")
        return vectorstore
    
    def load_vectorstore(self):
        return Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embedding_function,
            persist_directory=self.persist_dir
        )
