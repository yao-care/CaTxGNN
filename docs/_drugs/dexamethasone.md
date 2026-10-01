---
layout: default
title: Dexamethasone
parent: Model Prediction Only (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Systemic Glucocorticoid Therapy to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent systemic glucocorticoid marketed in Canada under 20 DINs. The Health Canada records supplied contain no approved-indication text.
The TxGNN model predicts it may be effective for **alopecia areata**.
No registered clinical trial targets this indication (12 retrieved, all unrelated), but **about 13 of 20 retrieved publications** directly study dexamethasone in alopecia areata, including **1 RCT** and **1 systematic review / network meta-analysis**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence records (systemic glucocorticoid class) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (conservative call: one published RCT of unspecified phase, plus cohort data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for dexamethasone is not available in the input. Based on known information, dexamethasone belongs to the potent systemic glucocorticoid class. Its anti-inflammatory and immunosuppressive effects are well established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is a T-cell-mediated autoimmune attack on hair follicles after the follicle's immune privilege collapses. A systemic glucocorticoid can suppress this inflammation. Oral or IV "mini-pulse" dexamethasone regimens are used in practice to induce regrowth, which is why the literature contains many pulse-therapy studies in adults and children.

Guardrails apply. Relapse after tapering is common, and long-term systemic steroid toxicity is a concern. JAK inhibitors are an alternative for eligible patients, but several papers note they are unaffordable or unavailable for some patients, which keeps steroid pulses relevant.

---

## Clinical Trial Evidence

Twelve registered trials were retrieved, but **none studies alopecia areata**. Dexamethasone appears only as a backbone or supportive agent in oncology regimens, or as a diagnostic test. They give no direct support for this prediction. Ten are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Unknown | 74 | Placebo-controlled test of prophylactic dexamethasone for regorafenib-related fatigue (indication unrelated) |
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | Unknown | 118 | Pomalidomide + dexamethasone ± ixazomib in relapsed myeloma (dexamethasone as backbone) |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | Completed | 56 | Durvalumab + lenalidomide ± dexamethasone in newly diagnosed myeloma |
| [NCT02773030](https://clinicaltrials.gov/study/NCT02773030) | Phase 1/2 | Active, not recruiting | 466 | CC-220 with dexamethasone combinations in multiple myeloma |
| [NCT05408026](https://clinicaltrials.gov/study/NCT05408026) | Phase 1/2 | Withdrawn | 0 | Pomalidomide, bortezomib, low-dose dexamethasone and daratumumab in relapsed myeloma |
| [NCT01055496](https://clinicaltrials.gov/study/NCT01055496) | Phase 1 | Completed | 103 | Inotuzumab ozogamicin with R-CVP or R-GDP (dexamethasone in R-GDP) in lymphoma |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Steroid metabolome and bone strength in mild autonomous cortisol secretion (dexamethasone suppression test is a diagnostic criterion) |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | Completed | 24 | Cabazitaxel in temozolomide-refractory glioblastoma (dexamethasone likely only a comedication) |
| [NCT00282087](https://clinicaltrials.gov/study/NCT00282087) | Phase 2 | Completed | 47 | Adjuvant gemcitabine/docetaxel then doxorubicin in uterine leiomyosarcoma (unrelated) |
| [NCT01607554](https://clinicaltrials.gov/study/NCT01607554) | Phase 1/2 | Terminated | 2 | Irinotecan in NSCLC with high ISG15 expression (unrelated) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Open-label randomized comparison of low-dose oral dexamethasone mini-pulse vs. DPCP contact sensitisation in 30 children with severe non-progressive alopecia areata |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic review / network meta-analysis | Arch Dermatol Res | Compares systemic steroids, oral JAK inhibitors and contact immunotherapy for severe alopecia areata |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Reviews dosing regimens, administration and side effects of pulse corticosteroid therapy in children with alopecia areata |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective cohort | J Clin Med | Real-world effectiveness, safety and response factors of dexamethasone mini-pulse in alopecia areata |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Multicentre clinical study | Dermatologic Therapy | Oral dexamethasone mini-pulse in moderate to severe alopecia areata (design truncated in the source, to be verified) |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Cohort | Dermatologic Therapy | 73 children with severe alopecia areata: 1-day vs. 3-day IV dexamethasone pulses plus topical clobetasol |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort (long-term follow-up) | Dermatologic Therapy | 65 children treated with monthly oral dexamethasone pulses plus topical steroid, median follow-up 96 months |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative study | Dermatology | Compares efficacy, relapse rate and side effects of three systemic corticosteroid modalities |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Case series | J Dermatol | 30 patients with extensive alopecia areata given 5 mg dexamethasone on two consecutive days weekly |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case report with focused review | J Dermatol Treat | Durable remission of severe alopecia areata with oral mini-pulse in a patient for whom JAK inhibitors were unsuitable |

---

## Canada Market Information

Twenty DINs are on record. The first five are shown below. The supplied records do not include dosage form or approved-indication text.

| DIN | Product Name |
|---------|------|
| 02204266 | DEXAMETHASONE-OMEGA |
| 02261081 | APO-DEXAMETHASONE |
| 02250055 | APO-DEXAMETHASONE |
| 01977547 | DEXAMETHASONE SODIUM PHOSPHATE INJECTION, USP |
| 00664227 | DEXAMETHASONE SODIUM PHOSPHATE INJ USP 4MG/ML |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the input.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction for alopecia areata is supported by a published RCT, a network meta-analysis and several cohort studies of dexamethasone pulse therapy. However, there is no registered trial in this indication, and the RCT is small and of unspecified phase. The other nine predicted indications (alopecia mucinosa, telogen effluvium, folliculitis decalvans, and others) have no supporting evidence and are rated L5 / Hold.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved-indication and dosage-form data for the Canadian licences
- Dexamethasone mechanism of action data (from DrugBank)
- Verification of the study design of PMID 36070222, and a quality appraisal of the RCT and network meta-analysis
- A plan for relapse after tapering and for monitoring long-term systemic steroid toxicity, with JAK inhibitors as the comparator alternative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

