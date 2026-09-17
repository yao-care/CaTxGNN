---
layout: default
title: Ribociclib
parent: Moderate Evidence (L3-L4)
nav_order: 676
evidence_level: L4
indication_count: 4
---

# Ribociclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Ribociclib: From HR+/HER2- Metastatic Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Ribociclib (DrugBank DB11730) is a CDK4/6 inhibitor whose established use, as reflected throughout the supporting literature, is HR+/HER2-negative metastatic breast cancer. The TxGNN model predicts potential activity in **Myeloid Leukemia**, but this candidate is currently supported by only **3 publications** and **0 clinical trials**, with the underlying evidence pointing in conflicting directions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- Metastatic Breast Cancer (established from literature context; not confirmed via a formal regulatory license record — see Canada Market Information below) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ribociclib is not available in this evidence pack (`original_moa` is a data gap). Based on the literature evidence collected, ribociclib is a CDK4/6 inhibitor used in combination with endocrine therapy for HR+/HER2-negative metastatic breast cancer, and CDK4/6 also plays a role in cell-cycle regulation of myeloid leukemia cells.

The mechanistic case is mixed, not confirmatory. One preclinical study (PMID 32560251) suggests CDK4/6 inhibitors may help reverse pharmacokinetic drug resistance in acute myeloid leukemia (AML) cells — a potential *treatment* rationale. However, a second report (PMID 30575100) describes AML with eosinophilia arising **after** CDK4/6 inhibitor treatment for breast cancer, i.e., a possible *adverse, leukemia-inducing* signal rather than therapeutic benefit. These two findings point in opposite directions, and a third retrieved paper (PMID 41641105, a vulvar/breast adenocarcinoma case report) is unrelated to myeloid leukemia and was excluded from the mechanistic rationale.

Because of this contradictory evidence base, the prediction should be treated as an early-stage signal (L4: preclinical/case-report level) rather than a validated therapeutic hypothesis. No clinical trials of ribociclib in myeloid leukemia have been identified to date.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ribociclib in myeloid leukemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/Review | Cancers | CDK4/6 inhibitors may help overcome pharmacokinetic drug resistance (ABCB1/ABCG2 overexpression) in AML cells — a potential therapeutic mechanism |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case Report | American Journal of Hematology | AML with eosinophilia observed after CDK4/6 inhibitor treatment, linked to underlying clonal hematopoiesis of indeterminate potential — an adverse signal, not a treatment finding |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case Report | Frontiers in Oncology | Case of concurrent vulvar and breast adenocarcinoma; not related to myeloid leukemia and considered not directly relevant to this indication |

---

## Canada Market Information

Ribociclib is currently **not marketed** in Canada/Taiwan under this dataset — no licensed products (DINs) are on record (`total_licenses: 0`).

---

## Cytotoxicity

Ribociclib's original indication (per literature context) is oncologic (HR+/HER2- metastatic breast cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | High — hematological toxicity (neutropenia, leukopenia, thrombocytopenia) is repeatedly documented in the supporting literature (e.g., PMID 38753541, PMID 29147869, PMID 34248473), and is described as the class's dose-limiting toxicity |
| Emetogenicity Classification | Not specified in available data — please refer to product labeling |
| Monitoring Items | CBC with differential (given consistently reported myelosuppression); liver function and QT interval monitoring are commonly cited for this drug class but are not directly sourced in this evidence pack |
| Handling Protection | Specific handling data not provided — follow institutional cytotoxic/oncology drug handling precautions and refer to the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all currently data gaps — the DDI lookup returned no results, and TFDA/label warning data has not yet been retrieved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic evidence for ribociclib in myeloid leukemia is contradictory — one preclinical study suggests a therapeutic effect while a case report describes CDK4/6-inhibitor-associated AML as an adverse event — and no clinical trials currently exist for this indication. Combined with the absence of a Canadian/Taiwan market presence and missing safety labeling data, the evidence does not yet support advancing beyond a Hold decision.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (currently a Blocking data gap — required before any safety (S1) review)
- Confirmed mechanism of action data from DrugBank (High-priority data gap)
- Resolution of the conflicting mechanistic signal (therapeutic vs. leukemia-inducing) through further preclinical or translational study
- At least one prospective clinical trial or controlled study specifically evaluating ribociclib in myeloid leukemia

*Note: Two additional TxGNN-predicted indications (rank 3 "marcothrombocytopenia with mitral valve insufficiency" and rank 4 "hereditary thrombocytopenia with normal platelets") were also generated but carry L5 evidence (no literature or trials, and rank 3's disease name is likely a misspelling of "macrothrombocytopenia") — these are not addressed further here. Rank 2 ("thrombocytopenia") was also excluded from this report, as its own rationale indicates the TxGNN score reflects a known adverse-effect association (CDK4/6-inhibitor-induced myelosuppression) rather than a genuine treatment signal.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

