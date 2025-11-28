import os
from dotenv import load_dotenv
from api.rag.core.VectorStoreIngestor import VectorStoreIngestor
from huggingface_hub import HfApi, login
acess_token = os.getenv("ACESS_TOKEN")
api = HfApi()
login(acess_token)



def main():
    load_dotenv()
    pdf_path = os.getenv("FILE_PATH")

    if not os.path.exists(pdf_path):
        print(f"Erro: PDF não encontrado em {pdf_path}")
        return

    ingestor = VectorStoreIngestor(
        embedding_model_name="sentence-transformers/all-MiniLM-L6-v2",
        persist_dir="api/rag/vector_store/db/chroma",
        collection_name="pdf_documents",
        chunk_size=1000,
        chunk_overlap=200,
        min_clean_length=100
    )

    vectorstore = ingestor.load_vectorstore()
    ###Quantidade de embeddings
    doc_count = vectorstore._collection.count()
    if doc_count == 0:
        print("⚠️ Banco vazio! Ingerindo PDF...")
        vectorstore = ingestor.ingest_pdf(pdf_path)
        doc_count = vectorstore._collection.count()
        print(f"{doc_count} documentos ingeridos!")
    else:
        print(f"ChromaDB carregado com {doc_count} documentos")

if __name__ == "__main__":
    main()



