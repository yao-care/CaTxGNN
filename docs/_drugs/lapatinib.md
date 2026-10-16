---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Lapatinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: HER2-positive breast carcinoma"
---

# Lapatinib
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

# Lapatinib: From HER2-Positive Breast Carcinoma to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib was originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor, and its efficacy in HER2-positive breast carcinoma is established.

A clear mechanistic link to DFSP is not evident. DFSP is typically driven by the COL1A1-PDGFB fusion, which causes constitutive PDGFRB activation. This is a different driver from EGFR/HER2, and the standard targeted therapy is imatinib, a PDGFR inhibitor. Any link for lapatinib would be indirect, for example shared downstream signaling (PI3K/AKT, MAPK) or a possible role for the EGFR pathway in resistance. This remains speculative.

The very high score (0.993) likely reflects network proximity to other kinase inhibitors in the knowledge graph rather than a validated mechanism. The score should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02326442 | TYKERB | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; given the liver, cardiac and lung signals below, liver function, cardiac function (including QT) and electrolytes are relevant |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease relationship data, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, potassium deficiency disease, interstitial lung disease, drug-induced liver injury, heart failure.
- **Drug Interactions**: The interaction query returned 100 records. Those listed in the compiled data include:
  - **Major**: loperamide, clarithromycin.
  - **Moderate**: acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexlansoprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), pioglitazone, saxagliptin, aprepitant, and laxatives or bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes).

Health Canada package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for this indication (evidence level L5). The known mechanism (EGFR/HER2 inhibition) does not match the main driver of DFSP (PDGFRB activation), and imatinib is the established targeted option. The safety profile also carries cardiac (QT), hepatic and pulmonary signals.

**To proceed, the following is needed:**
- Mechanism of action data to assess any plausible link to DFSP
- Preclinical evidence (for example, DFSP cell-line or model data showing EGFR/HER2 pathway dependence)
- A literature and trial search for lapatinib in sarcomas or DFSP
- The Health Canada package insert (warnings, contraindications, approved indication and dosage form), which is needed before safety screening
- A review of the clinical relevance of the major interactions (loperamide, clarithromycin) and of the QT and hepatic risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

