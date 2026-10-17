---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "GUAIFENESIN"
predicted_indications: ["acute laryngopharyngitis", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
---

# Guaifenesin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Guaifenesin: From Allergic Rhinitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is an expectorant that thins and loosens airway mucus. It has been used for upper-airway conditions such as allergic rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**.
Evidence is very limited: **no registered clinical trials** and **1 publication** (a 2002 review), so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text in the Canadian licence records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction with no clinical studies; only one indirect review) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this report. Based on known information, guaifenesin is an expectorant that thins and loosens airway mucus. Its use in rhinitis and nasopharyngitis has been established, and mechanistically it may help with mucus-related nasal symptoms.

Nasal cavity disease is a broad category that includes the rhinitis conditions already listed as original indications. The very high TxGNN score (99.98%) probably reflects this overlap and is not an independent repurposing signal. In other words, the prediction is largely a restatement of existing uses rather than a new therapeutic discovery.

The only supporting publication is a 2002 article on respiratory allergies in voice users. It mentions that decongestants containing guaifenesin may be useful, which is indirect support only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Treatment strategies for hidden respiratory allergies in voice users. Antihistamines are generally avoided, while decongestants containing guaifenesin may be useful. Steroids are helpful in perennial allergic symptoms. |

## Canada Market Information

All 20 licences are valid single-ingredient products. The data compiled for this report does not include dosage forms or approved indication text. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02121999 | Bronchophan Expectorant (Sans Sucrose) | Not available | Not available |
| 02434725 | Mucinex Chest Congestion | Not available | Not available |
| 02534762 | Mucus & Phlegm Relief Extra Strength | Not available | Not available |
| 02142783 | Robitussin Extra Strength Mucus and Phlegm | Not available | Not available |
| 00609951 | Balminil Expectorant (Sucrose Free) | Not available | Not available |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for safety information.

The knowledge graph links guaifenesin to a list of contraindicated conditions. This is graph-derived and not label text, so it should be verified against the official label. The conditions include:
- Cardiovascular: hypertension
- Hepatic and gastrointestinal: liver failure, liver disease, cirrhosis, gastric ulcer, peptic ulcer disease, pancreatitis, gallbladder disease, inflammatory bowel disease
- Respiratory: chronic obstructive pulmonary disease
- Neuropsychiatric: epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder
- Metabolic and endocrine: porphyria, hypothyroidism, myxedema, adrenocortical insufficiency (Addison disease)
- Renal and haematological: kidney disease, thrombocytopenia

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication largely overlaps with guaifenesin's existing rhinitis-related uses. There are no clinical trials, and the single publication is an indirect, low-tier review. The package insert safety review is also incomplete, so the candidate cannot move beyond the research-question stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clarification of which specific nasal cavity conditions are meant, beyond those already covered by existing indications
- Controlled clinical evidence, or a targeted literature search, for the predicted indication
- Dosage form, route and approved indication details for the Canadian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

