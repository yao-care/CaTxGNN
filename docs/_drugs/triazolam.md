---
layout: default
title: Triazolam
parent: Model Prediction Only (L5)
nav_order: 936
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Triazolam: From Short-Acting Benzodiazepine Hypnotic to Insomnia (Sleep Initiation and Maintenance)

## One-Sentence Summary

Triazolam is a short-acting benzodiazepine hypnotic. The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep** (insomnia). This is closer to an established use than a new one. The prediction is supported by **0 registered clinical trials** and **20 publications**, including a clinical practice guideline and systematic reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 (systematic reviews and a guideline; no completed Phase 3 trials supplied) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

The Canadian license record does not include an approved indication text, so no original indication is listed.

---

## Why is This Prediction Reasonable?

Triazolam is a positive allosteric modulator of the GABA-A receptor. It enhances inhibitory neurotransmission and promotes sleep onset. The DrugBank mechanism field was not populated in this dataset, but this is the drug's well-established pharmacology.

The very high TxGNN score (0.997) most likely reflects a known hypnotic use rather than a novel repurposing signal. The input had no recorded original indications, which looks like a data-completeness gap, not evidence that the use is new. The literature supports this reading. Reviews describe triazolam, together with temazepam, as a shorter half-life benzodiazepine hypnotic that began replacing flurazepam in the early 1980s.

Mechanistically, enhanced GABAergic inhibition fits the treatment of difficulty falling or staying asleep.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No RCTs were supplied. The table lists guidelines and systematic reviews first, then narrative reviews. Relevance screening of all entries is still pending.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | AASM guideline on pharmacologic treatment of chronic insomnia in adults. It evaluates individual drugs, including FDA-approved hypnotics, rather than broad drug classes. |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic review / network meta-analysis | Sleep | Compares the efficacy and safety of various hypnotics for insomnia in older adults. |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic review / network meta-analysis | Psychiatry Clin Neurosci | Meta-analysis of double-blind RCTs of sleep medication classes, including benzodiazepines, added to antidepressants in major depressive disorder with insomnia. This is an indirect population. |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management recommendations for chronic insomnia in the elderly. Behavioral therapy is the first-line approach. |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults, whose pharmacokinetics may be altered. |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Med | Overview of insomnia disorder: prevalence, daytime symptoms and health risks. |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | Compares zolpidem with triazolam, emphasizing efficacy and safety in humans. |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Critical review of rebound insomnia after short half-life benzodiazepines. Rebound is a distinct possibility after stopping triazolam. |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Experimental study (type pending) | J Sleep Res | Tests the retrograde effects of triazolam and zolpidem on sleep-dependent motor learning. |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Review | Drug Saf | Assessment of short-acting hypnotics, noting that insomnia is very common. |

---

## Canada Market Information

| License / DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 808571 | TRIAZOLAM | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

No warnings, contraindications or drug-interaction records were available in the input. The absence of interaction records most likely reflects missing data, not evidence of no interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Triazolam's use for insomnia is established pharmacology and is covered by guideline and systematic-review literature. However, no trials were supplied, and the evidence level is L3 under the standard rules, not the L1 assigned in the source data. Benzodiazepine hypnotics carry risks of dependence, tolerance, rebound insomnia, next-day impairment, falls and cognitive effects, especially in older adults. Use should be short-term, at the lowest effective dose, with attention to CNS-depressant interactions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- A drug-interaction review.
- Confirmation that triazolam was included in each cited guideline and meta-analysis, since the supplied titles and abstracts are truncated.
- The Canadian approved indication, dosage form and manufacturer for license 808571.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

