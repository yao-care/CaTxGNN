---
layout: default
title: Teprotumumab
parent: Model Prediction Only (L5)
nav_order: 760
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: Exploring Monosomy X as a Predicted New Indication

## One-Sentence Summary

> Teprotumumab (DB06343) is not currently marketed in Canada, and no approved-indication or mechanism-of-action data are on file for this drug in the evidence pack.
> The TxGNN model's top-ranked prediction is **Monosomy X** (score **99.79%**), but this candidate has **0 clinical trials** and **0 publications** supporting it, and the pack's own pharmacological review flags several closely related top-10 predictions as likely knowledge-graph embedding artifacts rather than genuine mechanistic signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication data on file (drug not marketed in Canada) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for teprotumumab is not available in this evidence pack (flagged as a High-severity data gap, DG002), and the drug currently has no on-file original indication or Canadian market authorization (0 DINs, "not marketed"). This severely limits our ability to assess mechanistic plausibility for any predicted new use.

That said, the pack's own pharmacologist-authored rationale for the surrounding top-10 candidates repeatedly references teprotumumab's known action as an **IGF-1R antagonist** (with possible TSHR pathway involvement). Using that partial mechanistic context, the reviewer explicitly concluded that **9 of the top 10 predictions — including Monosomy X and its closely related variants (Turner syndrome, mosaic monosomy X, X chromosome number anomaly, mixed gonadal dysgenesis)** — have **no plausible mechanistic link** to IGF-1R blockade. These conditions are chromosomal/developmental disorders (X-chromosome anomalies, gonadal dysgenesis) or vascular/structural conditions (esophageal varices, varicose disease) with etiologies unrelated to IGF-1R signaling.

One entry in this cluster (sex chromosome disorder of sex development, rank 8) is explicitly annotated in the evidence pack as **likely an artifact of node-embedding similarity** in the knowledge graph — i.e., diseases clustering together in TxGNN's embedding space due to shared ontological categorization (rare chromosomal/developmental disease grouping), not shared drug-response biology. Given that Monosomy X sits at the top of this same score band and disease family, the same concern applies: this prediction should be treated as a **candidate for exclusion/artifact review** rather than a genuine repurposing lead, pending expert curation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Teprotumumab is **not currently marketed in Canada** — no DIN-listed products are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack. DG001 — TFDA/Health Canada label warnings and contraindications — is classified as Blocking, meaning this candidate cannot proceed to safety pre-screening until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is unsupported by any clinical trial or literature evidence (Evidence Level L5), the drug has no confirmed original indication or MOA on file, and the pack's own mechanistic review found no plausible pharmacological link between IGF-1R antagonism and Monosomy X or its related top-ranked neighbors — several of which are explicitly flagged as probable embedding artifacts rather than genuine signals.

**To proceed, the following is needed:**
- TFDA/Health Canada label data resolving the Blocking safety gap (DG001: warnings/contraindications)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Expert curation of the full top-10 prediction list to distinguish genuine mechanistic candidates from knowledge-graph clustering artifacts before any further evaluation
- Confirmation of teprotumumab's actual approved indication(s) to enable a meaningful original-vs-new indication comparison
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

