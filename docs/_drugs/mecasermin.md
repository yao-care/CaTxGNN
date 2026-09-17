---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 489
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X

## One-Sentence Summary

Mecasermin is a recombinant human IGF-1 analogue, originally used to treat severe primary IGF-1 deficiency (growth hormone insensitivity syndromes such as Laron syndrome). The TxGNN model predicts it may be relevant to **Monosomy X (Turner syndrome)**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic link is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe Primary IGF-1 Deficiency / GH insensitivity syndrome (e.g. Laron syndrome) — no official Canadian label text available, drug not marketed |
| Predicted New Indication | Monosomy X (Turner syndrome) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, mecasermin is a recombinant human insulin-like growth factor-1 (IGF-1), whose efficacy in severe primary IGF-1 deficiency / GH insensitivity syndrome has been established, and mechanistically it may have theoretical relevance to other growth-related conditions.

Monosomy X (Turner syndrome) commonly presents with growth failure, which is conventionally treated with growth hormone (GH) rather than IGF-1. Since IGF-1 is the downstream signaling effector of GH, there is a shared pathway rationale for considering it in growth disorders.

However, the growth failure in Turner syndrome is primarily attributed to SHOX gene haploinsufficiency rather than a classic GH/IGF-1 deficiency state. The mechanistic link is therefore an indirect inference based on shared phenotype (growth impairment) rather than a confirmed shared etiology, and no clinical or literature evidence currently exists to support or refute it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Mecasermin currently holds no Health Canada marketing authorization (0 DINs, market status: Not marketed). No product listings are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 (model prediction only) — there are no clinical trials or publications supporting mecasermin for monosomy X, the mechanistic link is indirect (shared "growth failure" phenotype rather than shared etiology), and the drug is not currently marketed in Canada. All other TxGNN-ranked candidates for this drug (Wolman disease, GH insensitivity with immune dysregulation, esophageal varices with/without bleeding) are similarly L5 with no supporting evidence, and several show a plausible knowledge-graph comorbidity artifact rather than a true treatment signal.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Dedicated literature and clinical trial searches specific to monosomy X and IGF-1 pathway overlap
- Endocrinology expert input on whether SHOX-driven growth failure is a biologically plausible target for exogenous IGF-1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

