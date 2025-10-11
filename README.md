# 📈📉📊 stock_intelligence_mcp

A Model Context Protocol (MCP) server enabling AI agents to access and analyze Yahoo Finance data.
The toolkit enpowers LLMs to analyze the data of selected tickers based on latest price trends, market news or calculated technical indicators.
It also features tools for generating buy or sell suggestions based on analysts' recommendations.

## 🛠️ MCP Server Tools (to be extended)

| Tool | Description |
| :---- | :----------- |
| `get_closing_stock_price` | Get the closing price for a given stock ticker on a specific date. |
| `get_14d_closing_stock_price` | Get the closing prices for the last 14 days for a given stock ticker. |
| `technical_analysis_rsi` | Get RSI (Relative Strength Index) technical analysis for a stock ticker. |
| `get_sell_buy_advice` | Get buy/sell/hold advice for a stock ticker based on a summary of analysts recommendations. |
| `get_recent_stock_news` | Get the most recent news articles for a stock ticker. |

## 💻 Demo

The screenshot below demonstrates the usage of this server in a customized Streamlit client:

![alt text](https://github.com/zhenxiay/stock_intelligence_mcp/blob/dev/mcp_si_server_demo.png?raw=true)

The server is fully compatible with popular MCP clients such as Claude Desktop and VS Code.

Check out the *Connect to the Server* section for more details!

## ✨ Key Features

| Feature | Description |
| :------- | :----------- |
| 🔌 **Easy plugin** | The server can be integrated with the main stream mcp clients (Claude, VS code etc.) seamlessly. |
| 🖥️ **CLI Interface** | Offers a CLI interface to start the server. |
| 🐳 **Docker-Ready** | Dockerfile available. |
| ⚓ **k8s & Helm-Ready** | k8s manifest and Helm chart also available. |
| 📦 **Extensible** | The server can be extended with additional tools easily. |
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
export PYTHONPATH=./src
uv run src/stock_intelligence_mcp/main.py --help
```

```powershell
$env:PYTHONPATH=".\src"
uv run src/stock_intelligence_mcp/main.py
```

An example of starting the server with port 8008, streamable-http as transport and example_server as name:

```bash
export PYTHONPATH=./src
uv run src/stock_intelligence_mcp/main.py --name example_server --port 8008 --transport streamable-http
```

### 🧑‍💻 Option 2: Run with Docker/ k8s/ Helm chart

❗Make sure that Docker engine/ a k8s cluster (minikube/ kind etc.)/ Helm is installed on your PC.

#### Create a new directory for your project

⚙️ Clone the repository:

```bash
git clone https://github.com/zhenxiay/stock_intelligence_mcp.git
cd stock_intelligence_mcp
```
#### Build the Docker container

```bash
docker build . -t mcp-server-stock-intelligence:test -f Docker/Dockerfile
```

#### Run the Docker container

```bash
docker run --name mcp-server-stock -p 8008:8008 mcp-server-stock-intelligence:test
```

#### Run the k8s manifest

❗A secret has first to be created with some proxy specifications as env variable has to be created:

```bash
kubectl create secret generic proxy-env --from-literal=HTTP_PROXY=http://localhost:3128 --from-literal=HTTPS_PROXY=https://localhost:3128 --from-literal=NO_PROXY=localhost,127.0.0.1,kind
```

Then apply the deployment and service:

```bash
kubectl apply -f k8s/mcp-server-deployment.yaml
kubectl apply -f k8s/mcp-server-service.yaml
```

#### Run Helm to create the server

You can use the Helm chart and the following commands to create the server as well:

```bash
helm upgrade --install mcp-server-stock-intelligence k8s/helm --set proxy.http="http://your-proxy:8080" --set proxy.https="http://your-proxy:8080"
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

❗Please notice that the real port number is related to your own settings on your py command/ docker container/ helm chart values.

Exact instructions for Claude desktop or VS code can be found here:

📋 Claude Desktop: https://modelcontextprotocol.io/quickstart/server

📋 VS Code GitHub Copilot Extention: https://code.visualstudio.com/docs/copilot/chat/mcp-servers
