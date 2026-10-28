---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 512
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "KETOPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Ketoprofen
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

## Ketoprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and other arthropathies.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoprofen is a non-selective COX inhibitor (NSAID) with established anti-inflammatory and analgesic effects in arthritis and related joint conditions.

The predicted disease is a rare skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, which disrupts BMP/GDF5 signaling in bone and cartilage development. COX inhibition has no evident link to this pathway. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, ketoprofen might offer symptomatic pain relief, and no data support even that.

**Other predictions worth noting.** Among the top 10 predictions, two have a more plausible, though still unproven, rationale:
- **Juvenile arthritis due to LACC1 defect** (score 0.9974): NSAIDs are used symptomatically in juvenile arthritis. There is no evidence of disease-specific efficacy, and paediatric safety would need review.

The other predictions (for example brachyolmia, myosclerosis, pseudoachondroplasia and WHIM syndrome) have no supporting mechanism in the data compiled for this report. Pseudoachondroplasia offers only a weak symptomatic rationale for joint pain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02172577 | KETOPROFEN SR | Not listed | Not listed |
| 00790435 | KETOPROFEN-E | Not listed | Not listed |
| 00842664 | KETOPROFEN-E | Not listed | Not listed |

All three licences are valid single-ingredient products. None are cancelled.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model relationships, not package insert text): hypertension and hypertensive disorder, liver failure, kidney disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, cardiovascular disease and heart disease.
- **Drug interactions**: 100 interactions were found in the interaction database. The first 20 records reviewed include:
  - **Moderate**: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, acetylsalicylic acid, metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, naltrexone, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - **Minor**: famotidine, ranitidine, cimetidine, linaclotide

Please refer to the package insert for official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or publications. No plausible mechanistic link exists between COX inhibition and the GDF5/BMP signalling defect underlying this disease. The knowledge-graph contraindications, covering cardiovascular, renal, hepatic, bleeding and ulcer risks, also call for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search for ketoprofen in the predicted indication
- A re-prioritisation to review the more plausible candidates (spondyloarthropathy and LACC1-related juvenile arthritis) as research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

