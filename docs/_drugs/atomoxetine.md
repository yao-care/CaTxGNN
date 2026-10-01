---
layout: default
title: Atomoxetine
parent: Model Prediction Only (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Atomoxetine
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

# Atomoxetine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Atomoxetine is a selective norepinephrine reuptake inhibitor, a non-stimulant medication already used to treat ADHD.
The TxGNN model predicts it may be effective for **specific developmental disorder**, supported by **7 clinical trials** and **15 publications**.
In practice this evidence is almost entirely about ADHD, including ADHD symptoms in children with autism, so the prediction is largely on-label rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (Health Canada indication text is not included in the data; taken from the drug's known labeling) |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** The Evidence Pack assigned L1. Under the level rules, L1 requires at least 2 completed Phase 3 RCTs, and only one is present (NCT00498173, Phase 3, n=60). Three completed Phase 4 double-blind RCTs and several meta-analyses add support. L2 is therefore the stricter reading.

---

## Why is This Prediction Reasonable?

Atomoxetine blocks the norepinephrine transporter (NET), raising noradrenaline levels in the prefrontal cortex. This is thought to improve attention and impulse control.

Detailed mechanism data from DrugBank is not available in the current data. The mechanism above comes from the drug's established pharmacology.

The predicted "specific developmental disorder" is closely related to ADHD, which is itself a neurodevelopmental condition. The trials and literature mostly cover ADHD, including ADHD symptoms in children and adolescents with autism spectrum disorder (ASD). This is the only repurposing-relevant subset in the evidence. Because ADHD is already a labeled indication, the high TxGNN score mostly reflects an existing use. It does not point to a new therapeutic area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | Completed | 60 | Double-blind, placebo-controlled RCT of atomoxetine for ADHD symptoms in children and adolescents with autism, Asperger's or PDD-NOS |
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | Completed | 445 | Double-blind atomoxetine vs placebo in young adults with ADHD, with functional outcomes assessed |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | Completed | 128 | Atomoxetine, placebo and parent management training in children with autism spectrum conditions and ADHD symptoms |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | Completed | 97 | Randomized, double-blind atomoxetine vs placebo for ADHD symptoms in children and adolescents with ASD |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | Completed | 396 | Guanfacine prolonged-release study in ADHD (ages 6–17) with atomoxetine as an active comparator |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Small mechanistic study of smoking reinforcement in adults with ADHD |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1398 | Observational study of chronic ADHD drug effects (focused on methylphenidate, not an atomoxetine efficacy design) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Network meta-analysis | The Lancet Psychiatry | Compares drug, psychological and neurostimulation treatments for adult ADHD |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Systematic review/Meta-analysis | Autism Research | Three placebo-controlled RCTs (241 children) evaluating atomoxetine for ADHD in autism |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Systematic review | PLoS One | Sex differences in ADHD pharmacotherapy prescribing and efficacy in girls and women |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Review | Ther Adv Psychopharmacol | Atomoxetine efficacy in ADHD with common comorbidities across age groups |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Retrospective cohort | Neuropsychopharmacol Rep | Factors linked to atomoxetine efficacy in adult ADHD; long-term efficacy about 40% at 6 months |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Clinical practice report | J Dev Behav Pediatr | Teletherapy and medication management, including atomoxetine, for ADHD with internalizing symptoms and suicidality |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Preprint | bioRxiv | Structural connectivity deviations in youth with ADHD predict symptom and treatment outcomes |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | Clin EEG Neurosci | Quantitative EEG in childhood ADHD and learning disabilities |

Some retrieved publications were left out because they are off-topic (drug interactions with synthetic cathinones and phenethylamines) or add little (cost and prescribing-pattern studies).

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2318024 | APO-ATOMOXETINE |
| 2506815 | JAMP ATOMOXETINE |
| 2467755 | ATOMOXETINE |
| 2362511 | TEVA-ATOMOXETINE |
| 2471493 | AURO-ATOMOXETINE |

These are 5 of 20 licenses. Dosage form and approved-indication text were not provided for these entries.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Completed randomized trials and a meta-analysis support atomoxetine for ADHD symptoms, including in children with autism. This is mainly on-label use, so the "specific developmental disorder" prediction adds little that is new. Any further work should be limited to the ADHD-in-autism subset.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- DrugBank mechanism-of-action data
- A clear definition of what "specific developmental disorder" covers, and confirmation of the Health Canada indication wording against the ADHD-in-autism subset
- A pharmacovigilance plan that watches for reported tic exacerbation and mood destabilization (case reports of mania and tics appear in related indications)

**Other predicted indications:** Tourette syndrome (L3, research question only; the one Phase 2 pilot was terminated at n=5) and the remaining candidates (Hold) do not currently justify progression. Faciodigitogenital syndrome, chondromyxoid fibroma and the cerebellar ataxias have no clinical evidence and no plausible mechanism. For trichotillomania, evidence is limited to case reports and preclinical data that lean toward possible harm.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

