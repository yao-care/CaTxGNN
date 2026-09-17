---
layout: default
title: Silodosin
parent: Model Prediction Only (L5)
nav_order: 716
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Silodosin: From α1A-Mediated Lower Urinary Tract Action to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Silodosin is a highly selective α1A-adrenergic receptor antagonist acting primarily on prostate and lower urinary tract smooth muscle; no formal original indication or approved-label data is present in this evidence pack.
> The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare genetic disorder unrelated to known α1A receptor biology.
> This prediction is supported by **0 clinical trials** and **0 publications** — it is a pure model-generated signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (mechanistically associated with α1A-adrenergic antagonism on prostate / lower urinary tract smooth muscle) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (MOA) is not available for silodosin in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic rationale text associated with this candidate, silodosin is a highly selective α1A-adrenergic receptor antagonist, exerting its pharmacological effect mainly on prostate and lower urinary tract smooth muscle.

Ambras type hypertrichosis universalis congenita is a rare congenital disorder driven by chromosome 8 rearrangements affecting developmental gene expression, with no known connection to α1A-adrenergic receptor signaling. The evidence pack's own repurposing rationale explicitly states that the TxGNN score reflects knowledge-graph embedding similarity only, with **no mechanistic plausibility identified**.

This is a case where a very high TxGNN score (99.99%) is not accompanied by any biological rationale, clinical trial, or literature support — a pattern consistent with knowledge-graph "false positive" clustering rather than a genuine repurposing signal. The same pattern holds across all six ranked predictions in this pack (see below), reinforcing that this candidate should not be advanced without independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

*Note: Among the other ranked candidates in this evidence pack, rank 3 ("malformation syndrome with odontal/periodontal component") returned 20 literature hits, but all are general periodontology studies (diabetes-periodontitis links, scaling/root planing, gingival fibroblast biology, etc.) with no mention of silodosin or α1A-adrenergic pharmacology. These appear to be keyword-matching noise rather than genuine supporting evidence, and further reinforce the overall "Hold" pattern across this evidence pack.*

## Canada Market Information

Silodosin is currently **not marketed** in Canada (no DIN records available; `total_licenses = 0`). No approved indication, brand name, or dosage form data exists in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings and contraindications are flagged as data gaps in this pack — notably, TFDA/label warning-contraindication data (DG001) is marked as a **Blocking** severity gap, preventing entry into the S1 safety pre-screening stage. No drug-drug interaction data was found.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications for silodosin in this evidence pack are rated L5 (model prediction only, no supporting studies), and the repurposing rationale texts explicitly state there is no mechanistic plausibility linking α1A-adrenergic antagonism to any of the predicted diseases (hypertrichosis syndromes, periodontal malformation syndrome, Dandy-Walker malformation, hair shaft abnormalities, trichomegaly). Combined with a Blocking-severity data gap on TFDA safety labeling and a High-severity gap on MOA, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/official label data on warnings and contraindications (DG001, Blocking — required before any S1 safety pre-screening)
- Confirmed mechanism of action (MOA) documentation via DrugBank or equivalent source (DG002, High)
- Independent mechanistic or preclinical evidence linking α1A-adrenergic receptor pathways to the predicted phenotypes, before any clinical hypothesis is considered credible
- Re-evaluation of literature/trial search queries, as current hits (e.g., periodontology literature under rank 3) appear to be keyword-matching artifacts rather than relevant evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

