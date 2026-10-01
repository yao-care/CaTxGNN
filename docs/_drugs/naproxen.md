---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 4
---

# Naproxen
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

# Naproxen: From NSAID Pain and Inflammation Use to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation. The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation. **No clinical trials and no publications** support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence records (drug class: NSAID, analgesic and anti-inflammatory) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Naproxen is generally known as a non-selective COX-1/COX-2 inhibitor. By blocking COX enzymes, it reduces prostaglandin synthesis, which relieves pain, fever, and inflammation.

The predicted indication is a congenital limb malformation of genetic origin. Prostaglandin inhibition is not known to correct a developmental defect of this kind. The high score (99.35%) most likely reflects the structure of the knowledge graph rather than a biological rationale. At most, naproxen might offer symptomatic pain relief, which is not disease modification.

The other three top predictions show the same pattern, each with a score above 99%:

| Predicted Disease | Score | Assessment |
|------|------|------|
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.22% | Ultra-rare ocular and skeletal malformation. No known link to COX inhibition. |
| Acromesomelic dysplasia, Hunter-Thompson type | 99.17% | Linked to the BMP/GDF5 signalling pathway, which naproxen does not target. |
| Brachyolmia-amelogenesis imperfecta syndrome | 99.06% | Affects skeletal and enamel mineralization. Naproxen does not address either. |

All four are L5 (model prediction only) with no supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Naproxen has 20 licences in Canada. The five main ones are listed below. The supplied records do not include dosage form or approved indication text for these entries.

| DIN | Product Name |
|---------|------|
| 2162725 | ANAPROX |
| 2246701 | APO-NAPROXEN EC |
| 2243313 | TEVA-NAPROXEN EC |
| 2162717 | ANAPROX DS |
| 2162423 | NAPROSYN |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or publications, and no plausible mechanism links COX inhibition to correcting a genetic limb malformation. Naproxen is widely marketed in Canada, but that does not support this new indication.

**To proceed, the following is needed:**
- A mechanistic review of whether prostaglandin signalling plays any role in the disease's pathophysiology
- Mechanism of action data for naproxen from DrugBank
- Health Canada package insert warnings and contraindications, needed before any safety screening
- Any preclinical or case-level evidence linking naproxen to this condition. Without it, the candidate should not advance beyond Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

