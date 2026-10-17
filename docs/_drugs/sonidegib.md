---
layout: default
title: Sonidegib
parent: Model Prediction Only (L5)
nav_order: 862
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sonidegib: predicted new indication Medulloblastoma with extensive nodularity (evidence level L5). Approved use: Skin carcinoma, basal cell carcinoma, sweat gland cancer…"
monitor_inn: "SONIDEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "trichothiodystrophy photosensitive", "benign neoplasm of sweat gland", "obsolete cataract, microcephaly, failure to thrive, kyphoscoliosis syndrome"]
---

# Sonidegib
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

# Sonidegib: From Basal Cell Carcinoma to Skin Cancer (Advanced Basal Cell Carcinoma)

## One-Sentence Summary

Sonidegib was originally used to treat basal cell carcinoma and related skin carcinomas.
The TxGNN model's top-ranked prediction with clinical evidence is **skin cancer**, which largely overlaps with the existing indication, so it is essentially an on-label signal rather than a true repurposing finding.
It is supported by **6 clinical trials** and **20 publications**. The highest-scoring prediction, medulloblastoma with extensive nodularity, has no trials or literature behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skin carcinoma, basal cell carcinoma, sweat gland cancer, sebaceous adenocarcinoma (the Canadian licence record contains no indication text) |
| Predicted New Indication | Medulloblastoma with extensive nodularity (rank 1, no evidence); skin cancer (rank 6, the only prediction with substantial evidence) |
| TxGNN Prediction Score | 99.90% (medulloblastoma); 99.76% (skin cancer) |
| Evidence Level | L5 for medulloblastoma; L1 assigned for skin cancer, though the listed trials are Phase 2 only (see below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold for medulloblastoma; Proceed with Guardrails for skin cancer (advanced BCC) |

> **Note on the evidence level:** The L1 definition requires at least 2 completed Phase 3 RCTs. The compiled data list only Phase 2 trials, so by strict application the skin cancer entry would be closer to L2. The label of L1 reflects the strength of the approval-supporting evidence for BCC and guideline endorsement.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From the published literature, sonidegib is an oral Smoothened (SMO) receptor antagonist that blocks the Hedgehog signalling pathway. This pathway is abnormally activated in most basal cell carcinomas, which explains the drug's efficacy in advanced disease.

**Skin cancer (rank 6):** This entry mostly restates the original indication. Hedgehog inhibition is the central driver of BCC, and guidelines endorse it for difficult-to-treat disease.

**Medulloblastoma (rank 1):** The SHH subgroup of medulloblastoma, including the desmoplastic/nodular variant, is driven by Hedgehog signalling, so the link is biologically plausible. However, there are no trials or publications, and the high score is a computational prediction only. Sonidegib carries a known risk of premature growth plate closure in children, which matters because this tumour mainly affects children.

**Xeroderma pigmentosum (rank 2):** Patients develop multiple Hedgehog-driven BCCs because of defective DNA repair. Sonidegib acts on the tumours, not on the repair defect, so the support is indirect (a single 2026 case report).

Several other predictions (annular epidermolytic ichthyosis, epidermolysis bullosa simplex with mottled pigmentation, an obsolete cataract/microcephaly syndrome) have no identifiable mechanistic link and probably reflect network artefacts. Eccrine carcinoma and cutaneous adenocystic carcinoma are adjacent to the sweat gland cancers in the original indications but are unsupported by data.

---

## Clinical Trial Evidence

Trials for the skin cancer prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01327053](https://clinicaltrials.gov/study/NCT01327053) | Phase 2 | Completed | 230 | Randomised, double-blind comparison of two sonidegib dose levels in locally advanced or metastatic BCC; direct efficacy and safety evidence |
| [NCT03534947](https://clinicaltrials.gov/study/NCT03534947) | Phase 2 | Completed | 16 | Short-term neoadjuvant sonidegib followed by surgery or imiquimod for BCC in cosmetically challenging sites; small exploratory pilot |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | Recruiting | 80 | Dutch prospective registry of vismodegib and sonidegib in advanced and multiple BCC; real-world data |
| [NCT04007744](https://clinicaltrials.gov/study/NCT04007744) | Phase 1 | Active, not recruiting | 36 | Sonidegib plus pembrolizumab in advanced solid tumours; combination safety study, only partly skin-specific |
| [NCT02303041](https://clinicaltrials.gov/study/NCT02303041) | Phase 2 | Terminated | 10 | Sonidegib plus buparlisib in advanced BCC; terminated early, limited data |
| [NCT01757327](https://clinicaltrials.gov/study/NCT01757327) | Phase 2 | Withdrawn | 0 | Placebo-controlled study in early breast cancer; withdrawn with no enrolment, so no data |

No clinical trials are registered for medulloblastoma or the other predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Guideline | Eur J Cancer | Updated European consensus guideline on BCC diagnosis and treatment |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Guideline | Eur J Cancer | European guideline introducing "easy-to-treat" and "difficult-to-treat" BCC categories |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Review | Cell | Hedgehog pathway is activated in most BCC; sonidegib and vismodegib are SMO inhibitors approved for locally advanced BCC |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | Comprehensive review of BCC molecular features and resistance to systemic therapy |
| [33194718](https://pubmed.ncbi.nlm.nih.gov/33194718/) | 2020 | Review | Front Oncol | Sonidegib for advanced BCC |
| [33888008](https://pubmed.ncbi.nlm.nih.gov/33888008/) | 2021 | Expert opinion | Expert Opin Drug Saf | Efficacy, safety and tolerability of sonidegib |
| [26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/) | 2015 | Drug profile | Drugs | First global approval of sonidegib (Odomzo) as an SMO antagonist |
| [39062023](https://pubmed.ncbi.nlm.nih.gov/39062023/) | 2024 | Review | Biomedicines | Advanced and metastatic non-melanoma skin cancer: risk factors and treatment options |
| [33725197](https://pubmed.ncbi.nlm.nih.gov/33725197/) | 2021 | Review | Curr Treat Options Oncol | Neoadjuvant approaches in non-melanoma skin cancer, including Hedgehog inhibitors |
| [41862093](https://pubmed.ncbi.nlm.nih.gov/41862093/) | 2026 | Case report | Actas Dermosifiliogr | Sonidegib for multiple BCCs in a patient with xeroderma pigmentosum (supports BCC in XP, not XP itself) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02500337 | ODOMZO | Not specified | Not specified in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Creatine kinase (CK) and musculoskeletal symptoms; liver and renal function as clinically indicated |
| Handling Protection | Please refer to the package insert; embryo-fetal toxicity warrants caution in handling by women who are or may become pregnant |

---

## Safety Considerations

- **Key Warnings (from the repurposing assessment):** Musculoskeletal toxicity with CK elevation; embryo-fetal toxicity, so avoid in pregnancy; risk of premature growth plate closure in children, which is relevant for medulloblastoma.
- **Drug Interactions:** 100 interactions were identified. Examples by level:
  - **Major:** aprepitant, dexamethasone, clarithromycin, clotrimazole, cobicistat
  - **Moderate:** cimetidine, metreleptin, miconazole, troglitazone, deferasirox
  - **Minor:** famotidine, ranitidine, and proton pump inhibitors such as omeprazole, pantoprazole, esomeprazole, lansoprazole, rabeprazole

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (skin cancer / advanced BCC); Hold (all other predicted indications)**

**Rationale:**
- The skin cancer prediction is effectively the existing BCC indication, backed by a completed randomised double-blind Phase 2 trial (n=230), guidelines and many reviews. It is not a new repurposing opportunity.
- Medulloblastoma and the remaining predictions are computational signals only, with no trials or literature. Xeroderma pigmentosum is supported by a single case report that concerns BCC in an XP patient.

**To proceed, the following is needed:**
- Restrict use to advanced or metastatic BCC not amenable to surgery or radiation, with CK and musculoskeletal monitoring and pregnancy avoidance.
- Obtain Health Canada package insert warnings and contraindications (a blocking gap for safety screening), plus approved indication text and dosage form for the licence.
- Obtain detailed mechanism-of-action data.
- For medulloblastoma, preclinical or early clinical evidence and a paediatric safety assessment (growth plate effects) before any further consideration.
- For xeroderma pigmentosum, additional evidence beyond the single case report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

