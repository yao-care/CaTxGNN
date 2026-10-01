---
layout: default
title: Clascoterone
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Clascoterone: From Acne to Candidiasis

## One-Sentence Summary

Clascoterone is a topical androgen receptor inhibitor developed for acne.
The TxGNN model predicts it may be effective for **candidiasis**, but **no clinical trials and no publications** currently support this. The prediction rests on the model score alone, so it is best treated as a low-confidence hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (topical treatment; the Canadian licence text has no indication on file) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Clascoterone is a locally acting topical agent that inhibits the androgen receptor in the skin's oil-gland (pilosebaceous) unit. It is a steroid derivative with minimal systemic absorption.

A plausible link between this mechanism and candidiasis is hard to find. Clascoterone has no known antifungal activity, and its target (the androgen receptor) plays no recognised role in fungal infection. Steroid-like agents may even raise the risk of local fungal overgrowth. The high TxGNN score (94.82%) most likely reflects proximity in the knowledge graph rather than biology.

Other predicted indications are no better supported. Migraine-related conditions, leprosy, oral candidiasis, and multiple endocrine neoplasia have no mechanistic rationale. Two hypotheses are weakly plausible on mechanism alone, with no supporting data: atrophoderma vermiculata (a follicular skin disorder, given the drug's action on the pilosebaceous unit) and adrenal gland hyperfunction (because of the drug's steroid structure).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for candidiasis.

Note that the 20 publications retrieved for another predicted indication (migraine susceptibility) are all about epilepsy and migraine genetics. None mention clascoterone, so they are not drug-specific evidence.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2538881 | WINLEVI |

Dosage form and approved indication text are not available in the current data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction has no trials, no literature, and no plausible mechanism. Clascoterone has no antifungal activity, and steroid-like agents may increase fungal overgrowth risk. The high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal for clascoterone in fungal skin infection, which does not exist today
- If the team wants to keep exploring this drug, atrophoderma vermiculata is the only candidate with a mechanistic hypothesis (topical action on the pilosebaceous unit). It would need a literature review before any decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

