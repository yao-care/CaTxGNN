---
layout: default
title: Levomilnacipran
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 6
---

# Levomilnacipran
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levomilnacipran: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

> Levomilnacipran (DrugBank DB08918) is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally developed and approved for **major depressive disorder (MDD)**.
> The TxGNN model's top-ranked candidate (benign paroxysmal torticollis of infancy) was screened out as biologically implausible model noise; the strongest defensible signal instead points to **Melancholia**, a severe MDD subtype,
> supported by **0 dedicated clinical trials** but **20 publications** on levomilnacipran's antidepressant pharmacology — none of which directly studied melancholia as a named indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — inferred from literature evidence in this pack; the formal `original_indications`/`original_moa` registry fields are a flagged data gap (DG002) |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

**Note on candidate selection:** TxGNN's #1-ranked prediction (benign paroxysmal torticollis of infancy) and #2 (agoraphobia) carry no supporting trials or literature and were explicitly flagged in the model rationale as implausible/noise (an adult antidepressant predicted for an infantile paroxysmal disorder). Melancholia and neurotic depression share the same, stronger literature base (both L3/S2), so melancholia — the clinically recognized MDD subtype — is used as the lead candidate here.

---

## Why is This Prediction Reasonable?

The formal mechanism-of-action field for levomilnacipran is a documented data gap (DG002) in this evidence pack. However, the literature evidence collected under this same pack consistently and independently characterizes levomilnacipran as a **serotonin-norepinephrine reuptake inhibitor (SNRI)** — notably more potent against norepinephrine than serotonin reuptake relative to other SNRIs (PMID 40875503), and it is the more active enantiomer of milnacipran (PMID 26150694).

Melancholia is not a separate disease from a pharmacological standpoint — it is a severe, biologically-driven subtype within the MDD spectrum, characterized by pronounced anhedonia, psychomotor disturbance, and blunted mood reactivity. Because levomilnacipran's approved indication is adult MDD, and its proposed mechanism (elevating synaptic 5-HT/NE) is the same pathway targeted across the MDD spectrum, extrapolation to melancholia has direct pharmacological plausibility.

That said, plausibility is not evidence of efficacy in this specific subtype: every supporting publication in this pack studies levomilnacipran in "MDD" broadly (efficacy, safety, tolerability, pharmacokinetics) — none isolates or names melancholia as a study population. The TxGNN score therefore reflects strong drug-class/disease-family proximity rather than a validated, disorder-specific signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38700708](https://pubmed.ncbi.nlm.nih.gov/38700708/) | 2024 | RCT (Phase 3) | J Child Adolesc Psychopharmacol | Two Phase 3, randomized, double-blind, placebo/active-controlled trials of levomilnacipran ER in pediatric (7–17y) MDD |
| [27455513](https://pubmed.ncbi.nlm.nih.gov/27455513/) | 2016 | Post-hoc analysis (Phase 3 RCT) | Int Clin Psychopharmacol | Post-hoc analysis of Phase 3 trial (NCT01034462, N=429) linking motivation/energy improvement to functional outcomes in MDD |
| [29197738](https://pubmed.ncbi.nlm.nih.gov/29197738/) | 2018 | Review/Network meta-analysis | J Affect Disord | Compares efficacy/safety of levomilnacipran, vilazodone and vortioxetine vs other second-generation antidepressants in MDD |
| [24016209](https://pubmed.ncbi.nlm.nih.gov/24016209/) | 2013 | Review | Int J Clin Pract | Systematic review of levomilnacipran ER efficacy/safety in MDD; reports NNT/NNH/LHH |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Review/Network meta-analysis | Mol Psychiatry | Network meta-analysis comparing antidepressants for MDD maintenance-phase treatment |
| [30611836](https://pubmed.ncbi.nlm.nih.gov/30611836/) | 2019 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Systematic review of pharmacological treatments targeting anhedonia in MDD — a core melancholic feature |
| [27508501](https://pubmed.ncbi.nlm.nih.gov/27508501/) | 2016 | Review | Psychother Psychosom | Critical review of safety/tolerability of newer antidepressants including levomilnacipran |
| [33549697](https://pubmed.ncbi.nlm.nih.gov/33549697/) | 2021 | Review/Meta-analysis | Prog Neuropsychopharmacol Biol Psychiatry | Meta-analysis of GI side effects across second-generation antidepressants in MDD |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guideline | Clin Pharmacol Ther | CPIC pharmacogenetics guideline for SNRIs/SSRIs including levomilnacipran (CYP2D6 etc.) |
| [38057644](https://pubmed.ncbi.nlm.nih.gov/38057644/) | 2024 | Preclinical (animal) | Mol Neurobiol | LPS-induced depression model: levomilnacipran acts via BDNF/TrkB–PI3K/Akt/mTOR pathway |

---

## Canada Market Information

Levomilnacipran is currently **not marketed in Canada** — no Health Canada Drug Identification Numbers (DINs) are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Health Canada/TFDA label warnings and contraindications are an outstanding **blocking data gap** — DG001 — and no drug-drug interaction records were found.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Melancholia extrapolation is mechanistically plausible and better supported than TxGNN's top-ranked candidates, but every piece of evidence addresses MDD generally rather than melancholia specifically (no dedicated trials, L3/S2), the drug has zero Canadian market presence, and the mandatory safety pre-assessment (S1) cannot proceed while label warnings/contraindications remain an unresolved blocking data gap (DG001).

**To proceed, the following is needed:**
- Retrieve official levomilnacipran label/monograph (warnings, contraindications) to close DG001 and unblock S1 safety review
- Confirm formal mechanism-of-action documentation from DrugBank/regulatory source to close DG002
- Clarify whether melancholia would require a distinct regulatory filing or falls under the existing MDD indication
- Assess Health Canada market-entry pathway given current non-marketed status (0 DINs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

