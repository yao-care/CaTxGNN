---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# CHLORTHALIDONE: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a long-acting thiazide-like diuretic classically used for hypertension and edema management.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
however, there are currently **no clinical trials** and **no publications** directly supporting this indication — evidence rests entirely on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Edema (not recorded in current evidence pack) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Chlorthalidone is a thiazide-like diuretic that acts primarily on the distal convoluted tubule, inhibiting sodium–chloride cotransporter (NCC) activity to reduce sodium and water reabsorption, resulting in decreased plasma volume and lowered blood pressure. Importantly, it also possesses weak carbonic anhydrase inhibitory (CAI) activity — a property shared with acetazolamide, a drug approved specifically for glaucoma.

This weak CAI activity forms the theoretical mechanistic bridge to glaucoma: by reducing carbonic anhydrase activity in the ciliary epithelium, chlorthalidone could theoretically lower aqueous humor production and reduce intraocular pressure (IOP). Historical reports from the 1960s–1980s noted modest IOP-lowering effects with systemic thiazide-class agents, likely mediated through a combination of systemic diuresis and this weak CAI mechanism.

However, primary hereditary glaucoma is fundamentally a genetic disease — driven by mutations in *MYOC*, *OPTN*, and *TBK1* — and the dominant pathology is structural outflow tract dysfunction, not excess aqueous production. Chlorthalidone's systemic diuretic mechanism cannot correct the underlying genetic defect, and modern glaucoma management relies on topical agents (prostaglandin analogues, β-blockers, and topical CAIs) that achieve far higher intraocular concentrations with lower systemic risk. The mechanistic relevance is therefore considered weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Chlorthalidone currently has no approved products registered in Canada (0 DINs). No authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting chlorthalidone for primary hereditary glaucoma, and the mechanistic link is weak — weak CAI activity may theoretically lower IOP but cannot address the genetic mutations driving hereditary glaucoma. Furthermore, chlorthalidone is not marketed in Canada and has no existing DINs, adding a regulatory barrier on top of the evidence gap.

**To proceed, the following is needed:**
- Mechanism of action data (query DrugBank API for complete MOA profile)
- Safety data including key warnings and contraindications (retrieve from package insert PDF)
- Preclinical or in vivo data demonstrating measurable IOP reduction with systemic chlorthalidone
- Comparative assessment against established topical CAIs (e.g., dorzolamide, brinzolamide) to evaluate whether systemic dosing could offer any clinical advantage
- Regulatory pathway scoping for potential Canadian market entry

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

