---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 510
evidence_level: L5
indication_count: 4
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Labetalol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Labetalol is a combined alpha/beta-adrenergic blocker marketed in Canada. The supplied data does not list its original indication, but general pharmacology places it in hypertension. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on general pharmacology; the supplied license data contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, labetalol combines alpha- and beta-adrenergic blockade and is used to lower blood pressure. Its efficacy in hypertension is established, and mechanistically it may be applicable to severe hypertension with kidney involvement.

Malignant hypertensive renal disease is kidney damage caused by severely elevated blood pressure. The link to labetalol therefore comes from its antihypertensive action, not from any supplied trial, literature, or mechanism data. This prediction is also better read as an extension within the drug's existing antihypertensive use than as true repurposing. The original indication should be confirmed against the Health Canada label.

The other three TxGNN predictions are also at L5 with a Hold recommendation:
- **Malignant renovascular hypertension** (score 99.08%): two papers were retrieved, but they are only topically related. One is a pediatric case report, and the other is a hallucinogen-induced vasculitis case in which labetalol and minoxidil were used to control blood pressure. Renovascular hypertension is also driven by renin-angiotensin activation, so the fit with adrenergic blockade is uncertain.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.08%): the retrieved papers matched on the word "hypoxia" and are unrelated to labetalol or pulmonary hypertension. Systemic antihypertensive action does not transfer to the pulmonary circulation, and beta-blockade may carry risks such as bronchospasm.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.08%): no trials or literature, and the same concerns as above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 11 licenses. Dosage form and approved indication text were not provided for any of them. The first 5 are shown:

| DIN | Product Name |
|---------|------|
| 2231689 | LABETALOL HYDROCHLORIDE INJECTION USP |
| 2243539 | APO-LABETALOL |
| 2489406 | RIVA-LABETALOL |
| 2541505 | LABETALOL HYDROCHLORIDE INJECTION USP |
| 2391090 | LABETALOL HYDROCHLORIDE INJECTION USP |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.08% TxGNN score is not backed by any trials or literature (L5). The link to malignant hypertensive renal disease also reflects labetalol's existing antihypertensive use more than a new indication. Safety data has not been obtained, so the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications) to complete the safety review and confirm the original indication
- Mechanism of action data (for example from DrugBank)
- A targeted literature and trial search for labetalol in malignant hypertension with renal involvement
- Full-text review of the two papers retrieved for malignant renovascular hypertension
- A separate safety assessment of beta-blockade before any consideration of the pulmonary hypertension predictions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

