---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 3
---

# Dolutegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir (DTG) is an integrase strand transfer inhibitor (INSTI) antiretroviral drug, widely established as a first-line treatment for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**, supported by **5 clinical trials** (all conducted in human HIV-1, providing mechanistic background) and **1 preclinical publication** directly evaluating dolutegravir-based combination antiretroviral therapy in FIV-infected cats.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (adults and paediatric patients) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 — Preclinical / animal study |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current evidence pack. Based on well-established published literature, dolutegravir is a second-generation integrase strand transfer inhibitor (INSTI). It binds the catalytic core domain of the retroviral integrase enzyme, chelating the two magnesium ions at the active site (the DDE catalytic triad: D64, D116, E152) and blocking the strand transfer step required for proviral DNA integration into the host cell genome. This mechanism is the basis for dolutegravir's robust clinical activity against HIV-1 in humans.

Feline Immunodeficiency Virus (FIV) belongs to the same *Lentivirus* genus as HIV-1, and both viruses depend on an integrase enzyme to complete proviral integration. This shared biological dependency is the core mechanistic rationale for the TxGNN prediction. However, the FIV integrase catalytic domain shares only approximately 40–50% amino acid sequence identity with HIV-1 integrase — significantly lower than the >80% identity seen between HIV-1 and SIV integrases. As a result, dolutegravir's binding affinity, inhibitory potency, and in vivo pharmacokinetics in cats (given feline hepatic metabolism differences) cannot be directly extrapolated from human data and must be independently validated.

One preclinical study (PMID 37112803, 2023) directly evaluated a dolutegravir-containing combination antiretroviral regimen (DTG 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) in FIV-infected domestic cats, providing the first real-world pharmacokinetic and clinical outcome data in the target species. While promising as a proof-of-concept, this remains a single animal observational study. Dose optimisation, long-term safety, and comparative efficacy against FIV specifically have not been established in controlled trials.

---

## Clinical Trial Evidence

> **Note:** No clinical trials for dolutegravir specifically in feline FIV have been registered. The five trials below were conducted in human HIV-1 patients and provide mechanistic and pharmacological background for dolutegravir's integrase inhibition activity. They cannot be directly extrapolated to FIV.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | 48-week RCT: dolutegravir 50 mg QD vs raltegravir 400 mg BID in antiretroviral-experienced, integrase-naïve HIV-1 adults. Established non-inferiority of DTG. |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | 96-week RCT: dolutegravir 50 mg QD vs raltegravir 400 mg BID with dual NRTI backbone in treatment-naïve HIV-1 adults. Confirmed safety and antiviral efficacy gold standard. |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | 96-week RCT: dolutegravir + ABC/3TC vs Atripla (EFV/FTC/TDF) in treatment-naïve HIV-1 adults. DTG arm showed superior virological response and tolerability. |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | CNS penetration study: measured CSF:plasma DTG concentration ratios in ART-naïve HIV-1 adults. Relevant for understanding CNS compartment drug levels (species-specific caution required). |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2b | Completed | 208 | Dose-selection study in treatment-naïve HIV-1 adults. Established 50 mg QD as the optimal human dose; feline dosing requires independent determination. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal / Preclinical | *Viruses* | Evaluated pharmacokinetics and clinical outcomes of combination ART (dolutegravir 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) in FIV-infected specific-pathogen-free cats. Assessed immunophenotype changes. First direct in vivo FIV feline evidence for dolutegravir-based cART. |

---

## Canada Market Information

Dolutegravir is currently **not marketed in Canada** and has no active Drug Identification Numbers (DINs) on file.

---

## Safety Considerations

Detailed Canadian product monograph warnings and contraindications are not available in the current evidence pack.

> Please refer to the Health Canada product monograph and the package insert for complete safety information, including warnings regarding neural tube defects associated with periconceptional exposure (Tsepamo study, *Lancet* 2019), hypersensitivity reactions, hepatotoxicity, and drug interactions (particularly with dofetilide, which is contraindicated with dolutegravir).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for dolutegravir activity against FIV is biologically plausible given shared lentiviral integrase dependency, but the evidence base is limited to a single small animal observational/preclinical study with no controlled efficacy trials in the target species. The FIV integrase shares only ~40–50% sequence homology with HIV-1 integrase, meaning in vitro potency against FIV integrase must be independently confirmed. Furthermore, dolutegravir has no current regulatory footprint in Canada (0 DINs), and formal veterinary regulatory pathways would apply.

**To proceed, the following is needed:**

- **In vitro integrase inhibition assay**: Confirm dolutegravir binding affinity and IC₅₀ against purified FIV integrase protein
- **Feline pharmacokinetic study**: Establish target plasma concentration thresholds, oral bioavailability, and metabolic clearance in domestic cats
- **Controlled efficacy study in FIV-infected cats**: Compare virological suppression (FIV RNA load) and CD4+ T-cell recovery between DTG-containing cART vs placebo or standard of care
- **Drug safety and tolerability data in cats**: Formal feline toxicology data and adverse event monitoring
- **Regulatory pathway clarification**: Determine whether this falls under veterinary drug regulation (e.g., Health Canada Veterinary Drugs Directorate) or a compassionate use framework
- **MOA data from DrugBank**: Complete the Drug Level data gap (DG002) to support mechanistic documentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

