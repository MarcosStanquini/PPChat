from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.response import responseLLm


app = FastAPI(
    title="PPChat RAG API",
    description="API para consultar documentos usando RAG (Retrieval-Augmented Generation)",
    version="1.0.0"
)

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
    return {"status": "healthy"}

@app.post("/ask")
def ask(request):
    try:
        answer = responseLLm(request)
        return answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))