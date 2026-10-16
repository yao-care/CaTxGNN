---
layout: default
title: Flurazepam
parent: Moderate Evidence (L3-L4)
nav_order: 402
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Flurazepam: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L4). Approved use: Insomnia"
monitor_inn: "Flurazepam"
predicted_indications: ["sleep disorder, initiating and maintaining sleep"]
---

# Flurazepam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Flurazepam: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Flurazepam is a benzodiazepine hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, but this is essentially the same condition as its original use, so it is not a true repurposing candidate.
The data compiled for this report contain **no clinical trials** and **19 publications** (mostly reviews and pharmacology papers).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (the Canadian license records contain no indication text; the original indication comes from the knowledge graph) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general pharmacological knowledge, flurazepam is a benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors. This enhances inhibitory neurotransmission and promotes sleep. A 2023 cryo-EM study (PMID 37730991) describing native GABA-A receptor assemblies and benzodiazepine pharmacology is consistent with this mechanism.

The predicted indication, difficulty initiating and maintaining sleep, is essentially the same as the original indication of insomnia. The very high TxGNN score (99.42%) most likely reflects this overlap with the approved use rather than a genuinely new therapeutic direction.

Flurazepam has a long-acting active metabolite. This helps sleep maintenance but also raises concerns about residual sedation, especially in older adults and in long-term use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below are mainly reviews and pharmacology papers. They describe insomnia management and hypnotic pharmacology, and they do not establish efficacy in a new indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | Systematic review / network meta-analysis | Eur Neuropsychopharmacol | Residual effects of sleep medications on driving performance, based on randomized trials |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Drugs for chronic insomnia |
| [37730991](https://pubmed.ncbi.nlm.nih.gov/37730991/) | 2023 | Preclinical/structural study | Nature | Cryo-EM structures of native GABA-A receptor assemblies and their pharmacology |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | History and pharmacology of benzodiazepine hypnotics; flurazepam was the first, in 1970 |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | Flurazepam is effective for both sleep induction and maintenance, retaining most efficacy over 4 weeks of nightly use |
| [6132933](https://pubmed.ncbi.nlm.nih.gov/6132933/) | 1983 | Sleep laboratory comparison | J Clin Psychopharmacol | Flurazepam, temazepam and triazolam compared for efficacy and withdrawal effects |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Rebound insomnia after discontinuing short half-life benzodiazepines |
| [32544795](https://pubmed.ncbi.nlm.nih.gov/32544795/) | 2020 | Efficacy comparison (modeling) | Sleep Med | Quantitative comparison of drug efficacy for insomnia |
| [10533351](https://pubmed.ncbi.nlm.nih.gov/10533351/) | 1999 | Review | J Am Pharm Assoc | Pharmacologic and non-pharmacologic management of insomnia |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00521698 | FLURAZEPAM | Not specified | Not specified |
| 00521701 | FLURAZEPAM | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications and cautions from the knowledge graph (not label text)**: The knowledge graph links flurazepam with the following conditions as contraindications:
  - Respiratory: sleep apnea syndromes, respiratory failure, lung disease
  - Organ function: liver disease, kidney disease, gallbladder disease
  - Psychiatric: psychotic disorders, schizophreniform and schizoaffective disorders, personality disorder, anxiety disorder, neurotic disorder, dysthymic disorder, intermittent explosive disorder
  - Substance use: substance-related disorders and substance abuse/dependence
  - Metabolic: porphyria
- **Drug Interactions**: The interaction query returned about 100 entries. The main ones are:
  - **Major**: morphine, including liposomal morphine (additive central nervous system and respiratory depression)
  - **Moderate**: bupropion, omeprazole, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide
  - **Minor**: antacids and mineral agents such as magnesium oxide, calcium carbonate and aluminum hydroxide
- **Literature-based concerns**: Residual sedation and impaired driving performance, risks in older adults, and rebound insomnia after discontinuation.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is essentially the same as flurazepam's established use in insomnia, so this is not a true repurposing opportunity. The evidence consists of reviews and pharmacology papers, with no clinical trials. The high prediction score likely reflects overlap with the approved indication.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication, dosage forms), which is a blocking gap for safety screening
- Confirmed mechanism of action data from DrugBank
- A genuinely distinct new indication, if repurposing is the goal, with supporting clinical evidence
- A safety plan for older adults, driving risk and long-term use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

