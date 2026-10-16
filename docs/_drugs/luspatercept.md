---
layout: default
title: Luspatercept
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Luspatercept: predicted new indication Monosomy X (evidence level L5). Approved use: Beta-thalassemia and related hemoglobin disorders"
monitor_inn: "Luspatercept"
predicted_indications: ["monosomy X", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "pyruvate kinase deficiency of red cells", "thalassemia, beta+, silent allele", "familial apolipoprotein C-II deficiency", "adenosine deaminase deficiency", "Hb Bart's hydrops fetalis"]
---

# Luspatercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Luspatercept: From Beta-Thalassemia to Monosomy X

## One-Sentence Summary

Luspatercept was originally used to treat beta-thalassemia and related hemoglobin disorders.
The TxGNN model predicts it may be effective for **monosomy X** (Turner syndrome), but **no clinical trials and no publications** currently support this direction. The prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Beta-thalassemia and related hemoglobin disorders (the Health Canada licence records contain no indication text) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 96.00% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge of the drug, luspatercept is an activin receptor ligand trap (a modified ActRIIB-Fc fusion protein). It modulates TGF-beta superfamily signaling to promote late-stage red blood cell maturation, which is why it is used in beta-thalassemia.

For monosomy X, no mechanistic connection is evident. Monosomy X (Turner syndrome) is a chromosomal condition whose main features are gonadal dysgenesis and growth and cardiac abnormalities. These are not problems of red cell maturation. The high TxGNN score is therefore best read as a computational signal, not as biological support.

### Other predictions in the top 10

None of the other nine predicted indications has any clinical trial or literature support either. They fall into three groups:

- **Biologically more credible (flagged as research questions):**
  - **Pyruvate kinase deficiency of red cells** (score 93.8%): a hereditary hemolytic anemia with ineffective erythropoiesis, overlapping biologically with beta-thalassemia. This is the most plausible candidate in the list.
  - **Thalassemia, beta+, silent allele** (93.3%): closely related to the existing indication, but silent carriers are usually asymptomatic and need no treatment, and the existing beta-thalassemia label largely covers it.
- **Indirect or unsupported links:**
  - **Hb Bart's hydrops fetalis** (92.8%): the most severe form of alpha-thalassemia, usually presenting in utero. Its thalassemia-class relationship gives some biological relevance, but use in a fetal or neonatal setting is unsupported.
  - **Hepatic veno-occlusive disease** (94.9%): the only plausible link is the shared hematologic transplant setting, which is indirect.
  - **Peliosis hepatis** (94.8%): likely reflects network proximity to hematologic disorders only.
- **No plausible mechanistic link:** hepatic infarction (95.7%), syndrome with combined immunodeficiency (94.3%), familial apolipoprotein C-II deficiency (93.1%) and adenosine deaminase deficiency (92.9%). For hepatic infarction, a thromboembolic risk is noted for luspatercept, which suggests a possible safety concern in this vascular setting.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02505568 | REBLOZYL | Not listed | Not listed |
| 02505541 | REBLOZYL | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

One point from the compiled data is worth noting: a thromboembolic risk has been noted for luspatercept, which is relevant to any vascular indication such as hepatic infarction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The monosomy X prediction has a high model score but no trials, no publications, and no plausible mechanistic link. Evidence is at the lowest level (L5, model prediction only), so there is no basis to advance this indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any clinical or preclinical evidence linking luspatercept to monosomy X
- If the program wants a more promising direction, a focused evidence review of pyruvate kinase deficiency, the most biologically credible candidate in the list, using external sources not included in the data compiled for this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

