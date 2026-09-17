---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Threonine: From No Approved Indication to Gastroparesis

## One-Sentence Summary

> Threonine (DB00156) is an essential amino acid with no approved therapeutic indication and no marketed product in Canada.
> The TxGNN model predicts it may be effective for **Gastroparesis**,
> but this is currently supported only by **0 clinical trials** and **1 non-drug-specific mechanistic publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None reported — no approved indication on file |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Threonine is a proteinogenic essential amino acid rather than a conventional pharmacological agent, and it carries no approved indication and no marketed product in Canada. Without a defined MOA or an established original indication, there is no pharmacological baseline from which to assess plausibility for gastroparesis.

The single supporting publication is a basic/mechanistic rat model study of diabetic gastroparesis that examines apoptosis and PI3K-AKT-mTOR / AMPK-mTOR signaling in gastric smooth muscle cells — it does not study threonine itself, and its relevance is marked as "pending." As stated directly in the evidence pack's rationale: the TxGNN score of 0.993 reflects knowledge-graph embedding similarity, not mechanistic evidence, and no meaningful mechanistic link between threonine and gastroparesis can currently be established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Basic/Mechanistic (non-drug-specific) | Molecular Medicine Reports | Rat model of diabetic gastroparesis showing dynamic changes in gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR / AMPK-mTOR signaling; does not evaluate threonine directly |

---

## Canada Market Information

No Health Canada authorizations (DINs) are on file for threonine — the product is not currently marketed in Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN embedding score (Evidence Level L5), with zero clinical trials and only one non-drug-specific mechanistic publication whose relevance is unconfirmed. There is no established MOA, no approved indication, and no Canadian market presence to anchor a repurposing hypothesis.

**To proceed, the following is needed:**
- Mechanism of action data for threonine relevant to gastric motility/gastroparesis pathophysiology
- TFDA/Health Canada label warnings, contraindications, and DDI data (currently blocking safety review per data gap DG001)
- Drug-specific preclinical or clinical evidence directly testing threonine in gastroparesis models
- Confirmation of relevance for the existing mechanistic literature (PMID 28627597) before it can be counted as supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

