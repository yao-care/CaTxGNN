---
layout: default
title: Desipramine
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 8
---

# Desipramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Desipramine: From Tricyclic Antidepressant to Attention Deficit Hyperactivity Disorder

## One-Sentence Summary

Desipramine is a tricyclic antidepressant that acts mainly on norepinephrine reuptake; the Canadian licence records provided do not list an approved indication.
The TxGNN model predicts it may be effective for **ADHD, inattentive type** (rank 1), and also for the parent condition **ADHD** (rank 2).
The subtype prediction has **0 clinical trials and 0 publications**, while the parent ADHD prediction has **0 registered trials** and **14 publications**, mostly reviews and systematic reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records (drug class: tricyclic antidepressant) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type (parent term: ADHD) |
| TxGNN Prediction Score | 99.81% (parent ADHD: 99.78%) |
| Evidence Level | L5 for the inattentive subtype; L3 for parent ADHD under the level rules (systematic reviews only, no verified RCT) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Desipramine is, however, a potent and relatively selective norepinephrine reuptake inhibitor. Noradrenergic modulation is an established mechanism in ADHD, as with atomoxetine. This makes the prediction pharmacologically plausible.

The subtype-specific prediction (inattentive type) has no trials or literature of its own. Any support comes from the parent ADHD indication. For ADHD, the retrieved literature includes a Cochrane systematic review of tricyclic antidepressants in children and adolescents (PMID 25238582) and several ADHD pharmacotherapy reviews. Older reviews describe desipramine as a reasonable second choice after stimulants (PMID 8032506). One 1997 review advises avoiding desipramine in youths because safer tricyclics are available (PMID 9418743). Cardiac conduction effects, reported sudden deaths in children and anticholinergic burden limit it to a second-line role.

Other predictions from the same drug carry weaker or different support:
- **Agoraphobia / panic disorder (L3):** tricyclics are historically effective. Desipramine data include two open-label studies (PMIDs 3624509 and 1829745) and a 12-week placebo-controlled study of 56 patients (PMID 8290663). Modern network meta-analysis favours other agents, so the clinical niche is narrow.
- **Obsessive-compulsive disorder (L4):** the mechanistic fit is weak. Desipramine is a norepinephrine-selective agent that serves as a non-serotonergic comparator against clomipramine and fluvoxamine. The only linked trial is unrelated.
- **Specific developmental disorder, chondromyxoid fibroma, faciodigitogenital syndrome, benign paroxysmal torticollis of infancy:** prediction only, with no meaningful clinical evidence. The last three lack a plausible mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top prediction (ADHD, inattentive type) or for parent ADHD.

---

## Literature Evidence

The table covers parent ADHD (rank 2), because the inattentive-subtype prediction has no literature of its own. Abstracts in the pack are truncated, so findings are summarised only as far as the text allows.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Systematic review | Cochrane Database Syst Rev | Tricyclic antidepressants as second-line treatment for ADHD in children and adolescents |
| [26693882](https://pubmed.ncbi.nlm.nih.gov/26693882/) | 2016 | Systematic review | Expert Rev Neurother | Alternative drug options for adult ADHD when methylphenidate or atomoxetine gives partial or no response |
| [29944175](https://pubmed.ncbi.nlm.nih.gov/29944175/) | 2018 | Systematic review | Cochrane Database Syst Rev | Drug treatment of ADHD in children with comorbid tic disorders; tricyclics are among the agents discussed |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Efficacy, tolerability and suicidality of antidepressants in children and adolescents, including ADHD |
| [30422834](https://pubmed.ncbi.nlm.nih.gov/30422834/) | 2019 | Systematic review | Int Clin Psychopharmacol | Drug options for ADHD comorbid with an anxiety disorder |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evid Rep Technol Assess | Effectiveness and safety of drug and non-drug ADHD treatments in children and adults |
| [10913503](https://pubmed.ncbi.nlm.nih.gov/10913503/) | 2000 | Review | Biol Psychiatry | Overview of the validity of adult ADHD, including psychopharmacology |
| [8032506](https://pubmed.ncbi.nlm.nih.gov/8032506/) | 1994 | Review | Arch Fam Med | Desipramine described as a reasonable second choice after methylphenidate |
| [9418743](https://pubmed.ncbi.nlm.nih.gov/9418743/) | 1997 | Review | J Clin Psychiatry | Antidepressants help impulsive and hyperactive behaviour but are less effective than stimulants; desipramine should be avoided in youths |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Clinical study | Expert Rev Neurother | Nonselective norepinephrine reuptake inhibitors (desipramine, imipramine) can be effective; P300 topography used to choose treatment |

---

## Canada Market Information

The licence records list five products named DESIPRAMINE. Dosage form, manufacturer and approved-indication text are not provided for any of them.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2216248 | DESIPRAMINE | Not provided | Not provided |
| 2216256 | DESIPRAMINE | Not provided | Not provided |
| 2216264 | DESIPRAMINE | Not provided | Not provided |
| 2216272 | DESIPRAMINE | Not provided | Not provided |
| 2216280 | DESIPRAMINE | Not provided | Not provided |

---

## Safety Considerations

- **Cardiac risk (from the literature-based rationale):** conduction effects and reported sudden deaths in children.
- **Anticholinergic burden:** limits use to a second-line role.
- **Pediatric caution:** one review advises avoiding desipramine in youths and possibly adults (PMID 9418743). Tricyclic exposure in infants would raise safety concerns for the infant-onset predictions.

No drug-interaction records were found. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (ADHD, inattentive type) is model output only, with no trials or literature. The parent ADHD indication has a plausible noradrenergic mechanism and systematic-review-level literature, but no registered trials and no verified RCT. Established first-line alternatives and cardiac safety concerns limit desipramine to a second-line, research-question role. Parent ADHD could be reconsidered as a research question once the items below are supplied.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- Review of the primary desipramine ADHD trials behind the Cochrane review (PMID 25238582) to confirm design, phase and outcomes
- Approved-indication text, dosage forms and manufacturers for the five DINs
- A cardiac safety assessment for any pediatric or adult ADHD use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

