# ---- Builder Stage ----

FROM python:3.11-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .

RUN uv venv .venv && . .venv/bin/activate && uv sync --no-cache

# ---- Final Stage ----

FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV no_proxy="localhost,127.0.0.1,"
ENV PATH="/app/.venv/bin:$PATH"

COPY --from=builder /app/.venv ./.venv

COPY src ./src

COPY pyproject.toml .

EXPOSE 8008

CMD ["uv","run", "src/main.py", "--port", "8008", "--transport", "streamable-http"]