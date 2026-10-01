---
layout: default
title: Nevirapine
parent: Moderate Evidence (L3-L4)
nav_order: 645
evidence_level: L4
indication_count: 3
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Nevirapine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used against HIV-1. The Canadian license records provided do not state the approved indication, so HIV-1 is inferred from the drug class. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and only **preclinical literature** (in vitro and macaque studies), most of it indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from drug class; not stated in the license data provided) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Nevirapine binds an allosteric pocket in HIV-1 reverse transcriptase. Detailed mechanism data was not available in the pack, so this description comes from the drug class. Because it targets the HIV-1 enzyme specifically, the mechanism does not obviously extend to SIV.

The mechanism actually argues against the prediction. Wild-type SIV and HIV-2 reverse transcriptases are generally intrinsically resistant to this class. The literature shows nevirapine is active against chimeric SHIV viruses that carry the HIV-1 RT gene (in vitro and in macaque models). In those studies nevirapine acts as a tool compound against the HIV-1 RT component, not as a treatment for SIV itself. SIV is also a nonhuman primate disease with no human indication.

The model's other top predictions are weak as well:
- **Feline acquired immunodeficiency syndrome** (score 99.85%, L4): the only support is a 2023 biochemical and structural study of NNRTIs against feline and human immunodeficiency viruses (PMID 38031646). That study is indirect, and its abstract does not show how large any nevirapine effect is.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.82%, L5): there is no identifiable mechanistic link, no literature and no trials. This looks like a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Compared 16 approved anti-HIV drugs plus one experimental drug against HIV-2, SIV and SHIV strains. Relevant to which antiretrovirals work against SIV. The abstract provided does not give nevirapine-specific results. |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro | Biochem Biophys Res Commun | A hybrid SIV carrying the HIV-1 RT gene (RT-SHIV) was markedly sensitive to NNRTIs. Plain SIV was not inhibited by this drug class. |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model | AIDS Res Hum Retroviruses | Cynomolgus monkeys infected with RT-SHIV were used to study the development of drug resistance. |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | J Virol | Characterized an SIV/HIV-1 RT chimera as a model for studying NNRTI resistance in pigtail macaques. Notes that NNRTIs do not effectively inhibit SIV RT. |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model | Virology | RT-SHIV transmitted efficiently by the vaginal route in rhesus macaques. This is a transmission model, not a treatment study. |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | Not yet classified | Virology | Pretreating HIV-1 and SIV virions with NRTIs and NNRTIs, alone or with NERT-stimulating substances, was explored as a virucide approach. |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | HIV post-exposure prophylaxis in the emergency department. Cites animal SIV studies as indirect support, but concerns HIV-1, not SIV treatment. |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro | Antimicrob Agents Chemother | Integrase inhibitors were subsynergistic with nevirapine. Nevirapine appears only as a combination partner. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2387727 | MYLAN-NEVIRAPINE |
| 2318601 | AURO-NEVIRAPINE |
| 2405776 | JAMP NEVIRAPINE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is preclinical only (L4), there are no clinical trials, and SIV is a nonhuman primate disease with no human indication. Wild-type SIV is generally intrinsically resistant to NNRTIs, so the high TxGNN score is not supported by mechanism. The macaque work uses nevirapine against the HIV-1 RT component of chimeric viruses, not against SIV.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data (e.g., via the DrugBank API) to support any mechanistic-link analysis
- Nevirapine-specific activity data against wild-type SIV, since the current literature mostly covers HIV-1 RT chimeras or other compounds
- Confirmation of the approved indication text for the three Canadian DINs
- A clear target-use case (veterinary or research tool), since SIV has no human indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

