---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 8
monitor_inn: "FOSFOMYCIN"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-28
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic that inhibits bacterial cell wall synthesis, and a relation to urinary tract infection is recorded in the knowledge graph.
The TxGNN model predicts it may be effective for **uterine inflammatory disease**,
but only **2 clinical trials** (both general pediatric pharmacokinetic studies) and **1 publication** (on cystitis in endometriosis patients) were retrieved, and none directly studies this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fosfomycin inhibits the bacterial enzyme MurA, an early step in cell wall synthesis, and has broad Gram-negative and Gram-positive activity. This could plausibly cover pathogens found in pelvic or uterine infections.

Uterine inflammatory disease is bacterial in many cases. The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. However, no study retrieved tests fosfomycin in uterine or pelvic infection, so the link is a hypothesis only.

The two trials are general pediatric pharmacokinetic studies of understudied drugs. The single publication concerns cystitis, a urinary condition, in women with endometriosis treated with dienogest. None of these evaluates uterine inflammatory disease, so the evidence level is L5.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pharmacokinetics of understudied drugs given to children as standard of care; not specific to uterine disease and no efficacy testing |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Umbrella PK/PD and safety study of understudied drugs in children; not specific to fosfomycin or uterine disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | J Obstet Gynaecol | Dienogest-related cystitis in women with endometriosis after laparoscopic surgery; a urinary outcome, not uterine infection |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02488086 | IVOZFO | Not listed | Not listed |
| 02473801 | JAMP-FOSFOMYCIN | Not listed | Not listed |
| 02240335 | MONUROL | Not listed | Not listed |

All three are valid single-ingredient licences.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: contraindication relations are recorded for kidney disease, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug Interactions** (3 found):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the package insert for warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no retrieved trial or publication studies fosfomycin in uterine inflammatory disease. The existing evidence is indirect and unrelated to efficacy in this condition, so this remains a model prediction only.

**To proceed, the following is needed:**
- Studies or case data on fosfomycin in uterine or pelvic infection, including tissue penetration
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- Confirmation of formulations and routes, since the dosage forms are not listed in the licence records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

