# System Design – Store Sales Forecasting

## Overview
Production-ready data pipeline and ML system for daily sales forecasting.

## Data Sources
- Sales transactions
- Store metadata
- External economic signals
- Holiday events

## Pipeline Flow
Raw Data → Validation → Cleaning → Feature Engineering → Model Training → Forecast API

## Components

### Ingestion
Loads raw CSV files into dataframes.

### Validation
Schema checks, missing value detection, and anomaly detection.

### Preprocessing
Cleaning, joins, and normalization.

### Feature Engineering
Time-based lags, rolling statistics, calendar features.

### Training
Model training, evaluation, and persistence.

### Inference
API service for generating forecasts.

## Storage Layers
- Raw layer (immutable)
- Processed layer
- Feature layer
- Model artifacts

## Retraining Strategy
Scheduled batch retraining with drift monitoring.

## Monitoring
- Data quality
- Prediction drift
- Model performance