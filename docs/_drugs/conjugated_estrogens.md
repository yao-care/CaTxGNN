---
layout: default
title: Conjugated Estrogens
parent: Moderate Evidence (L3-L4)
nav_order: 225
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Conjugated Estrogens: predicted new indication Migraine disorder (evidence level L3). Approved use: Psychologic dyspareunia"
monitor_inn: "Conjugated estrogens"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "heparin cofactor 2 deficiency", "Prinzmetal angina", "hemoglobinopathy", "migraine with or without aura, susceptibility to", "thrombophilia"]
---

# Conjugated Estrogens
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Conjugated Estrogens: From Psychologic Dyspareunia to Migraine Disorder

## One-Sentence Summary

Conjugated estrogens are a hormone therapy; the original indication recorded for this drug is psychologic dyspareunia.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **5 publications** (reviews and cohort studies, no controlled trials) supporting this direction, and the direction of effect is inconsistent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychologic dyspareunia |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, conjugated estrogens are an estrogen-replacement therapy marketed in several forms in Canada (vaginal cream, oral, intravenous, and in combination with bazedoxifene as Duavive), and their effect on hormone-sensitive conditions is established. Mechanistically they may be relevant to **migraine disorder**.

Menstrual and perimenopausal migraine is linked to fluctuations in estrogen levels, particularly large swings in estradiol during the perimenopausal period. The idea is that stabilising estrogen exposure might change migraine frequency. The connection to the original indication (psychologic dyspareunia) is only that both involve hormonal status, and the data compiled for this report do not describe a closer similarity.

The clinical literature does not point consistently in one direction. Oral conjugated estrogens and cyclic regimens worsened migraine in some postmenopausal women, whereas transdermal, continuous regimens tended to be better tolerated. The effect therefore depends on formulation and regimen. Migraine with aura also carries a higher risk of ischaemic stroke, and estrogen adds to that concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29521155](https://pubmed.ncbi.nlm.nih.gov/29521155/) | 2018 | Review | Climacteric | Hormonal fluctuations, especially large estradiol changes in the perimenopause, are an important migraine trigger; contraception and reproductive life can alter migraine course |
| [11306204](https://pubmed.ncbi.nlm.nih.gov/11306204/) | 2001 | Cohort | Maturitas | Evaluated how hormone replacement therapy influences the course of primary headaches in postmenopausal women |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral HRT schemes; hormone supplementation affected migraine differently depending on regimen |
| [8309263](https://pubmed.ncbi.nlm.nih.gov/8309263/) | 1994 | Review | Mayo Clinic Proceedings | Compared transdermal and oral estrogen therapy across clinical situations in women |
| [14195735](https://pubmed.ncbi.nlm.nih.gov/14195735/) | 1964 | Case series | Medizinische Klinik | Historical report on conjugated estrogens for climacteric disorders (no abstract available) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02043440 | PREMARIN VAGINAL CREAM | Not specified | Not specified |
| 02414678 | PREMARIN | Not specified | Not specified |
| 02414694 | PREMARIN | Not specified | Not specified |
| 02043386 | PREMARIN INTRAVENOUS | Not specified | Not specified |
| 02414686 | PREMARIN | Not specified | Not specified |

A sixth authorisation, DUAVIVE (DIN 02432854), is also valid.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs; the 20 reviewed here were mostly of Moderate level and one was Minor (cimetidine). Main examples:
  - Antidiabetic drugs: acarbose, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin, empagliflozin, acetohexamide, chlorpropamide
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Others: aprepitant, clarithromycin, clotrimazole, chenodeoxycholic acid, topical calcitriol
- **Class-level concerns relevant to this indication**: Estrogen raises thrombotic risk, and migraine with aura already carries an elevated ischaemic stroke risk.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the supporting evidence is limited to reviews and observational cohorts with inconsistent effects that depend on formulation and regimen. There are no controlled trials, and the stroke and thrombosis risks in migraine, especially with aura, are a significant safety concern.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing and blocking safety screening)
- Mechanism of action data
- A formulation- and regimen-specific review (for example transdermal and continuous versus oral and cyclic) of the effect on migraine
- Risk stratification for migraine with aura and stroke risk
- Controlled clinical evidence before any further development

---

### Notes on other predicted indications

The other predictions have weaker support or raise safety concerns:

- **Migraine with or without aura, susceptibility to** (99.37%, L3): shares the migraine literature, with the same mixed results and stroke concern.
- **Migraine with brainstem aura** (99.74%, L4): the literature addresses general migraine, not this subtype, and estrogen raises stroke concern with aura.
- **Rheumatoid arthritis** (99.55%, L4): only one animal study of a conjugated estrogen and bazedoxifene combination; no human evidence.
- **Antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, thrombophilia**: these are prothrombotic conditions, and estrogen would be expected to increase thrombotic risk. The predictions likely reflect disease associations, not therapeutic benefit.
- **Prinzmetal angina** (99.53%, L5): model prediction only, with no evidence.
- **Hemoglobinopathy** (99.44%, L4): the only paper is an endocrine observation in thalassemia and does not support a therapeutic indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

