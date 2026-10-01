---
layout: default
title: Lamivudine
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Lamivudine: From Human Retroviral Therapy to Feline Immunodeficiency Virus Infection

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor (NRTI) marketed in Canada. The approved-indication text was not supplied, but the supporting trials are in human HIV-1. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection)**. Support is indirect: **5 clinical trials**, all in human HIV-1 and none in cats, plus **5 publications** on FIV, of which only two are cat cohort studies and the rest are preclinical. This is a veterinary indication, not a human repurposing target.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (preclinical and mechanism studies; no clinical trial tests FIV) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, lamivudine is an NRTI that terminates the growing viral DNA chain. FIV is a lentivirus whose reverse transcriptase is homologous to that of HIV-1, so the mechanism is plausible for FIV.

The supplied trials are all in human HIV-1 and use lamivudine-containing backbones such as abacavir/lamivudine or darunavir plus lamivudine. They support the lentiviral mechanism but say nothing about efficacy in cats. The only species-specific evidence comes from small veterinary and laboratory studies of AZT/3TC-based combinations. The abstracts show the drug acts on FIV, but they do not by themselves establish clinical benefit.

The approved-indication text for the Canadian licences was not supplied, so this report does not use the human label as a reference point. The high TxGNN score reflects knowledge-graph similarity, not clinical proof.

## Clinical Trial Evidence

None of these trials tests FIV. All are in human HIV-1, so they are indirect support at most.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in treatment-naïve HIV-1 patients |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose selection for once-daily dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in treatment-naïve HIV-1 adults |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs Atripla over 96 weeks in treatment-naïve HIV-1 adults |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, each with a dual NRTI backbone (ABC/3TC or TDF/FTC), in treatment-naïve HIV-1 adults |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Single-arm study of dolutegravir + abacavir/lamivudine, with CNS and plasma pharmacokinetics in HIV-1 adults |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort | Viruses | Compared ZDV alone, ZDV + interferon-α, ZDV + lamivudine and ZDV + valproic acid in naturally FIV-infected cats over one year, tracking viral load and CD4+/CD8+ ratio; results not shown in the abstract |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort | J Feline Med Surg | Follow-up of long-term antiretroviral therapy in FIV-infected cats, starting with AZT over 5–6 years; results not shown in the abstract |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Preclinical | Vet Immunol Immunopathol | In vitro and in vivo evaluation of AZT/3TC against FIV; combination was additive to synergistic in primary PBMC but not in chronically infected cells |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Preclinical | Antiviral Res | Combined ZDV, 3TC and abacavir suppressed FIV replication in vitro; the abstract notes the cat is a model for HIV |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | Am J Vet Res | Compared replication kinetics and nucleoside analog susceptibility of FIV clones, including two 3TC-resistant pol mutants |

## Canada Market Information

The pack lists 20 licences in total. The dosage form, manufacturer and approved-indication fields were empty for all of them, so only the first five are listed here.

| DIN | Product Name |
|---------|------|
| 02369052 | APO-LAMIVUDINE |
| 02512467 | JAMP LAMIVUDINE HBV |
| 02192683 | 3TC |
| 02507129 | JAMP LAMIVUDINE |
| 02507110 | JAMP LAMIVUDINE |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the FIV literature is supportive, but it is small, mostly in vitro or preclinical, and no cat trial has been retrieved. The clinical trials supplied are all in human HIV-1. FIV is a veterinary indication, so it is not a target for human repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the two cat cohort studies (PMIDs 22816032 and 25855689), whose abstracts do not show outcomes
- A decision on whether a veterinary indication is in scope for this programme
- Approved-indication text for the Canadian licences, so the human label can be compared with the prediction

**Other predictions in the pack (not evaluated in detail):**
- Simian immunodeficiency virus infection: macaque studies with lamivudine-containing regimens support the mechanism as a preclinical model. It is not clinical repurposing evidence.
- Chronic hepatitis C: the retrieved material is mostly about hepatitis B or HCV regimens without lamivudine, which looks like disease-mapping noise. No anti-HCV activity is shown.
- The other two predictions (a neurodevelopmental disorder, and an obsolete familial combined hyperlipidemia term) have no supporting evidence; the obsolete term needs remapping first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

