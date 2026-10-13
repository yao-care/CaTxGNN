---
layout: default
title: Raltegravir
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Raltegravir is an HIV-1 integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. The related prediction of simian immunodeficiency virus infection has **16 preclinical publications** (10 listed below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS (the Canadian licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, raltegravir is an HIV-1 integrase strand transfer inhibitor. It blocks the step in which viral DNA is inserted into the host genome, and its efficacy in HIV infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus, like HIV, and carries an integrase enzyme that is structurally related to HIV-1 integrase. Inhibiting integrase is therefore biologically plausible. The high score most likely reflects the shared antiretroviral and lentiviral disease neighbourhood in the knowledge graph, rather than direct evidence. Whether FIV integrase is susceptible to raltegravir has not been tested in the available data.

This is a veterinary indication, so its relevance to human drug repurposing is limited. The second-ranked prediction, simian immunodeficiency virus (SIV) infection, has preclinical support, but it serves mainly as an animal model of HIV and overlaps with the existing approved indication. It is not a true new human indication. The third prediction (a rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter) has no plausible mechanistic link to integrase inhibition and is likely an artifact of graph-based inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked prediction (feline AIDS). The table below shows the preclinical literature for the second-ranked prediction (SIV infection). Study types are inferred from titles and the data's classification, and no clinical studies are included.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Preclinical (in vitro/animal) | Retrovirology | A regimen of two nucleoside/nucleotide reverse transcriptase inhibitors plus raltegravir was established in SIVmac251-infected macaques as a model of simian AIDS |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Preclinical (animal) | Journal of Virology | Dynamics of SIV 2-LTR circles, which arise from failed integration, studied in macaques treated with an integrase inhibitor, with and without CD8+ cells |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Preclinical (animal) | Science Translational Medicine | Topical integrase inhibitors protected macaques from vaginal SHIV infection after exposure |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Preclinical (animal) | PLoS One | Resistance mutations emerged in SIV-infected macaques on non-suppressive therapy that included raltegravir intensification |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical (in vitro) | Journal of Virology | Resistance profiles of integrase inhibitors characterized in SIVmac239 |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Preclinical (in vitro) | Journal of Virology | HIV-1 integrase resistance mutations introduced into SIVmac239 affected susceptibility to integrase inhibitors |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Preclinical (in vitro) | Antimicrobial Agents and Chemotherapy | Simian-tropic HIV used as a model to study resistance to integrase inhibitors |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Not classified | PLoS Pathogens | A highly intensified multidrug regimen induced long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Preclinical (in vitro) | Clinical Infectious Diseases | Dolutegravir and raltegravir showed proadipogenic and profibrotic effects and induced insulin resistance in human/simian adipose tissue and adipocytes |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical (animal) | mBio | Lentiviral infection persisted in the brain despite effective antiretroviral therapy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02301881 | ISENTRESS | Not stated | Not stated in the data |
| 02465337 | ISENTRESS HD | Not stated | Not stated in the data |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from disease associations, not label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, rhabdomyolysis, nodular fasciitis. Muscle-related conditions are the common theme.
- **Drug Interactions**: 36 interactions were identified in total (20 shown in the data compiled for this report).
  - **Major**: zinc sulfate, zinc acetate, aluminum hydroxide, calcium carbonate. These are polyvalent cation products that may reduce raltegravir absorption.
  - **Moderate**: magnesium oxide, magnesium sulfate, magnesium chloride, orlistat.
  - **Minor**: acid-reducing agents (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), pioglitazone, dexamethasone.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score, with no clinical trials or literature, so it sits at evidence level L5. It is also a veterinary indication with limited relevance to human repurposing. The SIV preclinical work (L4) is a model of the existing HIV indication and does not constitute a new human use.

**To proceed, the following is needed:**
- Mechanism of action data for raltegravir
- Package insert warnings and contraindications from Health Canada, which are currently missing
- Direct experimental data on raltegravir activity against FIV integrase, if a veterinary direction is of interest
- A decision on whether to deprioritise this candidate in favour of human-relevant predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

