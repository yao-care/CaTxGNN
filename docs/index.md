---
layout: home
title: CaTxGNN - Canada Drug Repurposing Predictions
description: "TxGNN drug repurposing reports for 932 medicines in Health Canada's Drug Product Database, with evidence levels L1–L5 from clinical trials and literature."
---

# CaTxGNN

Drug repurposing predictions for Health Canada approved medications using the TxGNN deep learning model.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Canada: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [Health Canada](https://www.canada.ca/en/health-canada.html) (Canada).

### This site's local data

| Item | Detail |
|------|--------|
| Dataset | Drug Product Database (DPD) full data extracts: marketed (`allfiles.zip`), inactive (`allfiles_ia.zip`), dormant (`allfiles_dr.zip`) and approved (`allfiles_ap.zip`) products |
| Publisher | Health Canada |
| Download | <https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/allfiles.zip> (the other three files use the same address with `_ia`, `_dr` and `_ap`) |
| Product identifier | DIN |
| Updates | Automatic weekly download (every Monday); each DIN takes the DPD status (Marketed, Approved, Dormant, Cancelled…); a DIN missing from the new files keeps its previous status |

Details: [Data Sources]({{ '/sources/' | relative_url }}).

Reports by evidence level:

| Evidence level | Reports | Share |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

73 predicted drug–disease pairs on this site appear on no other of the 30 TxGNN sites.

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Etafedrine](/drugs/etafedrine/) | L3 |
| [Butamben](/drugs/butamben/) | L5 |
| [Carbon Monoxide](/drugs/carbon-monoxide/) | L5 |
| [Gramicidin D](/drugs/gramicidin-d/) | L5 |
| [Romidepsin](/drugs/romidepsin/) | L5 |
| [Butalbital](/drugs/butalbital/) | L5 |
| [Monopotassium Phosphate](/drugs/monopotassium-phosphate/) | L5 |
| [Methotrimeprazine](/drugs/methotrimeprazine/) | L5 |
| [Thyroid Porcine](/drugs/thyroid-porcine/) | L5 |
| [Anti-Inhibitor Coagulant Complex](/drugs/anti-inhibitor-coagulant-complex/) | L5 |
| [Oxtriphylline](/drugs/oxtriphylline/) | L5 |
| [Dostarlimab](/drugs/dostarlimab/) | N/A |
| [Efinaconazole](/drugs/efinaconazole/) | N/A |
| [Lodoxamide](/drugs/lodoxamide/) | N/A |
| [Piperonyl Butoxide](/drugs/piperonyl-butoxide/) | N/A |

<!-- local-home:end -->

## Overview

This system analyzes Health Canada registered drugs to identify potential new therapeutic uses.

## Statistics

| Metric | Value |
|--------|-------|
| Drug Reports | {{ site.data.drug_stats.total_drugs }} |
| Mapped to DrugBank | 1,266 |
| Mapping Rate | 86.7% |
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

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.
