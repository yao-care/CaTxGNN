---
layout: default
title: Polyethylene Glycol
parent: Model Prediction Only (L5)
nav_order: 741
evidence_level: L5
indication_count: 1
---

# Polyethylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Polyethylene Glycol: From Osmotic Laxative to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polyethylene glycol (PEG) is best known as an osmotic laxative and a pharmaceutical excipient, and its approved indications are not recorded in the available data.
The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**.
**No clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data (PEG is generally known as an osmotic laxative) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indications are recorded for this drug. Based on general knowledge, PEG is used as an osmotic laxative and as an excipient. In topical products it can act as a humectant or vehicle that hydrates the stratum corneum.

That hydrating effect could superficially relate to symptom care in ichthyosis. It is a hypothesis only. It is not a disease-modifying mechanism for the keratinization defects behind congenital ichthyosiform erythroderma, such as defects in the TGM1 or ALOX12B/ALOXE3 pathways.

The very high TxGNN score (0.990) is a graph-based prediction. It may reflect network proximity rather than a true therapeutic signal, so it should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2354551 | RHINARIS NASAL MIST |
| 551805 | SECARIS |
| 2352699 | RHINARIS NASAL GEL |
| 777838 | PEGLYTE POWDER |

## Safety Considerations

- **Topical use on damaged skin**: Topical PEG applied over large areas of impaired skin barrier carries a documented risk of systemic absorption and renal toxicity. This is directly relevant to erythrodermic skin.
- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). There are no trials, no literature, and no validated mechanistic link. The renal toxicity risk of topical PEG on erythrodermic skin adds a safety concern.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence that PEG has a disease-relevant effect in congenital ichthyosiform erythroderma
- A topical-route compatibility assessment and a systemic absorption and renal safety evaluation for extensive barrier-impaired skin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

