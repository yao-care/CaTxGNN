---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 661
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

# Quinapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril (DB00881) is an ACE inhibitor internationally used for hypertension and heart failure; no specific Canadian licensing or original-indication text is on file in this evidence pack.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a prediction score of **99.86%**, but currently **no clinical trials and no literature** directly support this specific pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Canada licensing data (drug not marketed); internationally known as an ACE inhibitor indicated for hypertension |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for quinapril in this evidence pack. Based on known information, quinapril belongs to the ACE inhibitor (angiotensin-converting enzyme inhibitor) class, a group whose efficacy in hypertension is well established through inhibition of the renin-angiotensin-aldosterone system (RAAS).

Malignant hypertensive renal disease is a severe form of hypertension causing acute renal damage. Mechanistically, RAAS inhibition — the shared pharmacological basis of ACE inhibitors — lowers systemic blood pressure and reduces intraglomerular pressure, which is consistent with why a TxGNN model trained on drug-disease network relationships would link an antihypertensive agent to a hypertension-driven renal condition. However, this mechanistic plausibility is not yet corroborated by any disease-specific clinical or published evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Quinapril has no Health Canada drug licences on file (0 DINs; market status: not marketed). No product-level authorization data is currently available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (malignant hypertensive renal disease) has no supporting clinical trials or literature, and the drug is not currently marketed in Canada — there is insufficient evidence to progress this candidate at this time.

**To proceed, the following is needed:**
- TFDA/Health Canada package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action (MOA) data via DrugBank API
- Disease-specific clinical trial or literature evidence for malignant hypertensive renal disease (note: literature retrieved for the lower-ranked candidate "pulmonary hypertension owing to lung disease and/or hypoxia" was general hypoxia biology, not quinapril-specific, and does not substitute for direct evidence)
- Confirmation of quinapril's original approved indication and licensing status, since none is recorded in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

