---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ascorbic Acid: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Ascorbic acid deficiency"
monitor_inn: "ASCORBIC ACID"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "segmental odontomaxillary dysplasia", "florid cemento-osseous dysplasia", "perinatal disease", "disease by subcellular system affected", "vitamin deficiency disorder"]
---

# Ascorbic Acid
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

## Ascorbic Acid: From Ascorbic Acid Deficiency and Scurvy to Non-Syndromic Esophageal Malformation
{: .text-alpha }

## One-Sentence Summary

Ascorbic acid (vitamin C) is originally used to treat and prevent ascorbic acid deficiency and scurvy.
The TxGNN model (deep learning) predicts it may be effective for **non-syndromic esophageal malformation**, but **no clinical trials and no publications** currently support this prediction. It rests on the model's score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency; scurvy |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 13 of 13) |
| Number of DINs | 13 (valid: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ascorbic acid is an essential vitamin that works as an antioxidant and as a cofactor for collagen-forming enzymes. Its efficacy in vitamin C deficiency and scurvy is well established.

No mechanistic link to the predicted indication can be identified. Non-syndromic esophageal malformation is a congenital structural defect, and it is not plausibly modifiable by an antioxidant or collagen-cofactor vitamin. The very high score (0.9996) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ascorbic acid is marketed in Canada under 13 valid single-ingredient authorizations, with no cancelled licences. The approved indication text, dosage form and manufacturer are not available for these products. Five main authorizations:

| DIN | Product Name |
|---------|------|
| 00780634 | VITAMIN C |
| 02355981 | ASCOR L 500 |
| 02245214 | VITAMIN C |
| 02238890 | HOT LEMON RELIEF FOR SYMPTOMS OF COLD AND FLU EXTRA STRENGTH |
| 02359499 | MOVIPREP |

The remaining authorizations include multivitamin and pregnancy-vitamin products.

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label safety information.

- **Drug Interactions**: 25 interactions are recorded. Moderate-level interactions include amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine, aluminum hydroxide, bortezomib and deferoxamine. Minor-level interactions include paclitaxel, cisplatin, doxorubicin, ethinylestradiol, pseudoephedrine, ephedrine, flecainide, fluphenazine, indinavir and mexiletine.
- **Disease-level cautions from the knowledge graph** (not label text): kidney disease, primary hyperoxaluria, nephrocalcinosis, hereditary hemochromatosis, sickle cell anemia, diabetes mellitus, peptic ulcer disease, liver disease, hypercalcemia and epilepsy, among others.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no plausible mechanism. A congenital structural malformation is unlikely to respond to vitamin C. The high model score alone is not enough to justify further investment.

For context, the same data set lists other predicted indications with more evidence, such as vitamin deficiency disorder (which is essentially on-label), injury, and perinatal disease (hypoxic-ischemic encephalopathy). If the goal is to find a worthwhile repurposing direction for ascorbic acid, those candidates should be evaluated instead.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking ascorbic acid to esophageal development
- Any preclinical or clinical evidence in esophageal malformation
- Health Canada package insert warnings and contraindications for safety screening
- Review of why the model assigned this score, to rule out an artifact of similarities the model learned between related diseases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

