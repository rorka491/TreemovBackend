FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install uv


COPY pyproject.toml uv.lock ./
COPY shared ./shared
COPY services/auth-service/pyproject.toml ./services/auth-service/

RUN uv sync --frozen --no-install-project

RUN mkdir -p /app/keys && \
    openssl genrsa -out /app/keys/private.pem 2048 && \
    openssl rsa -in /app/keys/private.pem -pubout -out /app/keys/public.pem

    
COPY services/auth-service ./services/auth-service


WORKDIR /app/services/auth-service

    

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



