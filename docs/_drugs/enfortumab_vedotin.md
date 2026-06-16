---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Enfortumab vedotin (EV) is a Nectin-4–targeting antibody-drug conjugate (ADC) with MMAE payload, approved for locally advanced or metastatic urothelial carcinoma in the US and EU, but not yet marketed in Canada.
Among 10 TxGNN-predicted new indications, **HER2-positive breast carcinoma** (rank 10, score 98.99%) is the only clinically plausible candidate — supported by **1 active Phase 2 basket trial** (EV-202, NCT04225117, n=329) and **4 relevant publications** — while the top 9 predictions are mechanistically implausible or represent non-human disease artifacts in the knowledge graph.
Current evidence level is **L3**, and the recommendation is **Hold** pending Nectin-4 expression profiling in HER2-positive breast cancer populations and maturation of EV-202 cohort data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma (bladder cancer) |
| Most Actionable Predicted Indication | HER2-Positive Breast Carcinoma (TxGNN Rank 10) |
| TxGNN Prediction Score | 98.99% (HER2+ breast carcinoma); 99.53–99.13% (ranks 1–9, all model artifacts) |
| Evidence Level | L3 (HER2+ breast carcinoma); L5 (all other predictions) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## ⚠️ Prediction Quality Alert

**9 of 10 TxGNN predictions are mechanistically implausible or represent knowledge-graph artifacts.** This is an unusual evidence pack and the primary analysis below focuses on rank 10 (HER2-positive breast carcinoma) — the only prediction with clinical plausibility and direct trial evidence.

| Rank | Disease | Prediction Issue |
|------|---------|-----------------|
| 1 | Leprosy | Mycobacterial infection — no known link to Nectin-4 or MMAE mechanism |
| 2 | Multiple endocrine neoplasia | RET/MEN1-driven tumours; minimal Nectin-4 expression evidence |
| 3 | Cytomegalovirus infection | DNA virus; measles virus (not CMV) uses Nectin-4 as cell entry receptor — likely KG node confusion |
| 4 | Candidiasis | Fungal infection; only literature found is an ADC safety/FAERS adverse event report, not efficacy data |
| 5 | Cerebral infarction | Ischemic vascular disease; MMAE causes peripheral neurotoxicity, not neuroprotection |
| 6 | HIV infectious disease | CD4+ T-cell–targeting retrovirus; no Nectin-4 antiviral rationale exists |
| 7 | Homozygous familial hypercholesterolemia | LDL receptor gene disease; no mechanistic intersection with Nectin-4 signalling |
| 8 | Infectious bovine rhinotracheitis | **Veterinary disease (BoHV-1 in cattle)** — cross-species KG leakage |
| 9 | Malignant catarrh | **Veterinary disease (ruminant herpesvirus)** — cross-species KG leakage |
| 10 | HER2-positive breast carcinoma | ✓ Mechanistically plausible — see full analysis below |

Ranks 8–9 are non-human diseases and must be excluded from all repurposing consideration. The KG species-filtering pipeline requires a systematic fix to prevent future cross-species predictions in human drug repurposing outputs.

---

## Why Is This Prediction Reasonable?

Enfortumab vedotin is an antibody-drug conjugate in which an anti-Nectin-4 monoclonal antibody is site-specifically linked to MMAE (monomethyl auristatin E), a microtubule-disrupting agent. Although formal MOA documentation is not available in this Evidence Pack, EV's mechanism is well-characterized: following antibody binding to Nectin-4 on the tumour cell surface, the conjugate is internalised and MMAE is released to block mitosis in rapidly dividing cells. The antibody functions as a precision delivery vehicle; MMAE provides the cytotoxic kill.

Nectin-4 is not exclusively a urothelial antigen. Immunohistochemical studies have reported Nectin-4 expression in approximately **50–65% of HER2-positive breast cancers**, and emerging data suggest cross-regulatory interactions between Nectin-4 and the HER2/ERBB2 signalling axis. This biological overlap — combined with MMAE's potent activity against rapidly proliferating, HER2-overexpressing cancer cells — provides a mechanistic rationale for EV's potential in this population. The EV-202 Phase 2 basket trial (NCT04225117) has directly enrolled patients with **HER2-positive solid tumours**, generating the first clinical signals.

However, HER2-positive breast cancer is already served by multiple ADC options, including trastuzumab emtansine (T-DM1) and trastuzumab deruxtecan (T-DXd). EV's clinical positioning in this indication would most likely be among patients with confirmed Nectin-4 IHC positivity who have progressed on or are ineligible for HER2-targeted ADCs — a defined but narrow niche that requires prospective patient selection data to characterise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | Active, Not Recruiting | 329 | **EV-202 basket trial — primary evidence.** Evaluates EV as monotherapy (cohorts 1–8) and EV + pembrolizumab (cohort 9) across multiple solid tumours including HER2-positive disease. Primary endpoint: confirmed ORR per RECIST v1.1. Data maturation expected by September 2026. |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1b/2 | Recruiting | 428 | ASP2998 (anti-TROP2 ADC) as monotherapy and in combination with EV or pembrolizumab in advanced solid tumours. EV serves as a combination partner here; this trial reflects the competitive ADC landscape rather than providing direct EV-in-HER2+ evidence. |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | Recruiting | 90 | Trastuzumab Rezetecan (HER2-targeting ADC) in HER2-positive solid tumours including urothelial carcinoma. Competitive landscape reference; drug candidate is not EV. |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH biomarker-guided basket trial of approved drugs in new populations. Terminated early with only 11 participants enrolled — insufficient sample size for any meaningful efficacy signal. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Narrative Systematic Review | Critical Reviews in Oncology/Hematology | Synthesises real-world evidence for 10 recently approved oncology drugs; contextualises how EV's RCT-derived benefit-risk profile translates to broader populations including older adults and patients with comorbidities — relevant for anticipating off-label use patterns |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Translational/Basic Research | Cancer Letters | Polyploid giant cancer cells (PGCCs) mediate resistance to HER2-directed ADCs (T-DM1, T-DXd, disitamab vedotin) in HER2-positive breast and gastric cancer cell lines; highlights a resistance mechanism EV may encounter in HER2+ breast cancer and suggests combination strategies to explore |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | Comprehensive framework for ADC target selection (target expression, antibody, linker, payload); positions Nectin-4 and MMAE within the broader ADC landscape and contextualises EV's design rationale |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | Molecular pathology of bladder cancer covering Nectin-4 expression, KMT2D/KDM6A/TP53/FGFR3 mutational landscape, and personalised oncology classification; background reference for EV's primary indication rather than direct HER2+ breast cancer evidence |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | ADC with conventional cytotoxic payload — MMAE (monomethyl auristatin E) is a microtubule inhibitor (auristatin class); overall categorised as targeted-delivery cytotoxic chemotherapy |
| Myelosuppression Risk | Moderate-to-High — MMAE bystander effect causes neutropenia, anaemia, and thrombocytopenia; dose reductions frequently required in urothelial carcinoma trials |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (each cycle), LFTs (ALT/AST/bilirubin), fasting blood glucose (hyperglycaemia risk), peripheral neuropathy grading (neurological assessment each visit), skin inspection (severe cutaneous reactions including SJS/TEN reported) |
| Handling Protection | Must follow cytotoxic drug handling regulations; as a biohazardous ADC, EV requires pharmacist-prepared closed-system transfer device (CSTD) and dedicated disposal procedures |

---

## Safety Considerations

All warning and contraindication data returned as unavailable in this Evidence Pack. Please refer to the approved prescribing information — US FDA label or EMA SmPC for Enfortumab Vedotin — for complete safety information, including boxed warnings for peripheral neuropathy, severe skin reactions (Stevens-Johnson syndrome, toxic epidermal necrolysis), hyperglycaemia, and pneumonitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Of 10 TxGNN predictions, only HER2-positive breast carcinoma (rank 10) is mechanistically supportable: Nectin-4 is expressed in approximately half of HER2-positive breast tumours, and the EV-202 Phase 2 basket trial (NCT04225117) has already enrolled patients in this space. However, the prediction score hierarchy in this evidence pack is inverted — the 9 higher-ranked predictions are false positives, including 2 veterinary diseases, which raises questions about the KG filtering pipeline. Until EV-202 cohort-level efficacy data matures and prospective Nectin-4 IHC data in HER2+ breast cancer is available, proceeding is premature.

**To proceed, the following is needed:**

- **Nectin-4 IHC data**: Prospective expression profiling in HER2-positive breast cancer patients to confirm target-positive population and define a patient selection strategy
- **EV-202 results**: Outcome data from NCT04225117 HER2-positive solid tumour cohorts, expected by Q3 2026
- **Competitive differentiation**: Clear clinical positioning against T-DM1 and T-DXd — define the specific line of therapy and biomarker criteria (Nectin-4+ / HER2-targeted ADC failure) where EV adds value
- **Health Canada regulatory pathway**: EV does not currently hold a Canadian DIN even for its primary urothelial carcinoma indication; a regulatory filing strategy for Canada is a prerequisite before any off-label use discussion
- **KG pipeline fix**: Implement cross-species filtering in the TxGNN knowledge graph to exclude veterinary diseases (IBR, malignant catarrh) from future human drug repurposing outputs; audit other predictions for similar leakage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

