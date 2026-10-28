---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 651
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L4). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Nilotinib: From BCR-ABL1-Positive Chronic Myelogenous Leukemia to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor originally used to treat BCR-ABL1-positive chronic myelogenous leukemia.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but currently there are **0 registered clinical trials** and **1 publication** (a review) supporting this direction, so the evidence is at the model-prediction and mechanism level.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, nilotinib is a tyrosine kinase inhibitor that blocks BCR-ABL1, the driver of chronic myelogenous leukemia, and also has activity against PDGFR and KIT.

DFSP is characterized by a COL1A1-PDGFB translocation. This produces a constitutively active PDGFB ligand that drives PDGFR-beta signaling and tumor growth. Because nilotinib can inhibit PDGFR, there is a plausible mechanistic link. Imatinib, a related kinase inhibitor, is established for DFSP, which supports the analogy. This link relies on general knowledge rather than on the compiled data, and the high TxGNN score is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders, describing the role of PDGF/PDGFR signaling as a therapeutic target. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02368250 | TASIGNA | Not specified | Not specified |
| 02315874 | TASIGNA | Not specified | Not specified |
| 02550903 | APO-NILOTINIB | Not specified | Not specified |
| 02550881 | APO-NILOTINIB | Not specified | Not specified |
| 02556634 | REDDY-NILOTINIB | Not specified | Not specified |

Six valid single-ingredient licences are listed in total; the table shows the first five.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists thrombocytopenia, neutropenia and anemia among contraindicated conditions, suggesting haematological effects are relevant. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver function, electrolytes (potassium, phosphorus, calcium), blood glucose, ECG (QT interval) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (these come from drug-disease relationship data, not from package insert text):
  - Cardiovascular and QT: hypertension, long QT syndrome (including familial), torsades de pointes
  - Liver and biliary: liver disease, gallbladder disease, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), pancreatitis
  - Blood: thrombocytopenia, neutropenia, agranulocytosis, anemia (including macrocytic)
  - Metabolic: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia
- **Drug Interactions**: 100 interactions were found in total; 20 are listed in the data compiled for this report.
  - **Major**: dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - **Moderate**: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole (acid-reducing agents), hydrocortisone, betamethasone, triamcinolone, budesonide (including nasal), pioglitazone, loperamide, bupropion, aprepitant, bisacodyl, saxagliptin

Package insert warnings and contraindications from Health Canada were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for this indication is limited to a high TxGNN score, one review article, and a plausible PDGFR-related mechanism analogous to imatinib. There are no registered clinical trials, and the package insert safety data is missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (needed before safety screening)
- Mechanism of action data from DrugBank
- Searches for clinical trials, case series, and preclinical studies of nilotinib in DFSP
- Comparison with imatinib, the established option for DFSP
- Review of the QT prolongation, metabolic, and hepatic risks and the drug interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

