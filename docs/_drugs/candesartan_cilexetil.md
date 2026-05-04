---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker (ARB) widely used for the treatment of hypertension and heart failure, acting by selectively blocking the AT1 receptor to interrupt the renin–angiotensin–aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, a severe form of hypertension-driven renal injury with strong mechanistic overlap with the drug's established target pathway.
However, there are currently **0 clinical trials** and **0 direct publications** supporting this specific repurposing direction, placing this candidate at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in Canadian regulatory records — drug not currently marketed in Canada |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 (mechanistic rationale only; no clinical or observational studies identified) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Candesartan cilexetil is an orally administered prodrug that is hydrolyzed to its active metabolite, candesartan, upon absorption. Candesartan selectively and insurmountably blocks AT1 receptors on vascular smooth muscle, renal mesangial cells, and the adrenal cortex, thereby preventing angiotensin II from exerting its vasoconstrictive, pro-fibrotic, and aldosterone-stimulating effects. Within the kidney specifically, AT1 blockade reduces intraglomerular hypertension, suppresses mesangial cell proliferation, and attenuates the TGF-β–mediated fibrotic cascade — all well-characterized renoprotective mechanisms.

Malignant hypertensive renal disease (accelerated/malignant phase hypertension with renal involvement) is pathologically defined by fibrinoid necrosis of renal arterioles, thrombotic microangiopathy, and rapidly progressive renal failure. Its central driver is uncontrolled RAAS activation: markedly elevated angiotensin II levels sustain severe efferent arteriolar constriction, drive glomerular hypertension, and fuel the vascular injury cycle. This mechanistic overlap — RAAS over-activation as the shared denominator — is the biologically plausible basis for TxGNN positioning candesartan close to this disease node in the knowledge graph.

That said, a critical clinical safety nuance must be acknowledged: in the **acute phase** of malignant hypertension, when renal perfusion pressure has already collapsed, abruptly blocking AT1-mediated efferent arteriolar constriction can paradoxically precipitate or worsen acute kidney injury. This well-recognized ARB hazard in high-renin, volume-depleted states means the risk–benefit profile for this indication is context-dependent and demands careful patient selection, staged dosing, and close renal monitoring. No clinical trial evidence has yet defined when and how ARBs can be safely deployed in this setting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature directly linking candesartan cilexetil to malignant hypertensive renal disease is available.

---

## Canada Market Information

Candesartan cilexetil holds **no Drug Identification Numbers (DINs)** and is **not currently marketed in Canada** according to the regulatory dataset used in this analysis. No approved indications are on record.

> **Context note:** Candesartan cilexetil (marketed as Atacand® and generics in many regions) is approved in the United States, European Union, and Japan for hypertension and, in some jurisdictions, for heart failure with reduced ejection fraction. The absence of Canadian DINs reflects a gap in the current dataset and does not necessarily represent a global approval status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data were not available in the current evidence pack. Key safety gaps include TFDA product monograph warnings/contraindications (DG001, severity: Blocking) and mechanism-of-action–level safety data (DG002, severity: High). These must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although candesartan cilexetil has a mechanistically coherent rationale for renoprotection via AT1 blockade — directly relevant to RAAS-driven malignant hypertensive renal injury — the complete absence of clinical trials, direct supporting literature, and Canadian regulatory approval, combined with unresolved safety data gaps and an identified acute-phase ARB safety hazard, makes advancement premature at this time.

**To proceed, the following is needed:**

- Retrieve and parse the full product monograph (e.g., Atacand® Canadian or US prescribing information) to document contraindications, boxed warnings, and renal-specific precautions (resolves DG001)
- Query DrugBank API for complete MOA, pharmacodynamics, and toxicity profiles (resolves DG002)
- Conduct a targeted literature search for ARB-class drugs (losartan, valsartan, candesartan) in malignant/accelerated hypertension with renal involvement to establish class-level evidence before drug-specific trials
- Define the clinical scenario precisely: acute phase (ICU, IV antihypertensives) vs. subacute/chronic phase (oral ARB use after BP stabilization) — evidence requirements and risk profiles differ substantially
- Evaluate whether candesartan offers mechanistic advantages over other ARBs in this setting (e.g., insurmountable AT1 blockade profile), or whether a class-level development strategy is more appropriate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

