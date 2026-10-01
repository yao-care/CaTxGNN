---
layout: default
title: Acebutolol
parent: Model Prediction Only (L5)
nav_order: 16
evidence_level: L5
indication_count: 2
---

# Acebutolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Acebutolol: From an Unrecorded Original Indication to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Acebutolol is a marketed beta-blocker in Canada, but the record does not state its original approved indication.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded. Acebutolol is a beta-blocker, and its efficacy in its approved use cannot be checked against this record. As a general pharmacological hypothesis, a beta-1 blocker lowers blood pressure and suppresses renin release, which could reduce hypertensive renal injury.

Malignant hypertension is a hypertensive emergency that is usually managed with parenteral agents. The link between acebutolol and this condition is untested, and route compatibility has not been assessed.

A second, related prediction is **malignant renovascular hypertension** (same score, 99.10%). Its only retrieved record is a 1975 open study of 50 patients with arterial hypertension in general (PMID 768911). The title does not indicate a renovascular or malignant subgroup, so it does not directly support either prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the six authorizations are listed in the data. Dosage form and approved indication text are not recorded for any of them.

| DIN | Product Name |
|---------|------|
| 02204525 | TEVA-ACEBUTOLOL |
| 02204517 | TEVA-ACEBUTOLOL |
| 02204533 | TEVA-ACEBUTOLOL |
| 02147629 | APO-ACEBUTOLOL |
| 02147610 | APO-ACEBUTOLOL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or literature, and the mechanism and original indication are missing from the record. Malignant hypertensive renal disease is typically treated with parenteral agents, so the fit with an oral beta-blocker is unverified.

**To proceed, the following is needed:**
- Health Canada package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data (e.g., from DrugBank)
- The approved indications, dosage forms and routes for the Canadian DINs
- A route compatibility assessment against the parenteral use typical in malignant hypertension
- A targeted search for trials and literature on acebutolol in malignant hypertension and hypertensive or renovascular renal disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

