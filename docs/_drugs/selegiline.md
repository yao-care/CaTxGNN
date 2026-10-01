---
layout: default
title: Selegiline
parent: Model Prediction Only (L5)
nav_order: 831
evidence_level: L5
indication_count: 4
---

# Selegiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Selegiline: From Parkinson's Disease to Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis

## One-Sentence Summary

Selegiline is an irreversible MAO-B inhibitor, used for Parkinson's disease according to the published literature.
The TxGNN model predicts it may be effective for **polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis**, a rare congenital brain malformation syndrome.
**No clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (from published literature; the Canadian licence record has no indication text) |
| Predicted New Indication | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. In general pharmacology, selegiline selectively inhibits monoamine oxidase type B, which raises dopamine availability. This is the basis for its use in Parkinson's disease.

The predicted condition is a rare congenital cortical malformation syndrome. It arises from abnormal neuronal migration and cortical development. Selegiline has no known action on these processes, and no plausible mechanistic link was found. The high TxGNN score (0.991) is a graph-based prediction only. It should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2230641 | SELEGILINE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanistic link, so it is Level L5 (model prediction only). It does not justify further investment as it stands.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Health Canada product monograph warnings and contraindications
- A credible biological rationale linking MAO-B inhibition to neuronal migration or cortical development, plus any supporting preclinical data

**Note on other predictions for this drug:** The second-ranked prediction, **schizophrenia** (TxGNN score 99.14%), has much stronger support. It is rated L2 and classed as a "Research Question". Support includes a completed placebo-controlled trial (NCT00456976, n=70, labeled early Phase 1) of selegiline added to antipsychotics for negative symptoms. It also includes double-blind randomized studies (PMID 15677608, 17972359) and a 2023 systematic review and meta-analysis (PMID 37087864). Study designs, effect sizes and risk of bias have not been verified from full text. This candidate deserves a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

