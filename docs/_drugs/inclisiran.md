---
layout: default
title: Inclisiran
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: From LDL-C Lowering to Potassium Deficiency Disease

## One-Sentence Summary

Inclisiran (marketed in Canada as LEQVIO) is a liver-targeted siRNA that silences PCSK9 synthesis and lowers LDL cholesterol.
The TxGNN model predicts it may be effective for **potassium deficiency disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a graph-based association only and has no mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data (mechanistically an LDL-C lowering agent) |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Inclisiran is a small interfering RNA (siRNA) that acts in the liver. It silences PCSK9 synthesis, which increases LDL-receptor recycling and lowers circulating LDL-C. Detailed mechanism-of-action data from DrugBank is not available, so this description is based on the mechanistic assessment in the evidence pack.

The prediction is **not mechanistically convincing**. Inclisiran has no known effect on potassium homeostasis, and the PCSK9/LDL-receptor pathway is unrelated to potassium handling. The very high TxGNN score (0.9993) most likely reflects proximity in the knowledge graph rather than a biological rationale. It should be treated as a hypothesis-generating signal only.

The other top-ranked predictions show the same pattern. All 10 candidates are L5 (model prediction only), have no trials or literature, and were rated "Hold":

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 1 | Potassium deficiency disease | 99.93% |
| 2 | Esophageal disease | 99.87% |
| 3 | Atypical coarctation of aorta | 99.86% |
| 4 | Migraine disorder | 99.83% |
| 5 | Non-syndromic esophageal malformation | 99.83% |
| 6 | Migraine with brainstem aura | 99.78% |
| 7 | Migraine with or without aura, susceptibility to | 99.78% |
| 8 | Aortic malformation | 99.76% |
| 9 | Esophageal ulcer | 99.73% |
| 10 | Raynaud disease | 99.73% |

Raynaud disease and migraine have only speculative, indirect vascular links. The congenital malformations (aortic, esophageal) have no plausible link to LDL-C lowering.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2518376 | LEQVIO | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. Health Canada warnings and contraindications were not retrieved, and no drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There is no plausible mechanistic link between PCSK9 silencing and potassium deficiency, and no trials or literature support it. Safety review also cannot proceed until the Canadian label data is obtained.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication, dosage form)
- Mechanism-of-action data from DrugBank
- A biological rationale linking PCSK9 silencing to potassium homeostasis, followed by preclinical or mechanistic studies
- Any clinical or observational signal (for example, potassium changes in existing inclisiran trial data) before further evaluation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

