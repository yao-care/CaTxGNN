---
layout: default
title: Dantrolene
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 7
monitor_inn: "Dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
last_modified_at: 2026-11-20
description: "Dantrolene: predicted new indication moderate multiminicore disease with hand involvement (evidence level L5). In Canada: 3 DINs (3 marketed)"
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dantrolene: Ryanodine receptor–targeting skeletal muscle relaxant → moderate multiminicore disease with hand involvement
{: .text-alpha }

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant. The approved indication is not recorded in the local licence data.
The TxGNN model predicts it may be useful for **moderate multiminicore disease with hand involvement**, but **no clinical trials and no publications** currently support this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | moderate multiminicore disease with hand involvement |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dantrolene: "In isolated nerve-muscle preparation, dantrolene has been shown to produce relaxation by affecting the contractile response of the muscle at a site beyond the myoneural junction. In skeletal muscle, dantrolene dissociates the excitation-contraction coupling, probably by interfering with the release of Ca ++ from the sarcoplasmic reticulum." ([DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698), label version 2024-10-30; accessed 2026-11-19.) Dantrolene is generally understood to act on calcium release in skeletal muscle through the ryanodine receptor.

Multiminicore disease is commonly linked to variants in SELENON or RYR1. A RYR1-related subtype could plausibly share the calcium-handling mechanism that dantrolene targets. This is the only rationale for the prediction. The score is high, but no trial or publication tests the idea, so any benefit remains speculative. The mechanism would also be relevant only to RYR1-related cases, not to SELENON-related disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dantrolene is marketed in Canada, with 3 valid single-ingredient licences and none cancelled. The approved indication text is not recorded in the local data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01997572 | DANTRIUM INTRAVENOUS | Not recorded | Not recorded |
| 02529998 | DANTROLENE SODIUM FOR INJECTION, USP | Not recorded | Not recorded |
| 01997602 | DANTRIUM CAPSULES | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 72 interactions were found in the interaction database. The main ones are:
  - **Major**: morphine and liposomal morphine.
  - **Moderate**: dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol and promethazine.

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and no publications for this disease. The evidence level is therefore L5, and the mechanistic link is a plausible inference only.

**To proceed, the following is needed:**
- Genetic subtyping, to identify whether any patients have RYR1-related disease.
- Preclinical or case-level evidence that dantrolene affects the myopathy itself.
- Detailed mechanism-of-action data.
- Label warnings and contraindications from the Health Canada package insert.
- A safety plan for the interactions listed above, particularly with opioids.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for dantrolene is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

