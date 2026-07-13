---
layout: default
title: Metolazone
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 5
---

# Metolazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Metolazone: From Hypertension and Edema to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic known for its use in hypertension and fluid overload management.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** (score 99.84%),
however **no clinical trials** and **no directly relevant publications** are currently available for this specific indication — the prediction rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and edema (thiazide-like diuretic class; no Health Canada DIN on record) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on pharmacological class information embedded in the prediction rationale, Metolazone is a thiazide-like diuretic that inhibits the sodium-chloride cotransporter (NCC) in the distal renal tubule, reducing sodium and water reabsorption. This lowers intravascular volume and, consequently, systemic blood pressure — the central therapeutic rationale for its use in hypertension and oedema states.

Malignant renovascular hypertension arises from severe, treatment-resistant hypertension driven by excessive renin-angiotensin system (RAS) activation, typically secondary to renal artery stenosis or other renovascular pathology. Volume reduction via diuresis is a logical adjunctive antihypertensive strategy in this context, which explains why the TxGNN model — trained on pharmacological and disease-network relationships — assigns metolazone a high prediction score for this indication. A closely related indication, malignant hypertensive renal disease (rank 2, identical score 99.84%), further reflects this mechanistic clustering.

A key clinical limitation must be acknowledged: malignant renovascular hypertension frequently coexists with significant renal impairment. When the glomerular filtration rate falls below approximately 30 mL/min, thiazide-type diuretics lose substantial efficacy, and loop diuretics (e.g., furosemide) are clinically preferred. Metolazone's role in this setting would most plausibly be as a combination partner to furosemide via sequential nephron blockade — an approach with indirect clinical practice support — rather than as a monotherapy. This prediction therefore represents an indirect mechanistic inference with an important pharmacokinetic caveat, not a directly validated drug-disease association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on rank-4 indication (pulmonary hypertension owing to lung disease/hypoxia):** A PubMed search retrieved 20 publications, but upon review all 20 articles address general hypoxia biology (e.g., HIF-1α signalling, altitude physiology, neurodegeneration under hypoxia) and contain no mention of metolazone. These represent keyword-matching noise and do not constitute valid drug-disease evidence.

---

## Canada Market Information

Metolazone currently has no Health Canada Drug Identification Numbers (DINs) on record. The drug is not marketed in Canada. No authorisation data is available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data gap notice:** Package insert warnings, contraindications, and drug interaction data have not yet been retrieved. This is classified as a **Blocking** gap that must be resolved before any formal safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence specifically supports metolazone for malignant renovascular hypertension; the prediction is driven by mechanistic plausibility (thiazide-class volume reduction) alone, and two blocking or high-severity data gaps — package insert safety data and confirmed mechanism of action — remain unresolved.

**To proceed, the following is needed:**

- **[Blocking]** Obtain metolazone package insert (Health Canada or equivalent) and extract warnings, contraindications, and special population restrictions before any safety assessment can begin
- **[High]** Query the DrugBank API for DB00524 to confirm the mechanism of action and pharmacokinetic profile
- **[Evidence]** Conduct a targeted literature search: `metolazone AND ("renovascular hypertension" OR "resistant hypertension" OR "sequential nephron blockade")` — current zero-result search used narrow disease-name terms only
- **[Clinical]** Assess renal function threshold: clarify whether the anticipated patient population (malignant renovascular hypertension) typically presents with GFR < 30 mL/min, which would substantially limit thiazide efficacy and shift the clinical strategy toward furosemide ± metolazone combination
- **[Regulatory]** Determine whether metolazone can be accessed via Health Canada's Special Access Programme (SAP) if a future study is proposed, given its absence from the Canadian market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

