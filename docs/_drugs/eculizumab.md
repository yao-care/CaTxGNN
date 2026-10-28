---
layout: default
title: Eculizumab
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Eculizumab: predicted new indication Cyclic hematopoiesis (evidence level L5). Approved use: Paroxysmal nocturnal hemoglobinuria"
monitor_inn: "Eculizumab"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
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

## Eculizumab: From Paroxysmal Nocturnal Hemoglobinuria to Cyclic Hematopoiesis
{: .text-alpha }

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria and neuromyelitis optica.
The TxGNN model predicts it may be effective for **cyclic hematopoiesis** (cyclic neutropenia), but there are **0 clinical trials** and **0 publications** that directly support this prediction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria; neuromyelitis optica (the Canadian licence text is not available) |
| Predicted New Indication | Cyclic hematopoiesis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, eculizumab is a monoclonal antibody that blocks complement C5. It has proven efficacy in complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria, and it is also used in conditions such as atypical hemolytic uremic syndrome and myasthenia gravis.

For cyclic hematopoiesis, however, no supporting mechanistic link has been identified. Cyclic neutropenia is typically caused by *ELANE* mutations, which make neutrophil production oscillate. It is not primarily a complement-mediated disease, so there is no clear rationale for C5 inhibition. The high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are also neutropenia or neutrophil-related disorders: severe congenital neutropenia and its genetic subtypes, adult idiopathic neutropenia, and primary immunodeficiency due to p14 deficiency. None of them has a complement-driven mechanism or any supporting trial or literature. Eculizumab also carries a risk of serious meningococcal infection, which is a particular concern in neutropenic or immunodeficient patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications address cyclic hematopoiesis. The literature retrieved for the fourth-ranked prediction (congenital neutropenia-myelofibrosis-nephromegaly syndrome) and the tenth-ranked prediction (primary release disorder of platelets) concerns eculizumab's existing indications and does not support the predicted indication. Examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25237200](https://pubmed.ncbi.nlm.nih.gov/25237200/) | 2014 | Review | Blood | Reviews PNH, in which loss of CD55/CD59 causes uncontrolled complement activation and hemolysis |
| [28622911](https://pubmed.ncbi.nlm.nih.gov/28622911/) | 2017 | Review | Molecular immunology | Neurological features of congenital CD59 mutations and the role of eculizumab |
| [19556379](https://pubmed.ncbi.nlm.nih.gov/19556379/) | 2009 | Clinical report | Clin J Am Soc Nephrol | Eculizumab inhibits terminal complement in atypical hemolytic uremic syndrome |
| [23271156](https://pubmed.ncbi.nlm.nih.gov/23271156/) | 2012 | Review | Clin Adv Hematol Oncol | Case-based roundtable on PNH; reflects the existing indication |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02322285 | SOLIRIS | Not stated | Not stated |

## Safety Considerations

- **Drug Interactions**: Four minor interactions were identified, all with human immunoglobulin G products (intravenous, subcutaneous, intramuscular, and combined intravenous and subcutaneous).

Please refer to the package insert for warnings and contraindications. Eculizumab is generally known to carry a risk of serious meningococcal infection, which should be checked against the Canadian label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score (0.9997), with no clinical trials or directly relevant publications, and no plausible complement-mediated mechanism in cyclic hematopoiesis. Infection risk with C5 inhibition is a further concern in neutropenic patients.

**To proceed, the following is needed:**
- Evidence that complement activation contributes to the pathology of cyclic neutropenia
- Mechanism of action data for the drug
- Warnings and contraindications from the Health Canada package insert
- Approved indication text and dosage form for the Canadian licence
- Preclinical or case-level data, if any exist, before considering clinical studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

