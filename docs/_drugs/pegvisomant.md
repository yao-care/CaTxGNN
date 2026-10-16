---
layout: default
title: Pegvisomant
parent: Model Prediction Only (L5)
nav_order: 716
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pegvisomant: predicted new indication Borderline ovarian serous tumor (evidence level L5). Approved use: Acromegaly, hyperpituitarism"
monitor_inn: "Pegvisomant"
predicted_indications: ["borderline ovarian serous tumor", "rete ovarii cystadenoma", "ovarian papillary cystadenoma", "pyelonephritis", "malignant ovarian Brenner tumor", "aleukemic mast cell leukemia", "ovarian mucinous cystadenofibroma", "ovarian benign neoplasm", "mucinous ovarian cystadenoma", "ovarian surface papilloma"]
---

# Pegvisomant
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

# Pegvisomant: From Acromegaly to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Pegvisomant was originally used to treat acromegaly (a condition of excess growth hormone, often linked to hyperpituitarism).
The TxGNN model predicts it may be effective for **borderline ovarian serous tumor**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly, hyperpituitarism (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Borderline ovarian serous tumor |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pegvisomant is a growth hormone (GH) receptor antagonist that lowers IGF-1. Its efficacy in acromegaly is established, and mechanistically it may be applicable to conditions in which GH/IGF-1 signalling drives cell growth.

The IGF-1/GH axis has been discussed in relation to the proliferation of ovarian epithelial cells, so a hypothetical link to borderline ovarian serous tumor exists. This link is speculative. No trial or publication supports it, and the high score (0.986) reflects a computational prediction only.

The same pattern appears across the other top-ranked predictions. Most are ovarian tumors (benign, borderline or rare malignant types) with the same speculative GH/IGF-1 rationale. Others, such as pyelonephritis (a bacterial kidney infection) and aleukemic mast cell leukemia (driven mainly by KIT-pathway changes), have no plausible mechanistic connection and are likely network artifacts.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02448858 | SOMAVERT | Not specified | Not specified |
| 02272199 | SOMAVERT | Not specified | Not specified |
| 02272210 | SOMAVERT | Not specified | Not specified |
| 02272202 | SOMAVERT | Not specified | Not specified |
| 02448831 | SOMAVERT | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 74 interactions were recorded in total. The 20 listed in the data compiled for this report are all rated Moderate and mostly involve glucose-lowering drugs: acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, acetohexamide, ertugliflozin, exenatide, glimepiride, glipizide, glyburide, human insulin and insulin aspart. Morphine and pegvaliase are also listed. Blood glucose monitoring is advisable when pegvisomant is combined with antidiabetic agents.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or publications, the mechanism-of-action data are missing, and the proposed GH/IGF-1 link to ovarian tumors is speculative. Borderline and benign ovarian tumors are generally managed surgically, so the unmet need for a drug is also low.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical evidence that GH/IGF-1 signalling drives borderline ovarian serous tumor growth
- A literature search and trial registry review for any pegvisomant data in ovarian tumors
- Approved indication and dosage form details for the five Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

