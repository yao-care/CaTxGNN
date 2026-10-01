---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker, a class used mainly for hypertension and diabetic kidney disease. The original indication text was not provided in the Health Canada license records, so it is inferred from the drug class.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data provided (hypertension and diabetic nephropathy are typical for this drug class) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Irbesartan blocks the angiotensin II type 1 receptor. Malignant hypertension with kidney injury involves strong activation of the renin-angiotensin-aldosterone system (RAAS), so blocking this pathway is mechanistically coherent. The high TxGNN score (99.31%) is consistent with this link.

Two caveats limit how much weight the prediction can carry:
- The score is a model output only. No trials or publications support it.
- Irbesartan is already used for hypertension and diabetic nephropathy. This prediction may therefore restate existing class use rather than reveal a truly new indication.

The next-ranked prediction, malignant renovascular hypertension, has an identical score (99.31%). This suggests the two share a disease-node neighborhood in the knowledge graph rather than representing independent evidence.

The model also predicts two pulmonary hypertension indications (score 99.25%). The mechanistic link there is speculative, and the literature retrieved for it consisted of keyword matches on "hypoxia" with no irbesartan-specific studies. Both are rated Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorizations are listed below. The dosage form, manufacturer and approved indication text were not provided for these records.

| DIN | Product Name |
|---------|------|
| 2365197 | IRBESARTAN |
| 2237925 | AVAPRO |
| 2328488 | SANDOZ IRBESARTAN |
| 2372398 | IRBESARTAN |
| 2524821 | M-IRBESARTAN |

---

## Safety Considerations

No structured warning, contraindication or interaction data was available. Please refer to the package insert for full safety information.

The prediction rationale flags the following class-level guardrails:
- ARBs are contraindicated or require caution in **bilateral renal artery stenosis**, or stenosis of a solitary kidney, where they can precipitate acute renal failure. This is a specific concern for the renovascular hypertension prediction.
- Caution is also needed in **acute kidney injury** and **volume depletion**.
- Any use in this setting would require close monitoring of **renal function and serum potassium**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is plausible, but the evidence is at L5 (model prediction only) with no trials or literature. The prediction may also overlap with irbesartan's existing use in hypertension.

**To proceed, the following is needed:**
- The Health Canada product monograph, to confirm approved indications, warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank, to strengthen the mechanistic analysis.
- A targeted literature search for irbesartan or ARBs in malignant hypertension with renal involvement, and a check of whether current labeling already covers it.
- A clear definition of how this indication differs from existing hypertension and nephropathy use.
- A renal function and potassium monitoring plan, with screening for renal artery stenosis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

