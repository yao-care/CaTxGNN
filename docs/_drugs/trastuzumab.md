---
layout: default
title: Trastuzumab
parent: High Evidence (L1-L2)
nav_order: 932
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Trastuzumab: predicted new indication Progesterone-receptor positive breast cancer (evidence level L1). Approved use: HER2-positive breast carcinoma"
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Trastuzumab: From HER2-Positive Breast Carcinoma to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a HER2-targeted antibody originally used to treat HER2-positive breast carcinoma.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, the highest-ranked prediction with meaningful evidence.
It is supported by **12 clinical trials** and **20 publications**. However, this is largely a subset of the already-approved HER2-positive use rather than a true new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast carcinoma |
| Predicted New Indication | Progesterone-receptor positive breast cancer (the top-ranked prediction, "normal breast-like subtype of breast carcinoma", has only L4 evidence and is not selected) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the available evidence, trastuzumab binds the extracellular domain of HER2, blocks HER2 signalling and mediates antibody-dependent cellular cytotoxicity (ADCC).

HER2-positive tumours are often also progesterone-receptor (PR) positive, so this prediction largely overlaps with the approved HER2-positive breast cancer use. The evidence applies to HER2-positive disease with PR positivity. It does not support use in PR-positive/HER2-negative disease, where benefit is limited to HER2-low settings with the different agent trastuzumab deruxtecan.

The model's other breast-related predictions follow the same pattern. PR-negative disease (rank 3) is also an approved-use subset, since HER2-positive/hormone-receptor-negative tumours are a core responder group. The "normal breast-like" subtype (rank 1) is generally HER2-negative, so its mechanistic link is weak. Luminal A or B (rank 4) is plausible only for HER2-positive luminal B.

Predictions ranked 5 to 10 (rare skin, neuroendocrine, viral-related and urothelial tumours) rest on the model score alone, with no trial or literature support.

---

## Clinical Trial Evidence

Trials for progesterone-receptor positive breast cancer (up to 10 shown, ordered by relevance):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy with or without trastuzumab in node-positive or high-risk node-negative breast cancer; the strongest direct evidence |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Completed | 92 | Neoadjuvant paclitaxel and cyclophosphamide with or without trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | Completed | 50 | Neoadjuvant chemotherapy regimen in HER2-positive breast cancer (hormone receptor negative or positive); small, single-arm |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Unknown | 34 | Palbociclib, trastuzumab, pyrotinib and fulvestrant for brain metastases from ER/PR-positive, HER2-positive disease |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | Completed | 36 | Cabozantinib alone or with trastuzumab in breast cancer with brain metastases; exploratory |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole plus trastuzumab in ErbB2-positive, ER and/or PR-positive metastatic breast cancer |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib, endocrine therapy and trastuzumab in ER-positive, HER2-positive cancers |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus, letrozole and trastuzumab in hormone-receptor-positive, HER2-positive cancers |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 plus trastuzumab and docetaxel versus reference pertuzumab in HER2-positive, ER/PR-negative breast cancer |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Withdrawn | 0 | Trastuzumab with or without tamoxifen in hormone-receptor-positive, HER2-positive stage IV disease; no participants enrolled, so no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT (Phase 2) | Lancet Oncol | monarcHER: abemaciclib plus trastuzumab with or without fulvestrant versus trastuzumab plus chemotherapy in HR-positive, HER2-positive advanced breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT follow-up (Phase 2) | Lancet Oncol | NeoSphere 5-year analysis of neoadjuvant pertuzumab and trastuzumab in HER2-positive breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 weeks of neoadjuvant trastuzumab and pertuzumab with or without paclitaxel |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis | Lancet | EBCTCG overview of chemotherapy and hormonal therapy effects on recurrence and 15-year survival in early breast cancer |
| [41780642](https://pubmed.ncbi.nlm.nih.gov/41780642/) | 2026 | RCT (different agent) | Ann Oncol | DESTINY-Breast06: trastuzumab deruxtecan in HR-positive, HER2-low/-ultralow metastatic breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohort/multiomics | Theranostics | Molecular features and trastuzumab responsiveness of ER-positive, PR-positive, HER2-positive (triple-positive) breast cancer |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Review | Nat Rev Clin Oncol | Combining anti-HER2 therapy with aromatase inhibitors in HER2-positive, hormone-receptor-positive disease |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Targeted and cytotoxic inhibitors in breast cancer, organised by HER2, HR, ER and PR status |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | Phase 2a, single-arm | Lancet Oncol | Zanidatamab plus palbociclib and fulvestrant in HR-positive, HER2-positive metastatic breast cancer (different agent) |

---

## Canada Market Information

Health Canada lists 15 valid single-ingredient licences. Dosage form and approved-indication text are not available in the data compiled for this report. Main authorizations (up to 5 shown):

| DIN | Product Name |
|---------|------|
| 02240692 | HERCEPTIN |
| 02480697 | HERCEPTIN SC |
| 02483475 | TRAZIMERA |
| 02506211 | HERZUMA |
| 02474425 | OGIVRI |

Other licences include further TRAZIMERA, HERZUMA, OGIVRI, KANJINTI and ONTRUZANT presentations, plus PHESGO and PERJETA-HERCEPTIN.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low as a single agent; haematological toxicity is mainly driven by combined chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (LVEF) before and during treatment; CBC and liver and renal function when combined with chemotherapy |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Cardiotoxicity**: the literature on adjuvant trastuzumab trials raises questions about the reversibility of trastuzumab-related cardiac toxicity (PMID 17687157), so LVEF monitoring is a key guardrail.
- **Drug Interactions**: 94 interactions are recorded. Major-level interactions include deferiprone, samarium (153Sm) lexidronam, adalimumab and baricitinib. Moderate-level interactions include paclitaxel, warfarin, dicoumarol, azathioprine, alemtuzumab, anakinra and zidovudine, among others.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The strongest support is a completed Phase 3 adjuvant trial (n=3270) plus randomized Phase 2 data in HER2-positive, hormone-receptor-positive disease. However, this is essentially an approved HER2-positive use, not a new indication, and it does not extend to HER2-negative PR-positive disease. The other predictions (rank 1 "normal breast-like", rank 4 luminal A/B, ranks 5 to 10) should stay on Hold or as research questions.

**To proceed, the following is needed:**
- Confirmation of HER2 positivity before treatment, with use limited to HER2-positive disease
- LVEF monitoring plan and consideration of endocrine therapy combinations
- Health Canada package insert warnings and contraindications (currently a blocking data gap)
- Detailed mechanism of action data from DrugBank
- A second completed Phase 3 trial focused on the HR-positive/HER2-positive subgroup, if a separate indication claim is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

