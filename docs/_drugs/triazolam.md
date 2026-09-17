---
layout: default
title: Triazolam
parent: Moderate Evidence (L3-L4)
nav_order: 801
evidence_level: L3
indication_count: 1
---

# Triazolam
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

# Triazolam: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Triazolam is a short-acting benzodiazepine hypnotic; in this evidence pack, no structured original-indication or Health Canada licensing data is available, as the drug is currently **not marketed in Canada**. The TxGNN model predicts efficacy for **sleep disorder, initiating and maintaining sleep (insomnia)**, currently supported by **0 clinical trials** and **21 publications**. Notably, this predicted indication corresponds to triazolam's already well-established international use as an insomnia treatment, so the finding largely reconfirms known pharmacology rather than identifying a novel repurposing signal — but critical safety and regulatory data remain missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Canadian regulatory data (drug not marketed); internationally documented for short-term insomnia treatment |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep (Insomnia) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (MOA field is flagged as a data gap). Based on information within the supporting literature (e.g., PMID 19682231), triazolam acts as an allosteric activator at the benzodiazepine site of the GABA-A receptor complex — a well-characterized mechanism shared among benzodiazepine hypnotics used to treat insomnia.

The relationship between the "original" and "predicted new" indication here is unusual: triazolam is internationally recognized (and was historically marketed as Halcion) specifically for short-term insomnia treatment. The TxGNN-predicted indication, "sleep disorder, initiating and maintaining sleep," is essentially the same clinical entity. This means the model is not surfacing a genuinely novel repurposing hypothesis, but rather correctly reconfirming a well-established pharmacological use — which is expected given that triazolam is not currently marketed or licensed in Canada, so no structured "original indication" exists in the local regulatory record.

Mechanistically, this coherence is unsurprising: benzodiazepine site agonism at GABA-A receptors is the canonical mechanism for hypnotic efficacy in insomnia, and the literature base (multiple systematic reviews, a clinical practice guideline, and triazolam-specific pharmacology studies) consistently supports this application across decades of use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic Review/Meta-analysis | Psychiatry and Clinical Neurosciences | Compared efficacy/safety of sleep medication classes (incl. benzodiazepines) combined with antidepressants for MDD with insomnia |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic Review/Network Meta-analysis | Sleep | Compared efficacy and safety of hypnotics, including benzodiazepines, for insomnia in older adults |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline | J Clin Sleep Med (AASM) | Establishes pharmacologic treatment recommendations for chronic insomnia, evaluating individual drugs including triazolam |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Experimental Study | J Sleep Res | Human study on retrograde effects of triazolam and zolpidem (GABA-A allosteric activators) on sleep-dependent motor learning |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | Direct comparison of zolpidem vs. triazolam efficacy and safety in humans |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Critical review of rebound insomnia following discontinuation of triazolam, temazepam, flurazepam |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Pharmacology of benzodiazepine hypnotics including triazolam and temazepam |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | Clinical neuropharmacology of sleep disorders, covering triazolam's sleep induction/maintenance efficacy |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Review | Drug Safety | Assessment of short-acting hypnotics for insomnia |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clinical Therapeutics | Safety and efficacy review of sleep medicines in older adults |

---

## Canada Market Information

Triazolam is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) or product licenses are on file in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score and a reasonably consistent literature base (largely reconfirming triazolam's known role as a benzodiazepine hypnotic for insomnia), a **blocking data gap** exists: TFDA/product-label warnings and contraindications are unavailable, preventing initial safety screening (S1). No clinical trials or Canadian licensing data are on record, and the drug is not currently marketed in Canada.

**To proceed, the following is needed:**
- Product monograph / warnings and contraindications from a jurisdiction where triazolam is marketed (source: TFDA-equivalent or manufacturer labeling)
- Confirmed mechanism of action data via DrugBank API
- Clarification of whether this represents a genuine repurposing candidate or simply a reconfirmation of triazolam's existing international insomnia indication, given the absence of Canadian regulatory history
- Drug interaction (DDI) data, since the current query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

