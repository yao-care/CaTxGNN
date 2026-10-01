---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
---

# Octreotide
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

# Octreotide: From an Unspecified Original Indication to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analog marketed in Canada, but the licence records provided do not state its approved indications.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data provided |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Octreotide is a somatostatin analog and is marketed in Canada in several products, including Sandostatin and injectable suspension formulations. The approved indication text is missing from the licence data, so the link between its original use and the predicted new indication cannot be assessed.

The data do not support a mechanistic link to vulvar inverted follicular keratosis. The high score (0.996) is a graph-based prediction only. Any role for somatostatin receptor signalling in skin or follicular epithelium would be speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this predicted indication.

For context, the other top-ranked predictions are also weakly supported:
- **Addison disease** (rank 4, score 98.74%, L4) has two relevant papers.
  - [PMID 17984930](https://pubmed.ncbi.nlm.nih.gov/17984930/) (2007, case report) describes ACTH suppression in a probable corticotropic adenoma coexisting with Addison's disease. It does not show treatment of adrenal insufficiency.
  - [PMID 1973178](https://pubmed.ncbi.nlm.nih.gov/1973178/) (1990, physiological study) found that octreotide and somatostatin did not acutely affect hypothalamic-pituitary-adrenal function, which argues against a therapeutic role.
- **Adrenocortical insufficiency** (rank 8) has one pituitary pathology series, which is not a treatment study.
- The remaining predictions have no trials or literature.

## Canada Market Information

Dosage form, manufacturer and approved indication text were not provided for these licences.

| DIN | Product Name |
|---------|------|
| 2248640 | OCTREOTIDE ACETATE OMEGA |
| 839191 | SANDOSTATIN |
| 2248641 | OCTREOTIDE ACETATE OMEGA |
| 2503778 | OCTREOTIDE FOR INJECTABLE SUSPENSION |
| 2503751 | OCTREOTIDE FOR INJECTABLE SUSPENSION |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data provided.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (L5) and no plausible mechanism in the available data. The package insert and mechanism of action data are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications), which currently blocks safety screening
- Mechanism of action data for octreotide (for example, from DrugBank)
- A dedicated literature and trial search for vulvar inverted follicular keratosis, with a biological rationale for a somatostatin analog in this condition
- Review of the other top-ranked predictions. Two nephrotic syndrome entries have identical scores (98.57%), which suggests a shared disease-node artifact.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

