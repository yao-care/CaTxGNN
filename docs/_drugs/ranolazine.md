---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 1
---

# Ranolazine
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

# Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ranolazine is generally known as a late sodium current inhibitor used for chronic angina. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but currently **0 clinical trials** and **0 publications** support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic angina (general pharmacological knowledge; the Canadian license records provide no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ranolazine is generally described as a late sodium current (INa-late) inhibitor used in chronic angina. Its efficacy in angina is established, but no evidence links that action to NSIAD.

NSIAD is a rare condition caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*). These variants cause vasopressin-independent water reabsorption in the renal collecting duct. The pathway from late sodium current inhibition to V2 receptor signaling or aquaporin-2 regulation has not been established.

The score of 0.996 (rank 7,250) is a knowledge-graph prediction only. It may reflect network proximity or rare-disease graph artifacts, so it should not be read as mechanistic validation. Similarity between the original and predicted indications has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2510227 | CORZYNA | — | — |
| 2510219 | CORZYNA | — | — |

Dosage form and approved indication text are not recorded in the license data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it (evidence level L5), with no registered trials, no literature and no established mechanistic link to NSIAD. NSIAD arises from *AVPR2* gain-of-function, which is far from ranolazine's known pharmacology.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and an analysis of any plausible link to V2 receptor or aquaporin-2 signaling
- Health Canada package insert warnings and contraindications, to enable safety screening
- A systematic literature and trial registry search (including ICTRP) for ranolazine in NSIAD or related water-balance disorders
- Preclinical or in vitro evidence (e.g., V2 receptor gain-of-function cell models) before any clinical consideration
- Confirmation of the approved indication text and dosage forms for the two CORZYNA DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

