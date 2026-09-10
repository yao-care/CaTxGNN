---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial, historically used to treat bacterial infections (exact original indication not available in this evidence pack). The TxGNN model's top-ranked prediction for this drug is **Polyclonal Hyperviscosity Syndrome**, but currently **0 clinical trials** and **0 publications** support this specific pairing — it is a pure knowledge-graph score with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone class) — specific Canadian labeling text not available |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ofloxacin is not available in this evidence pack. Based on known information, ofloxacin belongs to the fluoroquinolone class of antibacterials, which act by inhibiting bacterial DNA gyrase and topoisomerase IV. This is a purely antibacterial mechanism with no established biological pathway connecting it to polyclonal hyperviscosity syndrome, a disorder driven by excess circulating immunoglobulins (typically seen in autoimmune or lymphoproliferative conditions).

The evidence pack's own rationale for this candidate is explicit: "No identifiable mechanistic link; this is purely a TxGNN knowledge-graph connectivity score, lacking clinical or literature support." Targeted searches against ClinicalTrials.gov, ICTRP, and PubMed for ofloxacin + polyclonal hyperviscosity syndrome all returned zero results.

Given the absence of both a plausible mechanism and any supporting evidence, this candidate should be treated as an early-stage, model-generated hypothesis rather than a scientifically grounded repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ofloxacin currently has no marketing authorizations (DINs) in Canada — market status is **Not Marketed**, with 0 licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Polyclonal Hyperviscosity Syndrome) has no clinical trials, no literature, and no plausible mechanistic link — it is a pure TxGNN model score (L5/S0) and does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA/product-label warnings and contraindications for ofloxacin (currently blocking — flagged as DG001)
- Mechanism of action (MOA) data from DrugBank (flagged as DG002)
- Targeted literature or preclinical work specifically linking ofloxacin to polyclonal hyperviscosity syndrome, if this candidate is to be pursued further
- Consider redirecting evaluation effort to stronger candidates already present in this same evidence pack — notably **septicemic plague** (rank 8, evidence level L3, "Proceed with Guardrails," supported by direct ofloxacin animal-efficacy literature) and **monoclonal gammopathy** (rank 6, evidence level L2, supported by a Phase 3 RCT on the closely related fluoroquinolone levofloxacin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

