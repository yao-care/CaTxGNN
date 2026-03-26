# CaTxGNN - Canada Drug Repurposing Predictions

Drug repurposing predictions for Canada using the TxGNN knowledge graph.

## Data Source

- **Regulatory Agency**: Health Canada
- **Database**: Drug Product Database (DPD)
- **URL**: https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html

## Usage

```bash
# Install dependencies
uv sync

# Prepare external data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py
```

## Disclaimer

This project is for research purposes only. Predictions are not validated for clinical use.
