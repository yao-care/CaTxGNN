---
layout: default
title: Imipramine
parent: Moderate Evidence (L3-L4)
nav_order: 469
evidence_level: L4
indication_count: 7
---

# Imipramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Imipramine: From Antidepressant Therapy to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Imipramine is a tricyclic antidepressant marketed in Canada, though the supplied data contains no label indication text.
The TxGNN model predicts it may be useful for **attention deficit-hyperactivity disorder (ADHD)**.
The evidence is thin: **1 registered clinical trial** (which does not test imipramine) and **20 publications**, most of them reviews, older small studies or background papers.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Attention deficit-hyperactivity disorder (ADHD) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on general pharmacology, imipramine is a tricyclic antidepressant that blocks reuptake of norepinephrine and serotonin. Its metabolite, desipramine, is strongly noradrenergic.

Noradrenergic modulation is plausibly relevant to ADHD. Stimulants such as methylphenidate and amphetamines are the usual first-line drugs. One retrieved review (PMID 17078784) notes that nonselective norepinephrine reuptake inhibitors (desipramine and imipramine) and selective ones (atomoxetine) can also be effective. Tricyclics have historically been discussed as second-line options, especially when stimulants fail. A small EEG study (PMID 18304665) looked at imipramine in children who did not respond to stimulants.

This mechanistic link comes from general pharmacology, not from the supplied data. The 99.90% score is a model prediction and is not clinical proof. The retrieved literature also shows how limited the evidence is:

- The ADHD-specific imipramine papers are small or old, or are mechanistic and biomarker studies.
- None of them is a large, modern randomized trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | Not applicable | Completed | 103 | An 8-week mindfulness training for children with ADHD and their parents, versus care as usual. It does not test imipramine and provides no drug evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Review (meta-review) | Front Psychiatry | Meta-review of antidepressant efficacy, tolerability and suicidality in children and adolescents, covering ADHD among other disorders. |
| [34002501](https://pubmed.ncbi.nlm.nih.gov/34002501/) | 2021 | Review (umbrella review) | World Psychiatry | Umbrella review of drug, psychosocial and brain stimulation interventions in youth with mental disorders. |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evid Rep Technol Assess (Summ) | Evidence report on the effectiveness and safety of drug and non-drug ADHD treatments in children and adults. |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Not classified | Expert Rev Neurother | Notes that nonselective norepinephrine reuptake inhibitors (desipramine, imipramine) can be effective. Focuses on P300 topography for choosing treatment. |
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Not classified | Clin EEG | 17 children with ADHD who responded poorly to pemoline were treated with imipramine. Prolonged P300 latency predicted poor response. |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Not classified | Int J Psychophysiol | Effects of imipramine on the EEG of children with ADHD who did not respond to stimulants but responded clinically to imipramine. |
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Not classified | Am J Psychiatry | "Imipramine for attention deficit disorder." No abstract is available, so the findings cannot be summarized. |
| [2258453](https://pubmed.ncbi.nlm.nih.gov/2258453/) | 1990 | Not classified | J Clin Psychopharmacol | Retrospective study of 36 children with ADHD on imipramine, with or without carbamazepine. It examined carbamazepine's possible effect on plasma imipramine and desipramine levels. |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Review | CNS Drugs | Overview of pharmacokinetic drug-drug interactions for ADHD agents. |
| [1974836](https://pubmed.ncbi.nlm.nih.gov/1974836/) | 1990 | Review | Clin Pharm | General review of ADHD epidemiology, diagnosis and the role of drug therapy. |

---

## Canada Market Information

There are 8 authorizations in total. Five are shown. Dosage form and approved indication text are not available in the input.

| DIN | Product Name |
|---------|------|
| 2546345 | JAMP IMIPRAMINE |
| 326852 | APO-IMIPRAMINE TABLETS |
| 644579 | APO-IMIPRAMINE TABLETS |
| 360201 | APO-IMIPRAMINE TABLETS |
| 2546353 | JAMP IMIPRAMINE |

---

## Safety Considerations

Please refer to the package insert for safety information.

The input contained no warnings or contraindications, and no drug interaction records were found. The retrieved literature raises two points worth checking:

- Carbamazepine may affect plasma imipramine concentrations in children with ADHD (PMID 2258453).
- The pediatric antidepressant meta-review (PMID 32982805) covers suicidality, which matters for any use in children and adolescents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is plausible and imipramine has a long history as a second-line ADHD option. However, the only registered trial does not test imipramine, and the imipramine-specific literature is small, older or mechanistic. The Canadian safety information is also missing, so this candidate stays at the research-question stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening.
- Mechanism of action data from DrugBank.
- Full-text review of the imipramine-specific ADHD studies (especially PMIDs 6849467, 9465283, 18304665 and 2258453) to confirm design, dose and outcomes.
- A check of controlled trials or meta-analyses on tricyclics in ADHD, and a comparison against approved ADHD therapies.
- A pediatric safety plan covering cardiac risk, overdose toxicity, suicidality and interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

