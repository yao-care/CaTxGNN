---
layout: default
title: Guaiacol
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 1
monitor_inn: "GUAIACOL"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-28
description: "Guaiacol: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis, common cold, rhinitis, nasopharyngitis"
---

# Guaiacol
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

## Guaiacol: From Pharyngitis and Common Cold to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

The TxGNN model predicts it may be useful for **nasal cavity disease**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, rhinitis, nasopharyngitis (relations recorded in the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Number of approvals | 2 DINs |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, guaiacol is a single-ingredient compound. Mechanistically it may be applicable to nasal cavity disease, but this cannot be confirmed from the data compiled for this report.

Guaiacol is traditionally described as an expectorant with mild antiseptic and local anesthetic properties, which could in principle relate to nasal conditions. The Canadian license records here carry no indication text. This reasoning is speculative and has no supporting study in the data compiled.

The TxGNN score is very high (0.9951), but it is a computational prediction only.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00319724 | DEMO-CINEOL ENFANTS/CHILDREN | Not specified | Not specified |
| 00319716 | DEMO-CINEOL ADULTES/ADULTS | Not specified | Not specified |

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): the knowledge graph records contraindication relations with many conditions, including:
  - Cardiovascular: hypertension, hypotensive disorder, coronary artery disease, myocardial infarction, coronary thrombosis
  - Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism, myxedema, congenital hypothyroidism, adrenocortical insufficiency, Addison disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
  - Renal and urinary: kidney disease, anuria, pyoureter, benign prostatic hyperplasia
  - Hepatic, biliary and gastrointestinal: liver disease, gallbladder disease, pancreatitis, peptic ulcer disease, inflammatory bowel disease
  - Other: epilepsy, rhabdomyolysis, nodular fasciitis, hemoglobinopathy

Please refer to the package insert for label warnings, contraindications and drug interaction information. No interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial or publication directly studies guaiacol in nasal cavity disease, so the evidence level is L5. Mechanism data and label safety information are also missing.

**To proceed, the following is needed:**
- Mechanism of action data for guaiacol (e.g., from DrugBank)
- Health Canada package insert warnings, contraindications and approved indication text for both DINs
- A literature and trial search for guaiacol in nasal cavity disease
- Confirmation of route and formulation compatibility with the predicted indication
- A safety review of the knowledge-graph contraindication relations before any further screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

