---
layout: default
title: Trastuzumab Emtansine
parent: High Evidence (L1-L2)
nav_order: 794
evidence_level: L1
indication_count: 10
---

# Trastuzumab Emtansine
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor-Positive Breast Cancer

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate already used to treat HER2-positive breast cancer.
The TxGNN model's top-ranked prediction is **progesterone-receptor (PR) positive breast cancer** —
a biomarker subgroup within the existing HER2+ population rather than a novel disease target —
supported by **4 clinical trials** and **15 publications**, including multiple ASCO practice guidelines.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (existing globally approved indication; not confirmed against Canadian regulatory data — see note below) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** `taiwan_regulatory.licenses` contains no records (0 DINs), so the original indication above could not be sourced from Canadian regulatory data. It is derived from the evidence pack's own mechanistic rationale, which explicitly identifies HER2-positive breast cancer as T-DM1's existing on-label population.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on the mechanistic rationale captured in the evidence pack, Trastuzumab emtansine is an antibody-drug conjugate (ADC): the anti-HER2 monoclonal antibody trastuzumab is chemically linked to the cytotoxic microtubule inhibitor DM1 (mertansine). The antibody component delivers the cytotoxic payload selectively to HER2-overexpressing tumor cells.

Importantly, this "predicted new indication" is not a typical repurposing signal. Progesterone-receptor (PR) status is a co-existing biomarker used for endocrine therapy decisions, not the pharmacological target of T-DM1. HER2+ breast cancer patients who are also PR-positive already fall within T-DM1's approved population — so this prediction is best understood as **confirmation of an existing on-label subgroup**, rather than discovery of a new disease application. The model's very high score reflects the strength of the underlying HER2+ breast cancer evidence base rather than a novel mechanistic hypothesis.

Because HER2 targeting is independent of PR expression, there is no biological reason to expect reduced efficacy in PR+ patients — several of the supporting trials and guidelines below directly address HER2+ breast cancer populations that include PR+ patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs. placebo added to neoadjuvant ddAC-paclitaxel-trastuzumab-pertuzumab in early HER2+ breast cancer (T-DM1-adjacent anti-HER2 regimen context) |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Preoperative T-DM1 + pertuzumab; studies impact of HER2 heterogeneity on treatment response |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | De-escalation of adjuvant chemotherapy after pathological complete response in HER2+/ER-negative early breast cancer with dual HER2 blockade |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective multicenter study on prevalence and treatment patterns of HER2-low metastatic breast cancer (indirect relevance; non-interventional) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline | J Clin Oncol | ASCO clinical practice guideline update for HER2-positive advanced breast cancer |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guideline | J Clin Oncol | ASCO guideline on systemic therapy for HER2-positive advanced breast cancer |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline | Eur J Cancer | EGTM biomarker guidelines: HER2 and PR/ER testing both mandated for treatment selection in invasive breast cancer |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacological Research | Overview of targeted and cytotoxic inhibitors used in breast cancer, including T-DM1 |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Current treatment trends in HR+/HER2+ breast cancer, including T-DM1 as a chemotherapy-free option |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohort (ChangeHER trial) | Scientific Reports | Prognostic relevance of HER2-positivity gain in metastatic breast cancer treated with pertuzumab and/or T-DM1 |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Case report | Case Reports in Oncology | Dose-reduced T-DM1 shown active and safe in a patient with acute hepatic dysfunction |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case report | Frontiers in Oncology | Durable response with pyrotinib and metronomic vinorelbine in HER2+ breast cancer with leptomeningeal disease |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Case report | BMJ Case Reports | Receptor conversion and vocal cord paralysis in a metastatic breast cancer patient |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-HER2 antibody linked to the cytotoxic maytansinoid DM1) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no structured toxicity data available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | ADCs with cytotoxic payloads generally warrant cytotoxic drug handling precautions; please confirm against the package insert |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by L1-level evidence (a completed Phase 3 trial, multiple ASCO guidelines, and mechanistic consistency), but it represents a biomarker subgroup of T-DM1's existing on-label HER2+ population rather than a genuinely novel indication. Critical safety and regulatory documentation remain missing, which prevents full sign-off.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph warnings and contraindications (Blocking data gap, DG001)
- Verified mechanism of action data from DrugBank (DG002)
- Confirmation of current Canada marketing authorization status and DIN(s), since this pack shows 0 licenses
- Clinical/regulatory clarification on whether PR+ status requires any label distinction from the standard HER2+ indication, or whether this should be treated as routine on-label use rather than a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

