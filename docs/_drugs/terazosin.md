---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 889
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From an Alpha-1 Adrenergic Blocker to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker marketed in Canada. Its approved indication text is not recorded in the data provided.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare hereditary hair-loss disorder. There are **0 clinical trials** and **0 publications** for this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, terazosin is an alpha-1 adrenergic blocker marketed in Canada. No established pharmacological link to hair growth has been identified.

The high score most likely reflects proximity in the knowledge graph to other hair-loss conditions, not a pharmacological rationale. Hypotrichosis simplex is a hereditary disorder, and alpha-1 blockade would not be expected to act on it. The score alone is not enough to justify further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Terazosin is marketed in Canada under 8 licences. Five are listed below. Dosage form and approved indication text are not available for these records.

| DIN | Product Name |
|---------|------|
| 02243521 | PMS-TERAZOSIN |
| 02234503 | APO-TERAZOSIN |
| 02243519 | PMS-TERAZOSIN |
| 02243518 | PMS-TERAZOSIN |
| 02243520 | PMS-TERAZOSIN |

## Safety Considerations

Please refer to the package insert for safety information.

Orthostatic hypotension is a known consideration for alpha-1 blockade. No interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature and no plausible mechanism, so the high score likely reflects a knowledge-graph artifact.

Other predicted indications have more support than the top-ranked one:

| Predicted Indication | Score | Evidence Level | Available Evidence | Assessment |
|------|------|------|------|------|
| Raynaud disease | 99.83% | L3 | 1997 clinical study of terazosin (PMID [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/)), design unverified | Plausible mechanism (reduced sympathetic vasoconstriction). Research question. |
| Migraine disorder | 99.92% | L3 | 1994 open study (PMID [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/)) and 1997 case series (PMID [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/)) | Old, small, uncontrolled. Research question. |
| Alopecia | 99.95% | L4 | One broad review of extracardiac effects of cardiovascular drugs (PMID [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/)) | Indirect support only. Hold. |

The other predictions have no clinical evidence and no plausible mechanism (L5, Hold). These are congenital hypotrichosis milia, diffuse alopecia areata, Ambras type hypertrichosis, manic bipolar disorder and kyphoscoliotic heart disease. Migraine with brainstem aura is L4 with only indirect evidence, also Hold.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A review of the Raynaud and migraine studies to confirm their design and results
- For any pursued indication, a controlled study with modern diagnostic criteria

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

