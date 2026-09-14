---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

> Telmisartan is a well-established angiotensin II receptor blocker (ARB) used to treat hypertension.
> The TxGNN model predicts it may be effective for **Prinzmetal angina**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class; jurisdiction-specific approved indication text not available in this evidence pack) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, telmisartan is an angiotensin II type 1 (AT1) receptor blocker that lowers blood pressure and provides some vascular/metabolic protective effects; its efficacy in hypertension is well established, but this action does not have a known mechanistic link to Prinzmetal angina.

Prinzmetal (variant) angina is caused by focal coronary artery vasospasm, and its standard treatment is calcium channel blockers (and nitrates), not blood-pressure-lowering RAAS inhibitors. The evidence pack's own mechanistic assessment confirms this gap: ARB-mediated blood pressure reduction has no established connection to relief of coronary vasospasm, and the high TxGNN score is not supported by any clinical trial or literature evidence.

Notably, within this same candidate set, telmisartan shows **substantially stronger evidence** for other predicted indications — *cerebral artery occlusion* (L2, S2, Research Question, 3 trials + 17 preclinical papers) and *intracerebral hemorrhage* (L2, S2, Research Question, 3 trials including a completed Phase 3 RCT with n=1671 + 11 papers) — both grounded in a plausible AT1-blockade/oxidative-stress/neuroprotection mechanism. These represent more promising repurposing candidates than the top-ranked Prinzmetal angina prediction and may warrant a separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial or literature evidence supporting telmisartan for Prinzmetal angina, and the mechanistic link is weak — ARB blood-pressure lowering does not address the coronary vasospasm pathology underlying this condition. This candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap — DG001)
- Detailed mechanism of action (MOA) data from DrugBank (High-severity data gap — DG002)
- Any preclinical or case-level evidence specifically linking ARBs to coronary vasospasm relief
- Consider re-evaluating the higher-evidence candidates in this drug's prediction set (cerebral artery occlusion, intracerebral hemorrhage) as alternative repurposing targets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

