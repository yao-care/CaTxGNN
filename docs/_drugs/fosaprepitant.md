---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea & Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is an intravenous prodrug of aprepitant, an NK1 receptor antagonist used internationally for prevention of chemotherapy-induced nausea and vomiting (CINV).
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, an ultra-rare X-linked genetic disorder caused by gain-of-function mutations in the AVPR2 receptor gene.
Currently, there are **no clinical trials** and **no published literature** supporting this specific repurposing direction — the prediction is supported by model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV) prevention |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological information, fosaprepitant is the intravenous prodrug of aprepitant — a selective neurokinin-1 (NK1) receptor antagonist. It works by blocking substance P from binding to NK1 receptors in the central and peripheral nervous system, which is the established mechanism for suppressing chemotherapy-induced emesis.

The connection to NSIAD is mechanistically indirect. NSIAD is caused by gain-of-function mutations in the *AVPR2* gene (arginine vasopressin receptor 2, located on the X chromosome), causing constitutive receptor activation and sustained antidiuretic signaling independent of vasopressin levels. While NK1 receptors theoretically participate in renal collecting duct neuromodulation, there is no established mechanistic bridge between NK1 antagonism and AVPR2-driven constitutive antidiuresis. The repurposing rationale notes that the predicted link likely arises from indirect knowledge graph paths connecting renal physiology nodes, not a direct mechanistic pathway.

At this stage, this signal is best understood as a hypothesis-generating output from the model. The prediction does not yet rise to a level warranting clinical investigation without prior basic science validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for fosaprepitant in nephrogenic syndrome of inappropriate antidiuresis.

---

## Literature Evidence

Currently no related literature available for fosaprepitant in nephrogenic syndrome of inappropriate antidiuresis.

---

## Canada Market Information

Fosaprepitant is currently not marketed in Canada. No DINs are registered for this drug.

> **Note for context:** Across all 10 predicted indications in this evidence pack, the most mechanistically supported signal is **retinitis** (rank 7), where a 2021 experimental study (PMID [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/)) demonstrated that fosaprepitant blocks UVR-B–induced NKR-1 (NK1 receptor) upregulation in ocular tissues in a mouse model. This is the only indication with direct fosaprepitant-specific mechanistic data in the pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN knowledge graph inference (L5) with no clinical trials, no published literature, and no established mechanistic link between NK1 receptor antagonism and the AVPR2 gain-of-function mechanism underlying NSIAD.

**To proceed, the following is needed:**

- Basic science investigation into whether NK1/substance P signaling modulates AVPR2 constitutive activity in renal collecting duct cells
- Preclinical models of NSIAD (e.g., *AVPR2* gain-of-function knock-in mice) to test whether NK1 antagonism affects water reabsorption or plasma sodium
- Mechanism of action data (MOA) from DrugBank or primary literature to characterize the full NK1 antagonist pharmacology
- Safety and contraindication data from a product monograph or package insert (currently unavailable; classified as a blocking data gap)
- Route compatibility assessment — fosaprepitant is IV-only and designed for short-term (1–3 day) perioperative/peri-chemotherapy use; NSIAD is a chronic condition requiring sustained management, representing a significant formulation barrier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

