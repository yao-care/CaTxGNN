---
layout: default
title: Flumethasone
parent: Model Prediction Only (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flumethasone: predicted new indication Alopecia areata (evidence level L5). Approved use: Atopic dermatitis, contact dermatitis, seborrheic dermatitis…"
monitor_inn: "Flumethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "primary cutaneous B-cell lymphoma", "alopecia universalis onychodystrophy vitiligo"]
---

# Flumethasone
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

# Flumethasone: From Inflammatory Skin Conditions to Alopecia Areata

## One-Sentence Summary

Flumethasone is a corticosteroid originally used for inflammatory and immune-related skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **alopecia areata**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on model output and drug-class reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis, contact dermatitis, seborrheic dermatitis, discoid lupus erythematosus and other inflammatory skin conditions (the Health Canada records compiled contain no indication text) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for flumethasone is not currently available. Based on known information, flumethasone is a potent topical corticosteroid, its use in inflammatory and autoimmune-related skin diseases is established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is driven by T-cell-mediated autoimmune inflammation around hair follicles. Corticosteroids suppress this type of inflammation, and other members of the class, such as intralesional triamcinolone and topical clobetasol, are established treatments. This is class-level reasoning, not flumethasone-specific data.

The high TxGNN score (99.93%) is a computational prediction only. Other predictions in the list vary in biological plausibility:

- **Plausible by class effect:** folliculitis decalvans (adjunct to antibiotics), alopecia mucinosa, and primary cutaneous B-cell lymphoma (adjunctive use at most, by analogy with the T-cell lymphoma indication).
- **Weak support:** telogen effluvium (usually non-inflammatory), and rare genetic conditions such as hereditary hypotrichosis with recurrent skin vesicles, atrichia with papular lesions, and alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome.
- **Possible harm:** alopecia with antibody deficiency, where immunosuppression may increase infection risk.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00074462 | LOCACORTEN VIOFORM | Not specified | Not specified |
| 00074454 | LOCACORTEN VIOFORM EARDROPS | Not specified | Not specified |

Both products are valid single-ingredient authorizations; none are cancelled.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not label text): hypopituitarism and related pituitary hormone deficiencies, hypogonadotropic hypogonadism (including Kallmann syndrome), growth hormone deficiency, thymus gland disease, skin atrophy, telangiectasis and capillary disease, and hereditary hemorrhagic telangiectasia. The skin atrophy and telangiectasis signals are consistent with known effects of potent topical corticosteroids, particularly with prolonged use on the scalp or face.
- **Drug Interactions:** No interaction records were found.

Please refer to the package insert for the complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for alopecia areata has no supporting trials or publications, so it remains a research question. The drug-class rationale is reasonable but not specific to flumethasone, and the Canadian products compiled are combination-type brands (LOCACORTEN VIOFORM) with no indication text on record.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for flumethasone, or comparable potent topical corticosteroids, in alopecia areata
- Confirmation of route and formulation compatibility with scalp or intralesional use
- Review of the contraindication signals above, including the risk of skin atrophy with long-term scalp use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

