---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
---

# Rifabutin
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

# Rifabutin: From Mycobacterial Infection Management to HIV Infectious Disease

## One-Sentence Summary

Rifabutin is a rifamycin-class antibacterial, historically used to prevent and treat *Mycobacterium avium* complex (MAC) bacteremia and tuberculosis in immunocompromised (largely HIV-positive) patients. The TxGNN model predicts it may be repositioned as an indication for **HIV infectious disease** itself, with **39 clinical trials** and **20 publications** currently associated with this signal — though on close inspection, most of this evidence documents rifabutin's *existing* role as a co-therapy/DDI partner in HIV-infected populations rather than a genuinely new antiviral mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Canadian regulatory data (unlicensed); documented clinical role per trial evidence: prophylaxis/treatment of MAC bacteremia and tuberculosis in HIV/AIDS patients |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Canada Market Status | 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — DrugBank MOA lookup pending). Based on known information from the evidence pack, Rifabutin is a rifamycin-class antibiotic whose pharmacological target is bacterial (mycobacterial) RNA polymerase; it has **no direct antiviral activity against HIV**.

The apparent link between rifabutin and "HIV infectious disease" in the TxGNN knowledge graph reflects strong *co-occurrence* rather than a shared mechanism: rifabutin is the preferred rifamycin for treating tuberculosis and preventing/treating MAC bacteremia in HIV-positive patients (because, unlike rifampicin, it has a milder CYP3A-inducing effect and is more compatible with protease inhibitors and integrase inhibitors). Consequently, the overwhelming majority of the supporting trials and literature are pharmacokinetic drug-drug interaction (DDI) studies between rifabutin and antiretrovirals (maraviroc, indinavir, dolutegravir, cabotegravir, darunavir/ritonavir, etc.), or MAC/TB prophylaxis trials conducted specifically in HIV+ cohorts.

In other words, the high TxGNN score and L1 evidence tier are real, but they largely capture rifabutin's **already-established supportive role in HIV patient management** (managing TB/MAC co-infection and antiretroviral compatibility) rather than a novel therapeutic effect against HIV infection itself. This distinction should be made explicit to decision-makers before treating this as a genuine repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Compared clarithromycin vs. rifabutin vs. combination for prevention of MAC bacteremia/disseminated MAC disease in HIV patients with CD4 ≤100 |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm trial: clarithromycin/ethambutol ± rifabutin (450mg or 300mg) vs. placebo for MAC bacteremia treatment in AIDS patients |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Daily vs. intermittent azithromycin/rifabutin regimens for prevention of disseminated MAC and fungal infections in HIV patients |
| [NCT00002343](https://clinicaltrials.gov/study/NCT00002343) | Phase 4 | Completed | 200 | Post-marketing PK/PD study optimizing rifabutin ± ethambutol dosing for MAC prophylaxis in AIDS patients (CD4 ≤100) |
| [NCT00002080](https://clinicaltrials.gov/study/NCT00002080) | N/A | Completed | N/A | Treatment-IND program providing rifabutin monotherapy to prevent/delay MAC bacteremia in HIV+ patients with CD4 ≤200 |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | N/A | Completed | 215 | TBTC Study 23: rifabutin-based intermittent regimen for treatment of HIV-related, rifamycin-susceptible tuberculosis |
| [NCT00023348](https://clinicaltrials.gov/study/NCT00023348) | Phase 2/3 | Completed | 150 | Pharmacokinetics of intermittent isoniazid/rifabutin in HIV-related TB (USPHS Study 23) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin as a rifampicin substitute alongside antiretroviral therapy for combined TB/HIV treatment (South Africa) |
| [NCT01059422](https://clinicaltrials.gov/study/NCT01059422) | Phase 4 | Completed | 10 | Efficacy/safety of raltegravir + 3TC/ABC in ART-naïve HIV/TB co-infected adults on rifabutin-based anti-TB therapy |
| [NCT00810446](https://clinicaltrials.gov/study/NCT00810446) | N/A | Completed | 72 | Post-marketing drug-use surveillance of Mycobutin (rifabutin) in HIV-infected patients (Japan) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review comparing rifamycins (incl. rifabutin) vs. isoniazid for TB prevention in HIV-negative people at risk |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | Reviews bidirectional TB-HIV disease interaction and rifabutin-based co-treatment strategies |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | Management of active TB in the HIV era, covering rifabutin-antiretroviral drug interactions |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Review | Clinical Pharmacokinetics | Establishes rifabutin's clinical effectiveness for MAC prophylaxis in HIV+ patients with low CD4 counts |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin PK and safety in TB/HIV-coinfected children on lopinavir/ritonavir-based second-line ART |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety/efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir ART; notes neutropenia risk |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | Cohort | J Antimicrob Chemother | PK and short-term safety of rifabutin + lopinavir/ritonavir in young HIV-infected children |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK modeling | Br J Clin Pharmacol | Characterizes DDI between rifabutin and dolutegravir via population PK model |
| [32979587](https://pubmed.ncbi.nlm.nih.gov/32979587/) | 2020 | Retrospective observational | Int J Infect Dis | Tenofovir alafenamide + rifabutin co-administration did not lead to loss of HIV-1 suppression |
| [30217608](https://pubmed.ncbi.nlm.nih.gov/30217608/) | 2018 | Case report | J Fr Ophtalmol | Rifabutin-associated uveitis in a 10-year-old HIV-infected child — relevant safety signal |

---

## Canada Market Information

Rifabutin currently has **no active drug licenses in Canada** (market status: 未上市 / not marketed, 0 DINs on record). No product/DIN-level information is available to summarize.

---

## Safety Considerations

No formal Health Canada / package-insert safety data (warnings, contraindications, DDI database) is currently available for this drug (data gap DG001, flagged as Blocking severity — required before any S1 safety pre-assessment can proceed).

From the literature evidence collected, one notable safety signal worth flagging for follow-up: rifabutin has been associated with **drug-induced uveitis**, including in HIV-infected patients on concurrent prophylaxis/itraconazole therapy (PMID 8967681, PMID 30217608) and in a pediatric HIV case. This is a literature-derived signal, not a confirmed label warning, and should be verified against the official product monograph once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The evidence base is large (39 trials, 20 publications) and includes multiple completed Phase 3 RCTs, but it predominantly documents rifabutin's *already-established* role as a TB/MAC co-therapy agent and DDI partner for antiretrovirals in HIV+ patients — not a novel antiviral mechanism against HIV. This should be treated as a **repositioning of an existing standard-of-care use**, not a de novo repurposing hypothesis, and communicated as such to reviewers.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data via DrugBank API — currently a High-severity data gap (DG002)
- Clarification of the actual clinical claim being evaluated (e.g., "adjunct TB/MAC therapy in HIV patients" vs. "treatment of HIV infection"), since the current framing overstates rifabutin's role
- Given the drug is unlicensed in Canada (0 DINs), a market-entry/import pathway assessment would be required before any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

