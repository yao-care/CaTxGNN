---
layout: default
title: Clascoterone
parent: Model Prediction Only (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clascoterone: predicted new indication Candidiasis (evidence level L5). Approved use: Acne vulgaris"
monitor_inn: "Clascoterone"
predicted_indications: ["candidiasis", "migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "leprosy", "atrophoderma vermiculata", "oral candidiasis", "progeria-short stature-pigmented nevi syndrome", "adrenal gland hyperfunction", "multiple endocrine neoplasia"]
---

# Clascoterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Clascoterone: From Acne Vulgaris to Candidiasis
{: .text-alpha }

## One-Sentence Summary

Clascoterone is a topical androgen receptor inhibitor, marketed in Canada as WINLEVI and used for acne vulgaris (in patients 12 years and older). The TxGNN model predicts it may be effective for **candidiasis**, but **no clinical trials and no publications** currently support this direction. The prediction is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne vulgaris (per the pharmacology reference data; the Canadian licence record contains no indication text) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clascoterone is a topical androgen receptor inhibitor (a cortexolone 17α-propionate derivative) and its pharmacology is directed at the pilosebaceous unit in acne vulgaris.

No established mechanistic link to antifungal activity or *Candida* pathogenesis was identified. The prediction most likely reflects proximity in the model's knowledge graph rather than biological rationale. The score is high, but it is not evidence of efficacy.

For context, the other top predictions are also weakly supported:
- **Oral candidiasis** (86.7%): duplicates the candidiasis signal, and clascoterone is a skin cream, not an oral mucosal product.
- **Migraine disorder and related subtypes** (89.4%–92.1%): androgen receptor antagonism could theoretically touch hormonal influences, but low systemic exposure from topical use makes this unlikely.
- **Leprosy** (88.9%): no known antimicrobial activity; a shared dermatologic context is not a mechanism.
- **Atrophoderma vermiculata** (86.8%) and **adrenal gland hyperfunction** (85.9%): these are the only two flagged as "Research Question". The first has a weak hypothesis-level link through anti-androgen action on the pilosebaceous unit. The second relates to clascoterone's steroid structure, but the relationship is more safety-related (possible HPA-axis suppression) than therapeutic.

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
| 02538881 | WINLEVI | Not specified | Not specified in the licence record |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry: clascoterone acts on the **androgen receptor** (human, gene AR). This is a target relationship rather than a drug-drug interaction, and no interaction severity level was provided.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction rests on a model score alone (Evidence Level L5). There are no trials or publications, no plausible antifungal mechanism, and the Canadian licence record is incomplete. This does not justify advancing.

**To proceed, the following is needed:**
- Mechanism of action data, and any evidence of antifungal or anti-*Candida* activity (e.g., in vitro studies)
- The Health Canada package insert (warnings, contraindications, approved indication, dosage form), which is required before any safety screening
- Route and formulation compatibility assessment (topical cream versus the required route for the new indication)
- If exploratory work is desired, prioritise the "Research Question" candidates (atrophoderma vermiculata, adrenal gland hyperfunction) over candidiasis, starting with preclinical or case-level studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

