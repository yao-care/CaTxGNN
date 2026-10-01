---
layout: default
title: Prednicarbate
parent: Model Prediction Only (L5)
nav_order: 757
evidence_level: L5
indication_count: 7
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Prednicarbate: From Topical Corticosteroid-Responsive Dermatoses to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Prednicarbate is a topical corticosteroid, marketed in Canada as Dermatop Emollient Cream. The Canadian license record does not state an approved indication, so the original use here comes from the drug class.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record (drug class: topical corticosteroid) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prednicarbate is a medium-potency topical corticosteroid. Its efficacy in steroid-responsive inflammatory skin disease is established, but the record does not document it.

The top prediction is not well supported. Vulvar inverted follicular keratosis is a benign follicular neoplasm that is usually treated by excision. A topical corticosteroid has no clear anti-proliferative or anti-inflammatory target in it. The high score most likely reflects knowledge-graph proximity to other keratinizing skin disorders, not clinical plausibility.

Other predicted candidates have a more credible rationale:
- **Lichen planus variants** (hypertrophic, pigmentosus, annular atrophic, pemphigoides): topical corticosteroids are a standard first-line class for cutaneous lichen planus because they suppress the T-cell-mediated interface dermatitis. This is class-level evidence, not prednicarbate-specific. Hypertrophic lesions often need higher-potency steroids, so a medium-potency agent may be inadequate. Atrophic variants also raise a skin-atrophy concern with repeated steroid use.
- **Weak targets:** HEMA sensitization (management is mainly allergen avoidance) and primary cutaneous B-cell lymphoma (established treatments are excision, radiotherapy, intralesional steroids or rituximab).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

For the fourth-ranked candidate (annular atrophic lichen planus), one record was retrieved: [PMID 35001397](https://pubmed.ncbi.nlm.nih.gov/35001397/) (2022, *Clinical and Experimental Dermatology*), "Annular plaques on the back". It is a case-type report describing annular lichen planus. Its abstract does not show that prednicarbate was used or that it worked, so it is not direct evidence.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2230642 | DERMATOP EMOLLIENT CREAM | Cream (from product name) | — |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a model score alone, with no trials, no literature and no clear mechanistic link. The lichen planus candidates are more plausible research questions, but their support is indirect and class-level. Safety data from the Canadian package insert is also missing, which is a blocking gap for safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Mechanism of action data, for example from DrugBank
- A targeted literature search for prednicarbate or medium-potency topical steroids in lichen planus variants
- An assessment of whether medium potency is adequate for hypertrophic lesions, and of atrophy risk with repeated use
- Confirmation of the approved indication and dosage form for DIN 2230642
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

