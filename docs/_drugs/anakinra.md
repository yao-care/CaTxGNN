---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Autoinflammatory Diseases to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra (Kineret) is a recombinant human IL-1 receptor antagonist (IL-1Ra) used for rheumatoid arthritis and IL-1-mediated autoinflammatory diseases; its original indication is not formally recorded in this Evidence Pack.
The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
however, there are currently **0 clinical trials** and **0 publications** directly supporting this direction — making this a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack (known use: rheumatoid arthritis, autoinflammatory diseases) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not captured in this Evidence Pack. Based on established pharmacology, Anakinra is a recombinant human IL-1 receptor antagonist that competitively blocks the binding of both IL-1α and IL-1β to their shared receptor IL-1R1. By preventing IL-1 receptor engagement, Anakinra suppresses the downstream NF-κB signaling cascade and the release of secondary inflammatory mediators. It was developed specifically for diseases where IL-1β-driven inflammation is central to pathogenesis.

Extracutaneous mastocytoma is a rare neoplastic condition characterised by clonal mast cell accumulation in extracutaneous organs. Mast cells are capable of secreting IL-1β upon activation, and the theoretical rationale is that IL-1Ra blockade might dampen the local inflammatory microenvironment surrounding neoplastic mast cell infiltrates.

However, the biological link between IL-1 signaling and the oncogenic driver of extracutaneous mastocytoma (typically activating *KIT* mutations, e.g. D816V) has not been established in the literature. Unlike inflammasome-driven autoinflammatory diseases — where Anakinra's efficacy is well-documented — this is primarily a mast cell neoplasm rather than an IL-1-dependent inflammatory syndrome. The TxGNN prediction reflects network proximity in the knowledge graph and should be treated as a mechanistic hypothesis requiring experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Anakinra is currently not marketed in Canada. No Drug Identification Numbers (DINs) are on record in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported solely by TxGNN network-based inference (Evidence Level L5), with no clinical trials, observational studies, or publications directly evaluating Anakinra in extracutaneous mastocytoma. The mechanistic link via IL-1β secretion from neoplastic mast cells is biologically conceivable but entirely unvalidated, and the dominant oncogenic mechanism (*KIT* mutation) is independent of the IL-1 pathway.

**To proceed, the following is needed:**
- Preclinical studies (in vitro / in vivo) measuring IL-1β levels in extracutaneous mastocytoma tissue and assessing IL-1Ra response in relevant mast cell neoplasm models
- Literature review clarifying whether IL-1 signalling plays any functional role in *KIT*-mutant mast cell proliferation or survival
- Full MOA documentation retrieved via DrugBank API to confirm Anakinra's classification and target profile
- Health Canada / TFDA package insert review for complete warnings, contraindications, and drug interaction profile
- Exploration of whether any case reports describe IL-1 inhibition in systemic mastocytosis variants (noting that aggressive systemic mastocytosis at rank 4 has marginal indirect case report evidence via Schnitzler syndrome)

---

> **Disclaimer:** The results of this report are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

