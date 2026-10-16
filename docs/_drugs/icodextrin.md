---
layout: default
title: Icodextrin
parent: Model Prediction Only (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Icodextrin: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not stated in the Canadian licence data (the drug is used as an osmot…"
---

# Icodextrin
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

# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a high-molecular-weight glucose polymer used as an osmotic agent in peritoneal dialysis. The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but this is a computational prediction only. There are currently **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data (the drug is used as an osmotic agent in peritoneal dialysis) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, icodextrin is a glucose polymer that acts as an osmotic agent in peritoneal dialysis and is minimally absorbed from the peritoneal cavity.

No plausible mechanistic link to irritable bowel syndrome has been established. Icodextrin has no known action on gut motility, visceral hypersensitivity, or the gut-brain axis. The high score of 98.53% reflects knowledge-graph connectivity rather than biological or clinical evidence, so the prediction should be treated with caution.

The other top-ranked predictions are also unsupported by mechanism or evidence:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Non-syndromic esophageal malformation | 97.41% | Congenital structural anomaly; no plausible mechanism, likely a graph artifact |
| 3 | C1 inhibitor deficiency | 97.29% | No effect on C1-INH, kallikrein, or bradykinin pathways |
| 4 | Potassium deficiency disease | 97.19% | Icodextrin does not supply or retain potassium |
| 5 | Serpinopathy with toxic serpin polymerization | 97.06% | Not a chaperone, polymerization inhibitor, or protease modulator |
| 6 | Hereditary angioedema with C1Inh deficiency | 96.81% | Overlaps with rank 3; likely shared graph neighbours |
| 7 | Esophageal disease | 96.77% | Broad, nonspecific category match |
| 8 | Familial visceral myopathy | 96.34% | No known effect on smooth muscle function |
| 9 | Renal tubular acidosis | 95.81% | Only a weak, indirect link through the dialysis setting; does not correct tubular acid handling |
| 10 | Vitamin deficiency disorder | 95.78% | Does not supply vitamins; dialysis nutrient loss is a safety concern |

All ten predictions are at evidence level L5 with no registered trials and no literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240806 | EXTRANEAL | Not available | Not available |

## Safety Considerations

Please refer to the package insert for safety information.

Some general considerations arise from the dialysis context. Dialysis-related electrolyte shifts, metabolic acid-base changes, and nutrient losses are possible concerns. No interaction records were found for this drug in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for irritable bowel syndrome rests only on a knowledge-graph score. There is no mechanistic link, no clinical trial, and no literature. Safety information from the Canadian label is also missing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings and contraindications), which blocks safety screening
- Mechanism of action data, for example from DrugBank
- Original approved indication text for the EXTRANEAL licence
- A plausible biological rationale and preclinical or clinical evidence for irritable bowel syndrome
- Assessment of route compatibility, since icodextrin is administered intraperitoneally and is minimally absorbed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

