---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Darunavir
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

# Darunavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor used to treat HIV infection in humans.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, but the only supporting evidence is **1 clinical trial** in human HIV-1 patients (indirect) and **0 publications** on the feline disease. This is a model prediction, not a demonstrated new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (indirect evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Darunavir is a known HIV-1 protease inhibitor. It blocks cleavage of the viral Gag-Pol polyprotein, which prevents the virus from maturing into infectious particles.

Feline immunodeficiency virus (FIV) is a lentivirus closely related to HIV, so a graph-based model like TxGNN would plausibly link the two diseases through shared lentiviral biology. The high score most likely reflects this shared biology rather than a genuinely new indication.

There is an important caveat. FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so darunavir's antiviral activity in humans cannot be assumed to carry over to cats. No feline or veterinary data were provided.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Randomized, open-label comparison of boosted darunavir + lamivudine vs boosted darunavir + tenofovir/emtricitabine or tenofovir/lamivudine in treatment-naïve adults with HIV-1. It supports darunavir's antiretroviral use in humans but does not study FIV. |

## Literature Evidence

Currently no related literature available for feline immunodeficiency.

For context, the second-ranked prediction, simian immunodeficiency virus (SIV) infection, has 4 preclinical macaque studies (2011–2016) on combination antiretroviral regimens. These are PMIDs 26150024, 25033210, 22737073 and 21505294. Darunavir's specific role in each regimen could not be confirmed from the truncated data, and these studies are model-level readouts of the human HIV indication.

## Canada Market Information

Dosage form, manufacturer and approved indication text were not provided for these licenses.

| DIN | Product Name |
|---------|------|
| 2486121 | AURO-DARUNAVIR |
| 2487241 | APO-DARUNAVIR |
| 2486148 | AURO-DARUNAVIR |
| 2487268 | APO-DARUNAVIR |
| 2521350 | DARUNAVIR |

The 5 listed authorizations are a subset of the 8 total.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on shared lentivirus biology, not on any feline or veterinary data. The single trial is a human HIV-1 study, which is indirect evidence at best. The other predicted indications are weaker still. A neurodevelopmental disorder has no mechanistic link, and an obsolete familial hyperlipidemia term conflicts with the known lipid-raising effects of protease inhibitors. Both have no supporting studies.

**To proceed, the following is needed:**
- Veterinary data: in vitro FIV protease inhibition, and pharmacokinetic and efficacy studies in cats
- Comparison of FIV and HIV-1 protease structure and inhibitor sensitivity
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- Detailed mechanism of action data from DrugBank
- Approved indication text, dosage forms and manufacturers for the Canadian licenses
- Confirmation that a veterinary indication falls within the intended scope of this repurposing evaluation

*This report is for research reference only and does not constitute medical or veterinary advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

