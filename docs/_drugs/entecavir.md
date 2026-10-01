---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 330
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue antiviral whose established use is chronic hepatitis B (HBV).
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but the **40 matched clinical trials** and **20 publications** are almost all about HBV or HBV/HCV coinfection, and none shows entecavir treating HCV itself.
This prediction is best treated as a model artifact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B (the license records in the pack contain no indication text) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From general pharmacology, entecavir is a guanosine nucleoside analogue. Its triphosphate form inhibits HBV polymerase, blocking priming, reverse transcription and DNA synthesis.

HBV and HCV are both hepatotropic viruses, and they often occur together, which likely explains the graph proximity behind the high score. Mechanistically, though, they differ. HBV is a DNA virus with a reverse-transcription step. HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, and entecavir has no established activity against it.

The retrieved trials and papers are largely HBV studies, or HBV/HCV coinfection studies in which entecavir treats only the HBV component. The high TxGNN score most likely reflects closeness to viral hepatitis nodes in the knowledge graph, not a real anti-HCV effect.

## Clinical Trial Evidence

The table shows the 10 most relevant of the 40 matched trials, prioritising HCV/HBV coinfection studies. None of them tests entecavir as an HCV treatment.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Direct-acting antivirals in HCV/HBV coinfection; monitors HBV reactivation during anti-HCV treatment. Entecavir is not the HCV-active agent. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Whether nucleos(t)ide analogue prophylaxis (12 vs 24 weeks) prevents HBV reactivation in HCV/HBV patients receiving DAA therapy. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Entecavir for chronic hepatitis B in HCC patients after radiofrequency ablation. |
| [NCT01928511](https://clinicaltrials.gov/study/NCT01928511) | Phase 4 | Completed | 254 | Switching to or adding pegylated interferon in HBV patients on long-term nucleos(t)ide therapy. Matched to HCV by keyword only. |
| [NCT02881008](https://clinicaltrials.gov/study/NCT02881008) | Phase 1/2 | Completed | 48 | Myrcludex B versus entecavir in HBeAg-negative chronic hepatitis B. Entecavir is the HBV comparator. |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Early viral load reduction with entecavir versus adefovir in nucleoside-naive chronic hepatitis B. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Entecavir versus adefovir in HBV with hepatic decompensation. |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Early HBV DNA kinetics with telbivudine or entecavir. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Antiviral effect of entecavir in Black/African American and Hispanic patients with chronic HBV. |
| [NCT05416008](https://clinicaltrials.gov/study/NCT05416008) | N/A | Unknown | 150 | Long-term nucleos(t)ide analogue use and hepatic steatosis in chronic hepatitis B. |

## Literature Evidence

The table shows the 10 most relevant of the 20 retrieved publications, prioritising HBV/HCV coinfection topics.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide therapy; studies whether HCV reactivates and how HCV RNA evolves after anti-HBV treatment. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Treatment advances in HBV/HCV coinfection, a group at high risk of cirrhosis and HCC. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review / case report | Clin Res Hepatol Gastroenterol | HBV/HCV coinfection as a therapeutic challenge, with more severe liver injury and higher HCC risk. |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Observational | J Viral Hepat | Low incidence of HBV reactivation in HCV patients receiving direct-acting antivirals (25 coinfected and 765 resolved-HBV patients). |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | Risk of HBV reactivation during DAA therapy for chronic hepatitis C with HBV infection. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for hepatitis B and C and their effects on kidney function. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Managing hepatitis B and C around liver and kidney transplantation. Entecavir and tenofovir prevent HBV recurrence, with renal dose adjustment. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Management of viral hepatitis B and C in children. |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Review | Chin Clin Oncol | Timing and management of hepatitis B and C in patients with HCC. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Therapy of chronic viral hepatitis (B, C and D). Nucleos(t)ide analogues are the long-term backbone for HBV. |

## Canada Market Information

Dosage form and approved-indication text are not included in the license records provided. Five of the 10 DINs are listed below.

| DIN | Product Name |
|---------|------|
| 02485907 | MINT-ENTECAVIR |
| 02448777 | AURO-ENTECAVIR |
| 02396955 | APO-ENTECAVIR |
| 02282224 | BARACLUDE |
| 02467232 | JAMP ENTECAVIR |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir has no established anti-HCV mechanism, and the supporting trials and papers are all about HBV or HBV/HCV coinfection. The high TxGNN score is best explained by graph proximity to viral hepatitis nodes. The HBV indication (rank 2 in this pack) is on-label and well supported, so it is not a repurposing case.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- In vitro HCV replicon or other preclinical data showing entecavir activity against HCV
- Evidence that entecavir (not a direct-acting antiviral) improves HCV outcomes; without it, this candidate should not advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

