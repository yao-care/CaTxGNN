---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: From ACE Inhibitor Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril is an ACE inhibitor that is marketed in Canada under six licences.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials and no relevant publications** currently support this prediction, so it remains a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fosinopril is an ACE inhibitor, and this class acts on the renin-angiotensin system (RAS).

Renovascular hypertension is driven by RAS activation, so the target pathway fits the drug class. The link is plausible but unverified. The score rests only on the knowledge-graph prediction, with no supporting trials or literature.

A known safety concern applies directly to this setting. ACE inhibitors can cause acute renal function decline in bilateral renal artery stenosis or in a solitary kidney, and this must be resolved before any clinical consideration.

Four other diseases are also predicted, all at Evidence Level L5 with no supporting trials:
- **Malignant hypertensive renal disease** (score 99.87%): the RAS rationale is plausible but unverified.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.87%): the link is weak. The 20 retrieved publications are general hypoxia papers unrelated to fosinopril, and vasodilators may worsen ventilation-perfusion matching.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.87%): no mechanistic link is established.
- **Braddock syndrome** (99.81%): no credible link, likely an artifact of the shared pulmonary hypertension neighborhood.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Six licences are recorded in total. The Evidence Pack lists five of them, and none includes dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2247803 | TEVA-FOSINOPRIL |
| 2247802 | TEVA-FOSINOPRIL |
| 2266008 | APO-FOSINOPRIL |
| 2266016 | APO-FOSINOPRIL |
| 2459396 | FOSINOPRIL |

## Safety Considerations

- **Renal risk**: ACE inhibitors carry a known risk of acute renal function decline in bilateral renal artery stenosis or a solitary kidney. This is directly relevant to renovascular hypertension.
- **Monitoring**: Renal function and hyperkalemia monitoring would be central safety questions.

Please refer to the package insert for further safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.87%), but it is the only support. There are no trials or relevant literature, and the evidence level is L5. The main safety concern, renal impairment in renal artery stenosis, has not been addressed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Mechanism of action data (for example, from DrugBank)
- Targeted literature searches for ACE inhibitors in renovascular hypertension
- A review of the renal safety risk in renal artery stenosis and solitary kidney
- Approved indication and dosage form data for the Canadian licences

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

