---
layout: default
title: Sotatercept
parent: Model Prediction Only (L5)
nav_order: 733
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Unspecified Original Indication to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept's original approved indication is not documented in this evidence pack, and detailed mechanism of action data is currently unavailable. The TxGNN model predicts it may be effective for **Acute Lymphoblastic Leukemia**, but this is currently supported by **0 clinical trials** and **0 publications**, making it a pure model prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on file for this drug |
| Predicted New Indication | Acute Lymphoblastic Leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sotatercept is not available in this evidence pack, and no approved original indication is on file, so a direct original-to-new-indication comparison cannot be made. Based on contextual information found elsewhere in this evidence pack (in the rationale for other ranked candidates), sotatercept belongs to the ActRII ligand-trap drug class — the same class as agents like luspatercept — which modulates TGF-β superfamily signaling (activin/GDF ligands).

However, the mechanistic rationale specifically linking this drug class to **acute lymphoblastic leukemia** has not yet been generated: both `mechanistic_link` and `similarity_to_original` for this top-ranked candidate are marked "pending" in the evidence pack, meaning the automated rationale step has not completed for this indication. This stands in contrast to the other nine candidates (ranks 2–10) in this pack, which do carry preliminary mechanistic text (e.g., TGF-β/activin signaling in retinal fibrosis, osteoclast/osteoblast balance, tumor microenvironment modulation) — yet all of those were still assessed as L5/Hold due to a complete absence of trial or literature support.

Because acute lymphoblastic leukemia is the highest-scoring prediction (99.78%) yet lacks any accompanying rationale, evidence, or safety context, it must be treated as an unvalidated model output pending dedicated mechanistic and evidence review — not as a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Sotatercept currently holds no drug licenses in Canada (market status: **not marketed**, 0 DINs on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (acute lymphoblastic leukemia) has zero supporting clinical trials or literature, and its mechanistic rationale has not yet been generated (marked "pending"). Combined with a **Blocking**-severity gap in TFDA safety warnings/contraindications, this candidate cannot be advanced past initial screening.

**To proceed, the following is needed:**
- TFDA drug label warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- Mechanism of action data via DrugBank API (DG002, High)
- Completion of the pending mechanistic rationale and evidence review specifically for the acute lymphoblastic leukemia prediction
- Targeted clinical trial and literature search for sotatercept in acute lymphoblastic leukemia
- Canada regulatory/market status confirmation (currently 0 DINs, not marketed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

