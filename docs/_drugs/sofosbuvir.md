---
layout: default
title: Sofosbuvir
parent: Model Prediction Only (L5)
nav_order: 860
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Sofosbuvir: predicted new indication Hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

Sofosbuvir is a nucleotide polymerase inhibitor originally used to treat chronic hepatitis C virus infection.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but the mechanistic link is weak: **11 clinical trials** and **20 publications** are listed, and only one small single-arm Phase 2 study (ledipasvir/sofosbuvir in HBV-infected subjects) tests the drug in HBV directly. Most of the remaining evidence concerns HCV/HBV co-infection, where the main finding is a risk of HBV reactivation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (as assigned in the data compiled for this report; see the note in the Conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, sofosbuvir is a nucleotide analog prodrug whose active triphosphate inhibits the HCV NS5B RNA-dependent RNA polymerase. Its efficacy in hepatitis C is well established.

The mechanistic fit for HBV is poor. HBV is a DNA virus that replicates through reverse transcription, so sofosbuvir has no direct target there. The high TxGNN score may partly reflect the shared setting of viral hepatitis, the frequent HCV/HBV co-infection, and sofosbuvir's nucleotide-analog class.

The evidence in HBV is indirect. In co-infected patients, treating HCV with sofosbuvir-based regimens changes HBV-DNA and HBsAg kinetics and can trigger HBV reactivation. One Phase 2 pilot study of ledipasvir/sofosbuvir in HBV-infected subjects (NCT03312023, published as PMID 36045503) reported a modest HBsAg reduction. It is small, single-arm, and uses a combination product, so any HBV effect cannot be attributed to sofosbuvir alone. Antiviral activity against HBV itself is not established.

Other predictions in the list have stronger or clearer mechanistic grounds. Chronic hepatitis E has a Phase 2 pilot and in vitro RNA-polymerase inhibition, but the clinical response was only transient. Flaviviruses such as Kyasanur forest disease and Omsk hemorrhagic fever are plausible targets because of their related RNA polymerases, but evidence there is preclinical or absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Ledipasvir/sofosbuvir for 12 weeks in HBV-infected subjects; tests the combination directly in HBV, but is single-arm and small |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAAs in HCV/HBV co-infected patients; monitors HBV reactivation during anti-HCV therapy |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL with prophylactic TAF in HCV/HBV co-infection; addresses HBV reactivation prevention |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | Completed | 72 | Randomized single-dose sofosbuvir/daclatasvir (± ribavirin) in genotype 4 HCV; primary endpoint is HCV |
| [NCT02483156](https://clinicaltrials.gov/study/NCT02483156) | Phase 2/3 | Completed | 80 | Sofosbuvir + ribavirin vs a single-dose combination in genotype 4 HCV; HBV relevance depends on co-infection enrollment |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | Ledipasvir/sofosbuvir in HCV-associated indolent B-cell lymphoma; no clear HBV link |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | Unknown | 25 | E/C/F/TAF switch followed by SOF/VEL in HIV-HCV co-infection; any anti-HBV activity comes from TAF |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Phase 4 | Completed | 64 | HCV screening and treatment program in prisons; not an HBV efficacy study |
| [NCT02363517](https://clinicaltrials.gov/study/NCT02363517) | Phase 3 | Unknown | 420 | Sofosbuvir plus ledipasvir in people who inject drugs; HCV-focused |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completed | 803 | Simplified HCV treatment demonstration project in Myanmar; not designed for HBV outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label trial | J Med Virol | Ledipasvir/sofosbuvir for 12 weeks in HBV mono-infected subjects; primary endpoint was HBsAg decline, secondary was HBV DNA decline |
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | Multicenter study | J Clin Transl Hepatol | Safety and efficacy of SOF/VEL with TAF pre-treatment on HBV reactivation in HBV/HCV co-infection |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Cohort | J Clin Med | Different HBV-DNA and HBsAg kinetics in HCV co-infected patients during DAA therapy, with and without sofosbuvir |
| [42145438](https://pubmed.ncbi.nlm.nih.gov/42145438/) | 2026 | Comparative effectiveness study | Bioinformation | Four antiviral regimens in 480 patients; sofosbuvir-based regimens for HCV, tenofovir or entecavir for HBV |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | Review | J Clin Virol | HBV reactivation as a challenge during DAA treatment of HCV |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation in cancer patients with HBV/HCV co-infection receiving DAAs |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | HBV reactivation with an immune-escape mutant during sofosbuvir/velpatasvir therapy |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Case report | Hosp Pharm | HBV reactivation during simeprevir plus sofosbuvir treatment of HCV |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral medications for hepatitis B and C and their effects on kidney function |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Management of pediatric viral hepatitis; HBV treatment is far from curative |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02418355 | SOVALDI | Not available | Not available |
| 02432226 | HARVONI | Not available | Not available |
| 02456370 | EPCLUSA | Not available | Not available |
| 02467542 | VOSEVI | Not available | Not available |

All four authorizations are currently valid single-entity listings. Dosage form and approved indication text were not available in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions:** Eight interactions were identified.
  - **Major:** apalutamide, enzalutamide, lorlatinib
  - **Moderate:** fostamatinib, warfarin, dicoumarol, encorafenib
  - **Minor:** cyclosporine
- **HBV reactivation:** Published cohorts and case reports show that HBV reactivation can occur during sofosbuvir-based HCV therapy in HBV/HCV co-infected patients. This is directly relevant to any HBV repurposing question and calls for HBV screening and monitoring or prophylaxis.

For other warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but sofosbuvir has no direct mechanistic target in HBV. The only HBV-specific clinical study is a small, single-arm Phase 2 pilot of a combination product. Most other studies are HCV trials in co-infected patients, and their main HBV signal is a reactivation risk rather than a benefit. The L2 level assigned in the data compiled for this report is generous given this. Treat the indication as a research question, not a development candidate.

**To proceed, the following is needed:**
- Mechanism-of-action data (MOA) and in vitro evidence of anti-HBV activity for sofosbuvir alone, not in combination with ledipasvir
- Controlled HBV mono-infection studies with a comparator and durable endpoints (HBsAg loss, HBV DNA suppression)
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- An HBV screening and reactivation monitoring plan for any study in HBV-exposed patients
- A review of the interaction profile, especially with strong inducers such as apalutamide and enzalutamide
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

