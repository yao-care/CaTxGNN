---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 575
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Mecasermin: predicted new indication Monosomy X (evidence level L5). Approved use: Growth hormone insensitivity syndrome"
monitor_inn: "MECASERMIN"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices with bleeding", "esophageal varices without bleeding"]
---

# Mecasermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Mecasermin: From Growth Hormone Insensitivity Syndrome to Monosomy X
{: .text-alpha }

## One-Sentence Summary

Mecasermin (recombinant IGF-1) was originally used for growth hormone insensitivity syndrome and Laron syndrome.
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Growth hormone insensitivity syndrome; Laron syndrome (the Canadian licence record contains no indication text) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mecasermin is a recombinant form of insulin-like growth factor 1 (IGF-1). Its efficacy in growth hormone insensitivity and Laron syndrome, which are conditions of primary IGF-1 deficiency, is established, and it may mechanistically be applicable to other conditions involving growth failure.

Monosomy X (Turner syndrome) is characterized by short stature and growth failure, which gives a plausible biological connection to IGF-1 replacement. However, the link is weak. Patients with Turner syndrome usually have adequate GH/IGF-1 signaling and are treated with recombinant growth hormone, whereas the original indications involve a primary IGF-1 deficiency. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and no trials or publications were found to verify it.

**Other predicted indications (all L5, prediction only):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Wolman disease with hypolipoproteinemia and acanthocytosis | 0.9909 | No clear mechanistic link; the score likely reflects network proximity. Hold |
| Esophageal varices with bleeding | 0.9903 | No established rationale; IGF-1 safety considerations (e.g. hypoglycaemia, mitogenic effects) weigh against use in acute bleeding. Hold |
| Esophageal varices without bleeding | 0.9903 | Identical score to the bleeding form, which suggests the same TxGNN model (deep learning) signal rather than independent support. The score may reflect similarities the model learned between related diseases, not biological evidence. Hold |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02509733 | INCRELEX | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 24 interactions were identified in the interaction screening, and the 20 detailed records available are all rated Moderate. They fall into two groups, both related to blood glucose:
  - **Sulfonylureas and related agents**: chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide, nateglinide
  - **Insulins**: human insulin (regular, isophane, zinc, zinc extended, inhaled rapid-acting), insulin aspart (including aspart protamine), degludec, detemir, glargine, glulisine, lispro (including protamine)
- **Additional considerations**: IGF-1 is mitogenic and carries a hypoglycaemia risk, which is relevant to any new indication, particularly in an acute bleeding setting.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are supported only by the model score, with no clinical trials or publications. The top-ranked prediction (monosomy X) has a weak mechanistic rationale because Turner syndrome patients generally do not have IGF-1 signalling deficiency. The closest candidate, GH insensitivity with immune dysregulation (autosomal dominant), is better treated as a research question and an extension of the existing label.

**To proceed, the following is needed:**
- Mechanism of action data for mecasermin
- Package insert warnings and contraindications from Health Canada
- A targeted literature and trial search for IGF-1 in Turner syndrome and in STAT5B-related GH insensitivity
- Safety assessment of hypoglycaemia and mitogenic risk in the proposed populations, including glucose monitoring when combined with insulin or sulfonylureas
- Dosage form and approved indication details for the Canadian licence (DIN 02509733)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

