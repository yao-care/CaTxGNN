---
layout: default
title: Trastuzumab
parent: Moderate Evidence (L3-L4)
nav_order: 925
evidence_level: L3
indication_count: 10
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Trastuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Trastuzumab is an anti-HER2 monoclonal antibody, originally used for HER2-positive breast cancer. The Canadian licence records provided do not list an indication, so this original use comes from general drug knowledge. The TxGNN model predicts it may be effective for the **normal breast-like subtype of breast carcinoma**, but only **10 loosely related clinical trials** (mostly HER2-targeted regimens in breast cancer generally) and **1 publication** (a morphology study that does not test trastuzumab) are linked to this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (general knowledge; not recorded in the Canadian licence data) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, trastuzumab is an anti-HER2 antibody. It binds the HER2 extracellular domain, inhibits HER2 signalling and mediates antibody-dependent cellular cytotoxicity. Its efficacy in HER2-positive breast cancer is well established.

The normal breast-like subtype (a PAM50 gene-expression class) is usually HER2-negative. A benefit would therefore be plausible only in HER2-positive tumours that happen to be classified as normal-like. The trials retrieved mostly test HER2-targeted regimens in breast cancer broadly, not this subtype specifically. The very high TxGNN score most likely reflects the general breast cancer neighbourhood in the knowledge graph rather than subtype-specific biology.

The same pack shows much stronger support for related breast cancer subtypes defined by receptor status. For HER2-positive disease that is progesterone-receptor positive or negative, there are completed Phase 3 trials and randomized Phase 2 trials. Those are essentially established HER2-positive uses, not novel repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine with neoadjuvant chemotherapy and HER2-targeted antibody in breast cancer; immune response and safety; no results |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | Trastuzumab deruxtecan vs CDK4/6 inhibitors in non-luminal A, ER+/HER2-low metastatic disease; never enrolled, no evidence |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant weekly paclitaxel ± carboplatin in triple-negative breast cancer; trastuzumab role and subtype link unconfirmed |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | ARIADNE: trastuzumab deruxtecan with biology-driven neoadjuvant selection in HER2-positive disease; the agent is an ADC, not trastuzumab itself |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Drug screening on patient-derived tumour cell clusters to guide neoadjuvant therapy in HER2-positive early breast cancer |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib ± fulvestrant in HER2-mutant, non-amplified metastatic disease; trastuzumab not part of the regimen |
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, not recruiting | 55 | ATREZZO: atezolizumab with trastuzumab and vinorelbine in ER-negative or PAM50 non-luminal HER2-positive advanced disease |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | FASCINATE-N: subtype-based precision neoadjuvant platform in operable breast cancer |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Phase 1/2 | Recruiting | 120 | Hydroxychloroquine plus antibody-drug conjugate (trastuzumab deruxtecan or sacituzumab govitecan) vs ADC alone in advanced breast cancer |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Phase 2 | Recruiting | 65 | Neoadjuvant pyrotinib plus trastuzumab and nab-paclitaxel in HER2-enriched early or locally advanced breast cancer |

Further trials were retrieved but are not shown: NCT06348134 (neoadjuvant to adjuvant anti-HER2 therapy in Nigerian women, Phase 2, recruiting) and NCT01796197 (paclitaxel, trastuzumab and pertuzumab in inflammatory breast cancer, Phase 2, completed). None of the listed trials reports results for the normal breast-like subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Cohort | Breast Cancer (Tokyo) | Morphological and cytopathological features of the basal-like subtype; background on the five intrinsic subtypes, including normal breast-like; no trastuzumab efficacy data |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2483475 | TRAZIMERA | — | — |
| 2506211 | HERZUMA | — | — |
| 2474425 | OGIVRI | — | — |
| 2483467 | TRAZIMERA | — | — |
| 2518244 | KANJINTI | — | — |

Only 5 of the 15 authorizations are listed. The product names indicate trastuzumab biosimilars. Dosage form and indication text were not captured in the source data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as a single agent; may increase when combined with chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (LVEF) before and during treatment, infusion-related reactions; CBC when given with chemotherapy |
| Handling Protection | Please refer to the package insert and institutional policy for handling requirements |

These entries are general class knowledge, not drawn from the supplied record. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for the normal breast-like subtype rests on a high model score and indirect trial evidence. The trials mostly cover HER2-positive breast cancer in general, and one is withdrawn with no enrolment. The only publication is a morphology study with no efficacy data. Because this subtype is usually HER2-negative, a benefit is not supported unless the tumour is HER2-positive. That is already an established use, not new repurposing.

**To proceed, the following is needed:**
- Subtype-stratified (PAM50) outcome data for trastuzumab-treated HER2-positive tumours classified as normal-like
- Confirmation of HER2 status criteria for any proposed use in this subtype
- Mechanism of action data from DrugBank
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian authorizations
- Prioritization of the PR-positive and PR-negative HER2-positive predictions, which have much stronger evidence in this pack, as the more actionable candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

