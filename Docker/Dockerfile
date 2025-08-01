FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Set environment variables for proxy
ENV no_proxy=".bosch.com,localhost,127.0.0.1,"

COPY pyproject.toml .
COPY main.py .

RUN uv venv .venv
RUN uv sync

EXPOSE 8008

CMD ["uv","run", "main.py", "--port", "8008"]