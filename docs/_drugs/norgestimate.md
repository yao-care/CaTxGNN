---
layout: default
title: Norgestimate
parent: Model Prediction Only (L5)
nav_order: 662
evidence_level: L5
indication_count: 1
---

# Norgestimate
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

# Norgestimate: From Combined Oral Contraception to Elevated Plasma Zinc

## One-Sentence Summary

Norgestimate is a progestin used in combined oral contraceptives. The supplied data does not record an approved indication for it.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but there are **0 clinical trials** and **0 publications** behind this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (norgestimate is a progestin in combined oral contraceptives) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indications are recorded. Norgestimate is a progestin in combined oral contraceptives. Its activity at the progesterone receptor has no recognized role in lowering plasma zinc.

No mechanistic link to the predicted indication can be established from the supplied data. Any connection to zinc homeostasis is speculative. It may be an artifact of the knowledge graph, for example an indirect association through the estrogen co-formulation or shared network neighbors.

Elevated plasma zinc is a laboratory finding rather than a well-defined treatable disease, so its therapeutic relevance is also questionable. The high score (0.99) is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Five of the six authorizations are listed in the data. Dosage form and approved indication text are not recorded for any of them.

| DIN | Product Name |
|---------|------|
| 2508095 | TRI-CIRA 28 |
| 2401967 | TRI-CIRA LO 21 |
| 2486318 | TRI-JORDYNA 28 |
| 2508087 | TRI-CIRA 21 |
| 2486296 | TRI-JORDYNA 21 |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism, so it rests on a model score alone (L5, stage S0). The target is a laboratory finding rather than a treatable disease, so the result should not be advanced as a repurposing candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, and the approved indication text for each Canadian product
- Evidence that elevated plasma zinc is a clinically meaningful treatment target
- Any published or registered study linking norgestimate or progestins to plasma zinc changes
- A check of whether the prediction is a knowledge-graph artifact, for example one driven by the estrogen co-formulation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

