---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 6
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Atezolizumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Atezolizumab
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

## Atezolizumab: From Transitional Cell Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Atezolizumab is an antibody drug whose relation to transitional cell carcinoma is recorded in the knowledge graph. The TxGNN model's top-ranked prediction is **uterine ligament adenocarcinoma**, and no clinical trials or publications support this specific disease. The best-supported nearby direction is **endocervical carcinoma**, with **2 clinical trials** and **1 publication** (a review of a related cervical subtype).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (a relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Number of approvals | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Atezolizumab is generally known as an anti-PD-L1 antibody (this comes from general knowledge, not from the compiled data). Blocking PD-L1 can release the immune system's attack on tumours that express it.

A possible link is PD-L1 expression in such tumors, but nothing in the compiled data supports this for uterine ligament adenocarcinoma, a gynecologic adenocarcinoma. The very high score of 0.9993 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is a computational prediction only.

Among the other predicted diseases, endocervical carcinoma has the most supporting material. Cervical carcinomas are often HPV-driven and may express PD-L1. Combining atezolizumab with bevacizumab (anti-VEGF) or with chemoradiotherapy offers additional mechanistic rationale. These are rationales only, and neither trial's efficacy results are in the compiled data.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked disease, uterine ligament adenocarcinoma. Trials for the second-ranked prediction, endocervical carcinoma, are shown below for context. They study cervical cancer, not the top-ranked disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02921269](https://clinicaltrials.gov/study/NCT02921269) | Phase 2 | Completed | 11 | Atezolizumab plus bevacizumab in recurrent, persistent or metastatic cervical cancer. Very small; no efficacy outcome available. |
| [NCT03738228](https://clinicaltrials.gov/study/NCT03738228) | Phase 1 | Completed | 40 | Atezolizumab as an immune primer and with extended-field chemoradiotherapy in node-positive locally advanced cervical cancer. Early-phase feasibility study; no efficacy data available. |

---

## Literature Evidence

No literature is available for uterine ligament adenocarcinoma. One publication was found for the related cervical prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Small cell neuroendocrine carcinoma of the cervix: molecular basis and therapeutic advances. Evidence is limited to case series and case reports. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02462990 | TECENTRIQ | Not stated | Not stated |
| 02492393 | TECENTRIQ | Not stated | Not stated |
| 02546310 | TECENTRIQ SC | Not stated | Not stated |

All three are single-ingredient products with valid status.

---

## Safety Considerations

- **Drug Interactions**: 75 interactions are recorded. Examples include:
  - **Major**: adalimumab, baricitinib, and live BCG vaccine (Tice strain).
  - **Moderate**: corticosteroids such as hydrocortisone, prednisone, dexamethasone, and methylprednisolone. Others include azathioprine, anakinra, alemtuzumab, and several vaccines.

  Immunosuppressive drugs and live vaccines are the main concern, because they may work against or complicate immune-activating therapy.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, uterine ligament adenocarcinoma, rests on a model score alone, with no trials or publications. The evidence level is therefore L5. The nearby cervical cancer trials are small, early-phase, and have no reported efficacy, and they do not study this disease.

**To proceed, the following is needed:**
- Retrieve the Health Canada package insert, including warnings, contraindications, and approved indications. This is a blocking gap for safety screening.
- Obtain mechanism of action data from DrugBank.
- Search for studies on PD-L1 expression and checkpoint blockade in uterine ligament adenocarcinoma.
- Obtain efficacy results from the cervical cancer trials (NCT02921269, NCT03738228) and consider whether endocervical carcinoma is a better-supported candidate to assess first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

