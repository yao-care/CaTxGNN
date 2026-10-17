---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Atezolizumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
monitor_inn: "Atezolizumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
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

# Atezolizumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is a PD-L1 inhibitor originally used to treat transitional cell carcinoma (urothelial carcinoma).
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but the only linked evidence is **1 early-phase clinical trial** and **no publications**, so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (as assigned in the compiled data; the single linked trial is Phase 1b) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, atezolizumab is a PD-L1 inhibitor, its efficacy in urothelial carcinoma is established, and mechanistically it may be applicable to related urothelial cancers.

Prostatic urethra urothelial carcinoma is a histologically related urothelial malignancy, so a shared PD-L1 axis is biologically plausible. However, the only linked trial is a multi-cohort basket study of cabozantinib plus atezolizumab. No cohort specific to the prostatic urethra can be confirmed from the data provided.

Other high-scoring predictions are also urothelial subtypes (upper tract, sarcomatoid variants). Cervical carcinoma is the one non-urothelial area with registered atezolizumab trials, and it is summarised under Other Predictions below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | Active, not recruiting | 914 | Dose-escalation and expansion of cabozantinib alone or with atezolizumab in advanced solid tumours, including urothelial carcinoma (bladder, renal pelvis, ureter, urethra). No results provided; the combination partner confounds attribution to atezolizumab. |

## Literature Evidence

Currently no related literature available.

## Other Predictions Worth Noting

| Predicted Indication | Score | Evidence | Notes |
|------|------|------|------|
| Endocervical carcinoma | 99.92% | L2 (as assigned in the compiled data) | Two completed trials: [NCT02921269](https://clinicaltrials.gov/study/NCT02921269) (Phase 2, n=11, atezolizumab + bevacizumab in recurrent cervical cancer) and [NCT03738228](https://clinicaltrials.gov/study/NCT03738228) (Phase 1, n=40, atezolizumab with chemoradiotherapy). No efficacy outcomes provided. One review on cervical neuroendocrine carcinoma ([PMID 37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/), 2023) is also linked. |
| Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L5 | Model prediction only |
| Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.98% | L5 | Model prediction only |
| Renal pelvis papillary urothelial carcinoma | 99.98% | L5 | Model prediction only |

The remaining predictions (uterine ligament adenocarcinoma and several rare cervical adenocarcinoma variants) have no supporting trials or literature.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02462990 | TECENTRIQ | Not specified | Not specified |
| 02492393 | TECENTRIQ | Not specified | Not specified |
| 02546310 | TECENTRIQ SC | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified in total. The main ones listed are:
  - **Major**: adalimumab, baricitinib, and BCG live vaccine (Tice substrain).
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, methylprednisolone, deflazacort), roflumilast, azathioprine, alemtuzumab, anakinra, alefacept, and several vaccines (tetanus toxoid, anthrax, adenovirus).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For the top prediction, prostatic urethra urothelial carcinoma, the only supporting evidence is a Phase 1b basket trial with a combination partner and no literature. The mechanistic rationale is plausible, but it is not yet corroborated by clinical data. Endocervical carcinoma has the more developed trial record, but it consists of small early-phase studies without reported efficacy results.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Mechanism of action data (for example, from DrugBank)
- Results from NCT03170960, specifically any prostatic urethra or urothelial cohort data
- Efficacy outcomes from the cervical cancer trials (NCT02921269, NCT03738228) if cervical indications are to be pursued
- Approved indication text and dosage forms for the Canadian authorisations
- Literature review specific to urothelial carcinoma subsites
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

