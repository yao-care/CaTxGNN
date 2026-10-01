---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Etravirine is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI) marketed in Canada as INTELENCE.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**,
but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (Health Canada indication text was not provided in the data) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on known information, etravirine is an allosteric inhibitor of HIV-1 reverse transcriptase, and its efficacy in HIV-1 infection is established.

The prediction is only weakly reasonable. Feline immunodeficiency virus (FIV) is a retrovirus related to HIV, which likely explains the high graph score. However, FIV reverse transcriptase is generally insensitive to NNRTIs. The score therefore probably reflects the shared retroviral neighborhood in the knowledge graph, not real pharmacology.

This is also a veterinary indication. Nothing in the data shows etravirine has been tested against FIV, so the prediction should be treated as a model artifact until shown otherwise.

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
| 2306778 | INTELENCE |
| 2375931 | INTELENCE |

Dosage form and approved indication text were not available for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical or literature support. FIV reverse transcriptase is generally insensitive to NNRTIs, so the mechanistic basis is weak. The high score is most likely a knowledge-graph artifact.

Among the other top-10 predictions, only "congenital human immunodeficiency virus" (rank 4) and "AIDS related complex" (rank 5) have meaningful evidence (L3). Both overlap etravirine's approved HIV-1 use, so they are not true repurposing.

**To proceed, the following is needed:**
- In vitro data showing etravirine activity against FIV reverse transcriptase
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications
- Evidence that the prediction is relevant to a veterinary indication, and not just to a shared retroviral neighborhood in the graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

