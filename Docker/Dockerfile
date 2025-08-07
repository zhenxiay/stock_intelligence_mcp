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

ENV http_proxy=""
ENV https_proxy=""
ENV no_proxy="localhost,127.0.0.1,"

COPY --from=builder /app/.venv ./.venv

COPY src ./src

COPY pyproject.toml .

EXPOSE 8008

ENV PYTHONPATH="/app/src:$PYTHONPATH"
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv","run", "src/stock_intelligence_mcp/main.py", "--port", "8008", "--transport", "streamable-http"]