---
layout: default
title: Brentuximab Vedotin
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brentuximab Vedotin: predicted new indication Follicular lymphoma (evidence level L5). Approved use: Hodgkin lymphoma (classic Hodgkin lymphoma and related subtypes)"
monitor_inn: "BRENTUXIMAB VEDOTIN"
predicted_indications: ["follicular lymphoma", "myeloid leukemia", "acute lymphoblastic/lymphocytic leukemia", "B-cell neoplasm", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "Richter syndrome", "mantle cell lymphoma", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction"]
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin is a CD30-targeted antibody-drug conjugate, originally used to treat Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **follicular lymphoma**, but only **1 on-indication trial** (still recruiting, no results) and **no direct follicular lymphoma publications** currently support this direction.
Of the ten predicted indications, **B-cell neoplasm** (mainly CD30-positive diffuse large B-cell lymphoma) has the strongest supporting evidence and is also discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma (classic Hodgkin lymphoma and related subtypes) |
| Predicted New Indication | Follicular lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (by the compiled data's scoring; see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (research question only) |

*Note: The L2 label rests on a single Phase 2 trial that is still recruiting with no results. No completed Phase 2 or 3 RCT exists for follicular lymphoma, so the practical strength of evidence is weaker than the label suggests.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, brentuximab vedotin is an antibody-drug conjugate: an anti-CD30 antibody linked to the cytotoxic agent MMAE (vedotin). It is established in CD30-positive lymphomas, and its efficacy in Hodgkin lymphoma is proven.

The mechanistic link to follicular lymphoma is **weak**. CD30 expression in follicular lymphoma is variable and usually low, so any benefit would likely be limited to CD30-positive cases or to bystander effects of the released payload. Much of the supporting literature concerns peripheral T-cell lymphoma, not follicular lymphoma.

Other predictions differ in strength:
- **B-cell neoplasm**: CD30 is expressed in a subset of B-cell lymphomas (some DLBCL, notably EBV-positive, and primary mediastinal B-cell lymphoma). Published phase 2 and combination data support activity in CD30-positive disease.
- **Myeloid leukemia**: CD30 is expressed in some myeloid neoplasms, but early-phase data are limited.
- **Acute lymphoblastic leukemia, chronic lymphocytic leukemia variants, mantle cell lymphoma, Richter syndrome, ganglioneuroblastoma and the congenital T-cell dysfunction syndrome**: little or no mechanistic or clinical support, so these remain on hold.

---

## Clinical Trial Evidence

Trials for the top prediction, follicular lymphoma:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | Brentuximab vedotin plus bendamustine in relapsed/refractory follicular lymphoma; directly on-indication, no results yet |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | Brentuximab vedotin plus rituximab, frontline, CD30+ and/or EBV+ lymphomas; mixed population |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomized rituximab and bendamustine with or without brentuximab vedotin in CD30+ DLBCL; limited by early termination |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Rituximab, brentuximab vedotin and bendamustine in post-transplant lymphoproliferative disorder; no data |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin, bendamustine and rituximab in CD30+ B-cell NHL; no data |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | Brentuximab vedotin plus pembrolizumab in peripheral T-cell lymphoma; no data |

Key trials for the better-supported **B-cell neoplasm** prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01421667](https://clinicaltrials.gov/study/NCT01421667) | Phase 2 | Completed | 176 | Relapsed/refractory NHL; activity seen in CD30-positive DLBCL |
| [NCT04404283](https://clinicaltrials.gov/study/NCT04404283) | Phase 3 | Active, not recruiting | 239 | Randomized, double-blind: brentuximab vedotin or placebo plus lenalidomide and rituximab in relapsed/refractory DLBCL |
| [NCT01994850](https://clinicaltrials.gov/study/NCT01994850) | Phase 1/2 | Completed | 32 | Front-line brentuximab vedotin with multi-agent chemotherapy in CD30+ PMBCL, DLBCL and grey zone lymphomas |
| [NCT04745949](https://clinicaltrials.gov/study/NCT04745949) | Phase 2 | Recruiting | 31 | Brentuximab vedotin and nivolumab, then with R-CHP, in untreated primary mediastinal large B-cell lymphoma |
| [NCT02086604](https://clinicaltrials.gov/study/NCT02086604) | Phase 1 | Completed | 37 | Brentuximab vedotin with lenalidomide in relapsed/refractory DLBCL |

---

## Literature Evidence

Follicular lymphoma has no direct treatment publications. The most relevant items are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Cohort (Phase 2) | Blood Advances | Brentuximab vedotin plus gemcitabine in relapsed/refractory peripheral T-cell lymphoma (not follicular) |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy in indolent non-Hodgkin lymphoma, including follicular lymphoma |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case report | Gulf Journal of Oncology | Grade I follicular lymphoma transformed to CD30+ anaplastic large cell lymphoma, with complete response to brentuximab vedotin and high-dose methotrexate |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Treatment approaches in common peripheral T-cell lymphoma subtypes |

For the B-cell neoplasm prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39772655](https://pubmed.ncbi.nlm.nih.gov/39772655/) | 2025 | Clinical trial | J Clin Oncol | Brentuximab vedotin plus lenalidomide and rituximab versus placebo plus lenalidomide and rituximab in relapsed/refractory DLBCL |
| [41367262](https://pubmed.ncbi.nlm.nih.gov/41367262/) | 2026 | Clinical trial | Future Oncology | Nivolumab plus brentuximab vedotin in relapsed/refractory DLBCL (CheckMate 436) |
| [37352266](https://pubmed.ncbi.nlm.nih.gov/37352266/) | 2023 | Clinical trial follow-up | Blood Advances | 3-year follow-up of nivolumab plus brentuximab vedotin in relapsed/refractory primary mediastinal large B-cell lymphoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02401347 | ADCETRIS | Not stated | Not stated in the compiled data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate (CD30-targeted antibody with MMAE cytotoxic payload) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; haematological parameters (CBC) and liver and renal function are generally monitored with cytotoxic agents |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for safety information.

**Drug Interactions**: A screening found 100 interacting drugs, all listed at Moderate level in the first 20 shown. These include antidiabetic agents (acarbose, metformin, pioglitazone, glimepiride, glipizide, chlorpropamide, acetohexamide, alogliptin), GLP-1 and SGLT2 agents (albiglutide, dulaglutide, exenatide, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), and others (bupropion, chenodeoxycholic acid, clarithromycin, clotrimazole, eliglustat). The clinical significance of each pair should be checked against the full interaction record before use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For follicular lymphoma, the mechanistic link is weak because CD30 expression is low, the only directly relevant trial is still recruiting without results, and no follicular lymphoma publications exist. Evidence is clearly stronger for CD30-positive B-cell lymphomas (especially DLBCL), which may be a better repurposing focus and could warrant "Proceed with Guardrails" with CD30-based patient selection.

**To proceed, the following is needed:**
- Results from NCT04587687 in relapsed/refractory follicular lymphoma
- CD30 expression data in follicular lymphoma, to define a selectable subgroup
- Mechanism of action data and package insert safety information (warnings, contraindications), which are currently missing
- Review of the 100 identified drug interactions
- Canadian indication and dosage form details for DIN 02401347
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

