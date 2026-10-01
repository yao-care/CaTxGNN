---
layout: default
title: Lopinavir
parent: Model Prediction Only (L5)
nav_order: 553
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, marketed in Canada as KALETRA. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, a nonhuman primate research model rather than a human indication. Support consists of **0 clinical trials** and **3 animal-model publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from drug class; no approved indication text was provided in the Canadian licence records) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (animal and preclinical studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Lopinavir is known as an HIV-1 protease inhibitor, and SIV is the nonhuman primate counterpart of HIV. Mechanistically, a protease inhibitor could plausibly act against SIV, although SIV protease is related to HIV-1 protease but not identical.

The very high score (0.999) most likely reflects how close HIV and SIV sit in the knowledge graph. SIV infection is a laboratory model used to test antiretrovirals. It is not a human clinical indication, so this prediction is not a true repurposing signal.

The other two top predictions are also weak:
- **Feline acquired immunodeficiency syndrome** (score 99.90%, evidence level L5): FIV is a lentivirus, so a protease-inhibitor link is plausible in principle. This is a veterinary condition, and no trials or literature were found.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.90%, evidence level L5): no plausible mechanistic link to antiviral protease inhibition was identified, and the score is likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

All three publications are animal studies (tier 3).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Four SIVmac251-infected cynomolgus macaques received a 7-day quadruple antiretroviral regimen, and viral decay was rapid. The available excerpt does not confirm that lopinavir was a component. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model development | Microbes Infect | A chimeric SHIV carrying the HIV-1 protease gene was built as a tool for testing protease inhibitors in vivo. It caused weak but long-lasting infection in rhesus macaques, and a peptide-analog protease inhibitor blocked its growth in cell culture. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | J Virol Methods | Two SHIV 89.6P-infected rhesus macaques received oral AZT, 3TC and lopinavir/ritonavir for 28 days. The study examined effects on the peripheral CD8 subset. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02285533 | KALETRA |
| 02312301 | KALETRA |
| 02243644 | KALETRA |

Dosage form, manufacturer and approved indication text were not provided for these licences.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug-interaction records were available in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an animal research model, not a human disease, so it is not a genuine repurposing opportunity. Evidence is limited to three animal studies with no registered clinical trials. The same applies to the other top-ranked predictions, which have no supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmed original indication and dosage form details for the three KALETRA DINs
- Review of lower-ranked predictions for human indications with real clinical relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

