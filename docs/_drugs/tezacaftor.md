---
layout: default
title: Tezacaftor
parent: Model Prediction Only (L5)
nav_order: 898
evidence_level: L5
indication_count: 10
---

# Tezacaftor
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

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

Tezacaftor is a CFTR corrector, a drug that helps the CFTR protein fold and reach the cell surface. It is marketed in Canada in combination products for cystic fibrosis. The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from the CFTR-corrector mechanism; the license text in the pack is empty) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tezacaftor is a CFTR corrector used in combination products (SYMDEKO, TRIKAFTA, ALYFTREK). It improves folding and trafficking of the CFTR protein, and its efficacy in cystic fibrosis is established.

No established link to HIV has been identified. The high score most likely reflects proximity in the knowledge graph rather than a real antiviral mechanism. Tezacaftor is not known to act on viral replication or on host factors of HIV infection.

The other top-ranked predictions show the same pattern:
- **Viral and animal diseases:** simian immunodeficiency virus infection and feline acquired immunodeficiency syndrome have very similar scores to HIV. They appear to be graph artifacts, and neither is relevant to human repurposing.
- **Unrelated diseases:** leprosy, multiple endocrine neoplasia and female breast carcinoma have no plausible mechanistic link and no evidence.
- **Protein-misfolding hypotheses:** homozygous familial hypercholesterolemia and amyotrophic lateral sclerosis have a conceivable corrector rationale. It is untested, and tezacaftor is not known to act on the relevant proteins.
- **Rheumatoid arthritis:** this is the only one of the ten with a registered trial, but that trial does not test tezacaftor in RA (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

Among the other predicted indications, only rheumatoid arthritis (rank 7) has a linked trial. It is a non-interventional study in cystic fibrosis patients and gives no direct evidence for RA:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | NA | Completed | 47 | Analyzes blood neutrophil function and phenotype in cystic fibrosis patients, including effects of CFTR modulator treatment. It does not enroll RA patients (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved indication text are not provided in the source data. Five of the 7 authorizations are listed:

| DIN | Product Name |
|---------|------|
| 2478080 | SYMDEKO |
| 2542285 | TRIKAFTA |
| 2559676 | ALYFTREK |
| 2517140 | TRIKAFTA |
| 2526670 | TRIKAFTA |

## Safety Considerations

Please refer to the package insert for safety information. The drug-interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but no clinical trials, no literature and no plausible mechanism, so it sits at evidence level L5 (model prediction only). The other nine top predictions are in the same position, and several (SIV, feline AIDS) are not relevant to human use.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any plausible link to HIV exists
- Health Canada package insert warnings and contraindications (this blocks safety screening)
- Preclinical evidence, such as in vitro antiviral activity, before any clinical consideration
- Route and dosage-form compatibility for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

