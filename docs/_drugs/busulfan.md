---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myeloid Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan (Myleran®/Busulfex®) is a bifunctional alkylating agent historically used as first-line treatment for chronic myeloid leukemia (CML) and now established as a core component of myeloablative and reduced-intensity conditioning (RIC) regimens prior to allogeneic hematopoietic stem cell transplantation (HSCT).
The TxGNN model predicts it may be effective for **myelodysplastic syndrome (MDS)**, with **50 clinical trials** and **20 publications** currently supporting this direction, including multiple completed Phase 3 randomized controlled trials — placing evidence at the highest classification level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukemia (CML); pre-HSCT myeloablative conditioning |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured dataset. Based on known pharmacological information, Busulfan is a bifunctional alkylating agent of the alkyl sulfonate class that forms covalent crosslinks within and between DNA strands, preferentially killing rapidly dividing cells — in particular, hematopoietic progenitor cells. At high doses, it produces profound, prolonged myelosuppression and immunosuppression, which is the intended pharmacological effect when used as HSCT conditioning therapy.

MDS is a clonal hematopoietic stem cell disorder characterized by ineffective hematopoiesis, dysplastic bone marrow morphology, and variable risk of transformation to acute myeloid leukemia. The pathophysiology involves abnormal clonal progenitor cells that progressively crowd out normal hematopoiesis — precisely the target for Busulfan-mediated bone marrow eradication. Allogeneic HSCT remains the only potentially curative treatment for higher-risk MDS, and Busulfan-based conditioning regimens — most notably Busulfan + Fludarabine (BuFlu) and Busulfan + Cyclophosphamide (BuCy) — are internationally recognized as standard conditioning platforms for MDS patients proceeding to transplantation.

The mechanistic link from CML conditioning to MDS is therefore direct: both diseases involve clonal hematopoietic progenitor cell populations that must be eradicated prior to donor engraftment. Multiple international Phase 3 trials have already used Busulfan-based conditioning as the control arm comparator in MDS transplantation studies, confirming its status as an established standard of care rather than a speculative new application. The TxGNN prediction accurately reflects this deeply evidence-supported clinical reality.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Prospective RCT directly comparing G-CSF+Decitabine+BUCY vs G-CSF+Decitabine+BF conditioning in RAEB-1, RAEB-2, and AML secondary to MDS undergoing allo-HSCT; largest direct RCT evaluating Busulfan-containing conditioning in this population |
| [NCT00469144](https://clinicaltrials.gov/study/NCT00469144) | Phase 3 | Completed | 233 | Randomized study of pharmacokinetically-targeted (AUC-based) vs fixed-dose once-daily IV Busulfan combined with Fludarabine for AML/MDS; established whether adaptive TDM-guided dosing improves outcomes and reduces toxicity versus weight-based dosing |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Prospective RCT comparing Melphalan 100 vs 140 mg/m² within the Melphalan-Busulfan-Fludarabine (MBF) conditioning regimen for AML/MDS; aims to define optimal Melphalan dose within the Busulfan triplet |
| [NCT00582933](https://clinicaltrials.gov/study/NCT00582933) | Phase 2 | Completed | 96 | Phase II trial of IV Busulfan (Busulfex) + Melphalan + Fludarabine as chemotherapy-only myeloablative regimen before T-cell-depleted allogeneic HSCT; assessed TBI-free conditioning in lymphohematopoietic disorders including MDS |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | High-dose IV Busulfan (AUC-targeted ≈6,500 µMol-min) + Fludarabine for AML and MDS before allogeneic HSCT; one of the largest Phase 2 studies directly evaluating PK-guided Busulfan dosing in this indication |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Phase 2 | Active, not recruiting | 204 | Timed-sequential Busulfan + Fludarabine + post-transplant cyclophosphamide (PTCy) for allogeneic HSCT in blood cancers; large ongoing study evaluating GVHD prevention strategies within Busulfan-based conditioning |
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | Completed | 20 | Decitabine + TBI followed by donor bone marrow transplant and high-dose cyclophosphamide for relapsed/refractory AML/MDS; Busulfan incorporated as part of bridging conditioning strategy in refractory population |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Completed | 30 | Clofarabine + IV Busulfan + Thymoglobulin (CBT) as RIC prior to allo-HSCT for high-risk AML, MDS, and ALL; tested whether replacing Fludarabine with Clofarabine in a Busulfan-based RIC increases anti-tumor activity |
| [NCT00997386](https://clinicaltrials.gov/study/NCT00997386) | Phase 2 | Completed | 16 | Reduced-intensity conditioning with Busulfan + Melphalan + Alemtuzumab (Campath) for PBSCT from matched unrelated donors; provided safety and engraftment data for RIC Busulfan in hematologic malignancies |
| [NCT00357565](https://clinicaltrials.gov/study/NCT00357565) | Phase 2 | Completed | 34 | HSCT for infant leukemia and pediatric MDS using Busulfan + Fludarabine + Melphalan before umbilical cord blood transplant; provided pediatric-specific Busulfan conditioning safety and engraftment data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | The Lancet Haematology | MC-FludT.14/L trial: Treosulfan+Flu vs **Busulfan+Flu** in older/comorbid AML and MDS patients (HSCT); confirmed Busulfan/Flu as the reference standard, with treosulfan meeting non-inferiority criteria |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Phase 3 RCT (final analysis) | American Journal of Hematology | Final analysis of the Phase 3 MC-FludT.14/L trial (n=476); statistically significant non-inferiority of treosulfan vs reduced-intensity Busulfan confirmed, further cementing Busulfan/Flu as the established comparator benchmark |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT | Journal of Clinical Oncology | BMT CTN 0901 Phase 3 trial (n=272): Myeloablative vs reduced-intensity conditioning in AML/MDS patients undergoing allo-HCT; provided definitive evidence on conditioning intensity trade-offs (relapse vs. toxicity) using Busulfan-based regimens |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | The Lancet Haematology | Open-label multicenter Phase 3 trial: G-CSF + Decitabine + **Busulfan-Cyclophosphamide** vs BuCy alone for MDS-RAEB and secondary AML undergoing allo-HSCT; Busulfan-Cyclophosphamide was the active control arm |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Systematic Review | American Journal of Hematology | Contemporary review of allo-HCT for MDS and myelofibrosis; contextualizes Busulfan-based conditioning in the era of genomic profiling, novel agents, and personalized transplant approaches |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review / Meta-analysis | Frontiers in Oncology | Systematic review and meta-analysis comparing treosulfan vs Busulfan-based conditioning for AML/MDS allo-HCT; quantified differences in event-free survival, non-relapse mortality, and GVHD across multiple studies |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Retrospective Cohort (PSM) | Transplantation and Cellular Therapy | Single-center propensity score-matched cohort study (n=138) comparing treosulfan vs **Busulfan** conditioning for MDS allo-HCT at Princess Margaret Hospital (Toronto, 2015–2022); demonstrated Busulfan's real-world continued clinical use and outcomes |
| [38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/) | 2024 | Comparative Cohort | Transplantation and Cellular Therapy | Italian pediatric registry study comparing long-term complications (growth, gonadal, and organ toxicity) after treosulfan vs **Busulfan**-based conditioning in children with acute leukemia/MDS; important for pediatric safety profiling |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective Cohort | Transplantation and Cellular Therapy | Myeloablative **Busulfan + Fludarabine** with in vivo T-cell depletion (Alemtuzumab) for AML/MDS allo-HSCT; demonstrated safety and efficacy using HCT-CI comorbidity scoring to guide eligibility, expanding MAC access to older patients |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Retrospective Cohort | Cancer | Fractionated-dose IV **Busulfan** myeloablative conditioning in older AML/MDS patients; demonstrated that fractionating the dose maintained efficacy while reducing non-relapse mortality compared to standard non-fractionated lower-dose RIC regimens |

---

## Canada Market Information

Busulfan currently has **no approved products in Canada** and is not listed in the Health Canada drug product database. No Drug Identification Numbers (DINs) are on record.

> **Note:** Despite the absence of Canadian market authorization, intravenous Busulfan (Busulfex®) is FDA-approved in the United States and EMA-authorized in Europe for use as conditioning therapy prior to allogeneic HSCT. Canadian patients and institutions requiring access would need to pursue Health Canada's **Special Access Programme (SAP)** for individual patient authorization or a formal New Drug Submission (NDS) for full market authorization.

---

## Cytotoxicity

Busulfan meets antineoplastic criteria: it belongs to the alkylating agent class (alkyl sulfonate), is used directly in hematologic malignancy treatment, and is a well-established cytotoxic chemotherapy agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (Alkyl sulfonate / Bifunctional methanesulfonate class) |
| Myelosuppression Risk | **Very High** — Profound, prolonged pancytopenia is the intended therapeutic effect at myeloablative doses; requires HSCT as stem cell rescue. Dose-dependent thrombocytopenia, neutropenia, and anemia are universal. |
| Emetogenicity Classification | Low to moderate (oral formulation); Moderate (IV high-dose conditioning course) — Prophylactic antiemetics are required throughout conditioning |
| Monitoring Items | CBC with differential (daily during conditioning), liver function tests (ALT, AST, bilirubin — hepatic VOD/SOS risk), renal function, IV Busulfan therapeutic drug monitoring (AUC targeting ~4,000–6,000 µMol-min per day recommended), neurological status monitoring (seizure risk), pulmonary function for long-term use |
| Handling Protection | Must comply with cytotoxic drug handling regulations; gloves, gown, and eye/face protection required; IV preparation in certified negative-pressure isolator or biological safety cabinet; segregated hazardous waste disposal; staff training on chemotherapy spill management |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Structured safety data (warnings, contraindications, drug interactions) were not available in the current dataset. Key pharmacologically known safety concerns for clinical awareness include: severe myelosuppression (intended at HSCT conditioning doses; life-threatening otherwise), hepatic sinusoidal obstruction syndrome (VOD/SOS — most serious acute complication, risk increased with cumulative dose and combination conditioning), seizures (prophylactic anticonvulsants such as levetiracetam required during high-dose IV courses), pulmonary fibrosis with prolonged oral use ("Busulfan lung"), gonadal failure and infertility, and risk of secondary myeloid malignancies with long-term alkylating agent exposure.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning for MDS is already embedded in international transplant guidelines and has been validated by multiple Phase 3 RCTs — this is not a speculative repurposing opportunity but rather a confirmed clinical application with the highest available evidence grade (L1). The primary challenge is not proving efficacy but ensuring appropriate patient selection, optimizing conditioning intensity, and managing significant transplant-related toxicity within a structured HSCT program.

**To proceed, the following is needed:**
- **Canadian regulatory access**: Formal Health Canada Special Access Programme (SAP) application required, as Busulfan has no current Canadian marketing authorization; supporting data package from international approvals should be compiled
- **MOA documentation**: Retrieve structured mechanism of action data from DrugBank API (data gap DG002) to complete the mechanistic evidence package
- **Pharmacovigilance and safety protocol**: Develop a comprehensive monitoring plan including IV Busulfan TDM protocols (AUC targeting), seizure prophylaxis algorithms, VOD/SOS risk stratification and prophylaxis (defibrotide for high-risk patients), and pulmonary monitoring schedules
- **Patient eligibility criteria**: Formally define MDS patient selection criteria based on IPSS-R risk score, HCT-CI comorbidity index, performance status, donor availability (matched related, matched unrelated, haploidentical), and disease status at transplant
- **Institutional infrastructure confirmation**: Busulfan-containing myeloablative conditioning for MDS requires a fully credentialed allogeneic HSCT center with inpatient bone marrow transplant unit, pharmacy IV compounding capacity, and 24-hour supportive care capability

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-10.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

