---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Anastrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Anastrozole: From Adjuvant Breast Cancer Therapy to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation non-steroidal aromatase inhibitor long established as a standard adjuvant endocrine therapy for postmenopausal women with hormone receptor-positive breast cancer, though it is currently not registered in Canada.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction.
This prediction represents a high-confidence re-validation of the drug's primary clinical indication, anchored by some of the largest breast cancer RCTs ever conducted—including the landmark ATAC trial (n = 9,358) and MA.27 (n = 7,576).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; established global use in ER-positive breast cancer (postmenopausal, adjuvant and advanced/metastatic settings) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Anastrozole competitively inhibits CYP19A1 (aromatase), the enzyme that catalyses the final step of oestrogen biosynthesis—the conversion of androgens (androstenedione, testosterone) to oestrogens (oestrone, oestradiol) in peripheral tissues including adipose tissue, liver, muscle, and breast parenchyma itself. This reduces circulating oestradiol levels by more than 80% in postmenopausal women and simultaneously suppresses local intratumoral oestrogen synthesis, maximising endocrine blockade at the tumour microenvironment level.

Hormone receptor-positive (ER+/PR+) female breast carcinoma is critically dependent on oestrogen-driven signalling for cell proliferation and survival. Anastrozole's mechanism directly and specifically dismantles this oncogenic driver. Because the drug does not block the oestrogen receptor directly but eliminates the ligand, it avoids several tamoxifen-associated toxicities (endometrial stimulation, thromboembolic events) while achieving equivalent or superior tumour control. The drug also demonstrates activity in the chemoprevention setting, reducing incident breast cancer in high-risk postmenopausal women in the IBIS-II trial, demonstrating utility across the entire disease continuum.

The TxGNN model's high-scoring prediction (99.68%, ranked 6,707 globally) effectively re-discovers anastrozole's primary approved indication. Rather than constituting a traditional repurposing scenario, this result serves as an important internal validation of the TxGNN knowledge-graph methodology and provides a strong pharmacological rationale for pursuing formal Health Canada market authorisation of a well-characterised drug supported by decades of Phase 3 evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Completed | 9,358 | ATAC landmark trial: anastrozole alone vs tamoxifen alone vs combination as adjuvant therapy in postmenopausal women; anastrozole significantly prolonged disease-free survival and reduced contralateral breast cancer events vs tamoxifen |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | Completed | 7,576 | MA.27 (largest head-to-head AI trial): exemestane vs anastrozole in ER+ postmenopausal early breast cancer; established anastrozole as the efficacy and safety benchmark for third-generation aromatase inhibitors |
| [NCT03701334](https://clinicaltrials.gov/study/NCT03701334) | Phase 3 | Active, not recruiting | 5,101 | NATALEE: ribociclib combined with endocrine therapy (including anastrozole) as adjuvant treatment in HR+/HER2− early breast cancer; evaluating CDK4/6 inhibitor augmentation of standard AI therapy |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Completed | 4,172 | Direct comparison of letrozole vs anastrozole as 5-year adjuvant therapy in hormone receptor-positive, lymph node-positive postmenopausal women post-surgery |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | Completed | 3,420 | Denosumab vs placebo to reduce clinical fracture rate in non-metastatic breast cancer patients receiving non-steroidal aromatase inhibitor (anastrozole) therapy; addresses key bone safety concern |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Completed | 2,980 | IBIS-II DCIS: anastrozole vs tamoxifen in postmenopausal women after local excision of hormone receptor-positive DCIS; anastrozole showed superior tolerability and a trend toward improved locoregional control |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Completed | 1,914 | Optimal anastrozole duration: 6 years vs 3 years of adjuvant anastrozole following 2–3 years of tamoxifen in postmenopausal hormone-sensitive breast cancer; informing treatment optimisation |
| [NCT00256698](https://clinicaltrials.gov/study/NCT00256698) | Phase 3 | Completed | 514 | FACT study: anastrozole monotherapy vs maximal oestrogen blockade (anastrozole + fulvestrant) in HR+ postmenopausal breast cancer at first relapse; evaluated combination endocrine strategies |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Completed | 298 | Exemestane vs anastrozole as initial hormonal therapy in postmenopausal women with advanced/recurrent breast cancer; assessed non-inferiority in time to progression |
| [NCT01151215](https://clinicaltrials.gov/study/NCT01151215) | Phase 2 | Terminated | 482 | MINT: AZD8931 plus anastrozole vs anastrozole alone in ER+, endocrine-naïve locally advanced or metastatic breast cancer; progression-free survival as primary endpoint (terminated early, efficacy data limited) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT (landmark) | Lancet | ATAC 5-year results: anastrozole significantly prolonged disease-free survival (HR 0.87) and reduced contralateral breast cancer incidence vs tamoxifen, with distinct toxicity profiles (less VTE/endometrial cancer, more bone loss/fractures) |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT (prevention) | Lancet | IBIS-II long-term follow-up (median 131 months): anastrozole reduced breast cancer incidence by 49% vs placebo in high-risk postmenopausal women; protective effect persisted well beyond the active 5-year treatment period |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS double-blind RCT: anastrozole vs tamoxifen in postmenopausal women with HR+ DCIS; anastrozole demonstrated fewer serious adverse events (fewer thromboembolic events, gynaecological cancers) with comparable or superior recurrence prevention |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis | Oncotarget | Systematic meta-analysis of multiple RCTs comparing anastrozole vs tamoxifen; anastrozole improved disease-free survival and reduced contralateral events, with musculoskeletal adverse effects as the key tolerability difference |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Systematic Review | Rev Assoc Med Bras | Comprehensive review of anastrozole in breast cancer chemoprevention and treatment; covers pharmacokinetics, CYP19A1 mechanism, interindividual pharmacogenomic variability, and synthesis of major trial outcomes |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Review | Expert Opin Drug Saf | Safety profile analysis across multiple adjuvant RCTs; confirmed anastrozole superiority over tamoxifen in terms of thromboembolic and gynaecological safety while highlighting bone mineral density loss as the key monitoring requirement |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | Review | Expert Rev Anticancer Ther | Overview of anastrozole in advanced and early breast cancer; summarises ATAC long-term data and the shift from tamoxifen to aromatase inhibitors as standard of care in postmenopausal ER+ patients |
| [16034487](https://pubmed.ncbi.nlm.nih.gov/16034487/) | 2005 | Drug Review | Drugs Today | Reviews anastrozole mode of action and major clinical trials; discusses its regulatory status as the first aromatase inhibitor approved for adjuvant use specifically in ER+ postmenopausal tumours |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | Oncology | Maps anastrozole's clinical evidence across the breast cancer continuum—second-line advanced disease, first-line advanced disease, early-stage adjuvant, and prevention—supporting its versatility |
| [12113022](https://pubmed.ncbi.nlm.nih.gov/12113022/) | 2001 | Pharmacological Review | Expert Rev Anticancer Ther | Foundational pharmacological profile: oral bioavailability, plasma half-life (~50 hours), once-daily dosing rationale, and early efficacy benchmarks in hormone-sensitive postmenopausal breast cancer |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Endocrine/Hormonal agent (Third-generation non-steroidal aromatase inhibitor; not a conventional cytotoxic) |
| Myelosuppression Risk | Low — anastrozole does not act on rapidly dividing haematopoietic progenitors; clinically significant bone marrow suppression is not expected and is not a standard monitoring requirement |
| Emetogenicity Classification | Minimal — oral tablet formulation; nausea reported in <10% of patients across pivotal trials; routine antiemetic prophylaxis is not required |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and every 1–2 years); liver function tests; fasting lipid profile; musculoskeletal symptoms (arthralgia, myalgia, carpal tunnel syndrome); vasomotor symptoms (hot flushes); serum cholesterol |
| Handling Protection | Apply standard antineoplastic drug handling precautions per institutional policy (anastrozole is listed on the NIOSH Table of Hazardous Drugs); reproductive hazard — contraindicated in women of childbearing potential and during pregnancy |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal TFDA/Health Canada-approved labelling data for key warnings, contraindications, and drug interactions was not available in this Evidence Pack (Data Gaps DG001 and DG002). Remediation is required before proceeding to safety screening Stage S1.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of anastrozole for female breast carcinoma is powerfully corroborated by an L1-grade evidence base spanning multiple completed large Phase 3 RCTs (ATAC n = 9,358; MA.27 n = 7,576; IBIS-II n = 3,864), providing one of the most robust pharmacological evidence dossiers in oncology endocrine therapy; however, anastrozole is currently not registered in Canada (0 DINs), and critical safety labelling data remain absent, necessitating a structured regulatory and clinical operations plan before deployment.

**To proceed, the following is needed:**

- **Health Canada market authorisation pathway:** Initiate a New Drug Submission (NDS) or file a regulatory package leveraging the ATAC, MA.27, and IBIS-II Phase 3 dossiers as pivotal evidence
- **Safety labelling remediation (DG001):** Obtain and parse the full approved product monograph (key warnings, contraindications, drug interactions) from an approved jurisdiction (e.g., EMA, FDA, or TGA) to complete the safety screening gate
- **MOA documentation (DG002):** Formally document the CYP19A1 competitive inhibition mechanism with supporting references for the regulatory submission
- **Bone health management protocol:** Establish a baseline DEXA scan requirement, calcium and vitamin D supplementation guidance, and fracture risk stratification criteria for clinical sites
- **Pharmacovigilance plan:** Define monitoring for musculoskeletal adverse events (arthralgia prevalence up to 35%), cardiovascular lipid changes, and long-term bone density loss at 12 and 24 months
- **Population eligibility criteria:** Clarify applicable patient subpopulation (postmenopausal status confirmation, ER/PR receptor testing requirements, prior endocrine therapy history)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

