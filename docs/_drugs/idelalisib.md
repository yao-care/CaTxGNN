---
layout: default
title: Idelalisib
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Idelalisib: predicted new indication Mantle cell lymphoma (evidence level L5). Approved use: CLL/SLL, follicular lymphoma and other B-cell neoplasms"
monitor_inn: "IDELALISIB"
predicted_indications: ["mantle cell lymphoma", "Hodgkins lymphoma", "lymphoma, non-Hodgkin, familial", "myeloid leukemia", "chronic myelogenous leukemia, BCR-ABL1 positive", "small intestinal Burkitt lymphoma", "colon adenocarcinoma"]
---

# Idelalisib
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

# Idelalisib: From Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib (Zydelig) is an oral targeted drug originally used for B-cell blood cancers such as chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) and follicular lymphoma.
The TxGNN model predicts it may be effective for **Mantle Cell Lymphoma (MCL)**.
Support so far is limited to **5 early-phase clinical trials** and **20 publications**, mostly reviews and laboratory studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLL/SLL, follicular lymphoma and other B-cell neoplasms (taken from the TxGNN knowledge graph, because the Canadian licence records list no indication text) |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 (no Phase 3 or randomized efficacy data in MCL; evidence consists of early-phase trials, reviews and preclinical work) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. The published literature describes idelalisib as the first-in-class inhibitor of PI3Kδ (phosphatidylinositol 3-kinase delta). This enzyme sits in the B-cell receptor signalling pathway and supports the survival and growth of malignant B cells.

MCL is a B-cell non-Hodgkin lymphoma. Reviews and laboratory studies indicate that it relies on B-cell receptor and PI3K signalling. This is the same biology that underlies idelalisib's activity in CLL/SLL and follicular lymphoma, and it explains why the model ranks MCL highly.

The picture is not entirely favourable:
- Laboratory work reports that MCL cells can show **intrinsic resistance** to idelalisib.
- Preclinical studies suggest the resistance may be overcome by combinations. Examples are a P300/CBP inhibitor (A-485), the CDK4/6 inhibitor palbociclib, and propolis, which restores sensitivity in resistant cells by inducing CBX5-mediated ferroptosis.
- Another study found that idelalisib suppresses translation-regulatory pathways in MCL cells.

Overall, the mechanistic rationale is plausible, but no randomized efficacy evidence in MCL has been provided.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 / randomized Phase 2 | Completed | 106 | Lenalidomide with or without idelalisib in relapsed/refractory MCL. This is the most MCL-specific trial; no results are provided in the compiled data. |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Safety and activity of idelalisib with chemotherapy, immunomodulatory agents or anti-CD20 antibody in relapsed/refractory indolent lymphoma, MCL or CLL. MCL is only a subset of the population. |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib plus idelalisib in relapsed/refractory blood cancers, including MCL. Early termination limits interpretation. |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | Dose escalation of BCL201 plus idelalisib in follicular lymphoma and MCL, focused on safety and tolerability. |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as maintenance after allogeneic stem cell transplant in B-cell malignancies. Not MCL-specific. |

---

## Literature Evidence

No randomized controlled trials in MCL were found. The most relevant items are listed below, with reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33154951](https://pubmed.ncbi.nlm.nih.gov/33154951/) | 2020 | Review | Frontiers in Oncology | Mechanisms of resistance to BTK and PI3K inhibitors (ibrutinib, idelalisib) in B-cell malignancies, including MCL |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | British Journal of Haematology | Current regimens and novel agents for MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opinion on Pharmacotherapy | Standard and emerging treatment options for MCL |
| [26841011](https://pubmed.ncbi.nlm.nih.gov/26841011/) | 2016 | Review | Cancer Journal | Targeting the PI3K pathway with idelalisib in non-Hodgkin lymphoma |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Incidence and practical management of toxicity with ibrutinib and idelalisib |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clinical Cancer Research | Idelalisib inhibits cell growth in MCL by suppressing translation-regulatory mechanisms |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacologica Sinica | P300/CBP inhibitor A-485 overcomes idelalisib resistance in MCL cells in vitro and in vivo |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances the antitumour effect of palbociclib via PLK1 in B-cell lymphoma (DLBCL and MCL) |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ-inhibitor resistance in MCL; propolis restores sensitivity |
| [36297673](https://pubmed.ncbi.nlm.nih.gov/36297673/) | 2022 | Preclinical | Pharmaceutics | A ROR1 inhibitor, alone or combined with idelalisib and other agents, induces apoptosis in MCL cells |

---

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|-----------|
| 02438801 | ZYDELIG | Valid (single-ingredient) |
| 02438798 | ZYDELIG | Valid (single-ingredient) |

Dosage form, manufacturer and approved indication text are not listed in the Canadian licence records compiled for this report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ inhibitor); not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Trial-reported safety signal**: Several Phase 2/3 idelalisib trials in front-line CLL and early-line indolent lymphoma were stopped after a monitoring committee saw increased deaths and serious adverse events with idelalisib combinations. Colitis and diarrhea are also recognized with this drug, and one trial is dedicated to studying the mechanism.
- **Drug interactions**: The interaction screen returned 100 interacting drugs. Examples are below.
  - **Major**: loperamide, triamcinolone, budesonide, eliglustat.
  - **Moderate**: clarithromycin, dexamethasone, hydrocortisone, betamethasone, bupropion, aprepitant, doxycycline, minocycline, pioglitazone, acarbose, saxagliptin, chenodeoxycholic acid, eluxadoline.

Warnings and contraindications from the Canadian package insert were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale for MCL is reasonable. However, the clinical evidence consists only of Phase 1 and early Phase 2 studies, several of them terminated and with MCL as a minor subset. There is no randomized efficacy data, laboratory work shows intrinsic resistance, and idelalisib carries a serious toxicity history. These points together do not justify moving forward yet.

**To proceed, the following is needed:**
- MCL-specific efficacy results, such as response rates and progression-free survival, from NCT01838434 and any other MCL-focused studies.
- The Canadian package insert warnings and contraindications, to complete the safety screen.
- Detailed mechanism-of-action data, with attention to the reported resistance in MCL and the combination strategies that might overcome it.
- A comparison against existing MCL therapies, such as BTK inhibitors, to define any unmet need for idelalisib.
- A risk-management plan for hepatic, gastrointestinal, pulmonary, infectious and cutaneous toxicities and for drug interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

