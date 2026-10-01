---
layout: default
title: Temazepam
parent: High Evidence (L1-L2)
nav_order: 880
evidence_level: L2
indication_count: 1
---

# Temazepam
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Temazepam: Predicted Indication for Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Temazepam is a benzodiazepine-class hypnotic marketed in Canada as RESTORIL. The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, with **0 registered clinical trials** and **20 publications** in the evidence pack, including 1 Phase III RCT. This is better read as a confirmation of known on-label use than as a true repurposing signal, because the original indication fields in the pack are empty.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temazepam is a benzodiazepine receptor agonist. It enhances GABA-A receptor-mediated inhibitory signaling, which produces the sedative-hypnotic effects relevant to falling asleep and staying asleep. This mechanism comes from the repurposing rationale in the pack, because the DrugBank mechanism-of-action field is not available.

The pack does not list an original indication for temazepam, and the Canadian license records contain no indication text. The high score (0.998) is consistent with temazepam's established use as a marketed hypnotic for insomnia. The literature also shows temazepam used as a hypnotic since the 1970s and 1980s. The prediction is therefore mechanistically coherent, but it does not point to a new therapeutic area.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39304187](https://pubmed.ncbi.nlm.nih.gov/39304187/) | 2024 | RCT (Phase III) | J Palliat Med | Three-arm, double-blind, placebo-controlled multicenter trial of temazepam or melatonin versus placebo for insomnia in advanced cancer |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | Masked taper combined with behavioral intervention for discontinuing benzodiazepine receptor agonist hypnotics |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic review / network meta-analysis | Sleep | Compares the efficacy and safety of hypnotics for insomnia in older adults |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine guideline on drug-by-drug pharmacologic treatment of chronic insomnia in adults |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management of insomnia in the elderly; behavioral therapies are generally the first-line intervention |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults, whose pharmacokinetics may be altered |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Critical review of rebound insomnia after stopping short half-life benzodiazepine hypnotics, including temazepam |
| [2859305](https://pubmed.ncbi.nlm.nih.gov/2859305/) | 1985 | Double-blind sleep-lab study | J Clin Psychopharmacol | Midazolam 15 mg and temazepam 30 mg versus placebo in middle-of-the-night dosing for sleep maintenance insomnia (18 volunteers) |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | Describes temazepam as effective only for sleep maintenance, in contrast to flurazepam |
| [342551](https://pubmed.ncbi.nlm.nih.gov/342551/) | 1978 | Sleep-lab study | J Clin Pharmacol | In six insomniac subjects, temazepam 30 mg showed no effect on sleep induction, and effectiveness for sleep maintenance was not demonstrated |

The older sleep-lab studies are small and sometimes disagree, so they should be weighed against the more recent guideline and meta-analysis. The literature relevance screening in the pack is still pending.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 604453 | RESTORIL |
| 604461 | RESTORIL |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the pack. Please refer to the package insert for safety information.

The literature and guideline set flags the following risks, especially for older adults:
- **Falls and cognitive impairment:** these are the concerns behind the Beers criteria.
- **Dependence and withdrawal:** the rebound insomnia review ([2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/)) describes worsening of sleep after stopping short half-life benzodiazepine hypnotics.
- **Recommended use:** short-term, at the lowest effective dose, with a discontinuation plan. Behavioral therapy (CBT-I) is generally the first-line approach, and benzodiazepine receptor agonist discontinuation is itself the subject of an RCT ([39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/)).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temazepam is an established marketed hypnotic, and one Phase III double-blind RCT in advanced cancer insomnia is supported by guidelines and a network meta-analysis. The dependence, falls and cognitive risks mean any use should be short-term, at the lowest effective dose, with a discontinuation plan.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block the safety screening step
- Approved indication text, dosage form and manufacturer for the two RESTORIL DINs
- The DrugBank mechanism of action, to complete the mechanistic analysis
- Drug interaction data, as the query returned no results
- Completion of the literature relevance screening, which is still pending
- Confirmation of the original indication, since the pack has none
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

