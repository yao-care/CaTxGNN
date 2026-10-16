---
layout: default
title: Alectinib
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alectinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer"
---

# Alectinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alectinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Alectinib is an ALK inhibitor originally used to treat ALK-positive non-small cell lung cancer.
The TxGNN model's top-ranked prediction is **gingival fibromatosis**, but **no clinical trials and no publications** support this direction.
The prediction is model output only. Among the ten predicted indications, only lung germ cell tumor has any registered trial, and that trial was terminated after one participant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (the Canadian licence record has no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, alectinib is a selective inhibitor of anaplastic lymphoma kinase (ALK), with additional RET activity. Its efficacy in ALK-positive non-small cell lung cancer is well established.

No mechanistic link to gingival fibromatosis has been established. No ALK-driven pathology has been described in this condition. The very high TxGNN score is a graph-based prediction only. It most likely reflects network proximity to the approved lung cancer indication rather than biological rationale.

The other top-ranked predictions show the same pattern:
- **Benign lung conditions** (fibroma, hamartoma, benign neoplasm): the evidence is unrelated to benign disease, with no ALK-related mechanism known.
- **Lung cancer subtypes** (hilum carcinoma, pulmonary sulcus neoplasm): these are plausible only if the tumour is ALK-positive, and no direct evidence exists.
- **Lung germ cell tumor**: the most scientifically interesting. Case reports show responses to ALK inhibitors in other ALK-rearranged tumours, such as neuroendocrine carcinoma, neuroblastoma and glioma. This is indirect and depends on tumour ALK status.
- **Rare genetic or structural diseases** (VCP-related myopathy, junctional epidermolysis bullosa, a rare syndrome): no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials are registered for gingival fibromatosis.

For reference, the only trial found across the top ten predictions relates to the rank 7 prediction, lung germ cell tumor:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04644315](https://clinicaltrials.gov/study/NCT04644315) | Phase 2 | Terminated | 1 | Single-arm, home-based study of alectinib in ALK-positive solid tumours other than lung cancer. With one participant, it yields no interpretable efficacy or safety data. |

## Literature Evidence

Currently no related literature is available for gingival fibromatosis.

Publications were retrieved for other predictions. The most relevant are shown below, as context for the broader prediction list.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28586279](https://pubmed.ncbi.nlm.nih.gov/28586279/) | 2017 | RCT (Phase 3, ALEX) | N Engl J Med | Alectinib vs crizotinib in untreated ALK-positive NSCLC (the approved indication) |
| [28501140](https://pubmed.ncbi.nlm.nih.gov/28501140/) | 2017 | RCT (Phase 3, J-ALEX) | Lancet | Alectinib vs crizotinib in Japanese ALK-positive NSCLC |
| [38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/) | 2024 | RCT (Phase 3, ALINA) | N Engl J Med | Adjuvant alectinib vs chemotherapy in resected ALK-positive NSCLC |
| [32418886](https://pubmed.ncbi.nlm.nih.gov/32418886/) | 2020 | RCT follow-up | Ann Oncol | Updated overall and progression-free survival in the ALEX study |
| [41110693](https://pubmed.ncbi.nlm.nih.gov/41110693/) | 2026 | Comparative study | Ann Oncol | Final overall survival analysis of ALEX |
| [36690569](https://pubmed.ncbi.nlm.nih.gov/36690569/) | 2023 | Case report | Clin Lung Cancer | ALK-positive lung neuroendocrine tumour with favourable response to alectinib |
| [35200571](https://pubmed.ncbi.nlm.nih.gov/35200571/) | 2022 | Case report | Curr Oncol | ALK-rearranged combined adenocarcinoma/neuroendocrine carcinoma with partial response to alectinib |
| [32054410](https://pubmed.ncbi.nlm.nih.gov/32054410/) | 2020 | Case report | J Oncol Pharm Pract | Hypertriglyceridaemia-induced pancreatitis related to alectinib (a safety signal) |

These publications concern the approved NSCLC indication, other ALK-rearranged tumours, or adverse events. None supports efficacy in the predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02458136 | ALECENSARO | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/RET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Published reports describe anaemia, including a case of haemolytic anaemia. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert. Reported adverse events suggest attention to blood counts, liver function, lipids, weight and cardiac parameters. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug Interactions:** 92 interactions were identified. The first 20 records reviewed include one Major interaction and 19 Moderate interactions.
- **Major:** aminolevulinic acid
- **Moderate (examples):** dolasetron, naltrexone, mefloquine, quinine, methoxsalen, atazanavir, bedaquiline, and several beta-blockers (acebutolol, atenolol, betaxolol, bisoprolol)

**Adverse events from published case reports (not label data):** drug reaction with eosinophilia and systemic symptoms (DRESS), erythema multiforme, haemolytic anaemia, hypertriglyceridaemia-induced pancreatitis and weight gain.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for gingival fibromatosis rests on model output alone (L5). It has no trials, no literature and no plausible ALK-related mechanism.
- Alectinib's strong evidence in ALK-positive NSCLC does not transfer to this condition.
- Among the other top-ten predictions, lung germ cell tumor is the only one flagged as a research question. That is based on indirect ALK-fusion rationale, not direct evidence.

**To proceed, the following is needed:**
- Evidence that ALK or RET signalling is involved in gingival fibromatosis, for example molecular profiling of patient tissue
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Indication text and dosage form for the Canadian licence
- Preclinical or case-level efficacy data in the predicted indication before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

