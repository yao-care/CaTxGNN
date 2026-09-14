---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
---

# Siltuximab
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

# Siltuximab: From Multicentric Castleman Disease to Extracutaneous Mastocytoma

## One-Sentence Summary

> Siltuximab is an anti-IL-6 monoclonal antibody, referenced in this evidence pack in the context of its approved use for Multicentric Castleman Disease (MCD).
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but this specific pairing currently has **no clinical trials** and **no literature** support — the score is model-generated only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multicentric Castleman Disease (MCD) — noted contextually in the evidence pack; not confirmed via a Canadian licence record |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A structured MOA record is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, a clinical trial description captured in the evidence (NCT02796859) confirms siltuximab is "a recombinant chimeric (human-murine) anti-human interleukin-6 (IL-6) monoclonal antibody," administered by IV infusion. This is consistent with siltuximab's known role in suppressing IL-6-driven inflammatory and lymphoproliferative pathways.

The mechanistic rationale supplied for this candidate states that extracutaneous mastocytoma's biology is inferred to resemble that of systemic mastocytosis, which is IL-6-related — mast cell activation can drive IL-6 secretion, and blocking IL-6 signaling is hypothesized to dampen this loop. However, the rationale explicitly notes this link is "supported only by the prediction score, without empirical evidence" (無實證).

Because no clinical trials or publications specific to extracutaneous mastocytoma were found, the biological plausibility described above remains theoretical. It is worth noting that other candidates in this same prediction set — particularly TAFRO syndrome (rank 10) and Kaposi's sarcoma (rank 5) — have a mechanistically stronger and better-documented connection to siltuximab's IL-6 pathway (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Siltuximab is currently **not marketed in Canada** (0 licences/DINs on record in this evidence pack), so no Canadian authorization or approved-indication table can be produced at this time.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada-equivalent warnings and contraindications are flagged as a Blocking data gap — DG001 — and must be resolved before any safety pre-assessment (S1) can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The extracutaneous mastocytoma prediction is supported only by the TxGNN score (L5) — there are zero clinical trials and zero publications specific to this drug-disease pair, and the drug is not marketed in Canada.
- A Blocking data gap on product safety information (DG001) prevents even an initial safety screen (S1) from being completed.

**To proceed, the following is needed:**
- Canadian/TFDA-equivalent product monograph or package insert (resolves DG001, required for S1 safety screening)
- Formal DrugBank MOA record (resolves DG002, needed for mechanistic-link validation)
- Preclinical or case-level evidence directly linking siltuximab to extracutaneous mastocytoma
- Consider prioritizing higher-evidence candidates from this same prediction batch for separate review — notably **TAFRO syndrome** (L4, Research Question stage, mechanistically overlapping with the already-approved MCD indication) and **Kaposi's sarcoma** (L4, HHV-8/vIL-6-linked to Castleman disease), both of which have stronger biological rationale than extracutaneous mastocytoma despite similarly sparse direct trial/literature evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

