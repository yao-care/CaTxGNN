---
layout: default
title: Baricitinib
parent: Model Prediction Only (L5)
nav_order: 94
evidence_level: L5
indication_count: 2
---

# Baricitinib
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

# Baricitinib: From Inflammatory Disease Therapy to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is a JAK1/JAK2 inhibitor that dampens JAK-STAT-mediated inflammatory signaling and is marketed in Canada as OLUMIANT.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available data |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Baricitinib is generally known as a JAK1/JAK2 inhibitor that reduces JAK-STAT-mediated inflammatory signaling.

The predicted disease is a rare congenital developmental malformation affecting the eye and skeleton. A JAK-STAT inflammatory mechanism has no evident relevance to its pathogenesis, so **no supported mechanistic link** was identified. The very high TxGNN score (99.94%) is a knowledge-graph prediction and may reflect graph topology rather than biology. It should not be treated as clinical evidence.

The second-ranked prediction, **brachydactyly-syndactyly syndrome** (score 99.94%), has the same problem. It is a congenital limb malformation, and inhibiting JAK-STAT signaling would not be expected to correct a structural developmental defect. It also has no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2544768 | OLUMIANT |
| 2480018 | OLUMIANT |

Dosage form and approved indication text were not provided for these licenses.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the available data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no trials or publications, and no plausible mechanistic link between JAK-STAT inhibition and the pathogenesis of a congenital developmental malformation. The same applies to the second prediction.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Approved indication text and dosage forms for the two Canadian licenses
- Any preclinical or clinical evidence linking JAK-STAT signaling to the predicted syndromes, including a check that they are plausible targets for postnatal drug treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

