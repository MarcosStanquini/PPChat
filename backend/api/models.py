from pydantic import BaseModel, Field
from typing import List, Dict, Any

class QuestionRequest(BaseModel):
    question: str = Field(..., description="The question to ask the RAG system", min_length=1)

class DocumentMetadata(BaseModel):
    page: int
    total_pages: int
    chunk_method: str
    char_count: int
    source: str

class ContextDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]

class QuestionResponse(BaseModel):
    question: str
    answer: str
    context: str
    context_docs: List[ContextDocument]
