.PHONY: help venv install run run-http run-sse run-stdio docker-build docker-run docker-stop docker-clean clean test

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON := python3
UV := $(shell command -v uv 2>/dev/null)
VENV := .venv
SRC_DIR := src
MAIN_SCRIPT := $(SRC_DIR)/stock_intelligence_mcp/main.py
DOCKER_IMAGE := mcp-server-stock-intelligence:test
DOCKER_CONTAINER := mcp-server-stock
PORT := 8000
SERVER_NAME := StockIntelligence

# Check if we're in a virtual environment or have uv
ifdef UV
    RUN_CMD := $(UV) run
else ifdef VIRTUAL_ENV
    RUN_CMD := python
else
    RUN_CMD := $(PYTHON) -m
endif

help: ## Display this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

venv: ## Create virtual environment
	@echo "Creating virtual environment..."
ifdef UV
	@$(UV) venv
else
	@$(PYTHON) -m venv $(VENV)
endif

install: venv ## Install dependencies
	@echo "Installing dependencies..."
ifdef UV
	@. $(VENV)/bin/activate && $(UV) sync
else
	@. $(VENV)/bin/activate && pip install -e .
endif

run: run-sse ## Run the server with default settings (SSE transport on port 8000)

run-http: ## Run the server with streamable-http transport on port 8008
	@echo "Starting server with streamable-http transport on port 8008..."
ifdef UV
	@export PYTHONPATH=./$(SRC_DIR) && $(UV) run $(MAIN_SCRIPT) --name $(SERVER_NAME) --port 8008 --transport streamable-http
else
	@export PYTHONPATH=./$(SRC_DIR) && . $(VENV)/bin/activate && python $(MAIN_SCRIPT) --name $(SERVER_NAME) --port 8008 --transport streamable-http
endif

run-sse: ## Run the server with SSE transport on port 8000
	@echo "Starting server with SSE transport on port $(PORT)..."
ifdef UV
	@export PYTHONPATH=./$(SRC_DIR) && $(UV) run $(MAIN_SCRIPT) --name $(SERVER_NAME) --port $(PORT) --transport sse
else
	@export PYTHONPATH=./$(SRC_DIR) && . $(VENV)/bin/activate && python $(MAIN_SCRIPT) --name $(SERVER_NAME) --port $(PORT) --transport sse
endif

run-stdio: ## Run the server with stdio transport
	@echo "Starting server with stdio transport..."
ifdef UV
	@export PYTHONPATH=./$(SRC_DIR) && $(UV) run $(MAIN_SCRIPT) --name $(SERVER_NAME) --transport stdio
else
	@export PYTHONPATH=./$(SRC_DIR) && . $(VENV)/bin/activate && python $(MAIN_SCRIPT) --name $(SERVER_NAME) --transport stdio
endif

docker-build: ## Build Docker image
	@echo "Building Docker image..."
	docker build . -t $(DOCKER_IMAGE) -f Docker/Dockerfile

docker-run: ## Run Docker container
	@echo "Running Docker container..."
	docker run --name $(DOCKER_CONTAINER) -p 8008:8008 $(DOCKER_IMAGE)

docker-stop: ## Stop Docker container
	@echo "Stopping Docker container..."
	docker stop $(DOCKER_CONTAINER) || true
	docker rm $(DOCKER_CONTAINER) || true

docker-clean: docker-stop ## Clean up Docker container and image
	@echo "Cleaning up Docker resources..."
	docker rmi $(DOCKER_IMAGE) || true

test: ## Run tests
	@echo "Running tests..."
ifdef UV
	@export PYTHONPATH=./$(SRC_DIR) && $(UV) run pytest tests/
else
	@export PYTHONPATH=./$(SRC_DIR) && . $(VENV)/bin/activate && pytest tests/
endif

clean: ## Clean up virtual environment and cache files
	@echo "Cleaning up..."
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
