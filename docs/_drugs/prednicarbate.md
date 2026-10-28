---
layout: default
title: Prednicarbate
parent: Model Prediction Only (L5)
nav_order: 764
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "PREDNICARBATE"
predicted_indications: ["vulvar inverted follicular keratosis", "hypertrophic lichen planus", "lichen planus pigmentosus", "annular atrophic lichen planus", "lichen planus pemphigoides", "2-hydroxyethyl methacrylate sensitization", "primary cutaneous B-cell lymphoma"]
description: "Prednicarbate: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Prednicarbate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Prednicarbate: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Prednicarbate is a topical mid-potency corticosteroid, originally used for inflammatory skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis and lichen disease.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prednicarbate is a topical mid-potency corticosteroid. Its efficacy in inflammatory dermatoses is established, and it is expected to act through glucocorticoid receptor-mediated anti-inflammatory effects.

Seborrheic keratosis is one of its listed original indications. Inverted follicular keratosis is a benign epithelial lesion related to seborrheic keratosis, which likely explains the high TxGNN score. The link rests on disease similarity alone.

There are important limits to this reasoning. Inverted follicular keratosis is a benign growth that is normally managed by excision or observation, and an anti-inflammatory steroid is not expected to resolve it. The vulvar location also raises concerns about mucosal absorption and skin atrophy.

### Other Predicted Indications

The model also ranked the following diseases highly. None has trial or literature support, and all are rated L5 / Hold.

| Rank | Predicted Indication | Score | Key Considerations |
|------|------|------|------|
| 2 | Hypertrophic lichen planus | 0.9964 | Topical steroids are first-line for lichen planus, but thick hypertrophic lesions usually need super-potent steroids or intralesional therapy, so a mid-potency agent may be insufficient. |
| 3 | Lichen planus pigmentosus | 0.9964 | Topical steroids are sometimes used, but the response is inconsistent and pigmentation often persists. |
| 4 | Annular atrophic lichen planus | 0.9964 | The mechanism is plausible, but prolonged steroid use may worsen the atrophy. |
| 5 | Lichen planus pemphigoides | 0.9953 | Localized disease may respond to topical steroids, but moderate to severe disease usually needs systemic therapy. |
| 6 | 2-Hydroxyethyl methacrylate sensitization | 0.9947 | This overlaps with the existing contact dermatitis indication and may ease symptoms, but it does not treat the sensitization. Allergen avoidance remains the main management. |
| 7 | Primary cutaneous B-cell lymphoma | 0.9940 | The prediction is driven by the existing T-cell lymphoma use. B-cell lymphomas are biologically distinct, and topical steroids have no established disease-modifying role. |

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
| 02230642 | DERMATOP EMOLLIENT CREAM | Not available | Not available |

---

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text)**: adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease.
- **Relevance to the predicted use**: Skin atrophy is a particular concern for vulvar application and for atrophic lesions such as annular atrophic lichen planus.
- **Drug interactions**: No interaction records were found.

For label warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for vulvar inverted follicular keratosis is supported only by model similarity to seborrheic keratosis. There are no trials or publications. The lesion is benign and normally treated by excision or observation, and the vulvar site raises absorption and atrophy concerns. The other predicted indications are also unsupported by evidence, and several would likely need more potent or systemic treatment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank, to support the mechanistic-link analysis.
- Dosage form, route and approved indication details for the Canadian product, to check route compatibility.
- A literature and trial search for the predicted indications. Hypertrophic lichen planus and the lichen planus variants are the most biologically plausible candidates to prioritize.
- A vulvar-specific safety assessment covering mucosal absorption and skin atrophy, if that site is pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

