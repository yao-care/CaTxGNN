---
layout: default
title: Prasterone
parent: Model Prediction Only (L5)
nav_order: 754
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From an Unspecified Original Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (DHEA) is a marketed hormone-precursor drug in Canada, but the available data do not state its approved indication.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, a rare congenital clotting disorder.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Prasterone is a hormone precursor (DHEA), and the Canadian licence record does not list an approved indication. No mechanistic link to the predicted disease can be drawn from the provided data.

Heparin cofactor 2 deficiency is a congenital serpin (serine protease inhibitor) deficiency affecting coagulation control. Nothing in the data connects prasterone to this pathway. The very high TxGNN score (99.99%, rank 487) reflects a graph-based association only. It should not be read as a therapeutic rationale until clinical or mechanistic evidence appears.

A related safety point: the rank 2 prediction is also a thrombosis-prone genetic condition (factor 5 excess with spontaneous thrombosis). Raising levels of a hormone precursor in patients prone to clotting would need to be addressed before any further work on this drug family of predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2493500 | INTRAROSA |

Dosage form, manufacturer, and approved indication text are not available in the current record.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings and contraindications. These could not be retrieved for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support (L5), and the safety documentation needed for even an initial screen is missing. A high model score alone is not enough to proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication). This is a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank, to assess any link to the heparin cofactor 2 / serpin pathway.
- A thrombosis-risk safety assessment for a hormone precursor in congenital clotting disorders.
- Route and formulation compatibility analysis, which has not yet been done.

**Note on other predictions:** Among the other predictions, **scleroderma (systemic sclerosis)** has the most supporting material. It is backed by several observational studies reporting altered DHEA-S and androgen levels that track disease severity, and it is rated "Research Question". These studies measure hormone levels only and do not test prasterone as a treatment, so they support hypothesis generation but not efficacy.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

