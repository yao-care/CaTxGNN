---
layout: default
title: Rilpivirine
parent: Moderate Evidence (L3-L4)
nav_order: 801
evidence_level: L4
indication_count: 5
---

# Rilpivirine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Rilpivirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used against HIV-1 infection. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is a non-human pathogen. The prediction is supported by **0 clinical trials** and **4 publications**, all preclinical or review-level, so it is a model-organism finding and not a human repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the drug class; the Canadian label text was not provided) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Rilpivirine is known as an NNRTI that inhibits HIV-1 reverse transcriptase. It is used alone (EDURANT) and in combinations with cabotegravir (CABENUVA), dolutegravir (JULUCA) and emtricitabine/tenofovir (COMPLERA).

SIV is the primate counterpart of HIV. Macaque SIV/SHIV models are widely used to test HIV-1 therapies, including long-acting cabotegravir plus rilpivirine. These studies therefore support rilpivirine's HIV-1 use only indirectly. SIV is not a human disease, so the high score probably reflects the model-organism relationship in the knowledge graph and not a new human indication.

The other predictions are weaker or more relevant to humans in different ways:
- **Feline acquired immunodeficiency syndrome:** supported only by an in vitro and structural study. It is veterinary and not relevant to a human repurposing decision.
- **A rare neurodevelopmental disorder:** no mechanism, trials or literature. It is most likely a graph-propagation artifact.
- **AIDS-related complex and congenital HIV:** these are HIV-related human conditions with more trial evidence, discussed in the conclusion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical animal study | Nature Communications | In RT-SHIV-infected macaques, oral emtricitabine/tenofovir alafenamide plus long-acting cabotegravir/rilpivirine was tested for viral remission, with or without an immune-modulating agent. Early treatment and long-lasting antiviral activity were explored. |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Preclinical animal study | Antimicrobial Agents and Chemotherapy | Long-acting rilpivirine in macaques infected with SIV containing HIV-1 reverse transcriptase selected drug-resistant variants at low frequency, which is relevant to pre-exposure prophylaxis. |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical animal study | EBioMedicine | Tested whether a single injection of long-acting cabotegravir/rilpivirine could serve as post-exposure prophylaxis in a macaque model. |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Current Opinion in HIV and AIDS | Reviews the preclinical and clinical evidence for cabotegravir in antiretroviral therapy and prevention. It focuses on cabotegravir, not rilpivirine. |

---

## Canada Market Information

Six licenses are recorded in Canada; five are listed below. Dosage form and approved indication text were not provided for these entries.

| DIN | Product Name |
|---------|------|
| 2370603 | EDURANT |
| 2497247 | CABENUVA |
| 2475774 | JULUCA |
| 2497220 | CABENUVA |
| 2374129 | COMPLERA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a non-human infection, supported only by macaque studies and one review, with no clinical trials (evidence level L4). It has no direct bearing on a human repurposing decision.

For human-relevant HIV directions, the same Evidence Pack shows more promise:
- **AIDS-related complex:** rated Proceed with Guardrails, supported by a small Phase 3 trial (n=37) of darunavir/ritonavir plus rilpivirine. It may overlap with the approved HIV-1 label and so may not be true repurposing.
- **Congenital HIV:** rated as a Research Question, with indirect evidence only.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for each Canadian license, to confirm what counts as the original indication
- If pursuing human HIV-related directions, pediatric and neonatal dosing, pharmacokinetic and safety data, plus drug interaction and resistance testing review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

