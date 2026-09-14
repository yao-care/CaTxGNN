---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 728
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide analog NS5B polymerase inhibitor originally developed and approved for chronic **Hepatitis C virus (HCV)** infection. The TxGNN model predicts it may also be effective for **Hepatitis B virus (HBV) infection**, but the supporting evidence base is largely drawn from HCV/HBV co-infection studies monitoring HBV reactivation rather than direct antiviral efficacy trials against HBV — evidence strength is currently rated **L4 (mechanistic/preclinical level)**, and the recommendation is to **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (established labeled indication; drug is not currently marketed in Canada, so no Canadian product-specific indication text is available in this evidence pack) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sofosbuvir is a nucleotide analog prodrug that, once converted to its active triphosphate form, inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) — the enzyme HCV uses to replicate its RNA genome. This mechanism is highly specific to HCV and other RdRp-dependent RNA viruses.

Hepatitis B virus, in contrast, is a DNA virus that replicates through an entirely different enzyme — reverse transcriptase (RT) — not RdRp. There is no direct molecular target overlap between sofosbuvir's mechanism and HBV replication. The clinical trial and literature evidence collected for this candidate predominantly comes from HCV/HBV co-infected populations where sofosbuvir-based regimens were used to treat the HCV component, with HBV monitored only for the risk of viral reactivation during or after HCV clearance — not as a therapeutic target.

One direct exception exists: a Phase 2 open-label pilot study (NCT03312023 / PMID 36045503) tested ledipasvir/sofosbuvir in HBV-monoinfected subjects, based on the observation that HBsAg modestly declined in HCV/HBV co-infected patients treated with this combination. This is the strongest piece of evidence supporting the prediction, but it remains a small, single-arm, hypothesis-generating study. Overall, the TxGNN high score for this candidate likely reflects strong statistical co-occurrence in the HCV/HBV co-infection literature (a confounding signal) rather than a genuine, independently validated antiviral mechanism against HBV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label study of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; based on prior observation of modest HBsAg decline in HCV/HBV co-infected patients — the only trial directly testing sofosbuvir-based therapy as an HBV intervention. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL for HCV in HCV/HBV co-infected patients, with prophylactic TAF to prevent HBV reactivation — an HBV safety-monitoring design, not an HBV efficacy trial. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Ledipasvir/sofosbuvir in HCV genotype 1/2 patients with HBV co-infection (Taiwan); primary endpoint was HCV antiviral efficacy, not HBV outcomes. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of HBV reactivation incidence, morbidity, and predisposing factors during direct-acting antiviral treatment of HCV in HCV/HBV co-infected patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2, open-label) | Journal of Medical Virology | Pilot study of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; assessed decline in HBsAg and HBV DNA — most direct evidence for this indication. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir therapy in chronic HCV and HCV/HBV co-infected patients in Egypt; efficacy assessed for HCV, HBV outcomes secondary. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report / literature review | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin — illustrates reactivation risk rather than therapeutic benefit. |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort | Clin Infect Dis | Ledipasvir/sofosbuvir in HCV/HBV coinfected patients in Taiwan; 108-week follow-up for HBV reactivation during and after HCV treatment. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | J Clin Gastroenterol | Risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV infection. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infect Drug Resist | Management of HBV reactivation post-DAA treatment of HCV in HCV/HBV coinfected patients with pretreatment HBeAg seroconversion. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation in cancer patients receiving DAAs for HCV infection in HBV/HCV co-infection. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Review/epidemiology | Lancet Gastroenterol Hepatol | Global modelling study of HBV prevalence, care cascade, and prophylaxis coverage — background epidemiology, not sofosbuvir-specific efficacy data. |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Review | J Hepatol | Trends in HCV treatment uptake 2014–2023, with lessons applicable to emerging HBV/HDV therapies. |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatr | Overview of hepatitis B and C treatment in children; general background, not sofosbuvir-specific HBV efficacy. |

---

## Canada Market Information

Sofosbuvir is currently **not marketed in Canada** under this evidence pack (market status: 未上市 / Not Marketed), with **0 Drug Identification Numbers (DINs)** on file. No product license or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for sofosbuvir's activity against HBV is weak — sofosbuvir targets HCV's RdRp, while HBV replicates via reverse transcriptase, and nearly all supporting trials/literature reflect HCV treatment with HBV reactivation monitoring rather than direct anti-HBV efficacy. Evidence level L4 and the presence of Blocking/High-severity data gaps (missing product warnings/contraindications and MOA documentation) mean this candidate is not ready to advance past initial screening.

**To proceed, the following is needed:**
- Confirmed original-indication and product labeling data (currently absent from this evidence pack; original_moa and safety warnings are flagged as data gaps)
- TFDA/Health Canada-equivalent safety data (warnings, contraindications, drug interactions) via official product monograph
- A dedicated, adequately powered efficacy trial of sofosbuvir (or a sofosbuvir-based regimen) in HBV-monoinfected patients, building on the single existing Phase 2 pilot (NCT03312023)
- Note for portfolio prioritization: among this drug's predicted indications, **Hepatitis E virus infection (rank 2)** shows notably stronger evidence (L3, "Proceed with Guardrails," direct Phase 2 pilot trial plus multiple in-vitro/case-series data) and may warrant separate evaluation ahead of the HBV candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

