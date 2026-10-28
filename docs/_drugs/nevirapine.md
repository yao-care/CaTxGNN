---
layout: default
title: Nevirapine
parent: Moderate Evidence (L3-L4)
nav_order: 650
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-28
description: "Nevirapine: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "NEVIRAPINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Nevirapine: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Nevirapine is an antiretroviral drug originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this rests on **0 clinical trials** and **14 publications**, nearly all preclinical (in vitro or animal models).
SIV infection is an animal-model disease rather than a human clinical indication, so this prediction is of limited practical value for human repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Canadian licence records contain no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that targets HIV-1 reverse transcriptase, and its efficacy in HIV infection is established.

SIV is a lentivirus related to HIV, which probably explains the high TxGNN score. However, the published data (for example PMIDs 15040537, 7541200 and 16859727) indicate that the reverse transcriptases of wild-type SIV and HIV-2 are intrinsically resistant to HIV-1-specific NNRTIs. Activity is expected mainly in engineered SIV/SHIV chimeras that carry HIV-1 reverse transcriptase. The score therefore likely reflects structural similarity among lentiviral targets rather than true efficacy against wild-type SIV.

Two other predictions were also reviewed:
- **Feline acquired immunodeficiency syndrome** (score 0.9985): the only evidence is one biochemical and structural study of NNRTIs against feline immunodeficiency virus reverse transcriptase (PMID 38031646). It is indirect, preclinical and veterinary.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 0.9982): there is no supporting literature or trials and no identifiable mechanistic link to nevirapine (Evidence Level L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials were found. The table lists the most relevant publications, prioritizing those that study nevirapine or NNRTIs against SIV or SIV/HIV chimeras.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Annals of Emergency Medicine | HIV post-exposure prophylaxis; no direct efficacy studies, but animal studies suggest antiretrovirals can reduce SIV infection |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model | AIDS Research and Human Retroviruses | Monkey model (RT-SHIV) for studying emergence of resistance to reverse transcriptase-targeted drugs |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model | Virology | RT-SHIV carrying HIV-1 reverse transcriptase transmits efficiently by the vaginal route in rhesus macaques |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | Susceptibility of HIV-2, SIV and SHIV to anti-HIV-1 compounds, relevant to treatment and post-exposure prophylaxis |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro | Biochem Biophys Res Commun | Chimeric SIV with HIV-1 reverse transcriptase is sensitive to NNRTIs, whereas wild-type SIV is not |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | Journal of Virology | Characterization of an SIV/HIV chimera expressing HIV-1 reverse transcriptase for NNRTI resistance studies in pigtail macaques |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | In vitro | Virology | NRTIs and NNRTIs inhibit endogenous reverse transcription of HIV-1 and SIV virions |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro | Antimicrob Agents Chemother | Integrase inhibitor L-708,906 combined with nevirapine was subsynergistic; includes SIV (mac251) activity data |
| [1283296](https://pubmed.ncbi.nlm.nih.gov/1283296/) | 1992 | In vitro | Antimicrob Agents Chemother | Nucleoside analogue FTC is active against HIV, SIV and FIV in cell culture |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | In vitro | Chem Biol Drug Des | A small molecule (3G11) blocks HIV-1 but not SIV; nevirapine is not the subject |

## Canada Market Information

The Canadian licence records do not include dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02387727 | MYLAN-NEVIRAPINE | Not listed | Not listed |
| 02318601 | AURO-NEVIRAPINE | Not listed | Not listed |
| 02405776 | JAMP NEVIRAPINE | Not listed | Not listed |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B and C virus infection, hepatitis C virus infection, rash (exanthem), Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis and nodular fasciitis. The liver and severe skin reactions are the most clinically important.
- **Drug Interactions:** 100 interactions were identified in total. The first 20 reviewed are all Moderate severity, including rabeprazole, bupropion, aprepitant, clarithromycin, the corticosteroids (triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone), saxagliptin, linagliptin, eliglustat, naldemedine, naloxegol, naltrexone, cisapride, granisetron, nitisinone, ondansetron and orlistat.

Please refer to the Health Canada package insert for official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is preclinical (in vitro and animal studies), and it indicates that wild-type SIV is intrinsically resistant to HIV-1-specific NNRTIs such as nevirapine. SIV infection is an animal-model disease with no human clinical indication. The other two predictions (feline AIDS, and a rare neurodevelopmental disorder) are weaker still, being veterinary and indirect, or purely computational.

**To proceed, the following is needed:**
- The Health Canada package insert, to complete warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A decision on whether a research-model indication (SIV or SHIV) is relevant to the repurposing goal; otherwise, consider re-ranking toward predictions with human clinical relevance
- Direct evidence of nevirapine activity against the target virus, if the veterinary or animal-model direction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

