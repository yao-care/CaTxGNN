---
layout: default
title: Lemborexant
parent: High Evidence (L1-L2)
nav_order: 529
evidence_level: L1
indication_count: 1
---

# Lemborexant
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Lemborexant: From Insomnia (Approved Use) to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Lemborexant (Canadian brand DAYVIGO) is a dual orexin receptor antagonist already approved for adult insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as its approved use.
The prediction is supported by **1 registered clinical trial** and **20 publications**, including multiple Phase 3 randomized trials, so this is better read as a confirmation of the existing indication than as a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia in adults (from the literature; the Canadian licence records list no indication text) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Lemborexant is an orally administered dual orexin receptor antagonist. It reversibly and competitively blocks orexin receptors OX1R and OX2R, with higher affinity for OX2R (Scott, *Drugs*, 2020). Orexin is a key promoter of arousal and wakefulness. Blocking it reduces the hyperarousal state associated with insomnia and helps patients fall asleep and stay asleep. The DrugBank mechanism field is empty in the Evidence Pack, so this description comes from the published literature.

The predicted indication, difficulty initiating and maintaining sleep, is the same clinical picture as insomnia disorder, the condition lemborexant is approved to treat. The literature describes approval in the United States, Japan and Canada for adult insomnia. The model's very high score therefore mostly reflects that the drug already treats this condition.

Newer work extends the use to related settings. One example is insomnia comorbid with mild obstructive sleep apnoea (post-hoc analysis, 2025). Another is insomnia associated with psychiatric disorders (systematic review, 2024).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not yet recruiting | 15 | Double-blind, placebo-controlled trial of eszopiclone and lemborexant in people with obstructive sleep apnoea and a low arousal threshold who have difficulty falling or staying asleep (ELOSA); expected completion June 2027 |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | Phase 3 RCT | JAMA Netw Open | Lemborexant vs placebo and zolpidem ER in older adults with insomnia disorder |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | Phase 3 RCT | Sleep | SUNRISE 2: long-term efficacy and tolerability of lemborexant vs placebo in adults with insomnia disorder |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | Phase 3 RCT | Sleep Med | SUNRISE-2: effectiveness and safety with up to 12 months of continuous lemborexant treatment |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | RCT subanalysis | J Clin Sleep Med | Lemborexant vs zolpidem ER by polysomnography-defined insomnia subtype (short vs normal sleep duration) |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc analysis | Sleep Med | Effect of lemborexant on sleep architecture in insomnia with mild obstructive sleep apnoea |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Network meta-analysis | Transl Psychiatry | Risk-benefit comparison of daridorexant, lemborexant and suvorexant for insomnia |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effects of drug treatments for acute and long-term management of adult insomnia disorder |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Network meta-analysis | Sleep Med Rev | Efficacy and tolerability ranking of 20 insomnia drugs in adults |
| [32531478](https://pubmed.ncbi.nlm.nih.gov/32531478/) | 2020 | Network meta-analysis | J Psychiatr Res | Lemborexant vs suvorexant, based on four double-blind RCTs (n = 3237) |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Review | Drugs | Lemborexant: first approval overview (mechanism, US approval for adult insomnia) |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2507366 | DAYVIGO |
| 2507374 | DAYVIGO |

Dosage form, manufacturer and approved indication text are not listed in the licence records provided.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication matches lemborexant's approved use in insomnia. At least two Phase 3 RCTs (the older-adult comparison study and SUNRISE-2) and several network meta-analyses support it. The Health Canada safety information is missing and no formal safety screening has been done, so the decision is not a full "Go".

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, drug interactions), which blocks safety screening
- The Health Canada approved indication text, dosage form and manufacturer for both DINs
- Confirmation from DrugBank of the mechanism of action
- If the goal is a true repurposing, a more distinct target such as insomnia comorbid with sleep apnoea, to be tracked through the ELOSA trial (NCT06928766)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

