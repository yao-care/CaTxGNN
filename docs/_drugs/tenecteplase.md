---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 757
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From ST-Elevation Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

> Tenecteplase is a fibrin-specific tissue plasminogen activator (tPA), established for dissolving coronary artery thrombus in ST-elevation myocardial infarction (STEMI).
> The TxGNN model predicts it may also be effective for **Posterolateral Myocardial Infarction**, an anatomical MI subtype,
> but currently there are **no registered clinical trials** and **no supporting literature** for this specific candidate — the case rests entirely on mechanistic extrapolation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ST-elevation myocardial infarction (STEMI) — inferred from established pharmacology; not recorded in Canada regulatory data (product not marketed in Canada) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is flagged as a data gap in the source DrugBank record (DG002). Based on the information available in this evidence pack, tenecteplase is a fibrin-specific tPA analogue whose established mechanism is dissolution of coronary artery thrombus in STEMI — its broadly recognized original use.

Posterolateral myocardial infarction is not a distinct disease mechanism; it is an anatomical MI subtype defined by the location of the infarcted left ventricular wall. Because the underlying pathology is still coronary thrombotic occlusion, tenecteplase's fibrinolytic mechanism is in principle transferable to this subtype.

However, no subtype-specific clinical data exist to confirm whether dosing, timing, or reperfusion strategy needs adjustment for posterolateral involvement (e.g., management of concomitant right ventricular infarction, which is common with posterolateral/posteroinferior territory involvement). This prediction should be treated as a mechanistic hypothesis, not an evidence-backed indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Tenecteplase is currently **not marketed** in Canada under this evidence pack (0 DINs on file, no licenses recorded). No product/indication table can be generated from available regulatory data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (posterolateral MI) sits at evidence level L4 / decision stage S1 ("Research Question") — no clinical trials or literature directly address this indication, only mechanistic plausibility. This does not meet the bar for further pipeline investment on its own.

**To proceed, the following is needed:**
- Health Canada product monograph — key warnings and contraindications (currently a **blocking** data gap, DG001)
- Structured DrugBank mechanism-of-action documentation (DG002)
- Subtype-specific evidence (dosing/timing adjustments for posterolateral/right-ventricular involvement) before advancing past S1

**Note on prioritization:** among the 10 TxGNN candidates in this evidence pack, **rank #5 "coronary stenosis"** (intracoronary adjunctive tenecteplase during primary PCI) has materially stronger support — evidence level **L2**, decision stage **S2**, recommendation **"Proceed with Guardrails"**, backed by a completed Phase 2 RCT ([NCT00604695](https://clinicaltrials.gov/study/NCT00604695), n=40) and a related cohort/feasibility publication ([PMID 31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/)). If a single candidate must be selected for further development from this drug's portfolio, that indication is the stronger candidate rather than posterolateral MI.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

