---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 940
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Tretinoin: predicted new indication Rheumatoid nodulosis (evidence level L5). Approved use: Acne, acute promyelocytic leukemia, acquired keratosis…"
monitor_inn: "TRETINOIN"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
---

# Tretinoin
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

## Tretinoin: From Acne and Acute Promyelocytic Leukemia to Rheumatoid Nodulosis
{: .text-alpha }

## One-Sentence Summary

Tretinoin is a retinoid originally used for acne, acute promyelocytic leukemia, acquired keratosis and palmoplantar keratoderma.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**,
but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, acute promyelocytic leukemia, acquired keratosis, palmoplantar keratoderma (the Canadian licence records contain no indication text) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tretinoin is a retinoid (a vitamin A derivative, retinoic acid), its efficacy in acne, acute promyelocytic leukemia and keratinization disorders is established, and mechanistically it may be applicable to inflammatory conditions through immune modulation.

Retinoic acid has been reported to influence the balance between regulatory T cells and Th17 cells and to dampen inflammatory cytokines. This could plausibly relate to rheumatoid-type inflammation. However, this link is theoretical. No clinical or literature evidence supports use in rheumatoid nodulosis, and the missing mechanism data means the reasoning remains speculative.

Other top-ranked predictions (juvenile idiopathic arthritis and related entries, ranks 2–4) share the same speculative immune rationale, and their scores come from the TxGNN model (deep learning). They may reflect similarities the model learned between related diseases, not independent biological evidence. The most biologically plausible prediction in the set is Quinquaud's folliculitis decalvans (rank 10), which is consistent with tretinoin's dermatologic uses, but it also has no supporting trials or publications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02145839 | VESANOID | Not specified | Not specified |
| 00443794 | RETIN-A | Not specified | Not specified |
| 02264633 | RETIN-A MICRO | Not specified | Not specified |
| 02520036 | JAMP TRETINOIN | Not specified | Not specified |
| 01926462 | VITAMIN A ACID | Not specified | Not specified |

Ten valid single-ingredient licences are on record in total; the five above are shown.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Differentiating agent (retinoid) used in acute promyelocytic leukemia; not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph links tretinoin with the following conditions: sunburn; anxiety, neurotic and dysthymic disorders; psychotic, schizophreniform, schizoaffective and other mental disorders; kidney disease; pyoureter; pancreatitis; liver disease; gallbladder disease; congestive heart failure; adrenocortical insufficiency and Addison disease; Crohn disease, Crohn's colitis and inflammatory bowel disease; atopic eczema and atopic dermatitis; osteoporosis and postmenopausal osteoporosis; mycosis fungoides and related cutaneous T-cell lymphomas; diabetes mellitus and diabetic ketoacidosis.
- **Drug Interactions**: 100 interactions were found in total. The main ones rated Major are:
  - Doxycycline
  - Tetracycline
  - Minocycline
  - Vitamin A

  Moderate interactions include aprepitant, clarithromycin and naltrexone. Levofloxacin is rated Minor.
- **Population-specific concerns**: Retinoids carry teratogenicity risk and skeletal toxicity in growing children, which matters particularly for the juvenile arthritis and skeletal predictions.

Package insert warnings and contraindications from Health Canada were not available, so the label should be consulted directly.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rheumatoid nodulosis rests only on a high model score (0.9984) with no registered trials or relevant publications (Evidence Level L5). The retrieved publications on osteoarthritis do not support a tretinoin effect. The knowledge-graph contraindication list is broad, and retinoid skeletal and teratogenic risks add safety concerns.

**To proceed, the following is needed:**
- Mechanism of action data for tretinoin
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical or mechanistic studies of retinoic acid in rheumatoid nodulosis or related nodule-forming inflammation
- A systematic literature search targeted at tretinoin and rheumatoid disease
- Route and formulation compatibility assessment (oral versus topical) for the proposed indication
- Consideration of Quinquaud's folliculitis decalvans as a more biologically plausible alternative candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

