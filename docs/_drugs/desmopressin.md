---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 6
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
last_modified_at: 2026-10-27
description: "Desmopressin: predicted new indication congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Desmopressin: synthetic vasopressin analogue (V2 receptor agonist) → congenital prothrombin deficiency (congenital prothrombin deficiency)
{: .text-alpha }

## One-Sentence Summary

Desmopressin is a synthetic analogue of vasopressin that is marketed in Canada in several injectable, nasal and oral products.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **no clinical trials** and only **1 publication** (a 1993 general review of inherited bleeding disorders), so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on general pharmacology, desmopressin acts on the V2 receptor and triggers release of von Willebrand factor (vWF) and factor VIII from endothelial stores.

Prothrombin (factor II) is not part of this pathway. Desmopressin does not raise prothrombin levels, so there is no clear mechanistic rationale for this prediction. The single article linked to it is a 1993 general review of congenital bleeding disorders, not a study of prothrombin deficiency. The high score most likely reflects the closeness of coagulation disorders in the model's training data rather than a true therapeutic link. No study directly addresses this disease, so the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General overview of treatment options for inherited bleeding disorders such as haemophilia A and von Willebrand disease; does not study prothrombin deficiency or show a benefit of desmopressin for it |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02513579 | BIPAZEN | Not recorded | Not recorded |
| 00873993 | DDAVP INJ 4MCG/ML | Not recorded | Not recorded |
| 02284030 | APO-DESMOPRESSIN | Not recorded | Not recorded |
| 02024179 | OCTOSTIM LIQ INJ. 15MCG/ML | Not recorded | Not recorded |
| 02242465 | DESMOPRESSIN SPRAY | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Examples include:
  - Major: hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisolone, prednisone
  - Moderate: epinephrine, loperamide, morphine (including liposomal), opium, chlorpropamide
  - Minor: acetylsalicylic acid

Other safety details are not available here. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Desmopressin works through vWF and factor VIII release and has no known effect on prothrombin. There is no clinical trial and no study that directly addresses congenital prothrombin deficiency, so the score of 0.9970 is not backed by evidence.

**To proceed, the following is needed:**
- A mechanistic rationale showing how desmopressin could affect prothrombin levels or function
- Direct clinical or preclinical studies in congenital prothrombin deficiency
- Mechanism-of-action data and package insert warnings and contraindications from Health Canada
- A review of the interaction profile, especially with corticosteroids, before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

