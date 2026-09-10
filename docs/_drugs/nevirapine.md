---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 547
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed for HIV-1 infection. The TxGNN model predicts a possible link to **Simian Immunodeficiency Virus (SIV) Infection**, but this signal is supported only by **17 preclinical/mechanistic publications and zero clinical trials**, and closer reading suggests the literature cluster reflects HIV-1 drug-development animal models rather than a genuine human repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Nevirapine is an NNRTI that binds directly and non-competitively to HIV-1 reverse transcriptase, blocking viral replication. This mechanism is highly specific to the HIV-1 enzyme's binding pocket.

SIV is a lentivirus closely related to HIV-1, which is why it is used as an animal model for anti-HIV drug development. However, the reverse transcriptase sequences of wild-type SIV and HIV-1 differ substantially, and the literature consistently shows that NNRTIs — including nevirapine — do not effectively inhibit wild-type SIV. Most of the supporting evidence instead uses chimeric SHIV constructs (SIV engineered to carry the HIV-1 reverse transcriptase gene) specifically so that HIV-1-targeted drugs like nevirapine *can* be tested in a macaque model.

In other words, this evidence cluster is largely a byproduct of HIV-1 drug and vaccine research methodology (testing candidate NNRTIs in RT-SHIV/SHIV monkey models), not evidence that nevirapine treats naturally occurring SIV infection. It is also worth noting that humans are not susceptible to SIV, which limits the clinical relevance of this indication as a human repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro/Susceptibility profiling | Antiviral therapy | Evaluated 16 approved anti-HIV-1 drugs (including nevirapine) plus one experimental compound against HIV-2, SIV, and SHIV strains to inform treatment/PEP use |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro/Mechanistic | Antimicrobial Agents and Chemotherapy | Diketo integrase inhibitor combined with zidovudine, nevirapine, or nelfinavir showed only subsynergistic activity against SIV(MAC251) |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro/Resistance profiling | Biochemical and Biophysical Research Communications | Chimeric SIV carrying HIV-1 reverse transcriptase (RT-SHIV) was constructed specifically to test sensitivity to NNRTIs, since native SIV RT is not inhibited by this class |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro/Preclinical | Journal of Virology | Characterized an SIV-HIV chimera expressing HIV-1 reverse transcriptase to study NNRTI antiviral resistance evolution in pigtail macaques |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model | AIDS Research and Human Retroviruses | Cynomolgus monkeys infected with RT-SHIV (HIV-1 RT inserted into SIV) were treated to study in vivo resistance development to RT-targeted drugs |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model | Virology | Characterized vaginal transmission of RT-SHIV (encoding HIV-1 reverse transcriptase) in rhesus macaques as a preclinical transmission model |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | Mechanistic | Virology | Tested NRTIs and NNRTIs against endogenous reverse transcription of HIV-1 and SIV virions as a potential virucide strategy |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | In vitro/Mechanistic | Chemical Biology & Drug Design | Novel small-molecule RT inhibitor blocked HIV-1 replication but explicitly did **not** inhibit SIV(mac), underscoring the poor cross-reactivity of HIV-1-targeted RT inhibitors against native SIV |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro/Mechanistic | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 shown active against HIV-1 (including resistant strains), HIV-2, and SIV; used nevirapine-class comparators for context |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Annals of Emergency Medicine | Review of HIV post-exposure prophylaxis citing animal (including SIV) studies as indirect support for antiretroviral efficacy |

## Canada Market Information

Nevirapine is currently **not marketed** in Canada under this evidence pack (0 DINs on file). No Health Canada license records are available to summarize dosage forms or approved indications.

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug interaction data) are not yet available for this candidate — please refer to the package insert for safety information. Note that the TFDA/Health Canada label warnings are flagged as a **blocking data gap (DG001)**, meaning this candidate cannot yet proceed to a formal S1 safety review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting literature is entirely preclinical/mechanistic (Evidence Level L4), consists largely of HIV-1 drug-development animal models rather than evidence of efficacy against natural SIV infection, and SIV is not a human disease — limiting real-world repurposing value. No clinical trials exist, and mechanism-of-action and regulatory safety data are both currently missing (data gaps DG001, DG002).

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently blocking)
- Confirmed mechanism-of-action data from DrugBank
- Clarification of clinical relevance, since SIV does not naturally infect humans
- Note: the other two TxGNN-predicted indications for this drug (feline immunodeficiency-related syndrome, and an unrelated rare neurodevelopmental disorder) show similarly weak or absent evidence (L4/L5) and are likewise recommended for Hold pending further data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

