---
name: generate-stock-report
description: Guide for creating professional analysis report of a selected stock regarding investment decisions based on toolkit provided to the AI agent.
---

# Stock Analysis Report Guide

## Overview

This file is a guide for creating professional analysis report of a selected stock regarding investment decisions based on toolkit provided to the AI agent.

---

# Process

## 🚀 High-Level Workflow

Creating professional stock analysis report involves following main phases:

### Phase 1: Fetch necessary data for analysis

**Key Metrics**
Before writing the report, first fetch following key metrics of the selected stock:

- Company Business Summary
- Latest Closing Prices
- Technical Indicators (RSI, Williams R)
- Summary of Analyst Recommendations

**Availiable Toolkit**
The key metrics mentioned above can be retrieved with the MCP server `stock_intelligence_mcp`. This server is usually availiable over the url `http://localhost:8000/mcp`.

The documentation of this MCP server can be reviewed here: `https://raw.githubusercontent.com/zhenxiay/stock_intelligence_mcp/refs/heads/main/README.md`

---

### Phase 2: Generate Analysis Report

Generate the analysis report based on the data retrieved from previous phase.

**Output Instruction:**
Please include following key metrics in the report:
    - Short description of company's business,
    - Closing price changes of last 14 days, 
    - Analyst recommendations, 
    - Technical indicators such as Relative Strength Index (RSI), True Strength Index (TSI) and Williams %R.
Format the response using markdown and include tables where appropriate.

---