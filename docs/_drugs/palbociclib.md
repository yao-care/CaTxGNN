---
layout: default
title: Palbociclib
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
monitor_inn: "Palbociclib"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
description: "Palbociclib: predicted new indication Top TxGNN rank: hyperthyroidism . Best-supported candidate: myeloid leukemia (hyperthyroidism) (evidence level L5). Approved use: Not recorded in the local data"
---

# Palbociclib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Palbociclib: Top TxGNN rank: hyperthyroidism (no evidence). Best-supported candidate: myeloid leukemia (hyperthyroidism)
{: .text-alpha }

## One-Sentence Summary

Palbociclib is a CDK4/6 inhibitor used in the treatment of hormone receptor-positive breast cancer. The TxGNN model's top-ranked prediction is **hyperthyroidism**, but that prediction has no supporting evidence.

The original indication below comes from background knowledge, because the Canadian license records compiled for this report contain no indication text.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Top TxGNN rank: hyperthyroidism (no evidence). Best-supported candidate: myeloid leukemia (hyperthyroidism) |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | Hyperthyroidism L5; myeloid leukemia L3 |
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hyperthyroidism: Hold. Myeloid leukemia: Proceed with Guardrails |

**Note on ranking:** TxGNN scores are all very high (≥ 0.99) across the top 10 predictions and do not separate plausible from implausible ones. The evidence review is what distinguishes them. The table below shows how each prediction fared.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Hyperthyroidism | 0.9944 | L5 | Hold. No trials or literature |
| 2 | Rheumatoid arthritis | 0.9936 | L4 | Research question. Plausible preclinical rationale and one case report |
| 3 | Thrombotic disease | 0.9932 | L5 | Hold. Literature shows thrombosis as an adverse event, not a benefit |
| 4 | Thyroid hormone resistance (THRB mutation) | 0.9930 | L5 | Hold. No evidence |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, palbociclib selectively inhibits CDK4 and CDK6, which blocks cell-cycle progression from the G1 to the S phase. Its efficacy in HR-positive breast cancer is established.

Preclinical studies show palbociclib acting synergistically with venetoclax plus azacitidine, overcoming venetoclax resistance, and working with LSD1 or menin inhibitors. A 2026 review noted that CDK4/6 inhibitor monotherapy trials in leukemia were disappointing, whereas combinations showed more promise.

**Rheumatoid arthritis (research question).** Synovial fibroblast proliferation depends on CDK6, which makes CDK4/6 inhibition biologically plausible. Animal models support this. No registered trials exist.

**Thrombotic disease.** The literature indicates that thromboembolism is a *safety signal* of CDK4/6 inhibitors. This is an adverse effect, not a therapeutic benefit, so the prediction should not be pursued.

**Other predictions** (hyperthyroidism, thyroid hormone resistance) have no clinical trials, no literature, and no plausible mechanistic link in the available data. Their high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence


| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02310243](https://clinicaltrials.gov/study/NCT02310243) | Phase 1/2 | Unknown | 50 | Palbociclib in MLL-rearranged acute leukemias (AML and ALL); dose-finding then efficacy. No results available |
| [NCT03132454](https://clinicaltrials.gov/study/NCT03132454) | Phase 1 | Active, not recruiting | 32 | Palbociclib alone and combined with sorafenib, decitabine, or dexamethasone in relapsed/refractory leukemia |
| [NCT05627232](https://clinicaltrials.gov/study/NCT05627232) | Phase 1 | Recruiting | 24 | Palbociclib pre-treatment followed by CPX-351 (Part 2) in relapsed/refractory AML. Combination design limits attribution |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Precision-oncology platform trial. Uninformative given 2 participants |

They cover breast cancer studies (NCT03355157, Phase 4, 130 participants; NCT02894398, Phase 2, 388 participants) and the NCI-MATCH basket trial ([NCT02465060](https://clinicaltrials.gov/study/NCT02465060), Phase 2, 6,452 participants), so they do not support this indication.

No registered clinical trials were found for the other predicted indications.

---

## Literature Evidence


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41468895](https://pubmed.ncbi.nlm.nih.gov/41468895/) | 2026 | Preclinical | Cell Reports Medicine | Venetoclax plus palbociclib was highly effective across 302 AML patient samples and overcame venetoclax resistance |
| [36076608](https://pubmed.ncbi.nlm.nih.gov/36076608/) | 2022 | Preclinical | Biomed Pharmacother | Palbociclib boosted venetoclax plus azacitidine activity in AML |
| [42312423](https://pubmed.ncbi.nlm.nih.gov/42312423/) | 2026 | Preclinical | Haematologica | Dual CDK2 and CDK4/6 inhibition enhanced anti-leukemic activity; notes that CDK4/6 monotherapy trials were disappointing |
| [40883610](https://pubmed.ncbi.nlm.nih.gov/40883610/) | 2025 | Preclinical | EMBO Mol Med | Dual CDK6 and LSD1 targeting was synergistic and overcame differentiation blockade in AML |
| [38890447](https://pubmed.ncbi.nlm.nih.gov/38890447/) | 2024 | Preclinical | Leukemia | Menin plus kinase (CDK6/FLT3) inhibitors were effective in NUP98-rearranged leukemia |
| [38430306](https://pubmed.ncbi.nlm.nih.gov/38430306/) | 2024 | Case report | Cancer Chemother Pharmacol | Palbociclib with venetoclax and azacitidine used successfully in refractory therapy-related AML |
| [40755307](https://pubmed.ncbi.nlm.nih.gov/40755307/) | 2025 | Preclinical | Br J Haematol | CDK4/6 inhibitors showed synergy with ATRA in non-APL AML |
| [32260549](https://pubmed.ncbi.nlm.nih.gov/32260549/) | 2020 | Review | Int J Mol Sci | CDK6 inhibition as an emerging approach in AML management |

**Rheumatoid arthritis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case report | Mod Rheumatol Case Rep | RA improved in a breast cancer patient treated with palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Study of pre-existing and emerging immune-mediated diseases in breast cancer patients on CDK4/6 inhibitors |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical | Ann Rheum Dis | CDK inhibition combined with cytokine blockade improved arthritis in animal models without added immune suppression |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical | Int J Mol Sci | CDK6-dependent synovial hyperplasia in arthritic mice |

**Thrombotic disease (safety signal, not benefit)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Pharmacovigilance and systematic review | Expert Opin Drug Saf | Examined the association between CDK4/6 inhibitors and thromboembolism |
| [35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/) | 2022 | Cohort | Cancer Manag Res | Real-world thromboembolic events with ribociclib |

No literature was found for the other predicted indications.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02493535 | IBRANCE | Not available | Not available |
| 02493543 | IBRANCE | Not available | Not available |
| 02493551 | IBRANCE | Not available | Not available |
| 02547635 | TARO-PALBOCICLIB | Not available | Not available |
| 02552124 | PMS-PALBOCICLIB | Not available | Not available |

Nine valid single-ingredient licenses exist in total: 3 IBRANCE, 3 TARO-PALBOCICLIB and 3 PMS-PALBOCICLIB. None is cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | High. Neutropenia is the characteristic toxicity, and preclinical work reports palbociclib-induced myelosuppression. This is especially relevant for leukemia patients with compromised marrow |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, and signs of infection, thromboembolism, and interstitial lung disease |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified in total. Major interactions in the data include **clarithromycin, cobicistat, deferiprone and samarium (153Sm) lexidronam**. Moderate interactions include aprepitant, dexamethasone, cimetidine, simvastatin, cisapride, miconazole, clotrimazole, saxagliptin, eliglustat and cilostazol. Dexamethasone appears in one leukemia trial combination (NCT03132454), so that interaction deserves attention.
- **Safety signals from the literature:** Pharmacovigilance analyses link CDK4/6 inhibitors to thromboembolism, interstitial lung disease and pulmonary toxicity, with age-related toxicity patterns in older women.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold for hyperthyroidism (TxGNN rank 1); Proceed with Guardrails for myeloid leukemia**

**Rationale:**
- The top-scoring prediction, hyperthyroidism, is supported only by the TxGNN model (deep learning), whose score may reflect similarities the model learned between related diseases, not biological evidence, with no trials, no literature and no mechanistic link. The same applies to the other L5 predictions, and thrombosis is a drug-related risk rather than a potential benefit.
- However, there is no randomized evidence, and monotherapy results in leukemia were disappointing, so evidence is at L3 only.
- Rheumatoid arthritis is worth keeping as a research question (L4), not a development candidate.

**To proceed, the following is needed:**
- Results from the leukemia trials (NCT02310243, NCT03132454, NCT05627232), especially efficacy and safety of combination regimens
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Detailed mechanism of action data
- A myelosuppression management plan for leukemia patients and a review of interactions with leukemia co-medications
- For rheumatoid arthritis: a Phase 2 proof-of-concept design that addresses myelosuppression risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

