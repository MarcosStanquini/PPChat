# RAG

## Pré-requisitos

1. Instale o [uv](https://docs.astral.sh/uv/).
2. Garanta o Python $3.13$ com `uv python install 3.13`.

## Configuração

1. Sincronize dependências do [`pyproject.toml`](pyproject.toml):
   ```shell
   uv sync
   ```
2. Configure variáveis de ambiente:
   ```shell
   cp .env-example .env
   ```
   Edite `FILE_PATH` conforme a origem dos dados.

## Uso

- Executor principal: `uv run python main.py`, que invoca [`main.main`](main.py).
- Processamento de PDFs: `uv run python rag/PdfProcessor.py`, usando [`rag.PdfProcessor.PdfProcessor`](rag/PdfProcessor.py).

## Estrutura

- `rag/data`: armazenamento de fontes.
- `.env`: parâmetros dinâmicos (cópia de `.env-example`).