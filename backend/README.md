# PPChat - RAG-Powered Document Q&A System

A modern Question & Answer system powered by Retrieval-Augmented Generation (RAG) technology. Ask questions about your documents and get intelligent, context-aware answers.

## Features

- **Smart Document Processing**: Automatically processes PDF documents and creates searchable embeddings
- **RAG-Powered Answers**: Uses retrieval-augmented generation to provide accurate, context-based responses
- **Modern UI**: Clean, responsive React + TypeScript frontend
- **Source Context**: View the source documents and pages used to generate each answer
- **Real-time Health Monitoring**: Check backend service status at a glance

## Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **LangChain**: Framework for LLM applications
- **ChromaDB**: Vector database for document embeddings
- **HuggingFace**: Embedding models and LLM inference
- **Python 3.13+**

### Frontend
- **React 18**: Modern UI framework
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool and dev server
- **CSS3**: Custom styling with animations

## Prerequisites

1. **Python 3.13+**: Install via [uv](https://docs.astral.sh/uv/)
   ```bash
   uv python install 3.13
   ```

2. **Node.js 18+**: Download from [nodejs.org](https://nodejs.org/)

3. **PDF Documents**: Place your PDF files in `api/rag/data/` directory

## Installation & Setup

### Backend Setup

1. **Navigate to project root**:
   ```bash
   cd PPChat
   ```

2. **Install Python dependencies**:
   ```bash
   uv sync
   ```

3. **Configure environment variables** (optional):
   ```bash
   cp .env-example .env
   ```

   Edit `.env` to customize settings:
   ```env
   VECTOR_STORE_PATH=api/rag/vector_store/db/chroma
   EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
   LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct
   LLM_TEMPERATURE=0.3
   LLM_MAX_TOKENS=600
   CHUNK_SIZE=1000
   CHUNK_OVERLAP=200
   ```

4. **Ingest PDF documents**:
   ```bash
   uv run python api/rag/scripts/ingest.py
   ```

5. **Start the backend server**:
   ```bash
   uv run python main.py
   ```

   The API will be available at `http://localhost:8000`
   - Swagger docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/health`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure API URL** (optional):
   Edit `frontend/.env` if your backend runs on a different port:
   ```env
   VITE_API_URL=http://localhost:8000
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## Usage

1. **Ingest Documents**: Place PDF files in `api/rag/data/` and run the ingestion script
2. **Start Backend**: Run `uv run python main.py` from the project root
3. **Start Frontend**: Run `npm run dev` from the `frontend/` directory
4. **Ask Questions**: Open the frontend in your browser and start asking questions!
5. **View Sources**: Click "View Source Context" on any answer to see the original document excerpts

## Project Structure

```
PPChat/
├── api/
│   ├── rag/
│   │   ├── core/
│   │   │   ├── PdfProcessor.py          # PDF processing logic
│   │   │   └── VectorStoreIngestor.py   # Vector store management
│   │   ├── service/
│   │   │   ├── AnsweringModel.py        # LLM answering logic
│   │   │   └── RagService.py            # Main RAG service
│   │   ├── scripts/
│   │   │   └── ingest.py                # Document ingestion script
│   │   └── vector_store/                # Vector database storage
│   ├── config.py                        # Configuration management
│   ├── models.py                        # Pydantic models
│   └── routes.py                        # FastAPI routes
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── ragApi.ts                # API client
│   │   ├── components/
│   │   │   ├── ChatMessage.tsx          # Message component
│   │   │   ├── ChatInput.tsx            # Input component
│   │   │   └── ContextModal.tsx         # Context viewer
│   │   ├── App.tsx                      # Main app component
│   │   └── types.ts                     # TypeScript types
│   └── package.json
├── main.py                              # Backend entry point
├── pyproject.toml                       # Python dependencies
└── README.md
```

## API Endpoints

### `GET /`
Get API information

### `GET /health`
Check service health status

### `POST /ask`
Ask a question about your documents

**Request Body**:
```json
{
  "question": "What is this document about?"
}
```

**Response**:
```json
{
  "question": "What is this document about?",
  "answer": "Based on the documents...",
  "context": "Retrieved context from documents...",
  "context_docs": [
    {
      "content": "Document content...",
      "metadata": {
        "page": 1,
        "total_pages": 10,
        "source": "document.pdf"
      }
    }
  ]
}
```

## Development

### Backend Development
- Run with auto-reload: `uv run python main.py` (reload enabled by default)
- Run tests: `uv run pytest` (if tests are added)
- Format code: `uv run black .`
- Lint code: `uv run ruff check .`

### Frontend Development
- Dev server: `npm run dev`
- Build: `npm run build`
- Preview build: `npm run preview`
- Lint: `npm run lint`

## Configuration Options

### Backend Configuration (via `.env`)
- `VECTOR_STORE_PATH`: Where to store vector embeddings
- `EMBEDDING_MODEL`: HuggingFace model for embeddings
- `LLM_MODEL`: Model for generating answers
- `LLM_TEMPERATURE`: Response creativity (0-1)
- `LLM_MAX_TOKENS`: Maximum response length
- `CHUNK_SIZE`: Document chunk size for processing
- `CHUNK_OVERLAP`: Overlap between chunks

### Frontend Configuration (via `frontend/.env`)
- `VITE_API_URL`: Backend API URL

## Troubleshooting

### Backend Issues

**Vector store not found**:
- Make sure you've run the ingestion script: `uv run python api/rag/scripts/ingest.py`

**Module not found errors**:
- Reinstall dependencies: `uv sync`

**CORS errors**:
- Check that the frontend URL is allowed in `api/routes.py`

### Frontend Issues

**API connection failed**:
- Verify backend is running: `curl http://localhost:8000/health`
- Check `VITE_API_URL` in `frontend/.env`

**Build errors**:
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

## Future Enhancements

- [ ] User authentication
- [ ] Multiple document collections
- [ ] File upload via UI
- [ ] Conversation history persistence
- [ ] Support for more document types (DOCX, TXT, etc.)
- [ ] Advanced search filters
- [ ] Export conversations

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
