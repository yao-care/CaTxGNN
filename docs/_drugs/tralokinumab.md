---
layout: default
title: Tralokinumab
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Tralokinumab
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

Using the evidence pack as given (no external MOA/label lookup performed — see note at the end).

# Tralokinumab: From Atopic Dermatitis to Diabetic Cataract

## One-Sentence Summary

> Tralokinumab is an anti-IL-13 monoclonal antibody used for atopic dermatitis (based on mechanism-of-action context in the evidence pack; not confirmed in structured regulatory records).
> The TxGNN model predicts it may be effective for **Diabetic Cataract**,
> but **no clinical trials** and **no publications** currently support this direction, and the evidence pack's own mechanistic review flags it as a likely false-positive knowledge-graph association.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (inferred from mechanism-of-action note; `original_indications` field is empty in source data) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.69% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa` is a data gap). Based on the mechanistic notes attached to this candidate, Tralokinumab is an anti-IL-13 monoclonal antibody approved for atopic dermatitis, targeting the Th2 inflammatory axis.

Diabetic cataract, however, is primarily driven by the aldose reductase/sorbitol-polyol pathway causing osmotic lens changes and oxidative stress — a metabolic mechanism unrelated to IL-13-driven inflammation. The lens is also an avascular, immune-privileged tissue, making it difficult for a large systemic antibody to reach the target site. The evidence pack's own analysis explicitly concludes there is **no supporting mechanistic link**, and given the total absence of clinical trials or literature, this ranks as a probable false-positive association from the knowledge-graph embedding layer rather than a genuine repurposing signal.

Worth noting: among the 10 TxGNN-predicted indications for this drug, rank #10 (diabetic retinopathy) has a comparatively more plausible rationale — IL-13/Th2 cytokines have been indirectly linked to retinal neuroinflammation and vascular permeability in the literature — but it likewise has zero clinical trial or publication support and remains an unvalidated hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

No Health Canada marketing authorizations are currently on file for this drug (0 DINs; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this is an L5, model-only association with zero clinical trial or literature support. The evidence pack's mechanistic review directly contradicts biological plausibility — diabetic cataract pathogenesis (polyol pathway, lens osmotic/oxidative damage) does not align with Tralokinumab's IL-13/Th2 mechanism, and lens tissue has poor accessibility for systemic antibodies.

**To proceed, the following is needed:**
- Confirmed original indication and regulatory record (`original_indications` field currently empty)
- MOA documentation from DrugBank (currently a High-severity data gap, DG002)
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap, DG001) — required before any S1 safety screening
- Any preclinical or mechanistic studies specifically linking the IL-13 pathway to lens pathology, should they emerge, before re-evaluating this candidate
- If pursuing further, diabetic retinopathy (rank #10) may warrant separate tracking as a mechanistically more plausible — though still unvalidated — alternative candidate

---
Two items above (TFDA label PDF, DrugBank MOA API query) require external data retrieval not available in this session's evidence pack and were not fetched — they remain open per data gaps DG001/DG002 in `meta.data_gaps`.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

