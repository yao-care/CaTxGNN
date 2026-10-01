---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# Adapalene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical synthetic retinoid, used mainly for acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone and should be treated as a low-confidence signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (topical retinoid); the Canadian licence records provide no indication text |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Adapalene is known as a selective retinoic acid receptor (RAR-beta/gamma) agonist applied to the skin, with minimal systemic absorption. Its efficacy in acne is established, but the source data lists no original indications, so the prediction cannot be checked against documented pharmacology.

A link between retinoid signaling and zinc handling is conceivable in a knowledge graph, for example through retinol-binding protein or metallothionein pathways. This is speculative, and it is unlikely to matter at the low blood exposure that topical use produces.

The very high score (0.995) is most likely a knowledge-graph artifact. "Elevated plasma zinc" is a laboratory finding or biochemical phenotype, not a treatable disease. It has no clear therapeutic goal or clinical endpoint, so the prediction is hard to translate into a real treatment use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02148749 | DIFFERIN |
| 02274000 | DIFFERIN XP |
| 02231592 | DIFFERIN |
| 02517205 | SANDOZ ADAPALENE / BENZOYL PEROXIDE FORTE |
| 02456923 | TARO-ADAPALENE/BENZOYL PEROXIDE |

Ten licences are recorded in total; the five main ones are listed above. Dosage form and approved indication text were not supplied in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or publications. The predicted "indication" is a laboratory finding rather than a disease, and no plausible mechanism links topical adapalene to plasma zinc. The evidence does not justify further investment at this stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank
- A clinically meaningful target disease or endpoint in place of "elevated plasma zinc"
- Any human or preclinical data linking retinoid signaling to zinc homeostasis
- Confirmation that systemic exposure from topical use is relevant to the proposed effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

