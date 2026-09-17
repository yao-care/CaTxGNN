---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 813
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

Using no specific skill — this is a direct content-generation task with an explicit template and complete input data, not a coding/build/debug task.

---

# Upadacitinib: From Undocumented Original Indication to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib's original approved indication is not documented in the current evidence pack (mechanism of action is also a recorded data gap, though the model's own rationale identifies it as a JAK1/JAK-STAT pathway inhibitor). The TxGNN model predicts a possible association with **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare congenital skeletal/ocular malformation syndrome, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags the signal as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not currently documented in this evidence pack |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.61% (rank 7787 of scored disease nodes) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for upadacitinib is recorded as a data gap in this evidence pack (DG002). However, the model's own repurposing rationale references upadacitinib's known pharmacology as a **JAK1 / JAK-STAT signaling pathway inhibitor**, which is the pharmacological class this drug belongs to.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital malformation syndrome combining ocular coloboma (embryonic eye development defect) and rhizomelic skeletal dysplasia (limb development defect). These conditions are typically caused by developmental/structural gene defects (e.g., peroxisome biogenesis genes such as the PEX family, or ciliary-related genes) — a fundamentally different biological process from the inflammatory/autoimmune signaling that JAK1 inhibition targets.

**This prediction is not considered mechanistically reasonable.** The evidence pack itself concludes that the high TxGNN score most likely reflects a sparse knowledge-graph node (few connections for this ultra-rare disease) rather than a genuine drug-repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Upadacitinib currently holds **no Health Canada authorizations (DINs)** in this dataset (`total_licenses: 0`); no product listing is available for this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Note that TFDA/product-label warnings and contraindications for upadacitinib are currently marked as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any safety pre-assessment (S1) can proceed.

## Other Predicted Indication (Rank 2, for context)

| Item | Content |
|------|------|
| Disease | Brachydactyly-syndactyly syndrome |
| TxGNN Score | 99.58% (rank 8272) |
| Evidence | 0 trials, 0 publications |
| Rationale | Congenital limb malformation (HOX/SHH/BMP pathway), structurally unrelated to JAK1 inhibition; same "sparse graph node" caveat applies |
| Recommendation | Hold |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are ultra-rare congenital malformation syndromes with no supporting clinical trials or literature (Evidence Level L5), and the model's own mechanistic analysis judges them as biologically implausible relative to upadacitinib's JAK1-inhibitory mechanism — most likely knowledge-graph noise from sparse rare-disease nodes. In addition, the drug is not currently marketed in Canada (0 DINs), and a Blocking safety data gap (TFDA label warnings/contraindications) prevents any safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official product label for warnings/contraindications
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Document upadacitinib's actual approved original indication(s) for comparative analysis
- If pursued further, seek independent mechanistic or genetic evidence linking JAK-STAT signaling to either predicted syndrome before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

