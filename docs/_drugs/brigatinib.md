---
layout: default
title: Brigatinib
parent: Model Prediction Only (L5)
nav_order: 123
evidence_level: L5
indication_count: 9
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-11-24
description: "Brigatinib: predicted new indication Gingival fibromatosis (fibromatosis, gingival) (evidence level L5). In Canada: 4 DINs (4 marketed)"
---

# Brigatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Brigatinib: ALK/multi-kinase inhibitor → fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Brigatinib is an oral kinase inhibitor that targets ALK and several other tyrosine kinases and is marketed in Canada as ALUNBRIG.
The TxGNN model predicts it may be relevant to **gingival fibromatosis**, with a score of 0.9989.
There are **no clinical trials and no publications** for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gingival fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for brigatinib: "Brigatinib is a tyrosine kinase inhibitor (TKI) with in vitro activity at clinically achievable concentrations against multiple kinases including ALK, ROS1, insulin-like growth factor-1 receptor (IGF-1R), and FLT-3 as well as EGFR deletion and point mutations. Brigatinib inhibited autophosphorylation of ALK and ALK-mediated phosphorylation of the downstream signaling proteins STAT3, AKT, ERK1/2, and S6 in in vitro and in vivo assays." ([DailyMed: Alunbrig (brigatinib) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fe9ff20-d402-41f3-bc1e-7002ea7007db), label version 2026-01-12; accessed 2026-11-19.) Brigatinib is known from the literature as a next-generation ALK inhibitor that also inhibits other tyrosine kinases, such as ROS1 and EGFR.

No mechanistic link between this kinase inhibition and gingival fibromatosis has been identified. The high TxGNN score is a model-based prediction only. Gingival fibromatosis is a non-malignant overgrowth of gum tissue, and no biological rationale supports using a systemic oncology kinase inhibitor for it. The similarity between the drug's current use and this condition has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02479206 | ALUNBRIG | BRIGATINIB | Marketed |
| 02479214 | ALUNBRIG | BRIGATINIB | Marketed |
| 02479222 | ALUNBRIG | BRIGATINIB | Marketed |
| 02479230 | ALUNBRIG | BRIGATINIB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All four single-ingredient licences are valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Major-level interactions among those listed include aprepitant, dexamethasone and clarithromycin. Many moderate-level interactions are also listed, including acid-reducing agents (famotidine, ranitidine, rabeprazole, cimetidine) and several antidiabetic drugs (metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin).

Warnings and contraindications from the package insert were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no publications and no identified mechanistic link, so it remains a model output only (evidence level L5). Systemic kinase inhibitor toxicity would be hard to justify for a benign gum condition without supporting data.

**To proceed, the following is needed:**
- A mechanistic rationale linking brigatinib's kinase targets to gingival fibromatosis
- Preclinical or clinical studies in this disease
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Alunbrig (brigatinib) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fe9ff20-d402-41f3-bc1e-7002ea7007db) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

