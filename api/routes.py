from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag.service.RagService import RAGService


app = FastAPI(
    title="PPChat RAG API",
    description="API para consultar documentos usando RAG (Retrieval-Augmented Generation)",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Qual é o conteúdo do documento?"
            }
        }
        

@app.get("/")
def root():
    """Rota raiz - informações da API"""
    return {
        "message": "PPChat RAG API",
        "status": "online",
        "endpoints": {
            "docs": "/docs",
            "ask": "/ask (POST)"
        }
    }

@app.get("/health")
def health_check():
    """Verifica se a API está funcionando"""
    return {"status": "healthy"}

@app.post("/ask")
def ask(request: QueryRequest):
    try:
        rag = RAGService()
        response = rag.ask(request.query)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))