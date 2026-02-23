# Equivalent Makefile for the MCP project
# Variables
PY := uv run
API_PORT := 8000
TRANSPORT := "streamable-http"

# Help command
.PHONY: help
help:
	@echo "MCP - Model Context Protocol Server for Stock Intelligence"
	@echo ""
	@echo "Available targets:"
	@echo "  start-mcp   - Start the MCP Server FastAPI app at http://0.0.0.0:$(API_PORT)"
	@echo ""

# Start the MCP Server FastAPI app
.PHONY: start-mcp
start-mcp:
	$(PY) src/stock_intelligence_mcp/main.py --port $(API_PORT) --name "MCP Server Stock Intelligence" --transport $(TRANSPORT)

# Default target
.DEFAULT_GOAL := help