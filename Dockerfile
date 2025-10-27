FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

COPY . .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

CMD uv run gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app