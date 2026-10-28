---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 834
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is originally used for skin and inflammatory conditions such as acne, seborrheic dermatitis, fungal skin infections (tinea) and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 7 of 7) |
| Number of DINs | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Salicylic acid is generally proposed to act through inhibition of COX enzymes and modulation of inflammatory signalling (such as NF-kB). However, public bioactivity data confirming a primary molecular target are lacking.

Papillary conjunctivitis is an allergic or inflammatory eye condition. Salicylic acid is already linked to inflammatory and allergic conditions such as allergic rhinitis, which gives a possible shared inflammatory basis for the prediction. This link is inferred only.

There are important caveats. No trials or literature support this use, and the safety of salicylic acid in the eye has not been established. Keratolytic salicylic acid formulations are known to irritate the eye. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions are weaker. Most are rare genetic skeletal or developmental disorders (for example brachyolmia, pseudoachondroplasia and brachydactyly-syndactyly syndrome) with no plausible mechanistic link. Two have some rationale:
- Any assessment should compare against established NSAIDs.
- **Rosacea conjunctivitis** has a weak, speculative link through acne and inflammatory skin disease, with an eye irritation concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00666114 | SEBCUR-T | Not specified | Not specified |
| 00578436 | DIPROSALIC | Not specified | Not specified |
| 02428946 | ACTIKERALL | Not specified | Not specified |
| 02402149 | ACNE TREATMENT SYSTEM | Not specified | Not specified |
| 02245688 | RATIO-TOPISALIC | Not specified | Not specified |

Two further single-ingredient licences are valid: CANTHARONE PLUS (00772011) and TARDAN SHP (00266493). None are cancelled.

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry was found, involving the acid-sensing ion channel ASIC3. It has no assigned severity level and does not represent a clinical drug-drug interaction.
- **Ocular safety**: Keratolytic salicylic acid formulations are irritating to the eye. Ocular use has not been evaluated.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis has a high model score (0.9988) but no supporting trials or literature (Evidence Level L5). There is also a plausible ocular irritation concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Mechanism of action data for salicylic acid
- A literature and trial search specific to salicylates in allergic or papillary conjunctivitis
- Assessment of ocular tolerability and suitable ophthalmic formulations and routes, since the current Canadian products do not appear to be ophthalmic
- A comparison against established treatments for allergic conjunctivitis, and against NSAIDs if the spondyloarthropathy prediction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

