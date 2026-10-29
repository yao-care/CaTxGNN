---
layout: home
title: CaTxGNN - Canada Drug Repurposing Predictions
---

# CaTxGNN

Drug repurposing predictions for Health Canada approved medications using the TxGNN deep learning model.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Canada: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [Health Canada](https://www.canada.ca/en/health-canada.html) (Canada).

Reports by evidence level: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Solriamfetol](/drugs/solriamfetol/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Etafedrine](/drugs/etafedrine/) | L3 |
| [Butamben](/drugs/butamben/) | L5 |
| [Carbon Monoxide](/drugs/carbon-monoxide/) | L5 |
| [Gramicidin D](/drugs/gramicidin-d/) | L5 |
| [Romidepsin](/drugs/romidepsin/) | L5 |
| [Butalbital](/drugs/butalbital/) | L5 |
| [Methotrimeprazine](/drugs/methotrimeprazine/) | L5 |
| [Monopotassium Phosphate](/drugs/monopotassium-phosphate/) | L5 |
| [Thyroid Porcine](/drugs/thyroid-porcine/) | L5 |
| [Anti-Inhibitor Coagulant Complex](/drugs/anti-inhibitor-coagulant-complex/) | L5 |
| [Oxtriphylline](/drugs/oxtriphylline/) | L5 |
| [Dostarlimab](/drugs/dostarlimab/) | N/A |
| [Efinaconazole](/drugs/efinaconazole/) | N/A |
| [Lodoxamide](/drugs/lodoxamide/) | N/A |
| [Piperonyl Butoxide](/drugs/piperonyl-butoxide/) | N/A |

<!-- local-home:end -->

## Overview

This system analyzes **{{ site.data.stats.total_drugs | default: "11,511" }}** Health Canada registered drugs to identify potential new therapeutic uses.

## Statistics

| Metric | Value |
|--------|-------|
| Total Drugs | {{ site.data.stats.total_drugs | default: "11,511" }} |
| Mapped to DrugBank | {{ site.data.stats.mapped_drugs | default: "1,254" }} |
| Mapping Rate | {{ site.data.stats.mapping_rate | default: "85.2%" }} |
| Predicted New Indications (known uses excluded) | {{ site.data.site_stats.indications }} |

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

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

CaTxGNN is the Canada site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
