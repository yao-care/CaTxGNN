---
layout: default
title: Soybean Oil
parent: Model Prediction Only (L5)
nav_order: 867
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Soybean Oil: predicted new indication Amenorrhea (evidence level L5). Approved use: Not specified in the Health Canada licence data (the products are use…"
---

# Soybean Oil
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

# Soybean Oil: From Parenteral Nutrition Lipid Source to Amenorrhea

## One-Sentence Summary

Soybean oil is marketed in Canada mainly as a lipid component of parenteral nutrition products, where it supplies calories and essential fatty acids.
The TxGNN model predicts it may be effective for **amenorrhea**,
but there are currently **no clinical trials and no publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Health Canada licence data (the products are used as parenteral lipid emulsions) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, soybean oil is a marketed lipid source used in parenteral nutrition emulsions and as a dietary oil. No established mechanistic link to amenorrhea has been identified.

The TxGNN score (99.61%) is a knowledge-graph computation only. It is not backed by any clinical or literature evidence in the data compiled for this report. Soybean oil is not a recognised treatment for amenorrhea.

Some speculative, indirect pathways can be imagined:
- **Energy deficit or malnutrition:** Functional hypothalamic amenorrhea is linked to low energy availability, and long-term parenteral nutrition addresses malnutrition. Any benefit would come from correcting nutritional status, not from a direct effect on menstrual function.
- **Essential fatty acid deficiency:** Soybean oil supplies essential fatty acids, which could matter if a deficiency is contributing.
- **Phytoestrogen or lipid-mediated effects:** These could in theory influence the hypothalamic-pituitary-ovarian axis.

None of these pathways is supported by data here, and they should be treated as hypotheses only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada lists 13 valid single-ingredient licences. The data compiled for this report do not include dosage forms or approved indication text for these products. The main ones are:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02065673 | INTRALIPID 20% | Not available | Not available |
| 02344327 | CLINOLEIC 20% | Not available | Not available |
| 02396963 | SMOFLIPID 20% | Not available | Not available |
| 02352540 | OLIMEL 5.7% | Not available | Not available |
| 02477947 | OLIMEL 7.6% | Not available | Not available |

The remaining licences are SMOFKABIVEN variants (Electrolyte Free, Extra Nitrogen, Extra Nitrogen Electrolyte Free, Peripheral, standard), PERIOLIMEL 2.5% E, OLIMEL 5.7% E and OLIMEL 7.6% E.

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found, and no contraindication data were identified for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible direct mechanism. Soybean oil is also not a recognised treatment for amenorrhea. The package insert warnings and contraindications have not been reviewed, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (download and parse the product monographs)
- Mechanism of action data (for example, from DrugBank)
- A systematic literature and trial search on lipid emulsions or essential fatty acids in amenorrhea, particularly functional hypothalamic amenorrhea and parenteral nutrition populations
- Assessment of route compatibility, since the licensed products are all intravenous lipid emulsions
- Mechanistic and preclinical support before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

