---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 780
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Quinapril: From ACE-Inhibitor Therapy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril is an ACE inhibitor marketed in Canada under 14 DINs, but the supplied data do not state its approved indication.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a score of 99.86%.
This is a **model prediction only**: **0 clinical trials** and **0 publications** support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian licence data (drug class: ACE inhibitor) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Quinapril is an ACE inhibitor, so its pharmacology is blockade of the renin-angiotensin-aldosterone system (RAAS).

Malignant hypertension with kidney involvement is a severe form of hypertension in which RAAS activation is a plausible driver. Blocking this pathway is therefore biologically coherent with the prediction. That coherence is a hypothesis, not evidence. No trials or literature were supplied for this indication.

The other four predictions are weaker or carry safety flags:

- **Malignant renovascular hypertension** (score 99.86%): mechanistically coherent, because renovascular hypertension is strongly RAAS-driven. Bilateral renal artery stenosis is a known safety concern for ACE inhibitors and would need review before any progression.
- **Pulmonary hypertension, unclear multifactorial mechanism** (99.85%): the link to systemic RAAS inhibition is weak and non-specific.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.85%): the RAAS hypothesis is plausible but unsupported. The 20 retrieved publications (10 shown) are general hypoxia papers on brain aging, cancer metabolism, multiple sclerosis and altitude. None addresses quinapril or ACE inhibitors, so they appear to be keyword-match artifacts.
- **Braddock syndrome** (99.79%): no mechanistic rationale can be established from the supplied data. It is likely a knowledge-graph artifact needing expert review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction. The only publications retrieved belong to the lower-ranked pulmonary hypertension (hypoxia) prediction. They are not relevant to quinapril and are not listed here.

---

## Canada Market Information

Quinapril has 14 DINs in total. The supplied data list only the product names below. Dosage form, manufacturer and approved-indication text were not provided.

| DIN | Product Name |
|---------|------|
| 2517477 | JAMP QUINAPRIL |
| 2340585 | PMS-QUINAPRIL |
| 2517450 | JAMP QUINAPRIL |
| 2517469 | JAMP QUINAPRIL |
| 2340577 | PMS-QUINAPRIL |

---

## Safety Considerations

- **Drug Interactions**: no interaction records were found for this drug in the queried source.
- **Renovascular note**: bilateral renal artery stenosis is a known safety concern for ACE inhibitors. This is relevant if the malignant renovascular hypertension prediction is pursued.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predictions rest on model scores alone (L5, stage S0), with no supporting trials or relevant literature. The RAAS-blockade rationale is plausible for the two hypertensive-renal predictions. It is weak or absent for the pulmonary hypertension and Braddock syndrome predictions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap that prevents safety screening.
- Mechanism of action data from DrugBank.
- Approved indication text for the Canadian licences, to define the original indication.
- A targeted search for quinapril or ACE-inhibitor evidence in malignant hypertension with renal involvement.
- Expert review of the Braddock syndrome prediction.
- Route compatibility and similarity-to-original assessments, both still pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

