---
layout: default
title: Mycophenolate Mofetil
parent: Model Prediction Only (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Prevention of Organ Rejection to HIV Infection

## One-Sentence Summary

Mycophenolate mofetil (MMF) is an immunosuppressant best known for preventing rejection of transplanted organs, and it is also used off-label in autoimmune conditions.
The TxGNN model predicts it may be effective for **HIV infectious disease**, with **10 clinical trials** and **20 publications** linked to this prediction.
Only 2 of those trials test MMF directly in HIV. One has unknown status and the other was withdrawn with no participants, so the clinical evidence is thin and mixed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data provided. Prevention of allograft rejection is the standard use for MMF and is referenced in the literature. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 (borderline: the only completed randomized Phase 2 study combined MMF with an investigational drug) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. MMF is known to work by inhibiting IMPDH (inosine monophosphate dehydrogenase), an enzyme needed to make guanosine nucleotides. This mechanism explains its suppression of lymphocytes in transplant and autoimmune use.

The same mechanism could matter in HIV in two ways. First, depleting guanosine pools lowers the supply of nucleotide building blocks that HIV reverse transcription needs. Laboratory and early clinical work suggests this can strengthen abacavir and other nucleoside reverse transcriptase inhibitors. Second, chronic immune hyperactivation drives CD4 T-cell loss in HIV. A 2006 review (Argyropoulos & Mouzaki) discusses immunosuppressants as a way to target it.

The clinical picture is mixed. Some small studies show falling viral load or good tolerability. Others show no antiviral benefit. Immunosuppression in a person already living with HIV is a genuine safety concern.

---

## Clinical Trial Evidence

Only trials with a direct HIV link are strongest; most others are transplant or unrelated studies that matched on keywords.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study: tests whether MMF reduces immune hyperactivation and slows CD4 decline in antiretroviral-naive HIV-1 patients. No results visible. |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy: MMF effect on cardiovascular surrogate markers in HIV-1 infection. Not an antiviral endpoint. |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Planned MMF plus abacavir study for antiviral activity in treatment-experienced patients. No participants enrolled, so it provides no evidence. |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Placebo-controlled study of an investigational drug (DAPD) versus DAPD plus MMF added to anti-HIV regimens. MMF is an add-on, not the main study drug. |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Kidney transplantation in HIV-infected patients with end-stage renal disease. MMF is likely part of the regimen, so it informs safety, not HIV treatment. |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Follow-up of graft rejection after kidney transplant in HIV-1 patients on a raltegravir-based regimen. Not an efficacy trial for MMF in HIV. |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Stem cell transplant for HIV-positive patients. MMF is only a graft-versus-host disease prevention component. |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | Mismatched-donor bone marrow transplant with MMF as graft-versus-host disease prophylaxis. Not HIV-specific. |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine plus MMF versus cyclophosphamide plus prednisolone for anti-EPO antibody pure red cell aplasia. Unrelated to HIV. |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Conditioning regimen for transplant in elderly AML patients. MMF is incidental. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical study (not classified) | AIDS | HAART with or without MMF in treatment-naive patients. Examined effect on HIV-1 RNA decay and the latent reservoir. Results not visible in the available excerpt. |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | 17 patients with early chronic HIV. Tested MMF during and after interruption of HAART. |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort (5 patients) | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing regimens in patients failing therapy was associated with dGTP depletion and a decrease in plasma HIV-1 RNA. |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | 7 AIDS patients with multidrug-resistant HIV. MMF in combination therapy was well tolerated despite advanced disease. |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study (not classified) | AIDS | DAPD with or without MMF in drug-resistant HIV. Evaluated safety, tolerability and antiretroviral activity. |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects of MMF plus HAART in treatment-naive acute and chronic HIV-1 patients. |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort | Clin Pharmacokinet | Pharmacokinetics and pharmacodynamics of low-dose MMF with abacavir, efavirenz and nelfinavir. Monitoring recommended because of the low doses. |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | Cohort | Clin Pharmacokinet | Effect of MMF on antiretroviral drug levels and on intracellular nucleotide pools (dCTP, dGTP). |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Discusses targeting chronic immune activation in HIV with immunosuppressive drugs. |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | Retrospective study | Am J Transplant | Kidney transplantation in 27 HIV-infected patients in Paris, using MMF, steroids and tacrolimus or cyclosporine. |

---

## Canada Market Information

15 licences are on record; 5 are shown. Dosage form and approved-indication text were not provided in the source data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02444836 | Mycophenolate Mofetil for Injection, USP | — | — |
| 02242145 | CellCept | — | — |
| 02522233 | MAR-Mycophenolate Mofetil | — | — |
| 02313855 | Sandoz Mycophenolate Mofetil | — | — |
| 02386399 | JAMP-Mycophenolate Capsules | — | — |

---

## Safety Considerations

- **Immunosuppression in HIV**: MMF suppresses T-cell proliferation, which is a safety concern in people who already have impaired immunity.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.86% TxGNN score is high, and there is a plausible mechanism (IMPDH inhibition, enhancing nucleoside analogues, calming immune activation). However, results from the small HIV studies are mixed, and the only trials that test MMF directly in HIV are unresolved (one of unknown status, one withdrawn). No Phase 3 efficacy trial exists, and the immunosuppression risk in HIV is significant.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Published results, or a status update, for the MAN2 study (NCT00120419)
- Results of the HAART ± MMF studies (e.g., PMID 15353978) to settle the antiviral efficacy question
- A safety assessment of immunosuppression risk in HIV, including opportunistic infection risk and CD4 monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

