from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.models import QuestionRequest, QuestionResponse, ContextDocument
from api.rag.service.RagService import RAGService

app = FastAPI(
    title="PPChat RAG API",
    description="API to query documents using RAG (Retrieval-Augmented Generation)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_service = None

@app.on_event("startup")
async def startup_event():
    global rag_service
    try:
        rag_service = RAGService()
        print("RAG Service initialized successfully")
    except Exception as e:
        print(f"Error initializing RAG Service: {e}")

@app.get("/")
def root():
    return {
        "message": "PPChat RAG API",
        "status": "online",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "ask": "/ask (POST)"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "rag_service": "initialized" if rag_service else "not initialized"
    }

@app.post("/ask", response_model=QuestionResponse)
def ask(request: QuestionRequest):
    if not rag_service:
        raise HTTPException(status_code=503, detail="RAG service not initialized")

    try:
        result = rag_service.ask(request.question)

        context_docs = [
            ContextDocument(
                content=doc.page_content,
                metadata=doc.metadata
            )
            for doc in result["context_docs"]
        ]

        context_text = "\n\n---\n\n".join([
            f"[Page {doc.metadata.get('page', 'N/A')}]\n{doc.page_content}"
            for doc in result["context_docs"]
        ])

        return QuestionResponse(
            question=result["question"],
            answer=result["answer"],
            context=context_text,
            context_docs=context_docs
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
