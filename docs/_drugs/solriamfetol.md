---
layout: default
title: Solriamfetol
parent: Model Prediction Only (L5)
nav_order: 854
evidence_level: L5
indication_count: 10
---

# Solriamfetol
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

# Solriamfetol: From Excessive Daytime Sleepiness to Attention Deficit Hyperactivity Disorder

## One-Sentence Summary

Solriamfetol (marketed in Canada as SUNOSI) is a wake-promoting drug approved in the US and EU for excessive daytime sleepiness in narcolepsy and obstructive sleep apnea.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, with **2 completed clinical trials** and **6 publications** supporting this direction. Efficacy results from these trials are not in the supplied data and must be verified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Excessive daytime sleepiness in narcolepsy or obstructive sleep apnea (per US/EU approval cited in the literature; Canadian indication text is not available) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (one completed Phase 3 RCT and one completed Phase 2/3 RCT; the Phase 3 results are not yet verified) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Published literature describes solriamfetol as a dopamine and norepinephrine reuptake inhibitor (DNRI). The SUSTAIN trial title also refers to modulation of TAAR-1, dopamine, and norepinephrine.

ADHD is treated with agents that act on the same catecholaminergic pathways, including stimulants such as methylphenidate and amphetamine, and non-stimulants such as atomoxetine and viloxazine. A DNRI that already improves wakefulness and attention-related function in sleepiness disorders may therefore plausibly help ADHD symptoms. A published randomized pilot study and a completed Phase 3 trial in adults with ADHD support this link. Solriamfetol is not approved for ADHD, so any use would be off-label.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | Completed | 516 | FOCUS trial: multicenter, randomized, double-blind, placebo-controlled study of solriamfetol in adults with ADHD (2023–2025). Primary outcome results are not in the supplied data. |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | Completed | 66 | Double-blind, placebo-controlled pilot in adults aged 18–65 with ADHD (2021–2023). Small sample, so it supports signal detection rather than confirmation. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | Remote, randomized, double-blind, placebo-controlled 6-week dose-optimization pilot (75 mg or 150 mg) in 60 adults with ADHD, testing efficacy and tolerability. Outcome data are truncated in the supplied abstract. |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | Review of potential ADHD treatments in Phase III trials, covering new non-stimulant mechanisms. |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | Review of ADHD pharmacotherapy beyond stimulants, which carry misuse and dependence risks. |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacol Ther | Review of pharmacological, neuromodulatory, and psychotherapeutic options for adult ADHD. |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Commentary | CNS Spectr | Early commentary on solriamfetol for ADHD. No abstract is available. |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review (indirect) | Epilepsy Behav | Drugs for excessive daytime sleepiness in epilepsy, where ADHD is one comorbid cause. Indirect relevance. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2515814 | SUNOSI |
| 2515822 | SUNOSI |

## Safety Considerations

Please refer to the package insert for safety information. Health Canada warnings and contraindications are not available in the Evidence Pack, and no drug-interaction records were found.

Solriamfetol is known to raise heart rate and blood pressure. Cardiovascular safety should be assessed carefully in any ADHD use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (n=516) and a completed Phase 2/3 RCT (n=66) directly test solriamfetol in adults with ADHD, and a published randomized pilot supports the catecholaminergic rationale. The Phase 3 efficacy results have not been confirmed and the use would be off-label, so the decision carries guardrails.

**To proceed, the following is needed:**
- Primary and secondary outcome results from NCT05972044 and NCT04839562
- The Health Canada product monograph (warnings, contraindications, cardiovascular precautions)
- DrugBank mechanism-of-action data
- A cardiovascular monitoring plan covering blood pressure and heart rate, and an assessment of misuse potential

Other TxGNN predictions for this drug (insomnia, specific developmental disorder, ADHD inattentive type) have weaker evidence and are best treated as research questions. The remaining high-scoring predictions have no plausible mechanistic link and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

