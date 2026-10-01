---
layout: default
title: Sofosbuvir
parent: Moderate Evidence (L3-L4)
nav_order: 853
evidence_level: L4
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Sofosbuvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide polymerase inhibitor used to treat chronic hepatitis C and is marketed in Canada under four brand names.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection**, but among **50 retrieved clinical trials** and **19 publications**, almost none test HBV efficacy.
Most of the evidence concerns HCV treatment in HBV-coinfected patients, and part of it is a safety signal (HBV reactivation), so this prediction is currently **model-driven only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the marketed products and the NS5B mechanism; the Canadian license text was not supplied) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Sofosbuvir is known to be a nucleotide analog inhibitor of the HCV NS5B RNA-dependent RNA polymerase. Its efficacy in hepatitis C is well established, and its products (Sovaldi, Harvoni, Epclusa, Vosevi) are marketed in Canada.

Hepatitis C and hepatitis B are both chronic viral liver infections, so they sit close together in the knowledge graph. This closeness likely explains the very high TxGNN score. Mechanistically, however, the link is weak. HBV replicates through a reverse transcriptase and has no NS5B homolog, so there is no plausible direct antiviral mechanism for sofosbuvir against HBV.

The retrieved trials and papers mostly describe HCV treatment in patients who also have HBV, not treatment of HBV itself. One small Phase 2 pilot (NCT03312023, n=21) tests ledipasvir/sofosbuvir in HBV infection. It is based on a retrospective observation of modest HBsAg reduction in coinfected patients. Its outcome data were not included in the supplied material.

---

## Clinical Trial Evidence

The 10 trials below are those most relevant to HBV. Most of the 50 retrieved trials are HCV studies matched on keywords.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Ledipasvir/sofosbuvir for 12 weeks in HBV infection. The only trial that targets HBV directly; results were not provided |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Ledipasvir/sofosbuvir in HCV/HBV coinfection in Taiwan. Evaluates antiviral efficacy and safety for HCV |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | Sofosbuvir/velpatasvir with prophylactic TAF in HCV/HBV coinfection. Relevant to HBV reactivation prevention, not HBV efficacy |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02563943) | Phase 2/3 | Completed | 23 | Incidence and risk factors of HBV reactivation during anti-HCV treatment in coinfected patients |
| [NCT02349048](https://clinicaltrials.gov/study/NCT02349048) | Phase 2 | Completed | 68 | Simeprevir, daclatasvir and sofosbuvir in HCV genotype 1. No HBV endpoint |
| [NCT01805882](https://clinicaltrials.gov/study/NCT01805882) | Phase 2 | Completed | 229 | Anti-HCV combination pilot. No HBV endpoint |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | Sofosbuvir + velpatasvir in chronic HCV. No HBV endpoint |
| [NCT02292719](https://clinicaltrials.gov/study/NCT02292719) | Phase 2 | Completed | 70 | Ombitasvir/paritaprevir/ritonavir + sofosbuvir in HCV genotypes 2 and 3 |
| [NCT03612973](https://clinicaltrials.gov/study/NCT03612973) | N/A | Completed | 80 | Fibrosis, lipids and insulin resistance after HCV therapy. No HBV endpoint |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | Unknown | 1800 | Same-visit HCV testing and treatment in people who inject drugs |

*Note: the link for NCT02555943 should point to https://clinicaltrials.gov/study/NCT02555943.*

---

## Literature Evidence

No RCTs were retrieved. The table lists the most relevant studies, then reviews and case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label trial | J Med Virol | Ledipasvir/sofosbuvir in HBV infection. Hypothesis from retrospective coinfection data; primary endpoint is HBsAg decline at week 12 |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Clinical study | Clin Infect Dis | HBV reactivation during ledipasvir/sofosbuvir and 108-week follow-up in HCV/HBV coinfected patients in Taiwan |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir therapy in HCV and HCV/HBV coinfected patients in Egypt |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation in cancer patients with HCV/HBV coinfection receiving DAAs |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Clinical study | J Clin Gastroenterol | Risk of HBV reactivation during ledipasvir/sofosbuvir treatment for HCV |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Clinical study | Infect Drug Resist | Managing HBV reactivation after DAA therapy in HCV/HBV coinfected patients |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report and review | Medicine | HBV reactivation after successful sofosbuvir/ribavirin treatment of HCV |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Modelling study | Lancet Gastroenterol Hepatol | Global HBV prevalence, care cascade and prophylaxis coverage in 2022 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for HBV and HCV and their effects on kidney function |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatr | Treatment of hepatitis B and C in children |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2418355 | SOVALDI |
| 2432226 | HARVONI |
| 2456370 | EPCLUSA |
| 2467542 | VOSEVI |

---

## Safety Considerations

- **Literature-reported signal:** Several studies and case reports describe HBV reactivation during or after sofosbuvir-based HCV therapy in HBV-coinfected patients. Reactivation risk calls for HBV screening, monitoring or prophylaxis. This is a safety signal, not evidence of efficacy.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.77%) appears to reflect knowledge-graph proximity between HCV and HBV, not a real HBV mechanism, since HBV has no NS5B-type target. The retrieved evidence concerns HCV treatment in coinfected patients and HBV reactivation risk. The only HBV-directed study is a small Phase 2 pilot (n=21) whose results were not provided.

**To proceed, the following is needed:**
- Results of the Phase 2 pilot NCT03312023 (HBsAg and HBV DNA changes), and any larger controlled study in HBV monoinfection
- Mechanistic or in vitro data showing sofosbuvir activity against HBV
- Package insert warnings and contraindications from Health Canada, for safety screening
- A reactivation monitoring and prophylaxis plan for HBV-positive patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

