---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma, astrocytoma (excluding glioblastoma)…"
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Temozolomide: From Anaplastic Astrocytoma / Glioblastoma to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug. Its original uses in the knowledge graph are brain tumours: anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and glioblastoma.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, but there are **no registered clinical trials** and only **3 publications** (all case reports, one directly about a spinal tumour), so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma, astrocytoma (excluding glioblastoma), brain glioblastoma (relations recorded in the knowledge graph; the Canadian licence records compiled here contain no indication text) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 DINs (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge of the drug class, temozolomide is an oral alkylating agent that methylates DNA (O6-guanine, N7-guanine, N3-adenine). This causes cytotoxic lesions and apoptosis in tumour cells, and the drug crosses the blood-brain barrier.

Cauda equina neoplasms are most often myxopapillary ependymomas, which are glial tumours of the central nervous system axis. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the astrocytic and glial brain tumours for which temozolomide is a known use, not biological evidence.

Activity probably depends on MGMT promoter methylation status, which is not reported for the available cases. The very high TxGNN score is a computational prediction only and does not replace clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Temozolomide showed remarkable efficacy in a relapsed spinal myxopapillary ependymoma with multiple recurrences and cerebrospinal dissemination |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma with repeated responses to multimodal treatment including radiotherapy; indirectly related to the predicted disease |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Atypical neuromeningeal cryptococcosis in a child treated for pontine glioma; not about the predicted disease |

Only one report (PMID 29270703) concerns a tumour of the cauda equina region (spinal myxopapillary ependymoma), and it is a single case. No cited study directly addresses cauda equina neoplasm as a defined disease, so the evidence level is L5.

## Canada Market Information

Temozolomide is marketed in Canada as single-ingredient products. At least 20 DINs are on record; the list may be partial. The records compiled here have no dosage form or approved indication text. Representative authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02241093 | TEMODAL | Not available | Not available |
| 02241094 | TEMODAL | Not available | Not available |
| 02241096 | TEMODAL | Not available | Not available |
| 02312794 | TEMODAL | Not available | Not available |
| 02389835 | ACH-TEMOZOLOMIDE | Not available | Not available |

Other generic versions include TARO-TEMOZOLOMIDE, TEVA-TEMOZOLOMIDE and JAMP TEMOZOLOMIDE.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Medium to high; the knowledge graph lists neutropenia, thrombocytopenia, pancytopenia, lymphopenia and aplastic anaemia as contraindication-related conditions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph relations, not label text):** liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia, aplastic anaemia.
- **Drug Interactions:** 100 interactions were found in total. The only one rated Moderate is naltrexone. Levofloxacin is rated Minor. Most others (for example pantoprazole, omeprazole, lansoprazole, metformin, morphine, prednisone, hydrocortisone and doxycycline) have no assigned severity level.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and the mechanism is plausible, but the only supporting study on the target tumour area is a single case report, and no clinical trials are registered. Evidence is at the model-prediction level (L5). The package insert safety data are also missing.

**To proceed, the following is needed:**
- Obtain the Health Canada package insert warnings and contraindications
- Obtain official mechanism-of-action data
- Systematically review reports of temozolomide in spinal or cauda equina ependymoma, including MGMT status
- Assess the feasibility of a prospective study or registry
- Define a safety monitoring plan for myelosuppression and hepatic risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

