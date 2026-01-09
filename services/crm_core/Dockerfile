FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install uv


COPY pyproject.toml uv.lock ./
COPY shared ./shared
COPY services/crm_core/pyproject.toml ./services/crm_core/

RUN uv sync --frozen --no-install-project

RUN mkdir -p /app/keys

COPY services/crm_core ./services/crm_core


WORKDIR /app/services/crm_core



CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
