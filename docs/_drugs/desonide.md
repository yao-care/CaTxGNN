---
layout: default
title: Desonide
parent: Model Prediction Only (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Desonide: predicted new indication Polyp of vocal cord (evidence level L5). Approved use: Inflammatory dermatoses, such as atopic eczema…"
monitor_inn: "DESONIDE"
predicted_indications: ["polyp of vocal cord", "polyp of middle ear", "polyp of external auditory canal", "polyp of frontal sinus", "polyp of ureter", "polyp of vulva", "fibroepithelial polyp", "neoplastic polyp", "epulis", "uterine polyp"]
---

# Desonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Desonide: From Inflammatory Skin and Airway Conditions to Polyp of Vocal Cord
{: .text-alpha }

## One-Sentence Summary

Desonide is a low-potency topical corticosteroid, originally used for inflammatory conditions such as atopic eczema, contact dermatitis and seborrheic dermatitis.
The TxGNN model predicts it may be effective for **polyp of vocal cord**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory dermatoses, such as atopic eczema, contact dermatitis and seborrheic dermatitis (the Canadian licence records do not include indication text, so this comes from the model's knowledge graph) |
| Predicted New Indication | Polyp of vocal cord |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, desonide is a low-potency topical corticosteroid, its efficacy in inflammatory skin conditions is established, and mechanistically it may have an anti-inflammatory effect applicable to inflammation-related lesions.

Vocal cord polyps are often associated with chronic inflammation and oedema, so a glucocorticoid effect is plausible in principle. However, the available desonide products are dermatologic formulations (cream, ointment, lotion) that are not suited to delivery to the larynx. The link therefore rests on the TxGNN prediction alone.

The other top-ranked predictions are also polyp-type conditions (middle ear, external auditory canal, frontal sinus, ureter, vulva, fibroepithelial, neoplastic, epulis and uterine polyps), all with scores near 99.9% and no clinical or literature support. Some, such as sinonasal and aural polyps, have a class-level rationale because corticosteroids are used in chronic inflammatory conditions at those sites. Others, such as ureteral, uterine and neoplastic polyps, have little mechanistic plausibility and may be graph-based artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229323 | PDP-DESONIDE | Not specified | Not specified |
| 02229315 | PDP-DESONIDE | Not specified | Not specified |

## Safety Considerations

Safety information from the package insert was not available for this report; please refer to the package insert.

The drug-disease contraindication links in the TxGNN knowledge graph (not label text) include the following conditions, which should be verified against the product label:
- **Cardiovascular and metabolic:** hypertension, congestive heart failure, hyperglycaemia, liver disease, gallbladder disease
- **Infections:** herpes simplex virus keratitis, measles
- **Neurological:** epilepsy
- **Endocrine:** hypopituitarism and related pituitary deficiency and hypogonadotropic hypogonadism conditions, including growth hormone deficiency, Kallmann syndrome and Sheehan syndrome
- **Metabolic (urea cycle):** carbamoyl phosphate synthetase I deficiency, hyperargininemia, citrullinemia

No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5). Desonide's available formulations are topical dermatologic products with no established delivery route to the larynx. Mechanism of action and package insert safety data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- Health Canada package insert warnings and contraindications, and approved indication and dosage form details for the two DINs
- A route-of-delivery assessment showing whether a suitable formulation could reach the vocal cords
- A literature and trial search for corticosteroid use in vocal cord polyps, to establish whether any class-level evidence exists
- Review of the knowledge-graph contraindications against the label before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

