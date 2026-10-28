---
layout: default
title: Fedratinib
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Fedratinib: predicted new indication Benign PEComa (evidence level L5). Approved use: Primary myelofibrosis"
monitor_inn: "Fedratinib"
predicted_indications: ["benign PEComa", "lymphangiomyoma", "uterine corpus perivascular epithelioid cell tumor", "dermatofibrosarcoma protuberans", "rhabdoid tumor", "familial rhabdoid tumor", "autosomal recessive familial Mediterranean fever", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection", "lymphangioleiomyomatosis"]
---

# Fedratinib
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

## Fedratinib: From Myelofibrosis to Benign PEComa
{: .text-alpha }

## One-Sentence Summary

Fedratinib is a kinase inhibitor originally used to treat primary myelofibrosis and myelofibrosis.
The TxGNN model predicts it may be effective for **benign PEComa**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary myelofibrosis; myelofibrosis |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fedratinib is a JAK2/FLT3 inhibitor, and its efficacy in myelofibrosis is established.

PEComa (perivascular epithelioid cell tumour) is commonly driven by mTOR pathway activation through loss of TSC1/TSC2. No direct mechanistic link between fedratinib and mTOR signalling is established in the data compiled for this report. A possible connection through JAK/STAT crosstalk with the PI3K/AKT/mTOR pathway is speculative. The prediction is therefore best viewed as a network-similarity signal from the model, not as a mechanism-supported hypothesis.

Other top-ranked predictions are also without trial or literature support:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Lymphangiomyoma | 0.9983 | Related to LAM (TSC/mTOR-driven); no demonstrated JAK2 link |
| 3 | Uterine corpus PEComa | 0.9983 | PEComa family; no direct link |
| 4 | Dermatofibrosarcoma protuberans | 0.9980 | Driven by PDGFR signalling; imatinib is the established therapy |
| 5 | Rhabdoid tumour | 0.9978 | SMARCB1 loss; no link to JAK2/FLT3 |
| 6 | Familial rhabdoid tumour | 0.9977 | Hereditary form; likely network similarity |
| 7 | Familial Mediterranean fever (autosomal recessive) | 0.9975 | Speculative cytokine-signalling dampening; established therapies exist |
| 8 | Acquired HLH associated with malignancy | 0.9974 | JAK/STAT-driven cytokine storm; the more mechanistically plausible candidate |
| 9 | Infection-associated hemophagocytic syndrome | 0.9974 | Same rationale as rank 8 |
| 10 | Lymphangioleiomyomatosis | 0.9974 | mTORC1-driven; sirolimus is the established therapy |

Among these, the HLH indications have the most plausible biology, since JAK/STAT signalling mediates the cytokine storm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502445 | INREBIC | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (JAK2/FLT3 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver function and renal function) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Examples of those listed:
  - **Major**: dexamethasone, clarithromycin, eliglustat, naloxegol
  - **Moderate**: rabeprazole, omeprazole, lansoprazole, cimetidine, aprepitant, hydrocortisone, triamcinolone, betamethasone, budesonide, saxagliptin, naldemedine, naltrexone

Further safety information, including warnings and contraindications, should be taken from the package insert. For the HLH indications specifically, the safety profile (including the known risk of encephalopathy, including Wernicke's) needs careful consideration in critically ill patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high TxGNN score (0.9984). No clinical trials or publications were found, and no mechanistic link between JAK2/FLT3 inhibition and the mTOR-driven biology of PEComa is established. Evidence level is L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to allow a proper mechanistic-link analysis
- Preclinical evidence (for example, cell-line or animal models) testing fedratinib in PEComa or TSC/mTOR-driven disease
- Consideration of the HLH indications as the more biologically plausible alternative, with a dedicated literature review
- Confirmation of approved indication text and dosage form for DIN 02502445
- Assessment of route compatibility, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

