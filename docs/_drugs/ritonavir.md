---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 809
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor, used mainly as a CYP3A4 booster in HIV-1 combination regimens and in products such as Kaletra and Paxlovid.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**.
Only **1 clinical trial** (human HIV-1, indirect) and **0 publications** touch this indication, so the prediction is essentially model-driven.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (taken from the rationale text; the licence indication fields are empty) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (no feline or FIV study; the Evidence Pack scores it L4 based on indirect evidence only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, ritonavir inhibits HIV-1 protease and strongly inhibits CYP3A4, which is why it is widely used to boost other protease inhibitors.

Feline acquired immunodeficiency syndrome is caused by feline immunodeficiency virus (FIV), a lentivirus related to HIV. The high score most likely reflects the shared lentivirus and protease-inhibitor neighborhood in the knowledge graph. This link is weak. FIV protease has different substrate specificity from HIV-1 protease, so cross-species activity cannot be assumed. No feline efficacy data are provided.

A closely related prediction, simian immunodeficiency virus infection (rank 2), has more support. That support is preclinical only. In vitro, SIVmac239 was inhibited by ritonavir at 13 ± 5 nM, versus 25 ± 14 nM for HIV-1 (PMID 12709355). SIV in macaques is a research model for HIV, not a human clinical indication, and it does not establish activity against FIV.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs boosted darunavir + tenofovir/emtricitabine or lamivudine in treatment-naïve HIV-1 patients. Humans, not cats; ritonavir is only the booster, so this gives no direct evidence for FIV (relevance grade C). |

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02357593 | NORVIR |
| 02523620 | AURO-RITONAVIR |
| 02524031 | PAXLOVID |
| 02312301 | KALETRA |
| 02285533 | KALETRA |

These are human-use authorizations. The Evidence Pack lists 7 DINs in total but includes only the 5 shown here. Dosage form and approved indication text are empty in the data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any feline or FIV data. The only trial is an indirect human HIV-1 study in which ritonavir is just a booster. FIV protease differs from HIV-1 protease, and the Canadian licences cover human use only.

**To proceed, the following is needed:**
- In vitro FIV protease or antiviral susceptibility data for ritonavir
- Feline pharmacokinetic and efficacy or safety data
- Mechanism of action data (MOA) and original indication records in the Evidence Pack
- Health Canada package insert warnings and contraindications
- A veterinary regulatory pathway assessment, since the current Canadian licences are for human use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

