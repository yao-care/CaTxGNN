---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-11-20
description: "Bevacizumab: predicted new indication epiglottis neoplasm (evidence level L5). In Canada: 13 DINs (13 marketed)"
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

## Bevacizumab: anti-VEGF-A monoclonal antibody → epiglottis neoplasm
{: .text-alpha }

## One-Sentence Summary

Bevacizumab is a monoclonal antibody that neutralizes VEGF-A and inhibits tumour angiogenesis.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, with a prediction score of **0.9990**.
No clinical trials or publications were retrieved for this specific disease, so the prediction currently rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | epiglottis neoplasm |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 13 of 13) |
| Number of DINs | 13 (marketed: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bevacizumab binds and neutralizes VEGF-A, which reduces the formation of new blood vessels that tumours need to grow. According to the Mechanism of Action section of the US FDA-approved prescribing information for bevacizumab: "Bevacizumab products bind VEGF and prevent the interaction of VEGF to its receptors (Flt-1 and KDR) on the surface of endothelial cells. The interaction of VEGF with its receptors leads to endothelial cell proliferation and new blood vessel formation in in vitro models of angiogenesis." ([DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe), label version 2026-08-21; accessed 2026-11-19.) This description reflects the general, well-known action of the drug.

Neoplasms of the head and neck region, including the epiglottis, depend on angiogenesis like many other solid tumours. This offers a plausible, but generic, mechanistic rationale for the prediction. No study retrieved for this report examines bevacizumab in epiglottis neoplasm, so the link has not been tested in the data available here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02520737 | BAMBEVI | Not recorded | Not recorded |
| 02522829 | AYBINTIO | Not recorded | Not recorded |
| 02489430 | ZIRABEV | Not recorded | Not recorded |
| 02534185 | VEGZELMA | Not recorded | Not recorded |
| 02270994 | AVASTIN | Not recorded | Not recorded |

All 13 licences in the local data are valid single-ingredient authorizations, and the list above shows five of them.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure, urine protein, signs of bleeding, gastrointestinal perforation and wound-healing problems; please also refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded. Major-level interactions include deferiprone, samarium (153Sm) lexidronam, panitumumab, sunitinib and thalidomide. Moderate-level interactions include bisphosphonates (alendronic acid, risedronic acid, etidronic acid, ibandronate, pamidronic acid, tiludronic acid), filgrastim, pegfilgrastim, sargramostim, palifermin, idelalisib, romosozumab, strontium chloride Sr-89, radium Ra 223 dichloride and monobasic sodium phosphate (P32).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trials or publications directly address epiglottis neoplasm, so the evidence level is L5 and the mechanistic rationale is only generic.

**To proceed, the following is needed:**
- Searches for direct clinical or preclinical studies of bevacizumab in epiglottis and laryngeal neoplasms
- Mechanism-of-action data and package insert warnings and contraindications from Health Canada
- A safety review of the major drug interactions, particularly with other anti-angiogenic and targeted agents

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

