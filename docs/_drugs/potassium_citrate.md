---
layout: default
title: Potassium Citrate
parent: Model Prediction Only (L5)
nav_order: 750
evidence_level: L5
indication_count: 10
---

# Potassium Citrate
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

# Potassium Citrate: From an Unspecified Original Indication to Familial Visceral Myopathy

## One-Sentence Summary

Potassium citrate is a urinary alkalinizing agent marketed in Canada as UROCIT-K, but the source data does not list its original approved indication.
The TxGNN model predicts it may be effective for **familial visceral myopathy**, but **0 clinical trials** and **0 publications** support this prediction.
It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the source data (the approved indication text is empty) |
| Predicted New Indication | Familial visceral myopathy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Potassium citrate is known to raise urinary pH and urinary citrate. However, no identifiable mechanistic link to familial visceral myopathy, a rare genetic disorder of gut smooth muscle, was found.

The prediction rests on the TxGNN score alone, so it should be treated as a hypothesis, not a supported use. The high score reflects the model's knowledge-graph patterns, and no trial or publication in the evidence pack backs it.

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
| 2353997 | UROCIT-K | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were retrieved for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The familial visceral myopathy prediction has no clinical trials, no literature, and no identifiable mechanistic link. The score alone is not enough to justify further investment.

**Other predictions in the pack:**
The best-supported candidate is **nephrolithiasis** (rank 4). It has a completed Phase 3 randomized trial of potassium citrate in absorptive hypercalciuria ([NCT00004284](https://clinicaltrials.gov/study/NCT00004284), n=300). It also has a Phase 2/3 stent-encrustation trial ([NCT06819553](https://clinicaltrials.gov/study/NCT06819553)) and a 2017 meta-analysis ([PMID 27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/)). This is probably an established use whose indication field is missing from the source data. The pack grades it L1, but only one completed Phase 3 trial was confirmed, so L1 (which needs at least two) should be rechecked. A separate report on it is worth preparing.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm the approved indications, warnings, and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Any genetic or mechanistic rationale linking potassium citrate to visceral myopathy; without one, deprioritize this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

