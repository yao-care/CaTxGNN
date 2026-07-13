---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Glimepiride: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea antidiabetic agent, originally used to treat Type 2 Diabetes Mellitus by stimulating pancreatic insulin secretion.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
however, **0 clinical trials and 0 publications** currently support this direction, and mechanistic analysis raises fundamental doubts about the plausibility of this repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glimepiride acts by binding to the SUR1 subunit of ATP-sensitive potassium (K-ATP) channels on pancreatic beta cells, triggering channel closure, membrane depolarization, and calcium-dependent insulin release. As a third-generation sulfonylurea, it offers a more insulin-secretion–proportional response with lower hypoglycemia risk compared to earlier agents. It also carries modest PPAR-γ partial agonist activity, contributing to peripheral insulin sensitization. These mechanisms are well-established in the glycemic management of Type 2 Diabetes Mellitus.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder characterized by progressive axial muscle rigidity and episodic spasms. Its pathophysiology is driven by antibodies against glutamic acid decarboxylase 65 (GAD65) — the rate-limiting enzyme for GABA synthesis in inhibitory interneurons — leading to loss of GABAergic inhibition and motor hyperexcitability.

The mechanistic bridge between Glimepiride and SPS is extremely weak. Although K-ATP channels are present in neurons, they are of the SUR2 subtype; Glimepiride has high selectivity for SUR1 and negligible activity at SUR2. Critically, Glimepiride does not modulate autoimmune pathways (anti-GAD65 antibody production), does not enhance GABAergic neurotransmission, and has no established neurological mechanism of action. The high TxGNN prediction score most likely reflects knowledge graph proximity bias — both Glimepiride and GAD65 connect to pancreatic beta cell nodes in the graph — rather than true pharmacological relevance. This prediction should be considered a probable false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Glimepiride currently has no Health Canada Drug Identification Numbers (DINs) on record. It is not marketed in Canada under this data snapshot. No approved product monographs are available from the regulatory database for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (99.75%), the prediction is pharmacologically implausible — Glimepiride's mechanism is specific to pancreatic SUR1 K-ATP channels and has no relevant activity in the GABAergic autoimmune pathophysiology of Classic Stiff Person Syndrome. There is zero clinical or preclinical evidence to support this repurposing direction, and the drug has no market authorization in Canada.

**To proceed, the following would be needed:**
- Mechanistic evidence that Glimepiride affects neuronal SUR2 channels, GABAergic neurotransmission, or autoimmune regulation relevant to SPS
- At minimum, preclinical in vitro or animal model data showing activity in SPS-relevant endpoints (e.g., anti-GAD65 antibody suppression, GABA restoration)
- Resolution of regulatory data gaps: Health Canada product monograph for approved warnings and contraindications
- Full MOA data from DrugBank to complete mechanistic analysis before any further investment in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

