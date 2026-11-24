---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Lapatinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: HER2-positive breast carcinoma"
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Lapatinib: From HER2-Positive Breast Carcinoma to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Lapatinib was originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lapatinib: "Lapatinib is a 4-anilinoquinazoline kinase inhibitor of the intracellular tyrosine kinase domains of both Epidermal Growth Factor Receptor (EGFR [ErbB1]) and of Human Epidermal Receptor Type 2 (HER2 [ErbB2]) receptors (estimated K i app values of 3nM and 13nM, respectively) with a dissociation half-life of greater than or equal to 300 minutes. Lapatinib inhibits ErbB-driven tumor cell growth in vitro and in various animal models." ([DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c), label version 2026-01-27; accessed 2026-11-19.) Based on general pharmacology, lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor, and its efficacy in HER2-positive breast carcinoma is established.

A clear mechanistic link to DFSP is not evident. DFSP is typically driven by the COL1A1-PDGFB fusion, which causes constitutive PDGFRB activation. This is a different driver from EGFR/HER2, and the standard targeted therapy is imatinib, a PDGFR inhibitor. Any link for lapatinib would be indirect, for example shared downstream signaling (PI3K/AKT, MAPK) or a possible role for the EGFR pathway in resistance. This remains speculative.

The very high score (0.9930) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The score should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02326442 | TYKERB | LAPATINIB (LAPATINIB DITOSYLATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

