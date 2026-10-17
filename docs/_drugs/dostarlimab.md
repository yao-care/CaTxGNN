---
layout: default
title: Dostarlimab
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dostarlimab: predicted new indication Cervical adenofibroma (evidence level L5). Approved use: Not available in the Canadian license data (the label indication text…"
monitor_inn: "Dostarlimab"
predicted_indications: ["cervical adenofibroma", "vulvar alveolar soft part sarcoma", "LAMA5-related multisystemic syndrome", "primary biliary cholangitis/primary sclerosing cholangitis and autoimmune hepatitis overlap syndrome", "bile duct cystadenoma", "clear cell hidradenoma", "infantile hypotonia-oculomotor anomalies-hyperkinetic movements-developmental delay syndrome", "fallopian tube papillary adenocarcinoma", "bladder clear cell adenocarcinoma", "O'nyong'nyong fever"]
---

# Dostarlimab
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

# Dostarlimab: From an Unspecified Original Indication to Cervical Adenofibroma

## One-Sentence Summary

Dostarlimab (brand name JEMPERLI) is an anti-PD-1 antibody that is marketed in Canada. The indication text for its Canadian license was not available in the data compiled for this report.
The TxGNN model's top-ranked prediction is **cervical adenofibroma**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
Across the 10 predicted indications reviewed, only one (bladder clear cell adenocarcinoma) has any trial linked to it, and that link is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Canadian license data (the label indication text is blank) |
| Predicted New Indication | Cervical adenofibroma |
| TxGNN Prediction Score | 50.00% (a non-discriminative value; all 10 predictions share the same score) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action text is not available in the compiled data. Based on the target data, dostarlimab is an antibody that binds human PD-1 (gene *PDCD1*). It blocks the interaction of both PD-L1 and PD-L2 with PD-1, which releases the brake on T-cell activity against tumours. Its clinical use is documented elsewhere in the data: it is approved by the FDA and the EMA for mismatch repair-deficient (dMMR) recurrent or advanced endometrial cancer, and for other dMMR solid tumours. The FDA also approved it with chemotherapy for primary advanced or recurrent endometrial cancer.

For **cervical adenofibroma**, the link is weak. Adenofibromas are typically benign, and there is no evidence that PD-1 blockade helps them. The score of 0.5 does not discriminate between candidates, so it should not be read as a strong signal.

Other candidates in the list are more plausible than the top-ranked one:

- **Fallopian tube papillary adenocarcinoma** is a related Müllerian malignancy, and dostarlimab is already used in dMMR endometrial cancer. Any benefit would likely be limited to dMMR/MSI-H or PD-L1-positive subsets. No trials or publications were supplied, so it remains a research question.
- **Bladder clear cell adenocarcinoma** has one indirect basket trial (see below), but nothing specific to this tumour type.

Several other predictions have no plausible mechanistic link (for example LAMA5-related multisystemic syndrome, O'nyong'nyong fever, and a rare neurodevelopmental syndrome). One is a safety concern: in the autoimmune overlap syndrome of primary biliary cholangitis/primary sclerosing cholangitis and autoimmune hepatitis, PD-1 blockade can itself cause immune-mediated hepatitis and cholangitis.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication, cervical adenofibroma.

For reference, the only trial found among the 10 predicted indications relates to rank 9, bladder clear cell adenocarcinoma:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04779151](https://clinicaltrials.gov/study/NCT04779151) | Phase 2 | Terminated | 51 | Basket trial of niraparib (PARP inhibitor) priming followed by an anti-PD-1 antibody (dostarlimab) in DNA repair-deficient or platinum-sensitive solid tumours. No efficacy results were supplied. Whether bladder clear cell adenocarcinoma was a cohort cannot be confirmed. Relevance grade: C (indirect). |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02523434 | JEMPERLI | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry. It is a target record (PD-1, CD279) rather than an interaction with another drug, so it does not point to a clinically relevant drug interaction.
- **Class-related concern**: For autoimmune conditions such as the overlap syndrome of primary biliary cholangitis/primary sclerosing cholangitis and autoimmune hepatitis, immune activation by PD-1 blockade is mechanistically counterproductive and a safety concern.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, cervical adenofibroma, rests only on a non-discriminative model score (0.5). It has no trials or publications and no clear mechanistic rationale, so evidence is at L5. Among the other candidates, fallopian tube papillary adenocarcinoma and bladder clear cell adenocarcinoma are worth tracking as research questions, but neither has direct supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and the approved indication text (currently missing, and a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Targeted literature and trial searches for cervical adenofibroma, and for the more plausible candidates (fallopian tube papillary adenocarcinoma and bladder clear cell adenocarcinoma)
- For NCT04779151, confirmation of the exact drug combination, the cohorts enrolled, and any reported results
- If a dMMR/MSI-H or PD-L1-positive subset is considered, biomarker-based eligibility criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

