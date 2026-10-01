---
layout: default
title: Trazodone
parent: Model Prediction Only (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
---

# Trazodone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Trazodone: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is an antidepressant. The literature in this pack describes it as approved for major depression, although the Canadian licence records supplied here list no indication text.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**.
There are **no registered clinical trials**, but there are **20 publications**, including one small double-blind placebo-controlled study from 1992 whose result is not in the supplied data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (taken from the published review, not from a Canadian licence record) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 (one published double-blind placebo-controlled study; no registered trials; outcome not available) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. From general pharmacology, trazodone is a serotonin antagonist and reuptake inhibitor. It blocks 5-HT2A/2C receptors and weakly inhibits serotonin reuptake. A 1992 comparison with fluoxetine notes that its most potent action appears to be 5-HT2 antagonism rather than reuptake inhibition.

OCD is the strongest link to the original use. The literature describes OCD as responding preferentially to serotonin reuptake inhibitors, and trazodone is also a serotonergic antidepressant. Depression and OCD often occur together, and several case reports describe patients whose OCD and depression both improved on trazodone. A serotonergic mechanism is therefore plausible.

The evidence is weak, however. Apart from the one placebo-controlled study, it consists of open-label reports, augmentation case series and reviews. One open pilot of trazodone plus tryptophan showed only marginal benefit. The very high TxGNN score is consistent with the literature, but it does not replace confirmatory trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled study of trazodone in OCD. The supplied abstract is truncated and does not state the outcome. |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Reviews trazodone's mechanism, dosing and adverse effects across psychiatric and medical conditions. |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Lists OCD among common off-label uses of trazodone; discusses evidence, benefits and risks. |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | J Clin Psychiatry | Biological strategies for treatment-resistant OCD, mainly adding agents to a potent serotonin reuptake inhibitor. |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Open-label / case series | Clin Neuropharmacol | Nine patients who failed clomipramine: mild overall improvement, three marked responders, with symptom return on withdrawal. |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Open-label clinical study | Psychopathology | Responders showed shifts in caudate glucose metabolism on PET. |
| [2589561](https://pubmed.ncbi.nlm.nih.gov/2589561/) | 1989 | Case series | Am J Psychiatry | Trazodone-fluoxetine combination for OCD (no abstract supplied). |
| [3571943](https://pubmed.ncbi.nlm.nih.gov/3571943/) | 1986 | Pilot (open-label) | Int Clin Psychopharmacol | Trazodone plus tryptophan in 11 patients: poorly tolerated by several and only marginal benefit. |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case report | Am J Psychiatry | Early report on trazodone in OCD (no abstract supplied). |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case report | J Nerv Ment Dis | Two patients with severe OCD and depression who had failed many antidepressants improved rapidly on trazodone. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2164388 | TRAZODONE-150 D |
| 2442825 | JAMP TRAZODONE |
| 1937235 | PMS TRAZODONE HCL TAB 100MG |
| 2442817 | JAMP TRAZODONE |
| 2537915 | AG-TRAZODONE |

The supplied records give no dosage form or approved indication text for these products. There are 20 licences in total, and only the first 5 are shown.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The serotonergic rationale is reasonable and the literature is substantial. However, there are no registered trials, the only controlled study is small and its outcome is not in the supplied data, and the rest is open-label or case-level evidence from 1984-1993. Health Canada safety information is missing, so safety screening cannot proceed. Panic disorder with agoraphobia (L3) has comparable but older evidence. The remaining predictions (rank 2-5, 6, 10) have no meaningful supporting evidence.

**To proceed, the following is needed:**
- The full text and outcome of the 1992 placebo-controlled OCD study (PMID 1629380), plus a search for any more recent controlled trials
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Dosage form and approved indication text for the Canadian licences
- Drug interaction review, particularly for combinations with other serotonergic agents, which several OCD reports use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

