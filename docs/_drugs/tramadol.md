---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 927
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Tramadol
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

## Tramadol: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tramadol is an opioid/SNRI-type analgesic, originally associated with osteoarthritis and arthropathy pain management.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **0 clinical trials** and **0 publications** currently support this direction, so the prediction is purely computational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tramadol is a centrally acting analgesic (opioid/SNRI class). Its use in osteoarthritis and other joint pain is established, so it may mechanistically offer symptomatic pain relief in other skeletal or joint conditions.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia caused by CDMP1/GDF5 mutations. Tramadol has no known effect on this underlying pathway. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At best, any benefit would be limited to symptomatic pain relief.

The other top predictions show the same pattern. They are mostly rare skeletal disorders (brachyolmia, pseudoachondroplasia, myosclerosis) and juvenile or rheumatoid arthritis subtypes, all with scores above 0.9990 and none with supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction. (For the rank 7 prediction, juvenile idiopathic arthritis, the single retrieved publication concerns ketoprofen rather than tramadol and is not considered relevant evidence.)

## Canada Market Information

Tramadol has 20 valid single-ingredient licences in Canada. Dosage form and approved indication text are not available for these products. Main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02286459 | ZYTRAM XL | Not available | Not available |
| 02518759 | JAMP TRAMADOL HCL | Not available | Not available |
| 02480859 | MAR-TRAMADOL | Not available | Not available |
| 02373033 | DURELA | Not available | Not available |
| 02296381 | TRIDURAL | Not available | Not available |

Other marketed brands include AURO-TRAMADOL, RALIVIA, APO-TRAMADOL and TARO-TRAMADOL ER.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (graph-derived, not label text): hypertensive disorder/hypertension, liver failure, liver disease, cirrhosis, epilepsy, anxiety and neurotic disorders, dysthymic disorder, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, substance-related disorder, hyperlipidemia, respiratory failure, paracetamol poisoning, serotonin syndrome, pseudotumor cerebri/intracranial hypertension, alcohol withdrawal, Wernicke-Korsakoff syndrome, substance withdrawal syndrome, and central nervous system infections.
- **Drug interactions** (DDInter; 100 interactions found, 20 reviewed):
  - **Major**: alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine, fenfluramine.
  - **Moderate**: atropine, bisacodyl, castor oil, cimetidine, clarithromycin, clidinium, dicyclomine, eliglustat, eluxadoline, famotidine, glycerin.
- For the rank 7 prediction (juvenile idiopathic arthritis), opioid use in children raises additional safety concerns.

Please refer to the package insert for the complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or literature, and tramadol has no plausible disease-modifying mechanism for this rare skeletal dysplasia. Evidence is at level L5.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to support a mechanistic link
- Package insert warnings and contraindications from Health Canada, including approved indication text and dosage forms for the licences
- Any preclinical or clinical evidence in the predicted indication, or a clearly defined symptomatic-pain use case with a safety plan
- Review of the safety and interaction profile for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

