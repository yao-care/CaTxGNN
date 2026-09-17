---
layout: default
title: Trifarotene
parent: Model Prediction Only (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
---

# Trifarotene
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

# Trifarotene: From Data Gap (Original Indication Unavailable) to Zinc, Elevated Plasma

## One-Sentence Summary

> Trifarotene is a RAR-γ selective topical retinoid; its original approved indication is not documented in this evidence pack (data gap).
> The TxGNN model predicts a possible association with **Zinc, Elevated Plasma**,
> but **no clinical trials** and **no literature** currently support this direction, and the model's own rationale flags no direct biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.40% (rank 10704) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Trifarotene in this evidence pack. Based on the repurposing rationale supplied alongside the prediction, Trifarotene is a RAR-γ selective topical retinoid, a drug class typically used for keratinization/sebaceous gland disorders (e.g., acne-type conditions), though the original approved indication itself is not recorded here.

For the top-ranked prediction, "Zinc, Elevated Plasma," the model's own mechanistic annotation states: *"Trifarotene is a RAR-γ selective topical retinoid with no known pharmacological mechanism related to zinc metabolism or plasma zinc regulation. The high TxGNN score likely reflects an indirect node connection in the knowledge graph (e.g., shared skin-metabolism comorbidity), with no direct biological plausibility."*

In other words, this prediction should be treated as a graph-topology artifact rather than a mechanistically grounded repurposing candidate. Among the other nine ranked candidates in this pack, several (e.g., demodicidosis of sebaceous gland) have marginally more plausible mechanistic links to a topical retinoid's known pharmacology, but all ten candidates remain at evidence level L5 with zero supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Trifarotene currently has no marketed products or DIN authorizations in Canada (`market_status: Not marketed`, `total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information. (Note: a blocking data gap exists for TFDA/Health Canada label warnings and contraindications, which prevents any S1 safety pre-assessment for this candidate.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical or literature support, sits at evidence level L5 (model prediction only), and the mechanistic rationale explicitly states there is no direct biological plausibility. Trifarotene is also not currently marketed in Canada, and a blocking data gap on drug label warnings prevents any safety pre-screening.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action (MOA) for Trifarotene (currently data gaps)
- TFDA/Health Canada label warnings and contraindications (blocking gap, required for S1 safety screening)
- Independent mechanistic or preclinical evidence linking RAR-γ agonism to plasma zinc regulation, or reassessment of this TxGNN candidate given the flagged lack of biological plausibility
- If pursuing repurposing, consider re-ranking lower candidates (e.g., demodicidosis of sebaceous gland) which have comparatively more plausible—though still unvalidated—mechanistic links to this drug class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

