---
layout: default
title: Lanadelumab
parent: Model Prediction Only (L5)
nav_order: 521
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "Lanadelumab"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
description: "Lanadelumab: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). Approved use: Not recorded in the local data"
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lanadelumab: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Lanadelumab is a monoclonal antibody that targets plasma kallikrein and is marketed in Canada as TAKHZYRO.
The TxGNN model predicts it may be effective for **serpinopathy with toxic serpin polymerization**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the drug's identity as a monoclonal antibody against plasma kallikrein (gene KLKB1), it inhibits the kallikrein-bradykinin pathway. The target-binding data indicate it does not bind prekallikrein.

The predicted link is computational only. The likely driver of the high score is a shared relationship to the serpin protein family. Toxic serpin polymerization, however, is a cellular proteotoxic process, and blocking plasma kallikrein does not address it. The mechanistic fit is therefore weak, and the high score should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02505614 | TAKHZYRO | Not listed | Not listed |
| 02480948 | TAKHZYRO | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry was found, relating to the drug's own target, kallikrein B1 (KLKB1). It is a target-binding record rather than a clinical interaction with another medicine.

Please refer to the package insert for further safety information, including warnings and contraindications. Lanadelumab is known to prolong aPTT in laboratory assays, which may complicate coagulation testing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, and the proposed mechanism (toxic serpin polymerization) is not one that kallikrein inhibition would be expected to affect. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical data showing that plasma kallikrein inhibition affects serpin polymerization pathology
- Any clinical or published evidence directly studying lanadelumab in this disease
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism of action data (MOA)

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

