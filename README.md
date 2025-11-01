# Advanced ETL Pipeline for OMNICart

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for OMNICart, processing product and user data from an external API. The pipeline enriches product data and generates seller performance analytics.

## Features
- Fetches product and user data from external API
- Enriches product data with additional metrics
- Analyzes seller performance
- Generates JSON reports
- Configurable pipeline parameters
- Error handling and logging

## Pagination Strategy
uses 2 variables called start and limit
by default start is 0 while limit is gotten from the config file

based on the values of start and limit
the response from the api is spilced by the values
where start indicates what part of the response json to start from.

the sum of start and limit indicates the end position of the splice.


## Project Structure
```
.
├── pipeline/
│   ├── __init__.py
│   ├── pipeline.py        # Main ETL pipeline implementation
│   ├── api_client.py      # API interaction handling
│   ├── data_enricher.py   # Data enrichment logic
│   └── data_analyzer.py   # Analytics implementation
├── tests/
│   └── test_api_client.py # Unit tests
├── config.ini            # Configuration file
└── README.md
```

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Create a `config.ini` file with the following structure:
```ini
[pipeline]
name = omnicart_etl

[LOAD]
base_url = https://api.example.com
limit = 100
```

## Usage
Run the pipeline:
```bash
python -m pipeline.pipeline
```

The pipeline will:
1. Fetch product and user data
2. Enrich the data
3. Generate analytics
4. Save results to `seller_performance_report.json`

## Testing
Run tests using pytest:
```bash
pytest tests/
```


## Dependencies
- requests
- pytest (for testing)
- configparser

