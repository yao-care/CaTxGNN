---
layout: default
title: Dornase Alfa
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dornase Alfa: predicted new indication Paroxysmal hemicrania (evidence level L5). Approved use: Cystic fibrosis"
monitor_inn: "Dornase alfa"
predicted_indications: ["paroxysmal Hemicrania", "xanthoma disseminatum", "xanthogranuloma", "benign cephalic histiocytosis", "generalized eruptive histiocytosis", "Langerhans cell histiocytosis", "trigeminal autonomic cephalalgia", "phacolytic glaucoma", "congenital epulis", "necrobiotic xanthogranuloma"]
---

# Dornase Alfa
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

# Dornase alfa: From Cystic Fibrosis to Paroxysmal Hemicrania

## One-Sentence Summary

Dornase alfa is a recombinant human DNase I originally used to treat cystic fibrosis.
The TxGNN model predicts it may be effective for **paroxysmal hemicrania**, but the prediction score is non-discriminating (50%).
There are currently **no clinical trials** and **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis |
| Predicted New Indication | Paroxysmal hemicrania |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dornase alfa is a recombinant human DNase I that cleaves extracellular DNA and thereby reduces mucus viscosity. This property is the basis for its use in cystic fibrosis.

Paroxysmal hemicrania is a trigeminal autonomic cephalalgia driven by hypothalamic and trigeminovascular activation, and it characteristically responds to indomethacin. No plausible mechanistic link to DNase-mediated reduction of mucus viscosity has been identified.

The score of 0.5 does not discriminate between candidates. Nine other predicted indications share the same score, including xanthoma disseminatum, xanthogranuloma, benign cephalic histiocytosis, generalized eruptive histiocytosis, Langerhans cell histiocytosis, trigeminal autonomic cephalalgia, phacolytic glaucoma, congenital epulis and necrobiotic xanthogranuloma. None has clinical or literature support. The prediction should therefore be regarded as purely computational.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046733 | PULMOZYME | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: One interaction is recorded. Insulin human (inhalation, rapid acting) has a **Moderate** level interaction (source: DDInter).

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score of 0.5, with no clinical trials, no publications and no plausible mechanistic link between DNase activity and paroxysmal hemicrania. Indomethacin already provides an effective, well-established treatment for this condition, so there is little rationale for pursuing this candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- A credible mechanistic hypothesis and preclinical evidence linking extracellular DNA degradation to paroxysmal hemicrania
- Route compatibility assessment (dornase alfa is an inhaled product, and the required route for the new indication is not defined)
- Consideration of whether other predicted indications with a more plausible link, such as Langerhans cell histiocytosis, merit review instead (although their link is also weak and speculative)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

