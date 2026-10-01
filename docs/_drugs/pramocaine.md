---
layout: default
title: Pramocaine
parent: Model Prediction Only (L5)
nav_order: 753
evidence_level: L5
indication_count: 1
---

# Pramocaine
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

# Pramocaine: From Topical Itch and Pain Relief to Papillary Conjunctivitis

## One-Sentence Summary

Pramocaine is a topical anesthetic sold in Canada in itch-relief and anorectal products. Its license records do not state a formal indication, so this use is inferred from the product names. The TxGNN model predicts it may be useful for **papillary conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (product names suggest topical itch and anorectal symptom relief) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Pramocaine is generally understood to be a topical anesthetic that blocks voltage-gated sodium channels. This comes from its drug class, not from the input record, so it is unverified here.

If this class mechanism holds, a plausible link is symptomatic relief of ocular itching or irritation through sensory nerve blockade. This would not treat the underlying cause of papillary conjunctivitis, such as allergic or contact lens-related inflammation.

A high prediction score is not clinical evidence. The mechanistic link is unverified, and similarity to the original indication has not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

12 licenses are on record. The main ones are listed below. The records do not include dosage forms or approved indication text.

| DIN | Product Name |
|---------|------|
| 2484889 | ITCH RELIEF MOISTURIZING CREAM |
| 2486881 | ITCH RELIEF MOISTURIZING LOTION |
| 1945912 | ANUSOL PLUS OINTMENT |
| 1954210 | PRAMOX HC LOTION |
| 2236991 | GOLD BOND MEDICATED ANTI-ITCH CREAM |

## Safety Considerations

- **Route and formulation concern**: The marketed pramocaine products are formulated for skin and mucosal use, not for ophthalmic use.
- **Ocular toxicity concern**: Topical ocular anesthetics can cause corneal toxicity with repeated use. This is a significant risk for a chronic or recurrent condition such as papillary conjunctivitis.

Please refer to the package insert for further safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature. The likely benefit is symptom relief only, and ocular use raises a real safety concern because no ophthalmic formulation is marketed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank to verify the mechanistic link
- Assessment of route compatibility, including whether an ophthalmic formulation exists or could be developed
- Any preclinical or clinical evidence of ocular use, including a corneal safety evaluation
- Review of the approved indication text for the Canadian products, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

