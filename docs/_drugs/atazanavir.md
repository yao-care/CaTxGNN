---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atazanavir: From HIV-1 Infection to AIDS Related Complex

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor used as part of combination antiretroviral therapy (cART) for HIV-1 infection across adults and pediatric populations.
The TxGNN model predicts it may be effective for **AIDS Related Complex (ARC)** — the symptomatic, pre-AIDS stage of HIV-1 disease progression — with **2 completed Phase 3 clinical trials** and **3 publications** currently supporting this direction.
Given that ARC is directly caused by the same HIV-1 virus that Atazanavir targets, the mechanistic basis for this prediction is exceptionally strong.

> **Note on TxGNN Ranking:** The highest-scoring TxGNN prediction (score 99.98%, rank 1) was for *simian immunodeficiency virus (SIV) infection*, a non-human primate disease with no direct human clinical application. This report focuses on **AIDS Related Complex** (TxGNN score 99.71%), the highest-ranked *human clinical* indication with Level 1 evidence and an actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | AIDS Related Complex |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Complete mechanism of action data from DrugBank was not available at the time of this report. Based on established pharmacological knowledge, Atazanavir is an azapeptide HIV-1 protease inhibitor. It selectively binds to the catalytic site of the HIV-1 protease enzyme, preventing cleavage of the Gag-Pol polyprotein precursor into functional structural proteins and replication enzymes. Without this maturation step, newly assembled viral particles remain non-infectious — Atazanavir therefore suppresses HIV-1 plasma viral load at the post-assembly stage. This mechanism is typically combined with a pharmacokinetic booster (ritonavir or cobicistat) to maintain adequate drug exposure.

AIDS Related Complex (ARC) describes the symptomatic, immune-suppressed interval in HIV-1 disease progression that precedes full AIDS. It is characterized by persistent lymphadenopathy, constitutional symptoms (fever, weight loss, night sweats), and declining CD4 T-cell counts. The underlying driver of ARC is active, ongoing HIV-1 viral replication — the precise biological process that Atazanavir inhibits. The mechanistic link is therefore not an extrapolation but a direct application: suppressing HIV-1 protease in ARC patients reduces viral load, slows immune deterioration, and may prevent progression to AIDS-defining illness.

The TxGNN knowledge graph model captured this high-confidence relationship, assigning a score of 99.71%. This aligns with established clinical practice: protease inhibitor-based cART regimens are routinely used across the full HIV disease spectrum, including the ARC stage. NCT00035932, a Phase 3 trial directly evaluating Atazanavir-containing combination regimens in 571 treatment-experienced HIV subjects, represents the strongest direct evidence supporting this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Core Atazanavir efficacy trial: ATV/ritonavir or ATV/saquinavir vs. lopinavir/ritonavir, each combined with tenofovir and a nucleoside, in treatment-experienced HIV patients; assessed viral load reduction and long-term safety over multiple years |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I study: international multicenter single-arm trial evaluating safety, efficacy, and pharmacokinetics of ATV powder boosted with ritonavir plus an optimized NRTI backbone in HIV-infected pediatric patients aged 3 months to 6 years |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Retrospective Cohort | J Acquir Immune Defic Syndr | Evaluated differential effects of commonly prescribed cART regimens — including ATV-based regimens — on incidence of AIDS-defining neurological conditions; provides comparative effectiveness data across treatment stages relevant to ARC management |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Observational | AIDS Reviews | Reviewed the combined impact of HIV infection and ART (including Atazanavir) on gastrointestinal adverse events; directly relevant to tolerability in ARC patients, who frequently present with GI complaints |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | In vitro / Medicinal Chemistry | Antimicrob Agents Chemother | Developed next-generation CNS-targeting HIV-1 protease inhibitors with improved blood-brain barrier penetration, reinforcing the role of the PI drug class in addressing HIV-associated CNS complications that commonly emerge during ARC progression |

---

## Canada Market Information

Atazanavir is currently **not marketed in Canada** and has no registered Drug Identification Numbers (DINs) on file with Health Canada. No approved indications are on record. If a Canadian market entry is planned, a full regulatory submission will be required.

---

## Safety Considerations

Please refer to the package insert for safety information. Health Canada warnings, contraindications, and drug interaction data were not available at the time of this report. A blocking data gap has been identified: the TFDA package insert PDF requires download and parsing to enable a complete safety evaluation before this candidate can advance to Stage 1 safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atazanavir is a well-established HIV-1 protease inhibitor with robust Phase 3 evidence (NCT00035932, n=571) directly evaluating its efficacy in HIV/AIDS patients. Because AIDS Related Complex is a clinical stage of the same HIV-1 disease that Atazanavir is mechanistically designed to treat, this is less a novel repurposing question and more a confirmation that Atazanavir's known therapeutic mechanism extends across the clinical continuum of HIV infection — a strong basis for proceeding.

**To proceed, the following is needed:**
- Retrieve and parse the Health Canada package insert to complete the safety profile, including warnings, contraindications, and drug-drug interactions (currently a blocking data gap)
- Query the DrugBank API to formally confirm the complete mechanism of action and drug class categorization
- Clarify whether existing HIV-1 infection approvals in reference jurisdictions (FDA, EMA) already encompass ARC as a clinical staging of the same disease, or whether a separate indication filing would be required
- Conduct a comprehensive drug interaction review for co-medications commonly used in the HIV/ARC population (e.g., NRTIs, integrase inhibitors, TB medications, antifungals)
- Define a regulatory pathway for Health Canada DIN registration if Canadian market access is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

