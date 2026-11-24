---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In Canada: at least 20 DINs"
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
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ibuprofen: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), label version 2026-01-29; accessed 2026-11-19.) Based on general knowledge, ibuprofen is a non-selective cyclooxygenase (COX) inhibitor with analgesic and anti-inflammatory effects, and its efficacy in arthritis and pain is well established.

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

Ibuprofen has 20 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved indication text were not available for these licences.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00441643 | APO-IBUPROFEN | IBUPROFEN | Marketed |
| 00441651 | APO-IBUPROFEN | IBUPROFEN | Marketed |
| 00585114 | APO-IBUPROFEN TAB 600MG | IBUPROFEN | Marketed |
| 01933531 | ADVIL CAPLETS | IBUPROFEN | Marketed |
| 01933558 | ADVIL TABLETS | IBUPROFEN | Marketed |
| 02186934 | MOTRIN 200MG | IBUPROFEN | Marketed |
| 02232297 | CHILDREN'S ADVIL | IBUPROFEN | Marketed |
| 02242365 | CHILDREN'S MOTRIN | IBUPROFEN | Marketed |
| 02242632 | MOTRIN 300MG | IBUPROFEN | Marketed |
| 02242658 | MOTRIN 400MG | IBUPROFEN | Marketed |
| 02246403 | JUNIOR STRENGTH ADVIL | IBUPROFEN | Marketed |
| 02248231 | ADVIL EXTRA STRENGTH LIQUI-GELS | IBUPROFEN | Marketed |
| 02257912 | IBUPROFEN 200 MG | IBUPROFEN | Marketed |
| 02280175 | CHILDREN'S IBUPROFEN SUSPENSION | IBUPROFEN | Marketed |
| 02357275 | IBUPROFEN LIQUID CAPSULES | IBUPROFEN | Marketed |
| 02357283 | EXTRA STRENGTH IBUPROFEN LIQUID CAPSULES | IBUPROFEN | Marketed |
| 02374226 | MUSCLE & JOINT | IBUPROFEN | Marketed |
| 02376598 | IBUPROFEN LIQUID GEL CAPSULES | IBUPROFEN | Marketed |
| 02376601 | EXTRA STRENGTH IBUPROFEN LIQUID GEL CAPSULES | IBUPROFEN | Marketed |
| 02378310 | MOTRIN LIQUID GELS 400 MG | IBUPROFEN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

