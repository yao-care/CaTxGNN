---
layout: home
title: CaTxGNN - Canada Drug Repurposing Predictions
---

# CaTxGNN

Drug repurposing predictions for Health Canada approved medications using TxGNN knowledge graph methods.

## Overview

This system analyzes **{{ site.data.stats.total_drugs | default: "11,511" }}** Health Canada registered drugs to identify potential new therapeutic uses.

## Statistics

| Metric | Value |
|--------|-------|
| Total Drugs | {{ site.data.stats.total_drugs | default: "11,511" }} |
| Mapped to DrugBank | {{ site.data.stats.mapped_drugs | default: "1,254" }} |
| Mapping Rate | {{ site.data.stats.mapping_rate | default: "85.2%" }} |
| Potential Candidates | {{ site.data.stats.candidates | default: "21,392,510" }} |

## FHIR API

Access drug repurposing data via FHIR R4 API:

- **Capability Statement**: [/fhir/metadata](/fhir/metadata)
- **MedicationKnowledge**: Drug information with DrugBank mappings
- **ClinicalUseDefinition**: Predicted therapeutic indications

## Data Sources

- **Drug Data**: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html)
- **Knowledge Graph**: [TxGNN](https://github.com/mims-harvard/TxGNN)
- **Drug Identifiers**: [DrugBank](https://go.drugbank.com/)

## Disclaimer

This content is for **research purposes only**. Predictions are computational and have not been validated for clinical use. Always consult healthcare professionals before making any medical decisions.

## Contact

- GitHub: [yao-care/CaTxGNN](https://github.com/yao-care/CaTxGNN)
- Website: [yao.care](https://yao.care)
