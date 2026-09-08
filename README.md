# Digital Marketing Cost Optimizer

An end-to-end Data Engineering, Analytics, Optimization, and AI project designed to analyze digital marketing performance and optimize advertising budget allocation across platforms, campaigns, and markets.

## Project Overview

Digital marketing teams manage advertising investments across multiple channels, markets, and campaigns. Determining where budget should be allocated requires reliable data pipelines, consistent KPI definitions, performance analysis, forecasting, and optimization.

This project builds an end-to-end pipeline that transforms raw campaign performance data into validated analytical datasets and will progressively introduce marketing KPI engineering, forecasting, constrained budget optimization, and AI-assisted recommendations.

## Business Objectives

- Consolidate and validate multi-channel marketing performance data.
- Measure campaign and platform efficiency using standardized marketing KPIs.
- Identify high-performing and underperforming campaigns, channels, and markets.
- Forecast campaign performance using historical data.
- Optimize budget allocation under business constraints.
- Generate explainable recommendations for marketing decision-makers.

## Implemented Components

### Data Ingestion

- Built a reusable Python-based ingestion module.
- Loaded a 30,000-row digital marketing performance dataset.
- Implemented initial schema and dataset inspection.
- Established a structured raw-data ingestion layer.

### Data Quality & Validation

- Validated missing values and duplicate records.
- Converted campaign dates into standardized datetime format.
- Validated year and month fields against campaign dates.
- Added foundational data-quality checks before downstream analytics.

## Solution Roadmap

The project is being developed toward the following workflow:

```text
Marketing Data Sources
        |
        v
Data Ingestion Layer
        |
        v
Raw Data Storage
        |
        v
Data Quality & Validation
        |
        v
Transformation & KPI Layer
        |
        v
Exploratory & Performance Analytics
        |
        v
Forecasting
        |
        v
Constrained Budget Optimization
        |
        v
LangGraph AI Workflow
        |
        v
LLM-Generated Recommendations
        |
        v
Streamlit Decision Dashboard