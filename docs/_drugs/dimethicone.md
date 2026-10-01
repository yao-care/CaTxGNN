---
layout: default
title: Dimethicone
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Dimethicone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dimethicone: From Gas Relief and Skin Protection to Insomnia

## One-Sentence Summary

Dimethicone is a silicone used as an antifoaming agent and skin protectant. Canadian product names such as gas-relief tablets, infant colic drops and barrier cream point to these uses.
The TxGNN model predicts it may be effective for **insomnia**, but only **1 clinical trial** is registered, it is not an insomnia study, and there are **0 publications**.
This prediction looks like a knowledge-graph artifact rather than a real therapeutic signal, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records. Product names suggest gas relief and skin protection. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Dimethicone is a topical or luminal silicone. It works as a skin protectant and as an antifoaming agent in the gut, and it is barely absorbed into the body. It has no known effect on the central nervous system or on sleep.

Based on this, the link between the original uses and insomnia is not plausible. The high score (0.94) most likely reflects graph proximity in the knowledge graph rather than drug-specific biology. No mechanism was found that would connect dimethicone to sleep regulation.

The other top predictions show the same pattern. Seven of the next nine are cataract subtypes (immature, mature, senile, nuclear, cortical, diabetic, craniostenosis and tetanic cataract), several sharing an identical score. That points to ontology-neighbour propagation. Polydimethylsiloxane appears in eye surgery as silicone oil tamponade and in lens materials, but silicone oil in the eye is associated with cataract as an adverse effect, not a treatment. Severe nonproliferative diabetic retinopathy is also predicted. The only link there is a surgical device use for complications of the proliferative disease, which is not disease-modifying.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | N/A | Completed | 74 | Oral Inner Calm plus topical Super Calm regimen, assessing skin redness, sensitivity and reactivity. It is a dermatology/cosmetic study, not an insomnia study. Dimethicone is at most a formulation component and sleep is not an endpoint (relevance grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage form and approved indication text were not provided in the license records.

| DIN | Product Name |
|---------|------|
| 896675 | GAS-X EXTRA STRENGTH |
| 2328127 | GAS RELIEF TABLETS |
| 2248588 | INFACOL |
| 2256975 | PROSHIELD PLUS |
| 2455838 | CAVILON DURABLE BARRIER CREAM |

Showing 5 of 20 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5). The single registered trial is not about insomnia, no literature exists, and no plausible mechanism links dimethicone to sleep. The high TxGNN score appears to be a graph artifact. The cataract and diabetic retinopathy predictions have the same weakness.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting dimethicone to sleep regulation, which is unlikely given its negligible systemic absorption
- Detailed mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licenses
- Any direct clinical or preclinical evidence in insomnia. Without it, prioritising other candidates is advisable.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

