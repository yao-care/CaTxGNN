---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 796
evidence_level: L5
indication_count: 10
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is an antiviral that is mainly used together with peginterferon for chronic hepatitis C (the Canadian licence record does not list an indication text, so this is inferred from the trial context).
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**, but the **roughly 50 registered trials** found are almost all hepatitis C studies, and only **two enrol HBV/HCV co-infected patients**.
The prediction is therefore supported only indirectly, and no study tests ribavirin in HBV monoinfection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the licence record (chronic hepatitis C inferred from the trial context) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 (indirect and mechanistic or co-infection evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general knowledge, ribavirin is a guanosine analogue that inhibits the host enzyme IMPDH and viral RNA polymerase. Its efficacy in hepatitis C, as a partner for peginterferon, is well established.

HBV is a reverse-transcribing DNA virus, and ribavirin has no established anti-HBV activity. The very high TxGNN score most likely reflects closeness in the knowledge graph between hepatitis C, hepatitis B and HBV/HCV co-infection, not a direct antiviral mechanism against HBV.

The strongest link to HBV comes from co-infection. Reviews describe peginterferon plus ribavirin as an older option for patients with HCV/HBV co-infection who have detectable HCV RNA. In those patients, ribavirin acts against the HCV component rather than HBV.

The other nine predicted indications for ribavirin (for example IgG4-related diseases, portal hypertension conditions and hepatopulmonary syndrome) have no clinical evidence and no plausible mechanism, so they are not discussed further here.

---

## Clinical Trial Evidence

Almost none of the trials test ribavirin against HBV. The two co-infection trials are listed first, followed by representative ribavirin-containing hepatitis C trials. Relevance grades below are as assigned in the Evidence Pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in HCV/HBV co-infection versus HCV monoinfection. It is the most directly relevant trial, but no results are available in the pack. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Direct-acting antivirals in HCV/HBV co-infection, focused on HBV reactivation during anti-HCV therapy. Ribavirin is not the focus. |
| [NCT01623336](https://clinicaltrials.gov/study/NCT01623336) | Phase 2/3 | Unknown | 740 | BIP48 (peginterferon alfa-2b) versus Pegasys, both with ribavirin, in chronic hepatitis C. HCV only. |
| [NCT01805882](https://clinicaltrials.gov/study/NCT01805882) | Phase 2 | Completed | 229 | Pilot of multiple anti-HCV combination regimens. No HBV efficacy endpoint. |
| [NCT00630084](https://clinicaltrials.gov/study/NCT00630084) | Phase 4 | Completed | 120 | Peginterferon plus ribavirin in chronic hepatitis C patients with non-liver cancers. HCV only. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Ombitasvir/paritaprevir/ritonavir plus dasabuvir with ribavirin in HCV with decompensated cirrhosis. Wrong disease for this prediction. |
| [NCT00265395](https://clinicaltrials.gov/study/NCT00265395) | Phase 3 | Completed | 1428 | 72 versus 48 weeks of PEG-Intron plus Rebetol in slow-responding HCV genotype 1. HCV only. |
| [NCT00394277](https://clinicaltrials.gov/study/NCT00394277) | Phase 4 | Completed | 1175 | Higher-dose Pegasys and Copegus in heavy patients with HCV genotype 1. HCV only. |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | Sofosbuvir plus velpatasvir with or without ribavirin in HCV. HCV only. |
| [NCT00100659](https://clinicaltrials.gov/study/NCT00100659) | Phase 3 | Completed | 114 | Peginterferon with or without ribavirin in children with chronic hepatitis C. HCV only. |

---

## Literature Evidence

No randomised trials were found. The publications are reviews, mostly on HBV/HCV co-infection.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection carries a high risk of liver disease progression and should be treated aggressively. Older guidance recommended peginterferon plus ribavirin when HCV RNA is positive. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Dually infected patients progress faster than monoinfected patients. Treatment is guided by the relative viral loads of HCV and HBV. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Int | Dual HBV/HCV infection is common in endemic areas, and the viral interaction and its effect on long-term outcomes remain unresolved. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | Treating HBV/HCV co-infection remains a challenge for hepatologists (no abstract available). |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | Interferon-alpha with or without ribavirin was the prototype therapy for both viruses. Direct-acting antivirals can eliminate HCV, but HBV persists and needs long-term therapy. |
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Not classified | J Gastroenterol | Titled "Is ribavirin treatment really effective for chronic hepatitis B?", which suggests doubt about ribavirin's benefit in HBV. No abstract is available, so the conclusion cannot be confirmed. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Not classified | Annu Rev Med | Overview of treatment for chronic hepatitis B and C. For hepatitis B, interferon alfa-2b and lamivudine achieve response in a minority to a moderate share of patients. |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Not classified | Hepatology | Immune responses influence treatment-induced clearance of HBV and HCV. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B genotype predicts response to peginterferon plus ribavirin in HCV. Its relationship to HBV outcomes is less clear. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2170140 | VIRAZOLE | — | — |

The licence record does not include a dosage form or indication text.

---

## Safety Considerations

Please refer to the package insert for safety information.

One signal from the literature is worth noting. Several case reports describe porphyria cutanea tarda emerging during peginterferon/ribavirin treatment in patients with hepatitis C. This is a possible adverse event and is not evidence of benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ribavirin has no established anti-HBV activity, and the very high model score most likely reflects its link to hepatitis C. Nearly all registered trials are in hepatitis C. Only two small or incomplete co-infection studies exist, and none tests HBV monoinfection.

**To proceed, the following is needed:**
- Results from the HCV/HBV co-infection trials (especially NCT00154869) that show an HBV-specific outcome.
- Direct evidence in HBV monoinfection, such as in vitro anti-HBV activity or a controlled trial.
- The approved indication text and mechanism of action data.
- The Health Canada product monograph warnings and contraindications for a safety review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

