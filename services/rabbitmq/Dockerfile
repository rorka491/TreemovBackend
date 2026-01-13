FROM ghcr.io/astral-sh/uv:latest AS uv_base
FROM python:3.13-slim

COPY --from=uv_base /uv /uvx /bin/

ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY shared ./shared
COPY services/rabbitmq/pyproject.toml ./services/rabbitmq/

RUN uv sync --frozen --no-install-project


COPY services/rabbitmq ./services/rabbitmq


WORKDIR /app/services/rabbitmq

CMD ["uv", "run", "--package", "rabbitmq", "python", "-m", "main"]
