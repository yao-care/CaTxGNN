---
layout: default
title: Hexaminolevulinate
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Hexaminolevulinate"
predicted_indications: ["bronchitis"]
description: "Hexaminolevulinate: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Hexaminolevulinate
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

## Hexaminolevulinate: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Hexaminolevulinate (HAL) is a photosensitizer precursor marketed in Canada as CYSVIEW. The TxGNN model predicts it may be useful for **bronchitis**, where it would act as a fluorescence imaging agent rather than a treatment. Currently **3 clinical trials** (1 completed, 1 terminated, 1 withdrawn) and **4 publications** (including 1 RCT) support this direction.

Note: the Canadian license data compiled for this report does not list an approved indication, so the bladder imaging use is taken from the general description of the product, not from the license text.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold (research question: supports diagnostic imaging, not therapy) |

Note: the top-ranked TxGNN prediction is bronchitis (0.9906), but it has no clinical trials or literature (L5) and no plausible biological rationale.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, HAL is a precursor of protoporphyrin IX (PpIX). Neoplastic tissue accumulates PpIX preferentially, and under blue light it emits red fluorescence. This is the same principle behind its marketed use in bladder cancer imaging.

Colonic epithelium is a different tissue, but the same mechanism may apply. Neoplastic and pre-malignant colonic lesions can accumulate PpIX, so fluorescence colonoscopy could help detect lesions that white light misses. Laboratory work also shows that HAL-based photodynamic therapy induces apoptosis in a human colon carcinoma cell line, which hints at a possible therapeutic role.

The supported use is **diagnostic imaging**, not treatment. Evidence for a therapeutic use is limited to in vitro work.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00285701](https://clinicaltrials.gov/study/NCT00285701) | Phase 1/2 | Completed | 38 | Dose-finding study of local and oral HAL for fluorescence endoscopy to detect pre-malignant and malignant colonic lesions |
| [NCT01344902](https://clinicaltrials.gov/study/NCT01344902) | Phase 1/2 | Terminated | 13 | Dose-finding study of oral HAL imaging in patients at risk of colonic neoplasia; stopped early, so limited data |
| [NCT03272659](https://clinicaltrials.gov/study/NCT03272659) | Phase 2 | Withdrawn | 0 | Pilot correlating colorectal cancer specimen pathology with HAL fluorescence; no patients enrolled |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20066590](https://pubmed.ncbi.nlm.nih.gov/20066590/) | 2010 | RCT | Endoscopy | Compared HAL fluorescence colonoscopy with white light endoscopy for detecting colorectal neoplastic lesions, and assessed safety |
| [18197583](https://pubmed.ncbi.nlm.nih.gov/18197583/) | 2008 | Prospective clinical study | Endoscopy | Feasibility and dose-finding of local HAL sensitization for fluorescence detection of precancerous colonic lesions |
| [15332045](https://pubmed.ncbi.nlm.nih.gov/15332045/) | 2004 | Pilot clinical study | Gastrointestinal Endoscopy | Feasibility, safety, dose finding and efficacy of HAL photodetection in rectal adenoma and cancer |
| [16566715](https://pubmed.ncbi.nlm.nih.gov/16566715/) | 2006 | In vitro study | J Environ Pathol Toxicol Oncol | HAL-mediated photodynamic therapy induced apoptosis in human colon carcinoma cells (320DM) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02436639 | CYSVIEW | Not listed | Not listed |

---

## Safety Considerations

- **Drug Interactions**: One interaction is recorded. **Valrubicin** is rated **Major** (DDInter).

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Review of the full RCT results (PMID 20066590) for detection rates versus white light endoscopy
- Confirmation of the approved indication and dosage form for CYSVIEW (DIN 02436639)
- Assessment of route compatibility: the colonic studies used oral or local (enema) administration, while the marketed product is used for bladder imaging
- Larger confirmatory studies with a defined diagnostic endpoint, and a safety review of the Valrubicin interaction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

