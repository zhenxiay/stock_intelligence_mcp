# 📈📉📊 stock_intelligence_mcp

A Model Context Protocol (MCP) server which allows AI agents to interact with Yahoo Finance. 

## ✨ Key Features

| Feature | Description |
| ------- | ----------- |
| 📈 **Stock intelligence toolkit** | Get most recent price development and news of a selected ticker. |
| 📊 **Recommendation toolkit** | Get recommendations based on technical analysis indicators or analysts' opinions. |
| 🔌 **Seamless plugin with client** | The server can be integrated with the main stream mcp clients (Claude, VS code etc.) seamlessly. |
| 🖥️ **CLI Interface** | Offers a CLI interface to start the server. |
| 🐳 **Docker-Ready** | Dockerfile availiable. |
| 📦 **Extensible** | The server can be extended with addtional tools easily. |
---

## 🚀 Getting Started

To start this server, you can either clone this repository and run the server with python, or use the Docker image in the repo.

### 🧑‍💻 Option 1: Run with python (using uv)

#### Create a new directory for your project

⚙️ Clone the repository:

```bash
git clone https://github.com/zhenxiay/stock_intelligence_mcp.git
cd stock_intelligence_mcp
```

#### Create virtual environment in the folder and activate it

```bash
uv venv
source .venv/bin/activate
```

#### 🚀 Start the server

The server offers a CLI interface for the start.

Run the following command to check the availiable parameters:

```bash
uv run src/main.py --help
```

An example of starting the server with port 8008, streamable-http as transport and example_server as name:

```bash
uv run src/main.py --name example_server --port 8008 --transport streamable-http
```

### 🧑‍💻 Option 2: Run with Docker

Make sure that Docker engine is installed on your PC.

#### Create a new directory for your project

⚙️ Clone the repository:

```bash
git clone https://github.com/zhenxiay/stock_intelligence_mcp.git
cd stock_intelligence_mcp
```
#### Build the Docker container

```bash
docker build client/. -t mcp-server-stock-intelligence:test
```

#### Run the Docker container

```bash
docker run --name mcp-server-stock -p 8008:8008 mcp-server-stock-intelligence:test
```

## ⚙️ Connect to the Server

Here are some options with which you can connect the test this server:

### 🤖 Use MCP inspector:

Follow the instruction under: https://modelcontextprotocol.io/legacy/tools/inspector

### 🤖 Use a client (Claude Desktop, VS COde Copilot etc.)

Most of the clients would require you to configure your server in a json format like the following:

Example of using streamable_http transport

   ```json
   {
      "mcpServers": {
          "stock_intelligence": {
              "url": "http://localhost:8008/mcp/",
              "transport": "streamable_http"
          }
      }
   }
   ```

Example of using sse transport

   ```json
   {
      "mcpServers": {
         "stock_intelligence_sse": {
            "transport": "sse",
            "url": "https://localhost:8008/sse",
            "timeout": 600,
            "headers": null,
            "sse_read_timeout": 900
        }
      }
   }
   ```

Exact instructions for Claude desktop or VS code can be found here:

📋 Claude Desktop: https://modelcontextprotocol.io/quickstart/server

📋 VS Code GitHub Copilot Extention: https://code.visualstudio.com/docs/copilot/chat/mcp-servers
