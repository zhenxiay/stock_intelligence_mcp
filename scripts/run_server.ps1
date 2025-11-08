.venv/Scripts/Activate

$env:PYTHONPATH = ".\src"

uv run src/stock_intelligence_mcp/main.py --transport streamable-http