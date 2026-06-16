---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a catechol-O-methyltransferase (COMT) inhibitor approved as an adjunct to levodopa/carbidopa for Parkinson's disease, acting by prolonging the dopaminergic effect of levodopa.
The TxGNN model predicts it may have potential relevance for **PLA2G6-Associated Neurodegeneration (PLAN/NBIA2)**, a rare neurodegeneration with Parkinson-like features due to PLA2G6 gene mutations.
However, this prediction is supported by **no clinical trials and no publications**, making this a model-only hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) |
| Predicted New Indication | PLA2G6-associated neurodegeneration (PLAN/NBIA2) |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Entacapone is a peripheral COMT inhibitor that blocks the degradation of levodopa into 3-O-methyldopa, thereby increasing the bioavailability and extending the half-life of levodopa in the brain. Its efficacy in Parkinson's disease has been well established, and its mechanism is fundamentally tied to enhancing dopaminergic neurotransmission.

PLA2G6-Associated Neurodegeneration (PLAN), also designated NBIA type 2 (Neurodegeneration with Brain Iron Accumulation 2), is caused by loss-of-function mutations in the *PLA2G6* gene, which encodes a phospholipase involved in membrane phospholipid remodelling. A subset of PLAN patients — particularly those with the adult-onset phenotype — develop a clinical picture closely resembling early-onset Parkinson's disease, including nigrostriatal dopaminergic neuron degeneration, levodopa-responsive parkinsonism, and dyskinesia. This phenotypic overlap is the basis for the TxGNN model's prediction.

The mechanistic logic, while indirect, is not entirely implausible: if residual dopaminergic neurons are present in PLAN patients with parkinsonian features, COMT inhibition could theoretically prolong the effect of levodopa in the same manner as in idiopathic Parkinson's disease. However, this reasoning is highly speculative — PLAN is primarily a structural and metabolic disorder of membrane lipids, not a primary dopaminergic disease. The model prediction likely reflects topological similarity in the knowledge graph between PLAN and Parkinson's disease nodes, rather than a validated mechanistic connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Entacapone is not currently marketed in Canada and holds no Drug Identification Numbers (DINs).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is classified as L5 — pure model output with no supporting clinical trials, no published literature, and no approved use in Canada. Although the adult-onset PLAN phenotype does involve dopaminergic neurodegeneration that is conceptually compatible with COMT inhibition, the mechanistic link is indirect and highly speculative, and there is no empirical evidence to support pursuing this indication at this time.

**To proceed, the following is needed:**

- Confirm whether levodopa-responsive parkinsonism is present in the target PLAN patient population, as COMT inhibition is only meaningful in the presence of exogenous levodopa therapy
- Obtain Entacapone's full MOA data from DrugBank (DB00494) and any pharmacodynamic data relevant to secondary neurodegeneration models
- Conduct a targeted literature review for Entacapone or other COMT inhibitors in NBIA-spectrum disorders or PLA2G6 animal models
- Retrieve the product monograph / package insert safety data (TFDA or EMA/FDA label) to complete the safety profile before any S1 screening can proceed
- Consider whether the mechanistically stronger candidates identified in this same Evidence Pack — specifically **rank 4** (paralysis agitans, juvenile, of Hunt; L4, established class-effect rationale) and **rank 7** (Lewy body dementia; L4, with 1 clinical trial and 3 publications) — represent higher-priority repurposing targets for Entacapone that warrant earlier-stage evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

