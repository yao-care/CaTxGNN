---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Androgen Receptor Antagonist Use to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a nonsteroidal androgen receptor antagonist, and its original indication is not recorded in the licence data provided.
The TxGNN model predicts it may be relevant to **prostate cancer/brain cancer susceptibility**, but **no clinical trials and no publications** are linked to this prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Flutamide is known as a nonsteroidal androgen receptor antagonist, so the prostate cancer component of this prediction is mechanistically plausible.

The predicted term is a genetic susceptibility label, not a treatable clinical condition. A drug cannot be "indicated" for a susceptibility trait, so the prediction is best read as a signal of knowledge-graph proximity to prostate cancer. It is not a distinct new use. With no trials or literature linked, there is no support beyond the model score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2238560 | FLUTAMIDE |

Dosage form, manufacturer and approved indication text are blank in the source record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). The disease term is a susceptibility label rather than a treatable indication, and no supporting studies are linked.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm the original indication, warnings and contraindications
- Mechanism of action data (DrugBank)
- A clinically meaningful definition of the target indication

**Note on other candidates:** Among the ten predictions, the broad term "male reproductive organ cancer" (rank 6) has the strongest support. It has three Phase 2 trials that explicitly include flutamide (NCT00450463, NCT00817739, NCT00001266), and its evidence level is L2 with a "Proceed with Guardrails" recommendation. That term is dominated by prostate cancer, which is probably already an approved use, so it is likely not a true repurposing case. Any advancement should include liver function monitoring because of flutamide's hepatotoxicity risk.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

