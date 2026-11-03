---
layout: default
title: Data Sources
nav_order: 93
permalink: /sources/
description: "Data sources behind CaTxGNN: Health Canada registration data, TxGNN, ClinicalTrials.gov, PubMed and DrugBank."
---

# Data Sources

<div class="key-takeaway">
Every conclusion traces back to a public data source — nothing is a black box.
</div>

---

## Source overview

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Source</th><th>Used for</th></tr>
</thead>
<tbody>
<tr><td>Registration data</td><td><a href="https://www.canada.ca/en/health-canada.html">Health Canada</a> Drug Product Database (DPD)</td><td>Approved drug list, ingredients and DIN status for Canada</td></tr>
<tr><td>Prediction model</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Drug&ndash;disease association prediction</td></tr>
<tr><td>Clinical trials</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidence grading (NCT)</td></tr>
<tr><td>Literature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidence grading (PMID)</td></tr>
<tr><td>Drug information</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Ingredient mapping and target data</td></tr>
<tr><td>Interactions</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Drug&ndash;drug interaction data</td></tr>
</tbody>
</table>

---

## This site's local data

Canadian medicines, their Drug Identification Numbers (DIN) and market status come from the
Health Canada Drug Product Database (DPD) data extracts.

| Item | Detail |
|------|--------|
| Dataset | Drug Product Database (DPD) full data extracts: marketed (`allfiles.zip`), inactive (`allfiles_ia.zip`), dormant (`allfiles_dr.zip`) and approved (`allfiles_ap.zip`) products |
| Publisher | Health Canada |
| Download | <https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/allfiles.zip> (the other three files use the same address with `_ia`, `_dr` and `_ap`) |
| Product identifier | DIN |
| Updates | Automatic weekly download (every Monday); each DIN takes the DPD status (Marketed, Approved, Dormant, Cancelled…); a DIN missing from the new files keeps its previous status |

---

## Licensing

Each source has its own licence — please check before citing:

- **TxGNN**: academic use; cite Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: US NIH public data
- **DrugBank**: non-commercial use subject to its licence terms
- **Health Canada**: subject to the open data terms of the Canada regulator

---

## Update frequency

| Data | Frequency |
|------|-----------|
| Health Canada DPD | Weekly (every Monday) |
| Trial / literature evidence | Re-collected periodically |
| Interaction data | Reviewed quarterly |

---

## Academic citation

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
