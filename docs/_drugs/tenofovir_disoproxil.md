---
layout: default
title: Tenofovir Disoproxil
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Tenofovir Disoproxil: From Human HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir disoproxil is an antiretroviral drug already established for HIV in humans. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection in cats)**. This is a veterinary research question, supported by **2 animal studies** and **4 human HIV trials** that do not test tenofovir in cats.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the licence data provided (tenofovir is established for HIV in humans) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical/animal studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on general pharmacology, tenofovir is a nucleotide reverse transcriptase inhibitor. Its efficacy against HIV in humans is established, and mechanistically it may be applicable to feline immunodeficiency virus (FIV).

FIV is a lentivirus that causes progressive immune dysfunction in cats, similar to HIV in humans. It has a related reverse transcriptase, so the link is plausible. No antiviral is currently registered for FIV-infected cats, which makes the question practically relevant.

The high graph score probably reflects the similar disease phenotype, not independent human evidence. The only direct evidence is veterinary: tenofovir (PMPA) and combination antiretroviral therapy have been tested in FIV-infected cats. Because tenofovir is already established for HIV in humans, this is not a new human repurposing candidate.

---

## Clinical Trial Evidence

All four registered trials are in human HIV and none is feline. Tenofovir is not the evaluated intervention in any of them, so none supports the predicted indication directly.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose selection of once-daily dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in treatment-naive HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir plus lamivudine vs boosted darunavir plus emtricitabine/tenofovir or lamivudine/tenofovir in naive HIV-1 patients |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir plus abacavir/lamivudine vs Atripla (efavirenz/emtricitabine/tenofovir DF) over 96 weeks in HIV-1 |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, each with a dual NRTI backbone (abacavir/lamivudine or tenofovir DF/emtricitabine), over 96 weeks |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal study (FIV-infected cats) | Viruses | Evaluated pharmacokinetics and clinical outcomes of combination ART (dolutegravir, tenofovir, emtricitabine) in FIV-infected domestic cats |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Animal study (FIV-infected cats) | J Feline Med Surg | Treatment of naturally FIV-infected cats with PMPA (tenofovir); the abstract notes no antiviral is registered for FIV and that human antivirals used in cats have caused serious adverse effects |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2403889 | TEVA-TENOFOVIR |
| 2523922 | TENOFOVIR |
| 2453940 | PMS-TENOFOVIR |
| 2247128 | VIREAD |
| 2512939 | MINT-TENOFOVIR |

Showing 5 of 20 authorizations. Dosage form and approved indication text are not available in the provided data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is two animal studies in FIV-infected cats, and the registered trials are all human HIV studies that do not test tenofovir in cats. This is a veterinary research question, not a human repurposing candidate. The other predictions for this drug are also on Hold: simian immunodeficiency virus infection has macaque-only preclinical support, and the remaining two (a rare neurodevelopmental disorder and an obsolete hyperlipidemia term) have no evidence and no plausible mechanism.

**To proceed, the following is needed:**
- Full results and outcomes from the feline studies (PMID 37112803 and 24782459), including efficacy and adverse effects in cats
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A veterinary regulatory pathway assessment, since the target species is not human
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

