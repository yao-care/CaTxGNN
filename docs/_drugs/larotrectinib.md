---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Larotrectinib
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

# Larotrectinib: From NTRK Fusion-Positive Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is a highly selective TRKA/B/C kinase inhibitor originally indicated for NTRK gene fusion-positive solid tumors, regardless of tissue origin. The TxGNN model predicts potential activity in **Multiple Endocrine Neoplasia (MEN)**, but this is currently supported by only **1 loosely related clinical trial** and **2 review/mechanistic publications**, none of which directly test larotrectinib in MEN patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTRK gene fusion-positive solid tumors (tissue-agnostic) |
| Predicted New Indication | Multiple Endocrine Neoplasia (MEN) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data (DrugBank MOA field) is not currently available for larotrectinib. Based on other information within the evidence pack, larotrectinib is described as a highly selective TRKA/B/C (tropomyosin receptor kinase) inhibitor, approved for solid tumors carrying an NTRK1/2/3 gene fusion, independent of the tumor's tissue of origin.

Multiple Endocrine Neoplasia (MEN), including MEN2 and its associated medullary thyroid carcinoma, is driven primarily by **RET** gene alterations rather than NTRK fusions. RET and NTRK are both receptor tyrosine kinases and are frequently discussed together in the kinase-inhibitor literature for thyroid malignancies, which likely explains why the knowledge graph places them near each other. However, this is an indirect, target-class-level association rather than a validated NTRK-driven mechanism in MEN.

The supporting literature (a general review of kinase inhibitors in advanced thyroid cancer, and a mechanistic paper on RET-inhibitor resistance in medullary thyroid carcinoma) does not identify NTRK fusions as a driver in MEN, nor does it study larotrectinib directly. The single associated clinical trial (MATCH, NCT02465060) is a large, tumor-agnostic basket trial matching many genotypes to many targeted drugs — it is not a dedicated larotrectinib-in-MEN study. Overall, the mechanistic link is plausible only as a "kinase inhibitor / thyroid tumor neighborhood" association, not a validated NTRK-MEN pathway.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | Molecular Analysis for Therapy Choice (MATCH) — a large multi-arm basket trial matching genomically defined targeted therapies to refractory advanced solid tumors, lymphomas, and myelomas; not a larotrectinib-specific MEN trial (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Reviews kinase inhibitor therapy for advanced thyroid cancer, including mutation-specific approvals; does not address NTRK fusions in MEN specifically. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Cohort/Mechanistic | NPJ Precision Oncology | Describes acquired RET-inhibitor resistance mechanisms in RET-driven medullary thyroid carcinoma (a MEN2-associated tumor); focused on RET, not NTRK/larotrectinib. |

## Canada Market Information

Larotrectinib is **not currently marketed in Canada** — no Drug Identification Numbers (DINs) are registered (0 licenses on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective TRKA/B/C kinase inhibitor) |
| Myelosuppression Risk | Low–moderate; thrombocytopenia is noted elsewhere in the evidence pack as a known adverse effect of larotrectinib per labeling, though not a primary dose-limiting toxicity |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with platelet count, liver function tests |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis linking larotrectinib to MEN is indirect (RET-driven disease vs. an NTRK-targeted drug), and available evidence consists of one non-specific basket trial and two publications that do not test larotrectinib in MEN patients. This does not meet the bar to advance beyond hypothesis generation.

**To proceed, the following is needed:**
- Confirmed DrugBank mechanism of action data (currently a blocking data gap, DG002)
- TFDA/Health Canada label warnings and contraindications (currently a blocking data gap, DG001)
- Evidence of NTRK fusion prevalence in MEN-associated tumors, to establish a genuine molecular rationale
- A dedicated clinical trial or case series testing larotrectinib specifically in NTRK-fusion-positive MEN patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

