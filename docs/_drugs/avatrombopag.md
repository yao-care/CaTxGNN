---
layout: default
title: Avatrombopag
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Avatrombopag: predicted new indication Macrothrombocytopenia with mitral valve insufficiency (evidence level L5). Approved use: Thrombocytopenia"
monitor_inn: "Avatrombopag"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "dense granule disease", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "lower motor neuron syndrome with late-adult onset", "amyotrophic lateral sclerosis, susceptibility to", "Mills syndrome", "monomelic amyotrophy"]
---

# Avatrombopag
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

# Avatrombopag: From Thrombocytopenia to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is an oral thrombopoietin receptor agonist, originally used to treat thrombocytopenia.
The TxGNN model predicts it may be effective for **macrothrombocytopenia with mitral valve insufficiency**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia |
| Predicted New Indication | Macrothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, avatrombopag is a thrombopoietin receptor (TPO-R/c-Mpl) agonist. It stimulates megakaryocyte proliferation and platelet production, and its efficacy in thrombocytopenia is the basis of its original use.

A hereditary macrothrombocytopenia with low platelet counts could plausibly respond if the defect lies in platelet production rather than in platelet destruction or a structural defect of megakaryocytes. The mitral valve component of the condition would not be expected to respond to this drug. The underlying genetic cause is not specified, so the mechanistic link is speculative.

Other high-scoring predictions include hereditary thrombocytopenia with normal platelets, transient neonatal thrombocytopenia and dense granule disease. They are also hematological, but the links are weaker or unclear:
- **Hereditary thrombocytopenia with normal platelets:** the disease name is ambiguous, so the target population is unclear.
- **Transient neonatal thrombocytopenia:** the condition resolves spontaneously, so the benefit of a drug is doubtful. There are also no neonatal safety or dosing data.
- **Dense granule disease:** this is mainly a platelet function defect, not a low count, so raising platelet numbers does not address it. Thrombotic risk is also a concern.

Several further predictions are neurological: amyotrophic lateral sclerosis (ALS) and related motor neuron disorders, and a cortical malformation. No plausible mechanism links TPO-R agonism to these. The high scores likely reflect knowledge-graph proximity rather than biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02542706 | DOPTELET | Not specified | Not specified |

## Safety Considerations

**Drug Interactions:** 52 interactions were identified. The first 20 of them, all from the DDInter database, are summarized below.

- **Major:** fosphenytoin, carbamazepine, carfilzomib, dabrafenib, enzalutamide, fluconazole, imatinib
- **Moderate:** clarithromycin, nitisinone, cobicistat, fosamprenavir, gemfibrozil, fenofibrate, apalutamide, atazanavir, amprenavir, boceprevir, ceritinib, delavirdine, idelalisib

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has an extremely high model score, but there are no clinical trials or publications behind it. The evidence level is L5. The mechanistic link is speculative for macrothrombocytopenia and absent for the neurological predictions. Safety information from the Canadian package insert has also not yet been reviewed.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the Health Canada package insert for DOPTELET
- Mechanism of action data from DrugBank
- Clarification of the genetic cause and the platelet defect in the target macrothrombocytopenia population
- A literature search for avatrombopag, or other TPO-R agonists, in inherited thrombocytopenias
- Neonatal safety and dosing data, if transient neonatal thrombocytopenia is considered
- Approved indication and dosage form details for the Canadian product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

