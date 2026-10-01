---
layout: default
title: Tenofovir Alafenamide
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tenofovir Alafenamide: From HIV/Hepatitis B Antiviral Use to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir alafenamide (TAF) is a nucleotide reverse transcriptase inhibitor marketed in Canada in products such as VEMLIDY, DESCOVY, BIKTARVY and ODEFSEY. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**. This is supported by **1 loosely related clinical trial** and **8 publications**, all preclinical, mostly in macaque models. The prediction mainly reflects TAF's known anti-HIV activity rather than a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the input data (the brand names suggest HIV-1 and chronic hepatitis B) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. TAF is a prodrug of tenofovir, a nucleotide reverse transcriptase inhibitor that acts on lentiviral reverse transcriptase. It is delivered efficiently to lymphoid cells, where the active metabolite blocks viral DNA synthesis.

SIV and SHIV infection in macaques are the standard preclinical models for testing HIV antiretrovirals. A high model score for SIV infection is therefore mechanistically coherent. The macaque studies show protection against vaginal and rectal SHIV challenge, as well as use in remission strategies.

This is not a true repurposing signal. SIV infection is a non-human primate disease, and the evidence mostly confirms TAF's known anti-HIV activity (pre-/post-exposure prophylaxis) in animal models. The input also lists no original indications, so the relationship between the original and predicted indications cannot be assessed directly.

The same model run also ranked two other predictions:
- **Feline acquired immunodeficiency syndrome:** a veterinary indication with no trials or literature, so it is outside the scope of human repurposing.
- **A rare neurodevelopmental disorder (ataxic gait, absent speech, decreased cortical white matter):** no plausible mechanistic link and no evidence, so it is most likely a knowledge-graph artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab plus antiretroviral therapy to achieve virological remission in HIV-infected patients. TAF is at most a background ART component, and the population is human HIV rather than SIV, so this is only indirect support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical animal study | J Infect Dis | TAF/elvitegravir vaginal inserts gave extended post-exposure protection against SHIV in macaques. Earlier work showed 93% (before exposure) and 100% (after exposure) protection. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical animal study | J Infect Dis | Oral TAF/emtricitabine and TAF alone were tested against repeated vaginal SHIV exposure in macaques. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical animal study | J Infect Dis | Oral emtricitabine/TAF chemoprophylaxis protected macaques from repeated rectal SHIV exposure. |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical animal study | Nat Commun | Early treatment with oral emtricitabine/TAF plus long-acting cabotegravir/rilpivirine was studied for SHIV remission in macaques. |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Preclinical animal study | J Antimicrob Chemother | A biodegradable TAF-releasing implant was evaluated for safety and vaginal protection in macaques. |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Preclinical animal study | J Acquir Immune Defic Syndr | Oral tenofovir disoproxil fumarate and topical GS-7340 (TAF) were tested in infant macaques against repeated oral SIV challenge. |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Preclinical animal study | J Infect Dis | Oral PrEP was associated with reduced inflammation and CD4 loss in breakthrough acute SHIV infection. |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Model development | Front Immunol | A humanized mouse model was developed to test antiviral strategies against both SIV and HIV. |

---

## Canada Market Information

| License Number | Product Name |
|---------|------|
| 2464241 | VEMLIDY |
| 2454424 | DESCOVY |
| 2454416 | DESCOVY |
| 2478579 | BIKTARVY |
| 2461463 | ODEFSEY |

Seven authorizations are recorded in total; the five main ones are listed above. Dosage form and approved indication text are not available in the input.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is entirely preclinical (L4) and confirms TAF's known antiretroviral activity in non-human primate models. SIV is not a human disease, so this is not a new human indication. The single clinical trial is only loosely related.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- The drug's original approved indications and mechanism of action data (for example from the DrugBank API)
- A decision on whether SIV-model evidence has any translational value beyond the existing HIV indications, or whether a different human indication should be explored instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

