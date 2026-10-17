---
layout: default
title: Sodium Zirconium Cyclosilicate
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sodium Zirconium Cyclosilicate: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not available in the Health Canada licence data (the drug is a potass…"
monitor_inn: "Sodium zirconium cyclosilicate"
predicted_indications: ["breast fibrocystic disease", "benign mammary dysplasia", "blunt duct adenosis of breast", "apocrine adenosis of breast", "fat necrosis of breast", "breast abscess", "lactation disease", "breast adenosis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2"]
---

# Sodium Zirconium Cyclosilicate
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

# Sodium Zirconium Cyclosilicate: From Hyperkalaemia Treatment to Breast Fibrocystic Disease

## One-Sentence Summary

Sodium zirconium cyclosilicate is a non-absorbed potassium-binding agent that acts in the gastrointestinal tract. The data compiled for this report do not include an approved indication text from Health Canada.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Health Canada licence data (the drug is a potassium binder) |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 93.41% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, sodium zirconium cyclosilicate is a non-absorbed, selective inorganic cation exchanger. It traps potassium (and, to a lesser extent, ammonium) in the gut and has no known effect on breast tissue, hormonal signalling or fibrocystic pathology.

The relationship between the original use (potassium control) and the predicted indication is weak. The high TxGNN score appears to be a graph-based result, likely driven by a cluster of related benign breast-disease terms in the knowledge graph. The other top predictions, such as benign mammary dysplasia, blunt duct adenosis, apocrine adenosis, breast adenosis, fat necrosis of breast and breast abscess, share this pattern. Several of them have identical or near-identical scores, which points to an ontology-driven artefact rather than drug-specific biology.

The remaining top-10 predictions (lactation disease, heparin cofactor 2 deficiency and antithrombin deficiency type 2) also have no identified mechanistic link and no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02490722 | LOKELMA | Not specified | Not specified |
| 02490714 | LOKELMA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 16 interactions were found, all rated Moderate. They involve:
  - HIV antiretrovirals: atazanavir, rilpivirine, ritonavir, saquinavir, nelfinavir, indinavir, raltegravir
  - Azole antifungals: itraconazole, posaconazole, ketoconazole
  - Kinase inhibitors: dasatinib, nilotinib, erlotinib
  - Others: atorvastatin, ledipasvir, furosemide

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no clinical trials or publications, and the pharmacology of a non-absorbed gut potassium binder gives no biological reason to expect benefit in breast fibrocystic disease or any other top-ranked prediction.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, supported by preclinical or mechanism studies
- Detailed mechanism of action data
- Health Canada approved indication text and package insert warnings and contraindications
- Evidence from at least observational or preclinical studies in the predicted indication
- Assessment of route compatibility and the safety profile in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

