---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bevacizumab: predicted new indication Epiglottis neoplasm (evidence level L5). Approved use: Peritoneal and ovarian cancers, breast cancer…"
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

# Bevacizumab: From Peritoneal and Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF antibody originally used for cancers such as primary peritoneal carcinoma, ovarian cancer, breast cancer, metastatic colon cancer and glioblastoma.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but **no clinical trials or publications** were retrieved for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritoneal and ovarian cancers, breast cancer, metastatic colon cancer, glioblastoma (the Canadian licence records contain no indication text, so this comes from the knowledge graph indication list) |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bevacizumab is a monoclonal antibody that neutralizes VEGF-A and inhibits tumour angiogenesis. This is the general basis for its use in several solid tumours.

Epiglottis neoplasm is a head and neck tumour. Anti-angiogenic therapy is plausibly relevant to such tumours, and the TxGNN score is high. However, no trials or publications specific to this indication were retrieved, so the link is a biological hypothesis and has not been tested for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

## Canada Market Information

Thirteen valid single-ingredient licences were found. Dosage form and indication text were not available in the data compiled for this report.

| DIN | Product Name | Status |
|---------|------|------|
| 02270994 | AVASTIN | Valid |
| 02470748 | MVASI | Valid |
| 02470756 | MVASI | Valid |
| 02489430 | ZIRABEV | Valid |
| 02489449 | ZIRABEV | Valid |

Other valid licences are for BAMBEVI (02520729, 02520737), AYBINTIO (02522829, 02522837), VEGZELMA (02534177, 02534185) and ABEVMY (02522160, 02522179).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically blood pressure, urinary protein, and signs of bleeding or wound-healing problems |
| Handling Protection | Please refer to the package insert and local institutional handling policy |

## Safety Considerations

**Drug Interactions:** 22 interactions were recorded (DDInter). The Major-level interactions are:
- Deferiprone
- Samarium (153Sm) lexidronam
- Panitumumab
- Sunitinib
- Thalidomide

The remaining interactions are Moderate, mainly with bisphosphonates (alendronic, risedronic, etidronic, pamidronic, tiludronic acid, ibandronate), haematopoietic growth factors (filgrastim, pegfilgrastim, sargramostim, palifermin) and radiopharmaceuticals (strontium-89, radium-223, phosphorus-32 sodium phosphate), plus idelalisib and romosozumab.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.90%), but no clinical trials or literature support epiglottis neoplasm. The evidence is at L5 (model prediction only), and package insert safety data have not yet been compiled.

**To proceed, the following is needed:**
- Literature and trial searches specific to epiglottis and laryngeal tumours, including histology (benign vs. malignant)
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications, to allow safety screening
- A review of the Major drug interactions (sunitinib, panitumumab, thalidomide, deferiprone, samarium-153) against likely co-medications in head and neck oncology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

