---
layout: default
title: Elvitegravir
parent: Model Prediction Only (L5)
nav_order: 324
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Elvitegravir is an HIV integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome**, which has no supporting studies. The best-supported direction is **simian immunodeficiency virus (SIV) infection**, with **0 clinical trials** and **8 preclinical publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS (the Canadian licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (rank 1, no evidence); the best-supported prediction is SIV infection (rank 2) |
| TxGNN Prediction Score | 99.89% (both feline AIDS and SIV infection) |
| Evidence Level | L5 for feline AIDS; L4 for SIV infection |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, elvitegravir is an HIV-1 integrase strand transfer inhibitor. It blocks the step in which viral DNA is inserted into the host genome, and its efficacy in HIV infection is established.

**Feline AIDS (rank 1).** The feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1 and also encodes an integrase enzyme, so activity is biologically plausible. However, there are no trials, no literature, and no laboratory data on FIV. The high score is a computational prediction, most likely driven by the disease's similarity to HIV/AIDS in the knowledge graph. Differences between the FIV and HIV-1 integrase sequences could reduce susceptibility, and this has not been tested.

**SIV infection (rank 2).** SIV and HIV-1 integrases are closely related, and the preclinical literature shows that SIVmac239 is susceptible to integrase inhibitors and develops similar resistance mutations. Macaque studies of topical tenofovir alafenamide/elvitegravir inserts showed protection against SHIV (a simian/human hybrid virus). SIV infection is not a human clinical indication, so its realistic value is as a preclinical model for HIV prevention and treatment, which overlaps with elvitegravir's existing indication. The one prophylaxis study with elvitegravir in the rectal model showed only partial protection.

**Neurodevelopmental disorder (rank 3).** The third prediction, a neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter, has no evident mechanistic link. Elvitegravir targets a viral enzyme with no relevant human counterpart, and its brain penetration is limited. This prediction is likely a network artifact and is not evaluated further.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The following publications relate to SIV infection (rank 2). All are preclinical; no literature was found for the other two predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical (macaque challenge) | J Infect Dis | Vaginal TAF/elvitegravir inserts gave extended post-exposure protection against SHIV in macaques; earlier work showed 93% (before exposure) and 100% (after exposure) protection |
| [41342257](https://pubmed.ncbi.nlm.nih.gov/41342257/) | 2026 | Preclinical (macaque challenge) | J Infect Dis | Rectal TAF/elvitegravir inserts gave partial post-exposure protection against SHIV (82.9%); 93% efficacy as pre-exposure prophylaxis |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical (humanized mouse) | Front Immunol | Dual-purpose humanized mouse model for testing antiviral strategies against both SIV and HIV |
| [17977962](https://pubmed.ncbi.nlm.nih.gov/17977962/) | 2008 | Preclinical (in vitro) | J Virol | Elvitegravir blocks HIV-1 integration by inhibiting DNA strand transfer; broad activity across subtypes and drug-resistant strains, with a resistance profile described |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Preclinical (in vitro) | Antimicrob Agents Chemother | Simian-tropic HIV as a model for studying resistance to integrase inhibitors |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Preclinical (in vitro) | J Virol | HIV integrase resistance mutations introduced into SIVmac239 and their effect on integrase inhibitor susceptibility |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical (in vitro) | J Virol | Resistance profiles of integrase inhibitors in SIVmac239; SIV is susceptible and shows resistance phenotypes similar to HIV |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Preclinical (in vitro) | Antimicrob Agents Chemother | Bictegravir and cabotegravir activity against integrase inhibitor-resistant SIVmac239 and HIV-1 |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02449498 | GENVOYA | Not specified | Not specified |
| 02397137 | STRIBILD | Not specified | Not specified |

## Safety Considerations

**Drug Interactions:** 27 interactions were identified in total. The major-level interactions among those listed are:
- Zinc acetate, zinc gluconate, zinc sulfate, and zinc chloride
- Lumacaftor
- Apalutamide

Moderate-level interactions include:
- Antacids and mineral supplements (magnesium oxide, magnesium hydroxide, magnesium carbonate, magaldrate, aluminum hydroxide, calcium carbonate, sodium citrate, sodium bicarbonate), which may reduce absorption
- Dexamethasone, orlistat, diclofenac, elagolix, somatotropin, and ethinylestradiol

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline AIDS) rests on a model score alone, and the neurodevelopmental disorder prediction has no plausible mechanism. The SIV evidence is preclinical, indirect, and shows only partial protection in one study. SIV infection is not a human indication, so its value is as a research model for HIV rather than a new treatment, and it overlaps with elvitegravir's existing approved use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism of action data (MOA)
- For feline AIDS: laboratory data on elvitegravir activity against FIV integrase
- For SIV: a defined research purpose, such as use as a model for HIV prevention, rather than a therapeutic indication
- Indication text and dosage forms for the two Canadian authorisations (GENVOYA and STRIBILD)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

