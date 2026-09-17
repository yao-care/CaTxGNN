---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a prostaglandin F2α analogue (FP receptor agonist) whose established pharmacology reduces intraocular pressure in open-angle glaucoma/ocular hypertension. The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**, but currently **no clinical trials and no literature** support this direction — the prediction is not yet corroborated by any external evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in Canadian regulatory filings (product not marketed); based on known pharmacology, travoprost is used for open-angle glaucoma/ocular hypertension |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, travoprost is a prostaglandin F2α analogue (FP receptor agonist), used topically to lower intraocular pressure by increasing uveoscleral outflow; its efficacy in open-angle glaucoma and ocular hypertension has been confirmed across multiple Phase 3/4 trials embedded in this evidence pack (albeit under a different candidate indication).

However, for the top-ranked predicted indication — visceral calciphylaxis — the evidence pack explicitly states there is **no mechanistic, trial, or literature evidence** linking travoprost to this disease. Visceral calciphylaxis is a vascular calcification disorder, and there is no established biological rationale connecting a topical FP receptor agonist (with minimal systemic bioavailability) to this condition. The evidence pack itself flags this as a likely **non-specific model artifact**, arising from TxGNN's tendency to cluster high-dimensional vascular disease semantics rather than reflecting a genuine pharmacological relationship.

It is worth noting that lower-ranked candidates in this pack (e.g., "vascular disease," rank 5; "hemangioendothelioma," rank 10) do carry some literature and trial evidence — but on inspection, that evidence pertains to travoprost's **original glaucoma indication** (IOP-lowering trials, hyperemia studies, an adverse-event case report of uveal effusion), not to treatment of the vascular disease itself. This represents a disease-label mismatch rather than genuine repurposing support, and does not strengthen the case for the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Travoprost currently holds no Drug Identification Numbers (DINs) in Canada (0 licenses on file); the product is not marketed. No approved indication text is available for reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) has an extremely high TxGNN score but zero supporting clinical trials or literature, and the evidence pack itself identifies this as a likely non-specific model artifact with no biological rationale. Combined with the drug's unmarketed status in Canada (no DINs, no accessible label/warnings), there is insufficient basis to advance to safety screening (S1).

**To proceed, the following is needed:**
- Confirmed MOA data via DrugBank API query (currently a Blocking data gap)
- TFDA/Canadian product monograph or package insert for warnings and contraindications (currently a Blocking data gap)
- Preclinical or mechanistic studies specifically linking FP receptor agonism to vascular calcification pathways
- If evidence quality is prioritized over score ranking, consider re-scoping evaluation to candidates with at least partial trial/literature coverage (e.g., "vascular disease," rank 5) — while noting that even those data currently reflect travoprost's original glaucoma indication rather than genuine repurposing evidence, and would need disease-specific evidence before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

