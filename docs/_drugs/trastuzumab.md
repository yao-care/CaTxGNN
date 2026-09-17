---
layout: default
title: Trastuzumab
parent: Moderate Evidence (L3-L4)
nav_order: 792
evidence_level: L4
indication_count: 10
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

> Trastuzumab is an anti-HER2 monoclonal antibody established as standard therapy for HER2-positive breast cancer.
> The TxGNN model predicts it may be effective for **normal breast-like subtype of breast carcinoma**,
> but this subtype is typically HER2-low/negative, so the mechanistic fit is weak; **12 clinical trials** and **1 publication** are available, none of which specifically target this subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HER2-positive breast cancer (established anti-HER2 standard of care; not separately recorded in `original_indications`) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trastuzumab is not available in the current DrugBank extract (flagged as a High-severity data gap, DG002). Based on the evidence embedded in this pack, trastuzumab's mechanism is consistently described as **HER2 receptor inhibition** — it is a humanized monoclonal antibody that binds the extracellular domain of HER2/ErbB2 and blocks proliferation of HER2-overexpressing tumor cells. Its established use is in HER2-positive breast cancer, where HER2 amplification/overexpression is the key predictive biomarker for response.

The predicted new indication, "normal breast-like subtype of breast carcinoma," is one of the five intrinsic PAM50 molecular subtypes of breast cancer. Critically, this subtype is typically characterized by **low or absent HER2 expression** — the opposite of the biomarker profile trastuzumab targets. Nearly all of the clinical trials retrieved for this indication are general HER2-positive breast cancer studies (neoadjuvant chemotherapy + trastuzumab regimens, vaccine combinations, ADC comparisons) that were not designed to enrich for or specifically study the normal-like subtype.

Given this, the mechanistic rationale is weak: the high TxGNN score appears to be driven by breast-cancer-subtype proximity in the knowledge graph rather than by a biologically plausible HER2-targeting relationship. Any real-world extension would require confirmation of HER2 status at the individual tumor level (IHC/FISH) rather than reliance on subtype label alone — this is reflected in the model's own "Hold" recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine + chemotherapy + HER2-targeted mAb as neoadjuvant therapy in breast cancer; tests immunologic response, not subtype-specific |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | T-DXd vs CDK4/6 inhibitors in non-Luminal A, ER+/HER2-low metastatic breast cancer; withdrawn, no evidence contribution |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant paclitaxel ± carboplatin in triple-negative breast cancer; general HER2+ population, not normal-like-specific |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | T-DXd vs standard preoperative treatment in HER2-positive breast cancer with biomarker-driven subtype selection (ARIADNE) |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Organoid drug-screening-guided neoadjuvant therapy for HER2-positive early breast cancer |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib ± fulvestrant in HER2 non-amplified but HER2-mutant breast cancer |
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, not recruiting | 55 | Atezolizumab + trastuzumab + vinorelbine in ER-negative or PAM50 non-luminal HER2-positive advanced breast cancer (ATREZZO) |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | Precision neoadjuvant platform study stratified by molecular subtype in operable breast cancer (FASCINATE-N) |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Phase 1/2 | Recruiting | 120 | Hydroxychloroquine + antibody-drug conjugate (T-DXd/SG) vs ADC alone in advanced breast cancer |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Phase 2 | Recruiting | 65 | Pyrotinib + trastuzumab + Abraxane in HER2-enriched early/locally advanced breast cancer, referencing PAM50/BluePrint subtyping |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Review | Breast Cancer (Tokyo, Japan) | Describes morphological/cytopathological characteristics of basal-like subtype among the five intrinsic molecular subtypes (including normal breast-like); no trastuzumab efficacy data |

---

## Canada Market Information

Trastuzumab is currently **not marketed** in this jurisdiction — no DIN records or product license entries are available in the regulatory dataset.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (normal breast-like subtype) is typically HER2-low/negative, which conflicts with trastuzumab's core mechanism of HER2 receptor inhibition. No clinical trial or literature evidence directly studies trastuzumab in this specific subtype, and evidence level is L4 (mechanistic/indirect only).

**To proceed, the following is needed:**
- TFDA/Health Canada label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Verified mechanism of action from DrugBank API — currently a High-severity data gap (DG002)
- HER2 IHC/FISH expression data specific to the normal breast-like subtype population
- A dedicated clinical trial or biomarker-stratified cohort testing trastuzumab specifically in HER2-confirmed normal-like tumors, rather than relying on subtype label alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

