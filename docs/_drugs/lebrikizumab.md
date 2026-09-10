---
layout: default
title: Lebrikizumab
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From IL-13-Mediated Inflammatory Disease to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is an anti-IL-13 monoclonal antibody; this evidence pack does not contain a confirmed original/approved indication for the Canadian market (drug is currently **not marketed** in Canada, 0 DINs). The TxGNN model's top prediction is **Severe Nonproliferative Diabetic Retinopathy**, but this candidate currently has **zero clinical trials and zero publications** supporting it — it is a pure knowledge-graph prediction with no mechanistic or clinical corroboration in the evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug not marketed in Canada, no approved indication on file |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not recorded in the drug-level fields of this evidence pack (`original_moa: [Data Gap]`). However, literature captured elsewhere in the pack (e.g., PMID 36994947, PMID 36920778) describes Lebrikizumab as a high-affinity IgG4 monoclonal antibody that selectively binds and neutralizes interleukin-13 (IL-13), preventing formation of the IL-4Rα/IL-13Rα1 heterodimer signaling complex. This mechanism is well established in Th2-driven inflammatory skin disease, where the drug has extensive Phase 2/3 trial support (see the "dermatitis" prediction discussed below).

For the top-ranked candidate — severe nonproliferative diabetic retinopathy — the pack's own rationale field states there is **no known mechanistic link**: "IL-13 抑制與糖尿病視網膜病變之血管新生/代謝路徑無直接證據支持，僅為 TxGNN 圖譜預測分數" (no direct evidence connecting IL-13 inhibition to the angiogenic/metabolic pathways of diabetic retinopathy; this is a knowledge-graph score only). No clinical trials, ICTRP registrations, or PubMed literature were retrieved for this drug-disease pair (query log entries 2–4, all 0 results). The high TxGNN score therefore reflects a graph-topology signal rather than any biological or clinical corroboration currently on file.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication carries a high TxGNN score but has no supporting clinical trials, no literature, and no mechanistic rationale — the evidence pack explicitly flags this as a graph-only prediction. Combined with a Blocking-severity data gap on TFDA/Health Canada label warnings and contraindications, there is no basis to advance past S0.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Preclinical/mechanistic evidence connecting IL-13 signaling to diabetic retinopathy pathophysiology (angiogenesis, vascular permeability)
- Any exploratory or investigator-initiated trials in diabetic eye disease, once available

---

**Analyst note:** This evidence pack also captures a lower-ranked candidate, **dermatitis** (rank 5, score 95.97%), with 29 clinical trials (multiple completed Phase 3 RCTs, e.g., NCT04146363, NCT04178967, NCT06280716) and 20 publications — substantially stronger evidence than the top-ranked candidate. This volume of Phase 3 data is consistent with atopic dermatitis being Lebrikizumab's known, internationally approved indication rather than a genuinely novel repurposing signal; it is presented here as data-quality context and was not selected as the primary candidate under the report's ranking rule (predicted_indications[0]).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

