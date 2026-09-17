---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin Lispro is a rapid-acting insulin analog used for glycemic control in diabetes mellitus. The TxGNN model predicts a possible link to **Autoimmune Oophoritis**, with a very high raw prediction score (99.78%), but **zero clinical trials** and **zero publications** currently support this specific drug-disease pair, and the underlying mechanistic rationale suggests the association may reflect disease comorbidity rather than a genuine treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (glycemic control) — specific Health Canada label text not available in this evidence pack |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, insulin lispro is a rapid-acting insulin analog that activates the insulin receptor to promote glucose uptake; its efficacy in diabetes mellitus is well established.

However, the mechanistic rationale supplied with this candidate is explicit that **no known mechanistic pathway connects insulin/insulin-receptor signaling to autoimmune oophoritis**. The two conditions co-occur only because both can appear within Autoimmune Polyglandular Syndrome (APS), where autoimmune oophoritis and Type 1 diabetes are sometimes seen in the same patient. This is a **comorbidity association, not a causal or treatment relationship** — the TxGNN score most likely reflects shared autoimmune-disease network proximity in the knowledge graph rather than a therapeutic signal.

Given the absence of any supporting trial or literature evidence, and an explicit statement in the rationale that the link is non-causal, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada label warnings and contraindications are recorded as a Blocking-severity data gap (DG001) — this prevents any formal safety pre-screening (S1) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (autoimmune oophoritis) has no clinical trial or literature support (Evidence Level L5), and its own mechanistic rationale indicates the TxGNN association is likely driven by disease comorbidity rather than a plausible treatment pathway. Combined with a Blocking data gap on product safety labeling, there is currently no basis to advance this candidate past model prediction.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism-of-action data for insulin lispro (DG002)
- Independent literature or preclinical validation specifically linking insulin/insulin-receptor signaling to autoimmune oophoritis pathophysiology

**Additional note on other candidates in this evidence pack:** Among the 9 predicted indications for insulin lispro, one — *pancreatic agenesis* (rank 7, L3, 2 PubMed reviews) — is the most credible signal, but it reflects an existing clinical practice (insulin replacement in congenital neonatal diabetes) rather than a novel repurposing opportunity. Three others — *drug-induced localized lipodystrophy*, *centrifugal lipodystrophy*, and *pressure-induced localized lipoatrophy* — appear to have **reversed causality**: insulin injection is a known cause of these conditions, not a treatment for them, and should be excluded from further repurposing evaluation rather than pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

