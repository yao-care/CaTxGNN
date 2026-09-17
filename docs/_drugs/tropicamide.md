---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 808
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Ophthalmic Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a topical ophthalmic anticholinergic agent, currently used only for pupil dilation and cycloplegia in eye examinations. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but this prediction is currently supported by **no clinical trials and no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mydriasis / cycloplegia (topical ophthalmic anticholinergic) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not yet available for this candidate. Based on the information present in this evidence pack, tropicamide is a non-selective muscarinic receptor (M1–M5) antagonist, whose only established clinical use is topical ophthalmic administration for mydriasis and cycloplegia during eye examinations.

Cauda equina syndrome is a neurosurgical emergency caused by mechanical compression of the lumbosacral nerve roots — a pathology with no direct pharmacological relationship to muscarinic receptor blockade. The high TxGNN score most likely reflects an indirect graph connection through shared autonomic bladder/bowel dysfunction nodes (a downstream symptom of cauda equina syndrome that overlaps with anticholinergic-relevant physiology), rather than genuine mechanistic plausibility for treating the underlying nerve root compression.

No clinical trial or literature evidence currently exists to support or refute this hypothesis, and there is no established precedent — as there is with other anticholinergics (e.g., oxybutynin, tolterodine) — for tropicamide use outside the eye. This prediction should be treated as a low-confidence, exploratory model output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Tropicamide currently has no marketed products in Canada (0 DINs on record); no authorization or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only candidate with zero supporting clinical trials or literature, and the underlying rationale explicitly notes a lack of pharmacological plausibility connecting anticholinergic activity to cauda equina syndrome as a causal treatment target. The drug is also not currently marketed in Canada.

**To proceed, the following is needed:**
- Product monograph / official mechanism-of-action data (currently a data gap)
- Safety warnings, contraindications, and drug interaction data (currently unavailable)
- Systemic pharmacokinetic data, since tropicamide is currently only formulated as a topical ophthalmic solution — any non-ophthalmic indication (including the two lower-ranked candidates, neurogenic bladder and irritable bowel syndrome, which have somewhat stronger drug-class precedent) would require evidence of adequate systemic exposure
- At minimum, preclinical or case-level evidence before this candidate can be re-evaluated above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

