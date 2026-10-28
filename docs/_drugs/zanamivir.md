---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 988
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
description: "Zanamivir: predicted new indication Pyelonephritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zanamivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Zanamivir: Pyelonephritis
{: .text-alpha }

## One-Sentence Summary

Zanamivir is an antiviral drug originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zanamivir is known to be a viral neuraminidase inhibitor, and its efficacy in influenza is established. However, the mechanism does not readily extend to pyelonephritis.

Pyelonephritis is mainly a bacterial infection of the upper urinary tract, most often caused by *E. coli*. Some bacteria produce neuraminidase-like enzymes (sialidases), but zanamivir has no established antibacterial activity. Its poor systemic bioavailability (inhaled or intravenous use only) further limits plausibility.

The very high TxGNN score (0.9984) comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis-generating signal, not as supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pyelonephritis.

*Note on the second-ranked prediction (disorder of tyrosine metabolism, score 0.9902):* the three publications retrieved concern oseltamivir resistance, a neuraminidase inhibition assay, and a neuraminidase mutation in H5N1 influenza. None address tyrosine metabolism, and no mechanistic link is apparent. This prediction is likely a TxGNN model (deep learning) artifact.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240863 | RELENZA | Not listed | Not listed |

---

## Safety Considerations

**Knowledge-graph contraindication associations** (these come from the model's knowledge graph, not from label text, and should be verified against the product monograph):
- Epilepsy
- Chronic obstructive pulmonary disease (including severe early-onset COPD)
- Bronchial disease
- Delirium

**Drug Interactions** (8 recorded; only one has a severity rating):
- Insulin human (inhalation, rapid acting): Moderate
- Severity not classified: clarithromycin, loratadine, montelukast, ketotifen, fexofenadine, ibuprofen, diclofenac

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a model prediction (L5). There are no clinical trials or relevant publications, and no plausible mechanistic link between a viral neuraminidase inhibitor and a bacterial kidney infection. The poor systemic exposure of zanamivir further reduces feasibility.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale for activity in pyelonephritis
- Evidence of antibacterial or relevant host-directed activity (preclinical studies)
- Route and formulation compatibility assessment, since zanamivir is available only by inhalation or intravenous use
- Health Canada product monograph warnings and contraindications, to complete safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

