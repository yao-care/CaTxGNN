---
layout: default
title: Solriamfetol
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Solriamfetol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Solriamfetol: From Excessive Daytime Sleepiness to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Solriamfetol (DrugBank DB14754) is a dopamine/norepinephrine reuptake inhibitor (DNRI), previously identified in the literature as approved for excessive daytime sleepiness (EDS) associated with narcolepsy or obstructive sleep apnea.
The TxGNN model predicts it may also be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
with **2 completed clinical trials** (including a 516-patient Phase 3 RCT) and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Excessive daytime sleepiness (EDS) associated with narcolepsy or obstructive sleep apnea (per literature evidence — not formally recorded in this evidence pack's regulatory fields) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, literature evidence collected within this pack (PMID 34606437) identifies solriamfetol as a **dopamine/norepinephrine reuptake inhibitor (DNRI)** — it increases synaptic availability of dopamine and norepinephrine, which underlies its wake-promoting effect in EDS.

This catecholaminergic mechanism is pharmacologically analogous to established ADHD stimulant therapies (methylphenidate, amphetamines), which also act on dopamine/norepinephrine signaling to improve attention and executive function. This shared mechanistic pathway is a plausible biological basis for the TxGNN prediction, and is directly reflected in the repurposing rationale for a related, lower-ranked candidate (ADHD, inattentive subtype), which notes the mechanism is "identical to ADHD (combined type) and theoretically sound."

Critically, this mechanistic hypothesis is not purely theoretical — it has already been tested prospectively. The FOCUS trial (NCT05972044) is a completed, 516-participant, multi-center Phase 3 RCT specifically designed to evaluate solriamfetol in adult ADHD, and a smaller completed Phase 2/3 pilot study (NCT04839562, published as PMID 37819836) reported favorable tolerability and efficacy signals. This combination of mechanistic plausibility and completed prospective trial data distinguishes this candidate from several other TxGNN predictions in this pack that lack any supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | Completed | 516 | FOCUS trial: multi-center, randomized, double-blind, placebo-controlled parallel-group trial assessing efficacy and safety of solriamfetol in adults with ADHD |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | Completed | 66 | Double-blind, placebo-controlled pilot study of solriamfetol in adults aged 18–65 with a diagnosis of ADHD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | Remote, randomized, double-blind, placebo-controlled 6-week dose-optimization pilot trial (75mg/150mg) of solriamfetol in 60 adults with DSM-5 ADHD; examined efficacy and tolerability pattern |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Case Report | CNS Spectrums | Early clinical report describing solriamfetol use for ADHD symptoms |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | Reviews non-stimulant pharmacological options for ADHD, addressing limitations of traditional stimulant formulations |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | Focus on Phase III trial pipeline for ADHD treatments beyond stimulants, targeting alternative neurobiological mechanisms |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacol Ther | Comprehensive review of pharmacological, neuromodulatory, and psychotherapeutic interventions for adult ADHD |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review | Epilepsy & Behavior | Reviews drugs (including solriamfetol) for excessive daytime sleepiness and attentional deficits in epilepsy populations |

---

## Canada Market Information

Solriamfetol is **not currently marketed in Canada**. No Drug Identification Number (DIN) has been issued, and no Canadian product license or approved-indication text is available in this evidence pack.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) for solriamfetol has not yet been retrieved — this is flagged as a **Blocking** data gap (DG001) in this evidence pack, meaning safety pre-assessment (S1) cannot currently be completed. Please refer to the official product monograph (once available via Health Canada) or the FDA/EMA-approved labeling for solriamfetol (Sunosi) for interim safety reference.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction is supported by a mechanistically coherent rationale and a genuinely strong evidentiary base — including a completed 516-patient Phase 3 RCT (FOCUS) and a completed Phase 2/3 pilot RCT — which is unusually robust among the candidates in this evidence pack. However, this candidate cannot proceed past initial safety screening because official safety labeling (warnings/contraindications) is missing (Blocking gap, DG001), formal MOA documentation is unconfirmed (DG002), and the drug currently has zero market presence in Canada (0 DINs).

**To proceed, the following is needed:**
- Resolve DG001: obtain official product monograph / label safety data (warnings, contraindications) to complete S1 safety pre-assessment
- Resolve DG002: confirm formal mechanism of action record via DrugBank or equivalent source
- Clarify Canadian market-entry pathway, since solriamfetol currently holds no DIN
- Complete relevance grading for the FOCUS (NCT05972044) and pilot (NCT04839562) trials, currently marked "pending" in this evidence pack
- Note for context: several other TxGNN-predicted indications for this drug (e.g., faciodigitogenital syndrome, chondromyxoid fibroma, prionopathy) were independently flagged as low-confidence/Hold (L5, no supporting evidence), and the insomnia prediction carries an explicit mechanistic contradiction warning (solriamfetol is wake-promoting) — these should not be advanced without separate, dedicated review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

