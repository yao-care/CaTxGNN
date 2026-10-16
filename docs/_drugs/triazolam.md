---
layout: default
title: Triazolam
parent: Model Prediction Only (L5)
nav_order: 943
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Triazolam: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
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

# Triazolam: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Triazolam is a short-acting benzodiazepine, originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, but this is essentially the same condition as its original indication, so it is not a true new use.
Currently there are **0 registered clinical trials** and **20 publications** (mostly reviews and guidelines on insomnia treatment in general) related to this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Triazolam is a short-acting benzodiazepine. Based on general pharmacology, it enhances the inhibitory effect of GABA at GABA-A receptors, which dampens neural activity and promotes sleep onset. Detailed mechanism of action data is not available in the data compiled for this report, so this description comes from general knowledge rather than the supplied record.

The predicted indication, difficulty initiating and maintaining sleep, is essentially the same as insomnia, the drug's existing use. The very high score (99.72%) therefore reflects the model recovering a known indication. It does not point to a new repurposing opportunity. No separate mechanistic argument is needed for this prediction, and no new-disease hypothesis can be drawn from it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The compiled literature is mostly general insomnia reviews and guidelines. Only some papers address triazolam specifically. Study types are as classified in the data; several are not yet classified. Selected publications, prioritising guidelines, meta-analyses and reviews:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine guideline on drug treatment of chronic insomnia in adults, focusing on individual drugs |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Meta-analysis | Psychiatry Clin Neurosci | Efficacy and safety of sleep medication classes (including benzodiazepines) added to antidepressants for depression with insomnia |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Network meta-analysis | Sleep | Comparative efficacy and safety of hypnotics for insomnia in older adults |
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | Network meta-analysis | Eur Neuropsychopharmacol | Residual effects of sleep medications on driving performance |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Med | Overview of insomnia disorder: prevalence, daytime symptoms and health risks |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management recommendations for insomnia in elderly patients |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Rebound insomnia after stopping short half-life benzodiazepines, including triazolam |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | Comparison of zolpidem and triazolam for efficacy and safety |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Not classified | J Clin Psychiatry | Pharmacology of benzodiazepine hypnotics, including triazolam |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00808571 | TRIAZOLAM | Not specified | Not specified |

---

## Safety Considerations

Product-label warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindication-related conditions (from the knowledge graph, not label text)**: anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, liver disease, gallbladder disease, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, myasthenia gravis (including adult-onset), neuromuscular junction disease, substance-related disorder, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were found in total. The first 20 listed include:
  - **Major**: morphine (additive central nervous system and respiratory depression is the expected concern).
  - **Moderate**: ranitidine, bupropion, aprepitant, omeprazole, cimetidine, clarithromycin, dronabinol, eluxadoline, teduglutide, nabilone, metoclopramide, miconazole, clotrimazole.
  - **Minor**: dexamethasone, betamethasone, magnesium oxide, prednisone, aluminum hydroxide, calcium carbonate.
- **Literature-noted risks**: rebound insomnia after stopping, residual effects on driving, tolerance and dependence concerns with benzodiazepines, and special caution in older adults.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is essentially the same as triazolam's existing use for insomnia, so this is not a genuine repurposing opportunity. No clinical trials are registered, and the evidence level is L5. The model score is high, but it mainly reflects recovery of a known indication.

**To proceed, the following is needed:**
- Clarify whether any truly new indication is intended, since the current prediction duplicates the original use
- Health Canada package insert warnings and contraindications, and the approved indication text for DIN 00808571
- Mechanism of action data from DrugBank
- A safety review for the listed contraindicated conditions, the major morphine interaction, and risks in older adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

