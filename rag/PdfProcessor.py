from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
import os

class PdfProcessor:
    def __init__(self, chunk_size=100, chunk_overlap=20, min_clean_length=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap 
        self.min_clean_length = min_clean_length
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=[" "]
        )

    def process_pdf(self, pdf_path:str) -> List[Document]:
        loader = PyMuPDFLoader(pdf_path)
        pages=loader.load()
        processed_chunks = []

        for page_num, page in enumerate(pages):
            cleaned_text = self._clean_text(page.page_content)
            if len(cleaned_text) < self.min_clean_length:
                continue

            metadata = {
                **page.metadata,
                "page": page_num + 1,
                "total_pages": len(pages),
                "chunk_method": "smart_pdf_processor",
                "char_count": len(cleaned_text)
            }


            chunks = self.text_splitter.create_documents(
                texts = [cleaned_text],
                metadatas = [metadata]
            )

            processed_chunks.extend(chunks)
        return processed_chunks
        
    def _clean_text(self, text: str) -> str:
        text = " ".join(text.split())
        text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
        return text



load_dotenv()
file_path = os.getenv("FILE_PATH")
print(f"Carregando PDF de: {file_path}")

processor = PdfProcessor(
    chunk_size=500,
    chunk_overlap=50,
    min_clean_length=50
)

chunks = processor.process_pdf(file_path)

print(f"Total de chunks gerados: {len(chunks)}")

for c in chunks[:3]: 
    print("---")
    print("Conteúdo:", c.page_content)
    print("Metadata:", c.metadata)
