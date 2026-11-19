---
layout: default
title: Cetuximab
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
monitor_inn: "Cetuximab"
predicted_indications: ["bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "chondroid hamartoma", "non-seminomatous lesion", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "epiglottis neoplasm", "cystic neoplasm", "pre-malignant neoplasm"]
last_modified_at: 2026-11-20
description: "Cetuximab: predicted new indication bronchial adenomas/carcinoids childhood (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Cetuximab
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

## Cetuximab: EGFR-targeting monoclonal antibody → bronchial adenomas/carcinoids childhood
{: .text-alpha }

## One-Sentence Summary

Cetuximab is an anti-EGFR monoclonal antibody that is marketed in Canada.
The TxGNN model predicts it may be relevant for **bronchial adenomas/carcinoids childhood**, with a score of 0.9995.
No clinical trials or publications were retrieved for this prediction, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | bronchial adenomas/carcinoids childhood |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cetuximab blocks the epidermal growth factor receptor (EGFR) and prevents ligand binding, which interrupts tumour-promoting downstream signalling. According to the Mechanism of Action section of the US FDA-approved prescribing information for cetuximab: "The epidermal growth factor receptor (EGFR, HER1, c-ErbB-1) is a transmembrane glycoprotein that is a member of a subfamily of type I receptor tyrosine kinases including EGFR, HER2, HER3, and HER4. The EGFR is constitutively expressed in many normal epithelial tissues, including the skin and hair follicle. […] Cetuximab binds specifically to the EGFR on both normal and tumor cells, and competitively inhibits the binding of epidermal growth factor (EGF) and other ligands, such as transforming growth factor-alpha." ([DailyMed: Erbitux (cetuximab) prescribing information, ImClone LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8bc6397e-4bd8-4d37-a007-a327e4da34d9), label version 2026-04-16; accessed 2026-11-19.) The target (EGFR) is documented.

The link to this prediction is weak. Paediatric bronchial carcinoids are neuroendocrine tumours that are usually not driven by EGFR, and no EGFR dependence has been established for them. The high model score therefore should be read as a computational signal only, not as a mechanistic or clinical finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02271249 | ERBITUX | Not recorded | Not recorded in the local data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 20 interaction records were found. Two are rated Major: aminolevulinic acid and thalidomide. Most of the others are rated Moderate, including proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), fluorouracil, capecitabine, and the platinum agents cisplatin, carboplatin and oxaliplatin. Other Moderate entries are methoxsalen, idelalisib, omacetaxine mepesuccinate, verteporfin, and topical aminolevulinic acid and methyl aminolevulinate.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and EGFR blockade has no established rationale in paediatric bronchial carcinoids. It remains a model prediction only (Evidence Level L5).

**To proceed, the following is needed:**
- Evidence that EGFR is expressed or drives tumour growth in paediatric bronchial carcinoids
- Preclinical or clinical studies that directly address this disease
- Package insert warnings and contraindications from Health Canada, and detailed mechanism-of-action data
- A safety assessment for the paediatric population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action text is not available in the data compiled for this report, but t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Erbitux (cetuximab) prescribing information, ImClone LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8bc6397e-4bd8-4d37-a007-a327e4da34d9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

