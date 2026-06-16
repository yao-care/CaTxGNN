---
layout: default
title: Eliglustat
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Eliglustat
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

# Eliglustat: From Gaucher Disease Type 1 to Autosomal Ichthyosis Syndrome with Fatal Disease Course

## One-Sentence Summary

Eliglustat (Cerdelga) is a glucosylceramide synthase (GCS) inhibitor originally approved in the US and EU for the treatment of Gaucher disease type 1 (GD1), a lysosomal storage disorder caused by glucocerebroside accumulation.
The TxGNN model predicts it may be effective for **autosomal ichthyosis syndrome with fatal disease course**, with a prediction score of **98.42%**, but this direction is supported by **0 clinical trials** and **0 publications** to date.
The evidence base is currently model-prediction only, placing this candidate firmly in the exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gaucher disease type 1 (lysosomal storage disorder) |
| Predicted New Indication | Autosomal ichthyosis syndrome with fatal disease course |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Eliglustat is a substrate reduction therapy that inhibits glucosylceramide synthase (GCS), the enzyme responsible for synthesizing glucocerebroside. By reducing the synthesis of this glycosphingolipid substrate, Eliglustat lowers the pathological accumulation that drives Gaucher disease. Its efficacy in GD1 has been established in Phase 3 clinical trials (ENGAGE, ENCORE).

The theoretical link to autosomal ichthyosis syndrome rests on the role of ceramide and sphingolipid metabolism in maintaining the stratum corneum barrier. Some forms of autosomal recessive congenital ichthyosis (ARCI) involve lipid processing defects, and GCS inhibition could theoretically redirect ceramide precursor flow in keratinocytes. However, this connection is distant and speculative.

Critically, the "fatal disease course" qualifier in the disease name suggests the underlying mechanism extends well beyond lipid metabolism dysregulation, making it unlikely that GCS inhibition alone would be therapeutically meaningful. There is currently no preclinical or clinical data of any kind supporting this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Canada Market Information

Eliglustat is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) have been issued by Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Eliglustat are rated L5 (model prediction only), with zero supporting clinical trials and zero directly relevant literature across all candidates. The top prediction involves a rare syndrome with a fatal disease course that is mechanistically distant from Eliglustat's established GCS-inhibition pathway, and the drug is not currently marketed in Canada.

**To proceed, the following is needed:**

- **Mechanism of action data**: Retrieve full MOA documentation from DrugBank (DB09039) to enable mechanistic link assessment for any candidate indication
- **Safety profile**: Download and parse Health Canada (or FDA/EMA) product monograph to obtain key warnings, contraindications, and CYP2D6 pharmacogenomic interaction data
- **Preclinical evidence search**: Commission a targeted literature review for Eliglustat (or GCS inhibitors as a class) in sphingolipid-related skin disorders before advancing any ichthyosis hypothesis
- **Disease re-prioritization**: Consider evaluating lower-ranked TxGNN predictions that may have stronger mechanistic plausibility or existing background evidence before investing resources in rank-1 through rank-10 candidates as currently scoped
- **Canada regulatory pathway**: Confirm whether Eliglustat holds any EMA or FDA approval that could support a future Health Canada submission via the foreign reference drug pathway (if a viable indication is identified)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

