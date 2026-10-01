---
layout: default
title: Bupropion
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Bupropion
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

# Bupropion: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is a marketed antidepressant that is also used for smoking cessation, according to the supplied literature; the Canadian license data does not include indication text. The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**. This direction is supported by **8 clinical trials** (including one completed Phase 3 placebo-controlled trial) and **19 publications**, among them a Cochrane review and several network meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data; literature describes use in depression and smoking cessation |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* The Evidence Pack labels this L1. Under the rules used here, L1 needs at least two completed Phase 3 RCTs. Only one completed Phase 3 RCT (NCT00048360) and one completed Phase 2/3 trial (NCT00061087) are listed, so this report assigns L2. Several network meta-analyses and reviews add supporting evidence.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not in the Evidence Pack. The supplied literature (PMID 37405312) describes bupropion as an inhibitor of norepinephrine and dopamine reuptake with no serotonergic activity. These are the same catecholaminergic pathways targeted by established ADHD drugs, such as stimulants and atomoxetine. This overlap fits the very high TxGNN score.

The original use (depression) and the new use (ADHD) are both neuropsychiatric conditions in which dopamine and norepinephrine signalling is implicated. Reviews and meta-analyses already discuss bupropion as an off-label, non-stimulant option for ADHD. It is usually considered when stimulants are not effective or not tolerated, mainly in adults. Evidence in children and adolescents is weaker.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | 8-week randomized, double-blind, placebo-controlled, flexible-dose trial of extended-release bupropion (300-450 mg/day) in adults with ADHD |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Bupropion for ADHD in adolescents with substance use disorder |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Treatment of adult ADHD in methadone-maintained patients (drug not named in title) |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | NA | Completed | 32 | Open study of bupropion SR for ADHD in adults with recent or current substance use disorders |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | NA | Completed | 32 | Cocaine abuse comorbid with attention deficit disorder; small sample |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose bupropion for smoking cessation; ADHD is not the focus |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Bupropion and stimulant-use relapse, with and without ADHD; no data generated |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | NA | Withdrawn | 0 | CYP2B6 induction by ethanol and polymorphisms; pharmacogenetic study, not an efficacy trial |

The title of NCT00048360 is truncated in the Evidence Pack. Its drug arm, comparator and population should be confirmed against the registry.

---

## Literature Evidence

Only the first 10 of the 19 publications are listed below, prioritizing systematic reviews and meta-analyses. Summaries are based on the titles and the (partly truncated) abstracts in the Evidence Pack.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane systematic review | Cochrane Database Syst Rev | Bupropion for ADHD in adults, as an alternative when psychostimulants are not tolerated or not fully effective |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network meta-analysis | Lancet Psychiatry | Comparative efficacy and tolerability of ADHD medications in children, adolescents and adults |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematic review and network meta-analysis | PLoS One | Relative benefits and harms of pharmacologic treatments for adult ADHD |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Bayesian network meta-analysis | J Psychiatr Res | Efficacy and safety of monoamine reuptake inhibitors in ADHD, based on 31 clinical trials |
| [27813651](https://pubmed.ncbi.nlm.nih.gov/27813651/) | 2017 | Systematic review | J Child Adolesc Psychopharmacol | Bupropion, a dopamine and norepinephrine reuptake inhibitor, as a non-stimulant option for children and adolescents with ADHD |
| [26693882](https://pubmed.ncbi.nlm.nih.gov/26693882/) | 2016 | Systematic review | Expert Rev Neurother | Alternative drug strategies for adult ADHD when methylphenidate or atomoxetine are ineffective |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Review | Expert Rev Neurother | Non-stimulant medications for adults with ADHD when stimulants fail or are poorly tolerated |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Review | Health Psychol Res | Pharmacology and mechanisms of bupropion across depression, ADHD and smoking cessation |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Curr Pharm Des | Lists bupropion among common ADHD medications and reviews effects and side effects |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Systematic review and network meta-analysis | Lancet Psychiatry | Comparative cardiovascular safety (haemodynamic and ECG parameters) of ADHD medications |

---

## Canada Market Information

Health Canada lists 10 authorizations; the 5 provided are shown below. Dosage form, manufacturer and approved indication text are empty in the supplied data.

| DIN | Product Name |
|---------|------|
| 2275090 | WELLBUTRIN XL |
| 2439662 | TEVA-BUPROPION XL |
| 2475812 | TARO-BUPROPION XL |
| 2275074 | ODAN BUPROPION SR |
| 2439654 | TEVA-BUPROPION XL |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.

Warnings and contraindications were not available. Please refer to the package insert for safety information. Items to review before use in ADHD: seizure risk (bupropion lowers the seizure threshold), blood pressure effects, and CYP2B6/CYP2D6-related interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bupropion shares its catecholaminergic mechanism with established ADHD drugs. It has one completed Phase 3 placebo-controlled trial, a Phase 2/3 trial, a Phase 4 adolescent trial, a Cochrane review and several network meta-analyses. The evidence is strongest in adults and weaker in children and adolescents. It sits below the L1 threshold, and key label and safety data are missing.

**To proceed, the following is needed:**
- Registry confirmation of NCT00048360 (drug arm, comparator, population, results)
- Health Canada package insert warnings and contraindications, and approved indication text
- Mechanism of action data from DrugBank
- Review of seizure risk, blood pressure effects and CYP2B6/CYP2D6 interactions
- Full-text appraisal of the Cochrane review and the network meta-analyses

**Other predicted indications:** "ADHD, inattentive type" (rank 2) is a subtype of the same disease. It has only indirect evidence (Research Question, L4). The remaining predictions (ranks 3-10) have no supporting trials or literature and should be held; the "obsolete hypertelorism" term is likely a graph artifact and should be excluded.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

