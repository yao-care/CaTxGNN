---
layout: default
title: Daunorubicin
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: From Anthracycline Chemotherapy to Hodgkin Lymphoma

## One-Sentence Summary

Daunorubicin is an anthracycline chemotherapy drug that is marketed in Canada in three authorizations, including a liposomal combination product.
The TxGNN model predicts it may be effective for **Hodgkin lymphoma** (score 99.81%).
The pack lists **50 clinical trials** and **20 publications** for this indication, but none of the trials is confirmed to use daunorubicin; they mostly test doxorubicin-based regimens (ABVD/AVD).
The only daunorubicin-specific item is a small 1997 early study of liposomal daunorubicin in relapsed/refractory lymphoma.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hodgkin lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 (class-level evidence only; no drug-specific Phase 2/3 trial) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

The Canadian authorization records in the pack contain no approved-indication text, so the original labelled indication could not be confirmed.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Based on known information, daunorubicin belongs to the anthracycline class. Anthracyclines act by inhibiting topoisomerase II and intercalating into DNA. This is the established mechanism behind anthracycline-containing Hodgkin regimens such as ABVD and AVD.

Hodgkin lymphoma is routinely treated with anthracycline-based combination chemotherapy. That gives the model's prediction a plausible class-level basis.

The gap is that the supporting trials use **doxorubicin**, not daunorubicin. They therefore show that the class works in this disease, not that daunorubicin does. The trial titles in the pack are truncated, so daunorubicin use in individual regimens cannot be fully ruled out.

## Clinical Trial Evidence

The table lists the 10 most Hodgkin-relevant of the 50 trials. All test doxorubicin-containing (or other) regimens rather than daunorubicin.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04624984](https://clinicaltrials.gov/study/NCT04624984) | Phase 2 | Unknown | 42 | PD-1 inhibitor ± GVD (gemcitabine, vinorelbine, liposomal doxorubicin) in relapsed/refractory classical Hodgkin lymphoma |
| [NCT00002987](https://clinicaltrials.gov/study/NCT00002987) | Phase 3 | Unknown | 400 | Short neoadjuvant chemotherapy plus involved-field radiotherapy vs mantle radiotherapy in early-stage Hodgkin disease; anthracycline not confirmed as daunorubicin |
| [NCT03527628](https://clinicaltrials.gov/study/NCT03527628) | Phase 2 | Unknown | 220 | ACVD (doxorubicin-based) plus brentuximab vedotin in advanced Hodgkin lymphoma with positive interim PET |
| [NCT02661503](https://clinicaltrials.gov/study/NCT02661503) | Phase 3 | Active, not recruiting | 1500 | BrECADD vs escalated BEACOPP in first-line advanced Hodgkin lymphoma |
| [NCT03004833](https://clinicaltrials.gov/study/NCT03004833) | Phase 2 | Completed | 110 | Nivolumab plus AVD in early-stage unfavorable classical Hodgkin lymphoma |
| [NCT03907488](https://clinicaltrials.gov/study/NCT03907488) | Phase 3 | Active, not recruiting | 994 | Nivolumab + AVD vs brentuximab vedotin + AVD in newly diagnosed advanced classical Hodgkin lymphoma |
| [NCT06164275](https://clinicaltrials.gov/study/NCT06164275) | Phase 2 | Active, not recruiting | 30 | Pembrolizumab followed by limited AVD chemotherapy, including elderly patients |
| [NCT03755804](https://clinicaltrials.gov/study/NCT03755804) | Phase 2 | Active, not recruiting | 232 | Risk- and response-adapted chemotherapy (doxorubicin-containing) in pediatric classical Hodgkin lymphoma |
| [NCT00003389](https://clinicaltrials.gov/study/NCT00003389) | Phase 3 | Completed | 854 | ABVD vs Stanford V ± radiation in locally extensive and advanced Hodgkin's disease |
| [NCT04685616](https://clinicaltrials.gov/study/NCT04685616) | Phase 3 | Recruiting | 1042 | ABVD vs A2VD ± radiotherapy, PET-response-adapted, in stage IA/IIA Hodgkin lymphoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT | N Engl J Med | Nivolumab + AVD in advanced-stage classic Hodgkin lymphoma (doxorubicin backbone) |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT follow-up | N Engl J Med | Long-term follow-up of brentuximab vedotin + AVD vs ABVD in stage III/IV disease |
| [27332902](https://pubmed.ncbi.nlm.nih.gov/27332902/) | 2016 | RCT | N Engl J Med | Interim PET-CT-adapted treatment in advanced Hodgkin lymphoma (anthracycline backbone) |
| [20818855](https://pubmed.ncbi.nlm.nih.gov/20818855/) | 2010 | RCT | N Engl J Med | Reduced treatment intensity in early-stage favorable Hodgkin lymphoma |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Early clinical study | Invest New Drugs | Liposomal daunorubicin (DaunoXome) in 19 relapsed/refractory lymphoma patients: at the higher dose, 1 complete and 2 partial responses, with mild non-haematological toxicity and no clinical cardiac deterioration. This is the only daunorubicin-specific clinical item |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Role of radiotherapy in risk- and response-adapted treatment of early-stage Hodgkin lymphoma |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan To Kagaku Ryoho | Overview of haematologic tumours; notes ABVD as first-line chemotherapy for advanced Hodgkin lymphoma |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Review | Cancer Treat Rep | Roles and limitations of daunorubicin and adriamycin in cancer treatment (no abstract available) |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective cohort | Sci Rep | Predictive value of interim FDG-PET/CT in 245 ABVD-treated patients |
| [24220522](https://pubmed.ncbi.nlm.nih.gov/24220522/) | 2013 | Review | Br J Hosp Med | Classical Hodgkin lymphoma: past, present and future perspectives |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 1926683 | CERUBIDINE |
| 2539209 | DAUNORUBICIN HYDROCHLORIDE INJECTION |
| 2515490 | VYXEOS |

Dosage form and approved-indication text are not populated in the source records for these authorizations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class) |
| Myelosuppression Risk | High (class characteristic) |
| Emetogenicity Classification | Moderate (class-based estimate) |
| Monitoring Items | CBC with differential, cardiac function (e.g., LVEF, given cumulative-dose cardiotoxicity typical of anthracyclines), liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

These entries are class-level; the pack has no drug-specific toxicity data. Please refer to the package insert warnings and precautions for authoritative details.

## Safety Considerations

Please refer to the package insert for safety information. The pack has no Canadian warnings or contraindications, and the drug-interaction query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is supported only by class-level anthracycline evidence, and none of the listed trials is confirmed to use daunorubicin. Doxorubicin-based ABVD/AVD is already the established anthracycline backbone in Hodgkin lymphoma. Canadian safety information is also missing, so the candidate cannot yet pass safety screening. It is best treated as a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications for the three authorizations
- Drug-specific evidence for daunorubicin in Hodgkin lymphoma, such as regimen-level review of the trials above or a dedicated study
- Detailed mechanism of action data from DrugBank
- A rationale for choosing daunorubicin over the doxorubicin already standard in Hodgkin regimens, including a cumulative-dose cardiotoxicity plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

