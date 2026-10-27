---
layout: default
title: Menotropins
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Menotropins: predicted new indication Peptic esophagitis (evidence level L5). Approved use: Not specified in the licence data compiled for this report"
monitor_inn: "Menotropins"
predicted_indications: ["peptic esophagitis", "postural orthostatic tachycardia syndrome", "esophageal disease", "Raynaud disease", "non-syndromic esophageal malformation", "esophageal ulcer", "His bundle tachycardia", "sinoatrial block", "progressive familial heart block", "sinoatrial node disease"]
---

# Menotropins
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

## Menotropins: From Gonadotropin-Based Fertility Treatment to Peptic Esophagitis
{: .text-alpha }

## One-Sentence Summary

Menotropins (a human menopausal gonadotropin with FSH and LH activity) is a gonadotropin preparation that is marketed in Canada under the brand name MENOPUR.
The TxGNN model predicts it may be effective for **peptic esophagitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the licence data compiled for this report |
| Predicted New Indication | Peptic esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, menotropins acts through FSH and LH activity on gonadotropin receptors in the gonads, stimulating follicular development and spermatogenesis.

No established mechanistic link connects gonadotropin signalling to esophageal mucosal injury or acid reflux. The high TxGNN score is a knowledge-graph prediction and is not backed by any trial or publication.

Other top predictions show the same pattern. Several are esophageal conditions (esophageal disease, esophageal ulcer, non-syndromic esophageal malformation), and several are cardiac conduction disorders (sinoatrial block, sinoatrial node disease, His bundle tachycardia, progressive familial heart block). These clusters suggest a shared graph-neighbourhood artefact rather than independent signals. POTS and Raynaud disease have been loosely discussed in relation to sex-hormone influences, but there is no direct evidence that menotropins affects them.

## Other Predicted Indications (Top 10)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Peptic esophagitis | 98.44% | L5 | Hold |
| 2 | Postural orthostatic tachycardia syndrome | 98.33% | L5 | Hold |
| 3 | Esophageal disease | 97.61% | L5 | Hold |
| 4 | Raynaud disease | 97.43% | L5 | Hold |
| 5 | Non-syndromic esophageal malformation | 96.89% | L5 | Hold |
| 6 | Esophageal ulcer | 96.84% | L5 | Hold |
| 7 | His bundle tachycardia | 95.95% | L5 | Hold |
| 8 | Sinoatrial block | 95.88% | L5 | Hold |
| 9 | Progressive familial heart block | 95.66% | L5 | Hold |
| 10 | Sinoatrial node disease | 95.47% | L5 | Hold |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02283093 | MENOPUR | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: One interaction was identified. **Ganirelix** (Moderate severity, from DDInter).

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanistic link between gonadotropin activity and esophageal disease. The same lack of support applies to every other predicted indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian licence
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking gonadotropin signalling to the predicted conditions
- A route-compatibility assessment and similarity analysis against the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

