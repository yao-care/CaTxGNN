---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB) marketed in Canada, and its original indication is presumed to be hypertension. The TxGNN model predicts it may be effective for **Prinzmetal angina** with a very high score (99.98%). However, **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (presumed from drug class; no indication text in the supplied Health Canada records) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, telmisartan is an ARB, its efficacy in hypertension is established, and mechanistically it may be applicable to Prinzmetal angina.

Prinzmetal angina is caused by coronary artery vasospasm. Telmisartan blocks the AT1 receptor, which mediates angiotensin II vasoconstriction, and it also partially activates PPARγ. Both actions could plausibly improve vascular tone and endothelial function.

This link is a hypothesis only. No retrieved study tests telmisartan in vasospastic angina, so the prediction cannot be considered supported beyond the model score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2484544 | AG-TELMISARTAN |
| 2320177 | TEVA-TELMISARTAN |
| 2320185 | TEVA-TELMISARTAN |
| 2375966 | SANDOZ TELMISARTAN |
| 2407493 | ACH-TELMISARTAN |

Dosage form and approved indication text were not available for these products. Five of the 20 licenses are shown.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction has a very high model score but no trials or literature behind it, which places it at evidence level L5. Health Canada safety data and the mechanism of action are also missing, so the candidate cannot move forward.

Two other predicted indications for telmisartan have more evidence and may deserve a closer look:
- **Intracerebral hemorrhage** (L2): the Phase 3 TRIDENT trial (n=1,671) tests a low-dose triple blood-pressure combination that includes telmisartan, so any effect cannot be attributed to telmisartan alone, and no results were supplied.
- **Cerebral artery occlusion** (L4): supported only by animal stroke models.

**To proceed, the following is needed:**
- A targeted search for studies of telmisartan or ARBs in vasospastic (Prinzmetal) angina
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian DINs
- Published TRIDENT results, if the intracerebral hemorrhage direction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

