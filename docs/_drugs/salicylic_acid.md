---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 827
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Topical Dermatologic Use to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is a widely used topical agent, mainly as a keratolytic, and is marketed in Canada in several skin-treatment products.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical keratolytic and dermatologic use (indication text is not available in the Canadian license records provided) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, salicylic acid is a salicylate with keratolytic and anti-inflammatory activity. Its use in skin conditions is established, and mechanistically it might be applicable to inflammatory conditions of the ocular surface.

The link between the original use and the predicted indication is weak. Papillary conjunctivitis is an inflammatory eye condition, and salicylic acid's anti-inflammatory properties offer only a loose connection. Salicylic acid is mainly applied to the skin, and putting it on the ocular surface raises irritation and safety concerns. The very high TxGNN score (0.9988) therefore reflects model prediction rather than demonstrated biology or clinical evidence.

Other predictions for this drug are weaker still. Most of the top 10 are rare congenital skeletal or developmental disorders (for example brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome). No plausible mechanism for salicylic acid is evident for these, and they are likely knowledge-graph proximity artifacts. The one exception is spondyloarthropathy susceptibility (rank 10, L4). It has a class-level rationale through NSAID-type COX inhibition, but it is framed as genetic susceptibility rather than active disease and has no salicylic acid-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the seven authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 666114 | SEBCUR-T |
| 578436 | DIPROSALIC |
| 2428946 | ACTIKERALL |
| 2402149 | ACNE TREATMENT SYSTEM |
| 2245688 | RATIO-TOPISALIC |

Dosage form and approved indication text were not provided for these products.

---

## Safety Considerations

Please refer to the package insert for safety information.

Ocular application of salicylic acid raises irritation and safety concerns that would need to be addressed before any eye-related use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score, with no clinical trials or literature, and the mechanistic link to papillary conjunctivitis is weak. Ocular surface safety is a concern, and safety documentation for the Canadian products is not yet available.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Indication, dosage form, and route details for the Canadian products
- A literature and trial search specific to salicylic acid in conjunctival or ocular surface inflammation
- Ocular tolerability and formulation-route assessment, since current products are topical dermatologic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

