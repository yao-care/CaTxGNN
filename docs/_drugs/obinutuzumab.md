---
layout: default
title: Obinutuzumab
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Obinutuzumab: From an Unrecorded Original Indication to Pre-germinal Center CLL/SLL (with Follicular Lymphoma as the Best-Supported Candidate)

## One-Sentence Summary

Obinutuzumab is a glycoengineered type II anti-CD20 antibody marketed in Canada as GAZYVA. The Evidence Pack does not record its original indications.
The top-ranked TxGNN prediction, **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)**, has **no trials or publications** in the pack (Hold).
The third-ranked prediction, **follicular lymphoma**, is far better supported, with **50 clinical trials** and **19 publications** (Proceed with Guardrails).

---

## Quick Overview

| Item | Rank 1 (primary) | Rank 3 (best supported) |
|------|------|------|
| Original Indication | Not recorded in the supplied data | Not recorded in the supplied data |
| Predicted New Indication | Pregerminal center CLL/SLL | Follicular lymphoma |
| TxGNN Prediction Score | 99.21% | 99.18% |
| Evidence Level | L5 | L1 |
| Canada Market Status | ✓ Marketed | ✓ Marketed |
| Number of DINs | 1 | 1 |
| Recommended Decision | Hold | Proceed with Guardrails |

Rank 2 (IGHV-mutated CLL/SLL) has the same score (99.21%), L5 evidence and a Hold decision. Its identical score suggests it is inherited from the parent CLL/SLL node and is not subtype-specific.

---

## Why is This Prediction Reasonable?

Obinutuzumab is a glycoengineered type II anti-CD20 monoclonal antibody. It binds CD20 and acts through enhanced direct cell death, antibody-dependent cellular cytotoxicity and phagocytosis. Detailed mechanism of action data is not recorded in the pack, so this description rests on the literature abstracts.

CLL/SLL cells express CD20, so a CD20-targeting antibody is a plausible fit. The high TxGNN score (0.992) agrees with this. However, no trials or publications for this subtype are in the pack. The record should also be checked against the current label, because CLL is probably already an approved use rather than a repurposing.

Follicular lymphoma B cells also uniformly express CD20, which gives a coherent mechanistic basis for that prediction. One trial abstract in the pack (NCT02877550) also states that obinutuzumab has been approved in combination with chlorambucil for previously untreated CLL, which supports the on-label concern above. As with CLL, follicular lymphoma is likely on-label, so it should be handled as **label confirmation** and not as novel repurposing.

---

## Clinical Trial Evidence

No related clinical trials are registered for the rank 1 prediction (pregerminal center CLL/SLL) in the supplied data.

For **follicular lymphoma** (rank 3), 10 of the 50 trials in the pack are shown below, selected for relevance and phase.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | Obinutuzumab plus chemotherapy vs rituximab plus chemotherapy, with maintenance, in untreated advanced indolent NHL (GALLIUM) |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine vs bendamustine plus obinutuzumab (with obinutuzumab maintenance) in rituximab-refractory indolent NHL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | Local radiotherapy alone vs radiotherapy plus obinutuzumab in early-stage follicular lymphoma (GAZEBO) |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Recruiting | 780 | Zanubrutinib plus obinutuzumab vs lenalidomide plus rituximab in relapsed/refractory follicular or marginal zone lymphoma |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | Zanubrutinib plus obinutuzumab vs obinutuzumab alone in relapsed/refractory follicular lymphoma |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Completed | 96 | Obinutuzumab plus lenalidomide in previously untreated follicular lymphoma (direct efficacy evidence) |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Short-duration (about 90-minute) obinutuzumab infusion with chemotherapy in untreated advanced follicular lymphoma; supports safety and feasibility |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A | Completed | 299 | Non-interventional real-world study of obinutuzumab in untreated advanced follicular lymphoma |
| [NCT02689869](https://clinicaltrials.gov/study/NCT02689869) | Phase 2 | Unknown | 98 | Chemotherapy-free ibrutinib plus obinutuzumab in untreated high-tumour-burden follicular lymphoma |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Recruiting | 40 | Obinutuzumab, ibrutinib and venetoclax triplet in untreated follicular lymphoma |

The rationale text in the pack says the shown trials include no Phase 3 registry entry. The full 50-trial list in fact contains two completed Phase 3 trials (NCT01332968 and NCT01059630), which is why L1 is supported.

---

## Literature Evidence

No related literature is available for the rank 1 prediction in the supplied data.

For **follicular lymphoma** (rank 3), 10 of the 19 publications are shown.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | N Engl J Med | Rituximab-based vs obinutuzumab-based chemotherapy in previously untreated advanced follicular lymphoma |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM analysis: obinutuzumab prolonged PFS vs rituximab; report focuses on the effect of the chemotherapy backbone |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | Final GALLIUM analysis in untreated follicular or marginal zone lymphoma |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD: zanubrutinib plus obinutuzumab vs obinutuzumab alone in relapsed/refractory follicular lymphoma |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Phase 2 single-arm trial | Lancet Haematol | GALEN: obinutuzumab plus lenalidomide in relapsed/refractory follicular lymphoma |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Review of obinutuzumab in rituximab-refractory or -relapsed follicular lymphoma (GADOLIN; PFS prolonged) |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Obinutuzumab alone and in combination for follicular lymphoma |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Rapid review | Front Pharmacol | Efficacy, safety and cost-effectiveness of obinutuzumab in follicular lymphoma |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Review | Drugs Today | Obinutuzumab as a new-generation anti-CD20 antibody in follicular lymphoma |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | Comprehensive review of follicular lymphoma management |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2434806 | GAZYVA | Not recorded | Not recorded |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold for pregerminal center CLL/SLL and IGHV-mutated CLL/SLL; Proceed with Guardrails for follicular lymphoma**

**Rationale:**
- The two CLL/SLL predictions rest on model score and mechanism only (L5, no trials or literature), and the second appears to be inherited from the parent node.
- Follicular lymphoma has L1 support: two completed Phase 3 trials (GALLIUM and the rituximab-refractory bendamustine study), multiple randomized and single-arm Phase 2 studies, and RCT publications. It is probably already on-label, so the guardrail is to treat it as label confirmation and not as new repurposing.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications, dosage form), which is currently missing and blocks safety screening.
- Mechanism of action and original indication data from DrugBank.
- Confirmation of the current Canadian label for follicular lymphoma and CLL/SLL.
- Subtype-specific evidence for the IGHV-mutated and pregerminal center CLL/SLL predictions.
- Review of the full 50-trial and 19-publication lists, including the many trials and papers still marked as pending relevance grading.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

