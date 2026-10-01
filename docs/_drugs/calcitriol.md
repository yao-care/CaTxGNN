---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 146
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: From an Unspecified Original Indication to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Calcitriol is the active form of vitamin D and is marketed in Canada, but the data provided do not state its approved indication.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency**, a deprecated ontology term.
There are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the provided data |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Calcitriol is the active form of vitamin D, so a mechanistic link to vitamin D deficiency is biologically plausible.

The disease term is flagged "obsolete", meaning it is a deprecated entry in the disease ontology. The very high score (0.9996) is therefore likely an artifact of that deprecated node and not a usable repurposing signal. The original indication is also missing, so the relationship between the old and new indications cannot be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

The dosage form and approved indication text were not provided for these authorizations. Five of the 8 DINs are shown.

| DIN | Product Name |
|---------|------|
| 481823 | ROCALTROL |
| 2485710 | TARO-CALCITRIOL |
| 2485729 | TARO-CALCITRIOL |
| 2431645 | CALCITRIOL-ODAN |
| 481815 | ROCALTROL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score for a deprecated disease term, with no trials or literature behind it. The mechanism is plausible, but the score is not a reliable repurposing signal.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- The approved original indication and the mechanism of action (from DrugBank)
- Re-mapping of the prediction to a current, non-obsolete vitamin D deficiency term, followed by a fresh evidence search

**Note on other predictions in this pack:**
- **Hereditary hypophosphatemic rickets (rank 7)** has the strongest support. It has two trials that study calcitriol directly: NCT03820518 (Phase 4 dose comparison, status unknown) and NCT03748966 (Early Phase 1 monotherapy). It is graded L2 with a "Proceed with Guardrails" recommendation. Calcitriol plus phosphate appears to be conventional therapy here, so this is probably a gap in the labeled-indication data and not a true repurposing.
- **Renal tubular acidosis (rank 2)** is graded L4, with a plausible indirect rationale through associated bone disease. Its literature consists of physiology studies, case reports and reviews. None tests calcitriol as a treatment for the acidosis itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

