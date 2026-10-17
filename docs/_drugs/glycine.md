---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Glycine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "GLYCINE"
predicted_indications: ["acute laryngopharyngitis"]
---

# Glycine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Glycine: From Allergic Rhinitis and Upper Respiratory Conditions to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid that is listed in the knowledge graph for upper airway conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this is a model prediction only: **1 clinical trial** was retrieved (not relevant to the hypothesis) and **2 publications** were retrieved (basic research only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (from the knowledge graph; no approved indication text in the Canadian licence records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycine is an amino acid whose original indications in the knowledge graph (allergic rhinitis, vasomotor rhinitis, rhinitis, nasopharyngitis) are nasal and upper airway conditions. Mechanistically it may be applicable to nasal cavity disease, but this cannot be confirmed from the data compiled for this report.

The predicted indication sits in the same anatomical region as the original indications. This is a weak, indirect overlap and not evidence of efficacy. Glycine has inhibitory neurotransmitter and cytoprotective roles in other tissues, but nothing in the compiled data links these roles to nasal mucosal disease.

A second prediction, **acute laryngopharyngitis** (score 99.84%), is closely related to the existing pharyngitis, nasopharyngitis and common cold indications. It has no clinical trials and no literature, so the support is purely computational.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET imaging of αvβ3 integrin expression (18F-FPPRGD2) as an angiogenesis biomarker in glioblastoma, gynaecological cancers and renal cell carcinoma. It is a diagnostic imaging study and does not test glycine as a treatment, so it is not relevant to this hypothesis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic research (animal tissue histochemistry) | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. It is not a study of glycine in patients. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Basic research (drug delivery/biomaterials) | Chemical & Pharmaceutical Bulletin | Oligoarginine-linked polymers as a mucosal adjuvant for nasal vaccination in mice. It is not directly related to glycine therapy. |

## Canada Market Information

Health Canada lists 20 valid single-ingredient authorizations. Dosage form and approved indication text are not recorded for them. The main products are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00498793 | Glycine Irrigation USP | Not recorded | Not recorded |
| 00799955 | Glycine 1.5% Irrigation USP Sol | Not recorded | Not recorded |
| 02443651 | pH 12 Sterile Diluent for Flolan | Not recorded | Not recorded |
| 02046709 | Clinimix | Not recorded | Not recorded |
| 00872296 | Travasol | Not recorded | Not recorded |

The remaining authorizations include further Clinimix and Clinimix E strengths, 20% Prosol, Primene 10%, Olimel 7.6% and Essepna. Most are parenteral nutrition or irrigation products, not nasal or respiratory products.

## Safety Considerations

Safety data from the package insert were not available for this report, so please refer to the package insert for warnings and contraindications.

The knowledge graph records contraindication links between glycine and the diseases below. These come from graph relationships, not from label text, and should be verified against the product labelling.

- **Kidney and urinary conditions**: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- **Calcium and phosphate disorders**: hypercalcaemia, humoral hypercalcaemia of malignancy, hyperparathyroidism, osteitis fibrosa, hyperphosphataemia, phosphorus metabolism disease, hypervitaminosis, sarcoidosis, lytic metastatic bone lesion
- **Cardiovascular conditions**: heart disease, cardiovascular disease, arteriosclerosis obliterans, digitalis poisoning, ventricular fibrillation
- **Metabolic and other conditions**: phenylketonuria, disorder of phenylalanine metabolism, constipation disorder

A drug interaction search returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.85%) is a model prediction only. The only trial found is an unrelated imaging study, the two publications are basic research, and there is no mechanism of action data to explain a link to nasal cavity disease. Evidence is at level L5.

**To proceed, the following is needed:**
- Mechanism of action data for glycine, and an assessment of whether it applies to nasal mucosa
- Package insert warnings and contraindications from Health Canada, which are needed before safety screening
- Clinical or preclinical studies of glycine in nasal cavity disease or upper airway inflammation
- Confirmation of whether an intranasal or other suitable route and formulation exist, since the current Canadian products are mainly irrigation and parenteral nutrition products
- Review of the predicted contraindications, especially for kidney, calcium and phosphate disorders, before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

