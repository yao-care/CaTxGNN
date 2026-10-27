---
layout: default
title: Nusinersen
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nusinersen: predicted new indication Neoplasm of immature B and T cells (evidence level L5). Approved use: Spinal muscular atrophy"
monitor_inn: "Nusinersen"
predicted_indications: ["neoplasm of immature B and T cells", "myeloid/lymphoid neoplasms associated with eosinophilia and abnormality of PDGFRA, PDGFRB, FGFR1 or JAK2", "exanthem (disease)", "cytomegalovirus infection", "malignant teratoma of mediastinum", "papilloma of buccal mucosa", "neoplasm of mature T-cells or NK-cells", "drug-induced localized lipodystrophy", "leiomyoma of ciliary body", "isolated asymptomatic elevation of creatine phosphokinase"]
---

# Nusinersen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Nusinersen: From Spinal Muscular Atrophy to Neoplasm of Immature B and T Cells
{: .text-alpha }

## One-Sentence Summary

Nusinersen was originally developed to treat spinal muscular atrophy (SMA).
The TxGNN model predicts it may be effective for **neoplasm of immature B and T cells**, but the prediction score is non-informative (50%), and there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (the Canadian licence has no indication text on record; this comes from the knowledge graph) |
| Predicted New Indication | Neoplasm of immature B and T cells |
| TxGNN Prediction Score | 50.0% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Nusinersen is known to be an antisense oligonucleotide that modulates SMN2 splicing to increase SMN protein in spinal muscular atrophy.

No mechanistic link to immature B/T-cell neoplasms was identified. A score of 0.5 does not discriminate between candidates, so this prediction rests on the model alone. Nothing in the data compiled for this report connects SMN2 splice modulation to the biology of these blood cancers.

The same applies to the other nine predictions generated for this drug (for example myeloid/lymphoid neoplasms with eosinophilia, cytomegalovirus infection, exanthem and papilloma of the buccal mucosa). All carry the same non-informative score of 0.5, have no clinical trials, and have no plausible mechanistic rationale. The one publication retrieved for any of them (PMID 38750052, listed under neoplasm of mature T-cells or NK-cells) is an immunology study in SMA patients, not evidence of activity against a neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02465663 | SPINRAZA | Not specified | Not specified |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, and no drug interaction records were found. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it, no identified mechanistic link, and an uninformative model score of 0.5. It is a model-generated suggestion only (evidence level L5).

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to allow a proper mechanistic analysis
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Preclinical or mechanistic evidence that nusinersen affects immature B/T-cell neoplasm biology
- A more discriminating prediction or an independent rationale, since the current score does not separate this candidate from the others
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

