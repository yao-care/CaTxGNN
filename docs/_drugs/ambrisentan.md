---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Connective Tissue Disease–Associated PAH

> **Note:** This is a multi-indication evidence pack (10 TxGNN-predicted indications). This report highlights the most evidence-supported actionable indication (CTD-PAH) while summarizing all predictions.

---

## One-Sentence Summary

Ambrisentan is a selective endothelin receptor type A (ETA) antagonist used for pulmonary arterial hypertension (PAH).
The TxGNN model predicted 10 new potential indications; the strongest actionable evidence supports **PAH associated with connective tissue disease (CTD-PAH)**, backed by **3 clinical trials** and **19 publications**, and **PAH associated with HIV infection (HIV-PAH)**, backed by **1 completed Phase 3 RCT** (evidence level L1).
The top-ranked TxGNN prediction — pulmonary arteriovenous malformation (99.41%) — is considered a knowledge-graph topological artifact with no known biological plausibility, and is recommended as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (inferred from clinical evidence; no regulatory record available for this market) |
| Primary Predicted New Indication | PAH associated with connective tissue disease (CTD-PAH) |
| TxGNN Prediction Score | 99.30% (rank 3; overall top score 99.41% for pulmonary AVM — Hold) |
| Evidence Level | L2 (CTD-PAH, CHD-PAH); L1 (HIV-PAH) |
| Canada Market Status | Not Marketed (0 DINs in dataset) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails (CTD-PAH, CHD-PAH, HIV-PAH); Hold for all other predictions |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, ambrisentan is a selective endothelin receptor type A (ETA) antagonist. Endothelin-1 (ET-1) is a potent vasoconstrictor and vascular smooth muscle mitogen; chronic overactivation of the ET-1/ETA axis drives pulmonary arterial remodeling, vasoconstriction, and right ventricular failure — the cardinal features of PAH. By selectively blocking ETA, ambrisentan reduces pulmonary vascular resistance and right ventricular afterload, improving exercise capacity and hemodynamics.

All biologically plausible predicted indications belong to WHO Group 1 PAH — a classification spanning multiple etiological subtypes that converge on the same pathological endpoint of ET-1–mediated endothelial dysfunction and vascular remodeling. For CTD-PAH (particularly systemic sclerosis, SSc), ET-1 plasma concentrations are markedly elevated and ETA activation further drives organ fibrosis, making ambrisentan a mechanistically well-matched candidate with the most comprehensive subtype-specific evidence body. For HIV-PAH, viral proteins (e.g., gp120) stimulate pulmonary endothelial ET-1 secretion, providing a direct mechanistic rationale for ETA antagonism. For CHD-PAH (e.g., Eisenmenger syndrome), the pulmonary hypertensive mechanism is essentially identical to idiopathic PAH, and ambrisentan's broad Group 1 PAH approval already encompasses this subtype in several jurisdictions.

The top-ranked TxGNN prediction — pulmonary arteriovenous malformation (PAVM) — is a structural arteriovenous shunting defect. PAVM does not involve ET-1–driven vasoconstriction or vascular proliferation; ETA blockade has no known mechanism of action in anatomical AV shunts. The high TxGNN score almost certainly reflects topological proximity of "vascular disease" nodes in the knowledge graph rather than any genuine biological relationship.

---

## Clinical Trial Evidence

### PAH Associated with Congenital Heart Disease (CHD-PAH) — Rank 2 | Score 99.37% | Evidence Level L2

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3 | Completed | 134 | Open-label single-arm study in Chinese PAH patients; 12-week primary evaluation of ambrisentan 5 mg on 6-minute walk distance; CHD-PAH is a likely major subgroup in this registry-heavy Asian cohort |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 | Completed | 38 | Long-term open-label extension of pediatric PAH study (ages 8–18); pediatric PAH cohorts have high CHD-PAH representation; ambrisentan follow-up extending to 2022 |
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | Terminated | 33 | Ambrisentan 5 mg vs. placebo in inoperable CTEPH over 16 weeks; premature termination (target 160) substantially limits interpretation |
| [NCT01894022](https://clinicaltrials.gov/study/NCT01894022) | Phase 3 | Terminated | 19 | Long-term extension of the CTEPH trial above; terminated early following the parent study |

### PAH Associated with Connective Tissue Disease (CTD-PAH) — Rank 3 | Score 99.30% | Evidence Level L2

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | 36-week open-label study of ambrisentan + tadalafil combination therapy specifically in SSc-PAH; assessed 6MWD, NYHA functional class, hemodynamics, and RV function; directly supports AMBITION-trial findings in this subgroup |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | Randomized double-blind placebo-controlled proof-of-concept trial of ambrisentan in borderline/early SSc-PAH (EDITA); novel early-intervention design filling an evidence gap |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | Phase 4 | Terminated | 3 | Switch study from bosentan/macitentan to ambrisentan in CTD-PAH; terminated very early (3 patients enrolled), no interpretable data |

### PAH Associated with HIV Infection (HIV-PAH) — Rank 5 | Score 99.30% | Evidence Level L1

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Multi-center double-blind randomized placebo-controlled crossover study (PROWESS 15) in HIV-PAH patients; evaluated inhaled iloprost on exercise capacity in patients already receiving stable background ERA therapy (including ambrisentan); provides direct evidence of ambrisentan as an effective PAH background therapy in HIV-PAH |

---

## Literature Evidence

### PAH Associated with Connective Tissue Disease (CTD-PAH)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review & Meta-analysis | Internal and Emergency Medicine | Most current meta-analysis of RCTs in CTD-PAH; evaluated functional class, survival, 6MWD, clinical worsening, NT-proBNP; evidence mostly from PAH trial subgroups |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Earlier meta-analysis specifically focused on CTD-PAH treatment trials; established that ERA-class agents improve functional outcomes |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Prospective Cohort (Post Hoc RCT) | Annals of the Rheumatic Diseases | Post hoc analysis of AMBITION RCT in CTD-PAH modified ITT population: ambrisentan + tadalafil combination vs. either monotherapy; includes SSc-PAH subpopulation results |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Observational Study (RCT Subgroup) | Annals of the Rheumatic Diseases | AMBITION trial CTD-PAH subgroup: attenuated response vs. idiopathic PAH noted, with implications for treatment intensity decisions |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Retrospective Cohort | Respiratory Medicine | ARIES-E clinical trial CTD-PAH subgroup analysis: 3-year efficacy and safety of ambrisentan in CTD-PAH; supports long-term tolerability in this population |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | Prospective Cohort | American Journal of Respiratory and Critical Care Medicine | Up-front ambrisentan + tadalafil combination in SSc-PAH; demonstrated meaningful hemodynamic improvement in this historically treatment-refractory subgroup |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Drug Review | Therapeutic Advances in Respiratory Disease | Comprehensive clinical review of ambrisentan in PAH; summarizes CTD-PAH regulatory approval and evidence base including ARIES trials |
| [29282676](https://pubmed.ncbi.nlm.nih.gov/29282676/) | 2018 | Registry Study (PMS) | Clinical Drug Investigation | Post-marketing surveillance of ambrisentan (Volibris) in 702 Japanese PAH patients; real-world safety and efficacy data including CTD-PAH subgroup |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Authoritative JAMA review on PAH diagnosis and treatment; covers ERA use in CTD-PAH as part of current standard of care |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in CTD-PAH treatment; discusses ambrisentan combination regimens and monitoring requirements in CTD context |

### PAH Associated with HIV Infection (HIV-PAH)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Retrospective Cohort | Therapeutic Advances in Respiratory Disease | Real-world ambrisentan use across PH subtypes in a UK referral centre; includes HIV-PAH cases and tolerability data in this population |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry Study | Terapevticheskii Arkhiv | Russian National PAH Registry 6-year analysis; documents HIV-PAH subgroup prevalence, current ERA-based therapy patterns, and outcomes |

---

## Canada Market Information

The current dataset records **no registered Drug Identification Numbers (DINs)** for ambrisentan in this market, and no licensed product details are available to tabulate.

> **Important:** Ambrisentan (marketed as Letairis® and Volibris®) has been approved by regulatory authorities in the US, EU, and Japan for PAH. The absence of DIN data in this dataset may reflect a data collection gap rather than a genuine non-approval status. Current Health Canada authorization status should be verified independently via the Health Canada Drug Product Database before any regulatory or clinical decision-making.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Pending data gaps:** Package insert warnings and contraindications were not available in this evidence pack. Clinicians should specifically review hepatotoxicity monitoring requirements (aminotransferase elevation risk), teratogenicity (ERA class is contraindicated in pregnancy — REMS program in the US), fluid retention risk, and potential drug-drug interactions with antiretroviral agents (particularly relevant for HIV-PAH use).

---

## Conclusion and Next Steps

### Multi-Indication Decision Summary

| Indication | Rank | TxGNN Score | Evidence Level | Decision |
|-----------|------|------------|---------------|---------|
| Pulmonary arteriovenous malformation | 1 | 99.41% | L5 | **Hold** |
| PAH with congenital heart disease | 2 | 99.37% | L2 | **Proceed with Guardrails** |
| PAH with connective tissue disease | 3 | 99.30% | L2 | **Proceed with Guardrails** |
| PAH with schistosomiasis | 4 | 99.30% | L4 | Research Question |
| PAH with HIV infection | 5 | 99.30% | L1 | **Proceed with Guardrails** |
| PAH with chronic hemolytic anemia | 6 | 99.30% | L5 | **Hold** |
| Dental/periodontal malformation syndrome | 7 | 99.19% | L5 | **Hold** |
| Hypotrichosis simplex of the scalp | 8 | 99.15% | L5 | **Hold** |
| Hypertrichosis | 9 | 99.14% | L5 | **Hold** |
| Dandy-Walker malformation syndrome | 10 | 99.12% | L5 | **Hold** |

---

**Decision: Proceed with Guardrails** (CTD-PAH and HIV-PAH as priority indications)

**Rationale:**
For CTD-PAH, ambrisentan has two completed clinical trials (including one double-blind RCT), a comprehensive literature body of 19 publications including meta-analyses and dedicated AMBITION/ARIES subgroup analyses, and regulatory approvals for this specific subtype in the US and Japan — the mechanistic rationale (ET-1 overexpression and ETA-driven fibrosis in SSc) is the strongest among all predicted indications. For HIV-PAH, a completed Phase 3 RCT in this specific population (NCT00709956) provides the highest-grade direct evidence available in the entire dataset, meeting L1 criteria.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Download and parse the approved package insert to extract warnings, contraindications, pregnancy restrictions, hepatotoxicity monitoring requirements, and drug interactions — currently a Blocking data gap preventing formal S1 safety evaluation
- **MOA documentation:** Complete DrugBank API query to formally document mechanism of action for the mechanistic analysis section
- **Health Canada status verification:** Confirm current DIN status via the Health Canada Drug Product Database to clarify whether the 0-DIN result reflects a genuine non-approval or a dataset gap
- **CTD-PAH:** Obtain patient-level subgroup data from the AMBITION and ARIES trials specifically for the target market population; review SSc-PAH vs. other CTD subtype breakdown
- **HIV-PAH:** Assess drug-drug interaction profile between ambrisentan and current antiretroviral regimens (e.g., CYP3A4 and P-gp interactions with protease inhibitors/NNRTIs)
- **CHD-PAH:** Confirm CHD-PAH subgroup representation and outcome data from the NCT01808313 Phase 3 Chinese PAH study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

