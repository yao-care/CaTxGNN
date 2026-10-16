---
layout: default
title: Brigatinib
parent: Model Prediction Only (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brigatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma / lung cancer"
---

# Brigatinib
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

# Brigatinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a kinase inhibitor (ALK-targeted) originally used to treat ALK-positive non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 99.89%), but **no clinical trials and no publications** support this specific prediction.
The prediction is graph-based only, and the evidence is at the model-prediction level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma / lung cancer (from the TxGNN knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, brigatinib is a tyrosine kinase inhibitor whose efficacy in ALK-positive non-small cell lung cancer is established (for example, the phase 3 ALTA-1L trial). Its targets include ALK, ROS1 and EGFR.

No mechanistic link between these kinase targets and gingival fibromatosis has been identified. Gingival fibromatosis is a benign overgrowth of gum tissue and is biologically distant from lung cancer. The high score most likely reflects proximity in the knowledge graph rather than a specific biological rationale.

For this reason, the prediction should be treated as a hypothesis only. Using a systemic kinase inhibitor, with its toxicity profile, for a benign gingival condition would be hard to justify without supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predictions Worth Noting

Among the other top-ranked predictions, the following are the most informative:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Lung benign neoplasm | 99.85% | L5 | The 20 retrieved publications (10 listed) all concern brigatinib in ALK-positive NSCLC, which is the already-approved malignant indication. They are not evidence for benign lung tumours. |
| Lung hilum carcinoma / pulmonary sulcus neoplasm | 99.85% / 99.84% | L5 | These are anatomical-location labels that largely overlap with existing NSCLC use. Any benefit would depend on ALK/ROS1 status. |
| Lung germ cell tumor | 99.84% | L4 | Five publications cover ALK-driven tumours (neuroblastoma, pheochromocytoma, lung large cell neuroendocrine carcinoma) and preclinical work. This is indirect, mechanism-level support that applies only to ALK-altered tumours. |
| Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.83% | L4 | The literature actually concerns **NF2-related schwannomatosis**, not this syndrome. In NF2-related schwannomatosis, brigatinib showed tumour shrinkage in NF2-deficient meningioma and schwannoma models ([PMID 34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/)) and a 2024 clinical report in patients with progressive tumours ([PMID 38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/)). This is promising but should be evaluated as a separate indication. |

The remaining predictions (fibroma of lung, hamartoma of lung, VCP-related inclusion body myopathy, junctional epidermolysis bullosa) have no trials or literature and no identified mechanistic link.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02479214 | ALUNBRIG | Not specified | Not specified |
| 02479206 | ALUNBRIG | Not specified | Not specified |
| 02479222 | ALUNBRIG | Not specified | Not specified |
| 02479230 | ALUNBRIG | Not specified | Not specified |

All four licences are valid single-ingredient products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. The literature also reports cardiac toxicity signals and a fatal tumour lysis syndrome case, so cardiovascular and metabolic monitoring should be considered. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: A total of 100 interactions were recorded. Those listed include several **Major** interactions: aprepitant, dexamethasone and clarithromycin. Many **Moderate** interactions were also listed, including acid-reducing agents (famotidine, ranitidine, rabeprazole, cimetidine), antidiabetic drugs (metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, acarbose), loperamide, morphine and cisapride.
- **Literature safety signals**: Fatal tumour lysis syndrome in a lung adenocarcinoma patient ([PMID 34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/)) and cardiac toxicities in a pharmacovigilance analysis ([PMID 34418561](https://pubmed.ncbi.nlm.nih.gov/34418561/)).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gingival fibromatosis rests only on a graph-based score. There are no clinical trials, no publications and no identified mechanistic link. It cannot support further development at present.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a biological rationale connecting brigatinib's kinase targets to gingival fibromatosis
- Preclinical or clinical evidence in the predicted indication
- Package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Consideration of NF2-related schwannomatosis as a separate, better-supported repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

