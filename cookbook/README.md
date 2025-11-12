# Cookbook with Agno OS

Welcome to the cookbook section! 
Here you will find examples which shows the functionality of this MCP server with **Agno OS** as client tool.

## Setup

### Create and activate a virtual environment

```shell
uv venv cookbook

# bash
source cookbook/bin/activate

#powershell
.venv/scripts/activate

```

### Install libraries

```shell
uv pip install -U openai agno
```

### Configure LLM for the agent (OpenAI)

Run the following command to create a .env file.

Add your Open AI API key to the file.

```bash
cp template.env .env
# Edit .env with your Open AI API key
```

## Run a cookbook

Execute the following command to see the outcome.

Make sure that you are executing the command from the project root folder.

You can add the stock of your choice with the flag --ticker.

#### Example of using Symbol (ASML)

```shell
uv run cookbook/example_agno_os.py --ticker 'ASML'
```

#### Example of using stock name (Snowflake)

```shell
uv run cookbook/example_agno_os.py --ticker 'Snowflake'
```

## Demo

The follwoing gif shows the outcome of this cookbook file.

Check the demo_img folder for more details!

![alt text](demo_img/agno_stock_mcp_demo.gif)