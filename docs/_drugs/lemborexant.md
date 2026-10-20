---
layout: default
title: Lemborexant
parent: Model Prediction Only (L5)
nav_order: 534
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Lemborexant: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
---

# Lemborexant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Lemborexant: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Lemborexant is a dual orexin receptor antagonist originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as its original indication. This is a re-confirmation of an existing use rather than a novel repurposing candidate. It is supported by **0 registered clinical trials** in the data compiled for this report and **20 publications**, including a Phase 3 RCT and several network meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* No clinical trial registry entries were compiled for this report. The L1 level rests on published Phase 3 RCTs (SUNRISE-2 and a trial in older adults) and multiple network meta-analyses found in the literature. Because the predicted indication is the same as the approved one, this level reflects evidence for insomnia itself.

---

## Why is This Prediction Reasonable?

Lemborexant is a dual orexin receptor antagonist. It competitively blocks OX1R and OX2R, with higher affinity for OX2R. Orexin is a key neuropeptide promoting wakefulness. By dampening this signalling, the drug shortens the time to fall asleep and reduces waking after sleep onset. The mechanism-of-action field was not available in the structured data compiled for this report, so this description comes from the supplied literature (PMIDs 35972717, 37086045 and 32096020).

The predicted indication, difficulty initiating and maintaining sleep, is the same clinical problem as insomnia, the drug's original indication. The high TxGNN score therefore agrees with what is already known. It should be read as confirmation of an on-label use, not as the discovery of a new therapeutic direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the data compiled for this report. Pivotal Phase 3 trials are, however, described in the published literature below (for example SUNRISE-2).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem ER in older adults with insomnia disorder |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3) | Sleep | SUNRISE 2: long-term efficacy and tolerability of lemborexant vs placebo |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Phase 3) | Sleep Med | SUNRISE-2: effectiveness and safety over up to 12 months of continuous treatment |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Systematic review / NMA | Transl Psychiatry | Risk-benefit comparison of daridorexant, lemborexant and suvorexant |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic review / NMA | Lancet | Comparative effectiveness of drug treatments for acute and long-term insomnia |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Systematic review / NMA | Sleep Med Rev | Efficacy and tolerability ranking of 20 insomnia drugs |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Systematic review / NMA | Drugs | Comparative effectiveness and safety of insomnia drugs across 153 randomized trials |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Efficacy and safety of lemborexant vs other insomnia treatments |
| [39277609](https://pubmed.ncbi.nlm.nih.gov/39277609/) | 2024 | Systematic review | Transl Psychiatry | Lemborexant and suvorexant for insomnia comorbid with psychiatric disorders |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc analysis | Sleep Med | Effect of lemborexant on sleep architecture in insomnia with mild obstructive sleep apnoea |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02507366 | DAYVIGO | Not specified | Not specified |
| 02507374 | DAYVIGO | Not specified | Not specified |

Both authorizations are valid single-ingredient products. The literature notes that lemborexant is approved in Canada for adult insomnia (PMID 33636648).

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (these are not label text and need verification against the Canadian product monograph): narcolepsy, narcolepsy-cataplexy syndrome, central nervous system disease, Balo concentric sclerosis, X-linked adrenoleukodystrophy.
- **Drug Interactions:** 100 interactions were identified. Examples rated **Major**: ranitidine, aprepitant, morphine (including liposomal morphine), cimetidine, clarithromycin and clotrimazole. Examples rated **Moderate**: pioglitazone, bupropion, dexamethasone, saxagliptin, diphenoxylate, dronabinol, nabilone, metoclopramide and others. Many of the major interactions involve CYP3A inhibitors or CNS depressants, which warrants dose and sedation review.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several Phase 3 RCTs and multiple network meta-analyses support lemborexant for insomnia, and it is already marketed in Canada. Since the predicted indication is effectively the approved one, this is not a new repurposing opportunity, and the main remaining work is safety verification.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (currently missing, and blocking safety screening)
- Approved indication text and dosage form for both DINs
- Structured mechanism-of-action data from DrugBank
- Review of the major drug interactions, particularly with CYP3A inhibitors and opioids
- If a genuinely new indication is of interest, a separate assessment, because this prediction does not add one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

