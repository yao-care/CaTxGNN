---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Ibuprofen
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

## Ibuprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for arthritis, headache and pain conditions, and for closing a patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **no clinical trials and no publications** supporting this prediction. The evidence is model-prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ibuprofen is a non-selective cyclooxygenase (COX) inhibitor with analgesic and anti-inflammatory effects, and its efficacy in arthritis and pain is well established.

Acromesomelic dysplasia, Hunter-Thompson type, is a skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, which disrupt limb cartilage formation. COX inhibition would not be expected to correct this developmental defect. No direct mechanistic link is supported by the available data.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as musculoskeletal conditions that share features with ibuprofen's approved arthritis indications, not biological evidence. It does not reflect a biological rationale. At most, ibuprofen might be used for symptomatic pain relief, which is standard supportive care and not disease modification.

The other top-ranked predictions show the same pattern, and none has a plausible mechanism or supporting evidence:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9971 | Genetic skeletal and dental defect; no plausible pharmacological pathway |
| 3 | Myosclerosis | 0.9968 | Speculative; may relieve pain but no evidence of effect on fibrosis |
| 4 | Brachyolmia | 0.9967 | Genetic skeletal dysplasia; likely a similarity the model learned between related diseases |
| 5 | Brachydactyly-syndactyly syndrome | 0.9966 | Congenital limb malformation; no mechanistic rationale |
| 6 | Pseudoachondroplasia | 0.9966 | Indirect at best; symptomatic joint pain relief only |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9960 | Developmental genetic origin; COX inhibition not relevant |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ibuprofen has 20 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved indication text were not available for these licences. Five main authorisations are listed below.

| DIN | Product Name |
|---------|------|
| 02242632 | MOTRIN 300MG |
| 02376598 | IBUPROFEN LIQUID GEL CAPSULES |
| 00441643 | APO-IBUPROFEN |
| 02248231 | ADVIL EXTRA STRENGTH LIQUI-GELS |
| 00585114 | APO-IBUPROFEN TAB 600MG |

Other products include Advil caplets and tablets, Children's Advil, Children's Motrin, Junior Strength Advil and several liquid capsule products.

---

## Safety Considerations

**Contraindications / Disease Conflicts (from the knowledge graph, not label text):**
The knowledge graph links ibuprofen with caution or contraindication in the following groups of conditions:
- **Cardiovascular and cerebrovascular:** hypertension, hypotension, myocardial infarction, stroke, cerebral infarction
- **Gastrointestinal:** peptic ulcer disease, inflammatory bowel disease, gallbladder disease
- **Liver and kidney:** liver failure, liver disease, kidney disease
- **Blood:** thrombocytopenia, blood coagulation disease
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hypothyroidism, potassium deficiency
- **Other:** epilepsy, COPD, systemic lupus erythematosus, benign prostatic hyperplasia, substance abuse/dependence

**Drug Interactions:** The interaction query returned 100 interactions in total; the first 20 are summarised below.
- **Major:** acetylsalicylic acid (aspirin)
- **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, aprepitant, balsalazide, fenfluramine, dexfenfluramine, kanamycin, levofloxacin
- **Minor:** H2 blockers (famotidine, ranitidine, cimetidine)

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone, with no clinical trials, no literature and no plausible mechanistic link to the underlying genetic defect. The score is likely a TxGNN model (deep learning) artifact.

**To proceed, the following is needed:**
- Mechanism of action data for ibuprofen, and a biological rationale linking COX inhibition to GDF5-related limb development
- Preclinical or clinical evidence in acromesomelic dysplasia, or a review of whether symptom management is the only realistic goal
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Approved indication and dosage form data for the Canadian licences
- Route-compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

