---
layout: default
title: Trabectedin
parent: High Evidence (L1-L2)
nav_order: 786
evidence_level: L2
indication_count: 1
---

# Trabectedin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Trabectedin: From Soft Tissue Sarcoma/Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin is a marine-derived DNA-binding cytotoxic agent, approved in Europe for second-line soft tissue sarcoma and (in combination with pegylated liposomal doxorubicin) platinum-sensitive relapsed ovarian cancer.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Soft tissue sarcoma (2nd line) / platinum-sensitive relapsed ovarian cancer (EU-approved; not currently marketed in Canada — per evidence pack literature) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data (DrugBank `original_moa`) is currently a data gap. However, the evidence pack's mechanistic analysis indicates that Trabectedin binds the DNA minor groove and interferes with transcription-coupled nucleotide excision repair (TC-NER) and homologous recombination (HR) pathways — a mechanism with well-documented selective cytotoxicity against BRCA1/2-deficient, HR-deficient tumors.

Trabectedin's existing approved use in platinum-sensitive relapsed ovarian cancer already exploits this HR-deficiency selectivity. Breast cancer — particularly BRCA1/2-mutated and triple-negative subtypes — shares substantial HR-deficient biology with ovarian cancer, providing a biologically continuous rationale for extrapolation from the approved indication to breast cancer.

Multiple Phase 2 clinical trials and an exploratory biomarker analysis of the pivotal Phase 3 OVA-301 trial support this link: BRCA1/XPG mutation status predicts response to trabectedin-containing regimens, and this predictive relationship has been directly tested in BRCA1/2-mutated metastatic breast cancer populations. This constitutes a mechanistically grounded, biomarker-supported repurposing hypothesis rather than a purely computational signal — though breast-cancer-specific confirmatory data remain limited (small sample sizes, no completed Phase 3 in breast cancer).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Evaluated olaparib maintenance therapy after response to trabectedin + pegylated liposomal doxorubicin (PLD) induction in recurrent ovarian carcinoma; supports the HR-deficiency/BRCA-selective activity underlying the breast cancer extrapolation, though small N and not a direct breast cancer study. |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, multicenter, placebo-controlled, sequential-design study assessing trabectedin's effect on QT/QTc interval in participants with advanced solid tumor malignancies at therapeutic dose — the largest completed single trial in this evidence set. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | RCT (Phase 2) | Clinical Breast Cancer | Multicenter randomized Phase II study comparing two trabectedin dosing regimens as single-agent therapy in advanced breast cancer after anthracycline/taxane failure. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | RCT (Phase 2) | Clinical Breast Cancer | Phase 2 study of trabectedin (1.3 mg/m² q3w) in HR-positive, HER2-negative advanced breast cancer, stratified by XPG gene expression as a predictive biomarker. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 Trial | Annals of Oncology | International first-in-class Phase II trial evaluating trabectedin efficacy/safety specifically in germline BRCA1/2-mutated metastatic breast cancer. |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Phase 3 Exploratory Analysis | Annals of Oncology | Exploratory analysis of the pivotal Phase 3 OVA-301 trial: BRCA1 and XPG mutation status associated with response rate, PFS, and OS to trabectedin + PLD — biomarker basis for extending to BRCA-mutated breast cancer. |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews trabectedin's mechanism (transcription regulation, tumor-associated macrophage modulation) and its potential role in breast cancer treatment. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | Reviews trabectedin as a chemotherapy option specifically for BRCA-deficient patients, spanning its approved and investigational uses. |
| [38863768](https://pubmed.ncbi.nlm.nih.gov/38863768/) | 2024 | Review | Drug Design, Development and Therapy | Discusses trabectedin's continued role in ovarian cancer treatment amid PARPi resistance, informing HR-deficiency-based extrapolation logic. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Trabectedin depletes immunosuppressive myeloid cells and enhances IL-12-induced NK-cell cytotoxicity in triple-negative breast cancer models. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Demonstrates diverse apoptosis induction by trabectedin in MCF-7 (HER2-/ER+) vs. MDA-MB-453 (HER2+/ER-) breast cancer cell lines. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | European Cytokine Network | Shows anti-angiogenic effects of trabectedin on HUVECs and breast cancer cell lines via modulation of angiogenic cytokine profiles. |

---

## Canada Market Information

Trabectedin is **not currently marketed in Canada** — 0 DINs are on record, and no license entries are available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA minor-groove binder / DNA-repair pathway interferent; marine-derived alkaloid) |
| Myelosuppression Risk | High — literature reports grade 3–4 neutropenia in ~50% and thrombocytopenia in ~20% of patients treated with trabectedin |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests (hepatotoxicity reported alongside hematologic toxicity), renal function |
| Handling Protection | Must follow standard cytotoxic/antineoplastic drug handling precautions (IV infusion agent) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 2 breast-cancer-specific trials, a Phase 3 biomarker exploratory analysis, and a mechanistically coherent HR-deficiency rationale support an L2 evidence level — sufficient to advance cautiously, but not to a full "Go," given the absence of a completed confirmatory trial with breast cancer as the primary endpoint and the blocking safety data gap (TFDA/Health Canada label warnings and contraindications not yet available).

**To proceed, the following is needed:**
- Health Canada / regulatory label data — key warnings, contraindications, and DDI profile (currently blocking, DG001)
- Structured mechanism-of-action data from DrugBank (DG002)
- Confirmation of route/formulation compatibility for a Canadian regulatory pathway (currently no licenses on file)
- A larger confirmatory trial (ideally BRCA1/2-mutated or HR-deficient breast cancer population) to validate the Phase 2 signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

