---
layout: default
title: Patisiran
parent: Model Prediction Only (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
---

# Patisiran
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

# Patisiran: From Hereditary Transthyretin-Mediated (hATTR) Amyloidosis to Dermatitis

## One-Sentence Summary

Patisiran (DrugBank DB14582) is an siRNA therapeutic that silences TTR mRNA, developed for hereditary transthyretin-mediated (hATTR) amyloidosis. The TxGNN model predicts potential activity in **Dermatitis** with a raw similarity score of **90.65%**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal with no corroborating evidence.

*Note: formal original-indication text could not be extracted (no regulatory licenses on file); the indication above is inferred from the mechanistic description embedded in the evidence pack's own rationale fields (TTR mRNA-targeting siRNA for hereditary TTR-mediated amyloidosis).*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary transthyretin-mediated (hATTR) amyloidosis *(inferred from MOA description; no formal license record available)* |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 90.65% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap). Based on the limited information on file, Patisiran is known to act as a small interfering RNA (siRNA) that silences hepatic transthyretin (TTR) mRNA production, reducing circulating mutant and wild-type TTR protein responsible for amyloid fibril deposition in hATTR amyloidosis.

For all ten TxGNN-predicted candidates in this evidence pack — including the top-ranked Dermatitis — the model's own rationale text explicitly states there is **no known pathological or mechanistic link** to TTR gene silencing. The predicted scores derive purely from knowledge-graph embedding similarity, not from any pharmacological, genetic, or clinical rationale. None of the ten candidates (dermatitis, hydroa vacciniforme, amyopathic/neonatal dermatomyositis, acne keloid, childhood interstitial lung disease, acrodermatitis chronica atrophicans, two mastocytosis subtypes, overactive bladder) share an established biological pathway with TTR silencing.

This means the prediction should be treated as a hypothesis-generation signal only, not as evidence of plausible clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Dermatitis prediction sits at Evidence Level L5 (model prediction only) with no clinical trials, no literature, and no mechanistic plausibility identified even within the evidence pack's own analysis. A blocking data gap on regulatory warnings/contraindications (DG001) also prevents any safety pre-screen (S1) from being initiated.

**To proceed, the following is needed:**
- Verified mechanism of action (MOA) data for Patisiran (DG002)
- Regulatory label / warnings and contraindications data (DG001, blocking)
- Independent mechanistic or preclinical rationale linking TTR silencing to dermatologic/immune-mediated conditions, since none currently exists
- Confirmation this candidate should remain in the pipeline given the absence of any supporting evidence across all top-10 predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

