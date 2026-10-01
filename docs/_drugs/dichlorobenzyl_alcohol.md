---
layout: default
title: Dichlorobenzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 2
---

# Dichlorobenzyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dichlorobenzyl Alcohol: From Throat Lozenge Antiseptic to Bronchitis

## One-Sentence Summary

Dichlorobenzyl alcohol is a mild antiseptic marketed in Canada in throat lozenges (Cepacol and similar products).
The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **1 publication**, which concerns a different compound, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (marketed as throat lozenges) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded in the input. Dichlorobenzyl alcohol is generally known as a mild topical antiseptic in oropharyngeal lozenges. That gives a loose link to upper respiratory symptoms such as sore throat.

The link to bronchitis is weak. A lozenge acts locally in the mouth and throat and would not be expected to reach the bronchi. The high score (99.21%) is a knowledge-graph output. No mechanism or clinical data in this package supports it.

TxGNN also ranked **migraine disorder** second (score 99.02%). No plausible mechanistic link is apparent, since a topical antiseptic has no known action on migraine pathways (CGRP, serotonergic or trigeminovascular). No trials or literature were found. This looks like a knowledge-graph artifact and needs independent mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | Clinical observation | Arzneimittel-Forschung | Reports raised serum creatine kinase in 25 chronic bronchitis patients given oral clenbuterol. Clenbuterol is a different, unrelated compound, so this paper does **not** support the prediction. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2375567 | ANTIBACTERIAL THROAT LOZENGES |
| 2382938 | CEPACOL SENSATIONS |
| 2404982 | CEPACOL CHILDREN'S FRUITY STRAWBERRY |
| 2388642 | CEPACOL SENSATIONS SORE THROAT & COUGH |
| 2382881 | CEPACOL SENSATIONS SORE THROAT & BLOCKED NOSE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials, and the only publication concerns a different drug. A locally acting lozenge is also unlikely to reach the bronchi, so the score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data for dichlorobenzyl alcohol
- Health Canada product monograph warnings and contraindications
- Any clinical or preclinical evidence in bronchitis that involves dichlorobenzyl alcohol itself
- An assessment of whether a route or formulation could deliver the drug to the lower airways
- Independent mechanistic support before pursuing the migraine prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

