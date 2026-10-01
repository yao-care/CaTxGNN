---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 935
evidence_level: L5
indication_count: 6
---

# Triamterene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Triamterene: From Hypertension and Edema to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic, generally used for hypertension and edema and usually combined with a thiazide.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and edema (general pharmacology; the licence text does not state an indication) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC). Its efficacy in hypertension and edema is established, and it may be mechanistically applicable to hypertensive kidney disease through sodium and volume reduction.

The link to the new indication is plausible but weak. Malignant hypertension with renal involvement is a hypertensive emergency that needs rapid parenteral blood-pressure control, so a diuretic would at most be an adjunct. In impaired renal function, hyperkalemia and nephrotoxicity risk with a potassium-sparing diuretic is a major concern. The high score (0.9989) therefore reflects knowledge-graph proximity to other hypertension terms rather than clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

**Other predicted indications (for context):**

| Predicted Indication | Score | Evidence Level | Trials / Papers | Note |
|------|------|------|------|------|
| Malignant renovascular hypertension | 99.89% | L5 | 0 / 0 | Model prediction only; hyperkalemia and kidney injury risk, especially with RAAS inhibitors |
| Pulmonary hypertension, unclear multifactorial mechanism | 99.88% | L5 | 0 / 0 | No direct mechanistic rationale |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.88% | L5 | 0 / 20 | Retrieved papers concern general hypoxia biology and do not mention triamterene; not usable as support |
| Braddock syndrome | 99.84% | L5 | 0 / 0 | No identifiable rationale; likely a knowledge-graph artifact |
| Chronic pulmonary heart disease | 99.75% | L4 | 0 / 4 | Old papers (1976–1991) on diuretics and heart failure, including a small 1989 comparison of hydrochlorothiazide + triamterene vs digitalis. Evidence is indirect; marked as a research question |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 441775 | APO-TRIAZIDE |
| 532657 | TEVA-TRIAMTERENE/HCTZ |

---

## Safety Considerations

- **General pharmacology concern**: Hyperkalemia and nephrotoxicity risk in impaired renal function, particularly relevant to the predicted renal and renovascular indications and to co-administration with RAAS inhibitors.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5). The target conditions are hypertensive emergencies where a potassium-sparing diuretic has limited and potentially hazardous use. The only prediction with any indirect literature is chronic pulmonary heart disease, which is better handled as a separate research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search for triamterene-specific studies in hypertensive renal disease and chronic pulmonary heart disease
- A safety assessment for hyperkalemia and renal impairment in the target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

