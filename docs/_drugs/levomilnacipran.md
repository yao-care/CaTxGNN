---
layout: default
title: Levomilnacipran
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Levomilnacipran: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "LEVOMILNACIPRAN"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "dysthymic disorder", "melancholia", "neurotic depression", "neurotic disorder"]
---

# Levomilnacipran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Levomilnacipran: From Depressive Disorders to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Levomilnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally used for depressive and anxiety disorders, and it is marketed in Canada as FETZIMA.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy** (the top-ranked prediction), but **no clinical trials and no publications** currently support this specific prediction; it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (per the knowledge graph; no approved-indication text is available from Canadian licences) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, levomilnacipran is an SNRI. Its efficacy in major depressive disorder in adults is established, and it works by blocking reuptake of serotonin and norepinephrine.

For the top-ranked prediction, the mechanistic link is weak. Benign paroxysmal torticollis of infancy is a paediatric, migraine-related disorder often associated with CACNA1A (calcium channel) variants. Nothing in the data connects reuptake inhibition to this condition, and levomilnacipran is approved only for adults. The high score (0.995) is therefore a computational signal only.

Other predictions look more plausible mechanistically, but they largely overlap with existing indications:
- **Agoraphobia** (99.53%): an anxiety-spectrum disorder where SNRIs/SSRIs have class-level use, but no levomilnacipran-specific evidence was found, and the original indications already include anxiety disorder.
- **Dysthymic disorder** (99.24%), **melancholia** (99.20%), **neurotic depression** (99.20%) and **neurotic disorder** (99.19%): all closely related to the approved depressive indications. They reflect proximity to existing uses rather than a new mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for benign paroxysmal torticollis of infancy.

## Literature Evidence

Currently no related literature available for benign paroxysmal torticollis of infancy.

For context, the lower-ranked predictions "melancholia" and "neurotic depression" retrieved about 20 publications each. These are mostly general antidepressant reviews, safety analyses and levomilnacipran drug profiles, not studies specific to those conditions. Examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38700708](https://pubmed.ncbi.nlm.nih.gov/38700708/) | 2024 | Phase 3 RCTs | J Child Adolesc Psychopharmacol | Two randomised, double-blind studies of levomilnacipran ER in paediatric MDD (ages 7-17) |
| [23656841](https://pubmed.ncbi.nlm.nih.gov/23656841/) | 2013 | RCT | J Clin Psychiatry | Proof-of-concept study of levomilnacipran SR in moderate to severe MDD |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Network meta-analysis | Mol Psychiatry | Antidepressants in the maintenance phase of adult MDD |
| [31509357](https://pubmed.ncbi.nlm.nih.gov/31509357/) | 2019 | Review | Prim Care Companion CNS Disord | Mechanism, pharmacokinetics and efficacy; possible benefit on fatigue symptoms |
| [37413934](https://pubmed.ncbi.nlm.nih.gov/37413934/) | 2023 | Preclinical | Int Immunopharmacol | Reduced LPS-induced depression-like behaviour in rats via TLR4/Ras pathway |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02440989 | FETZIMA | Not specified | Not specified |
| 02441004 | FETZIMA | Not specified | Not specified |
| 02440970 | FETZIMA | Not specified | Not specified |
| 02440997 | FETZIMA | Not specified | Not specified |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: angle-closure (closed-angle) glaucoma.
- **Drug Interactions**: 100 interactions were identified. Examples rated **Major**: bupropion, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron, phentermine, dexfenfluramine and fenfluramine. Examples rated **Moderate**: isometheptene, epinephrine, morphine, acetylsalicylic acid, ephedrine, picosulfuric acid, sodium sulfate and polyethylene glycol (3350 with electrolytes).
- **Paediatric use**: the product is approved in Canada for adults only according to the available assessment. Any paediatric indication would need dedicated safety data.

Please refer to the package insert for further warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only a model score (evidence level L5), with no trials, no literature and no supported mechanistic link. A paediatric channelopathy-type migraine-related disorder is also far from the adult depression indication. Other predictions are plausible but mostly overlap with existing indications, so they do not offer strong repurposing signals.

**To proceed, the following is needed:**
- Mechanism of action data to evaluate any link to the predicted condition
- Health Canada product monograph warnings and contraindications, which are required before safety screening can proceed
- Approved indication text, dosage forms and manufacturer details for the Canadian licences
- Indication-specific preclinical or clinical evidence, particularly for agoraphobia, since a sound hypothesis would also need to be distinct from the existing anxiety disorder indication
- A paediatric safety assessment if benign paroxysmal torticollis of infancy remains a target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

