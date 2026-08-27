---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

Using the evidence pack, I selected **insomnia** (rank 2, TxGNN score 99.80%, L1 evidence) rather than the top-ranked "trigeminal nerve neoplasm" as the primary predicted indication, because the evidence pack's own rationale flags rank 1 as a likely knowledge-graph false positive with zero supporting trials or literature. Insomnia is the only candidate in this pack with a completed Phase 3 RCT, 23 registered trials, and 18 publications — the substantively decision-relevant signal. This deviation is noted explicitly below.

---

# Lorazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

> Lorazepam is a benzodiazepine (GABA-A receptor positive allosteric modulator) historically used for anxiety, sedation, and seizure control.
> The TxGNN model predicts it may be effective for **Insomnia**,
> with **23 clinical trials** and **18 publications** currently supporting this direction.
>
> Note: The single highest-scoring TxGNN prediction in this evidence pack ("trigeminal nerve neoplasm") was excluded from this report because it has **zero clinical trials and zero literature**, and the model's own rationale identifies it as a probable embedding artifact/false positive with no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in Canadian (Health Canada) regulatory records — the drug is not currently marketed in Canada. Classically used as an anxiolytic / sedative-hypnotic (benzodiazepine class), per the pharmacology stated in this evidence pack. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text was not returned for this drug (flagged as a High-severity data gap, DG002). However, the evidence pack's own repurposing rationale confirms the working pharmacology: Lorazepam is a **GABA-A receptor positive allosteric modulator**, producing central nervous system depression, anxiolysis, and anticonvulsant effects — the well-established core pharmacology of the benzodiazepine class.

Lorazepam's original therapeutic uses (anxiety, sedation, seizure control) and the predicted new indication (insomnia) share the same underlying mechanism: GABA-A potentiation produces sedative-hypnotic effects that induce and maintain sleep. This is not a speculative cross-disease inference — sedation/sleep induction is a direct, on-target pharmacological effect of the drug class, not an indirect or off-target mechanism. Benzodiazepines, including lorazepam specifically, have in fact been used clinically and studied for insomnia for decades (see literature from 1988 onward below), and a lorazepam-containing combination product (SM-1, with diphenhydramine and zolpidem) has been directly tested in Phase 2/3 trials for transient insomnia.

The main caveat is that benzodiazepine use for chronic insomnia is increasingly de-emphasized in guidelines due to tolerance, dependence, and withdrawal risk — several trials in this evidence pack (e.g., BE-SAFE, benzodiazepine cessation studies) reflect this shift toward *reducing* rather than expanding benzodiazepine use in sleep disorders, which should temper the strength of the "Go" signal despite the mechanistic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | Completed | 85 | Randomized, double-blind, 4-way crossover trial of SM-1 (diphenhydramine + zolpidem + lorazepam) vs. two comparator combinations and placebo in a phase-advance model of transient insomnia — direct efficacy/safety evidence. |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | Withdrawn | 0 | Planned double-blind, placebo-controlled trial of SM-1 for transient insomnia in adults; withdrawn before enrollment, so contributes no outcome data. |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | Completed | 39 | Single-dose pharmacodynamic study of SM-1 vs. comparator/placebo on total sleep time in a 5-hour phase-advance insomnia model. |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | Not yet recruiting | 14 | Crossover pharmacodynamic study of SM-1 vs. diphenhydramine+lorazepam in a 3-hour phase-advance transient insomnia model. |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1400 | Taiwanese prospective cohort assessing risk/benefit, usage patterns, and outcomes of hypnotics (including benzodiazepines) in elderly patients with sleep disorders. |
| [NCT02135198](https://clinicaltrials.gov/study/NCT02135198) | Phase 1 | Completed | 12 | Crossover biomarker study of a GABA-A modulator (AZD7325) on cortical inhibition, providing class-level GABAergic pharmacodynamic support relevant to insomnia/sedation mechanisms. |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | Completed | 12 | Crossover biomarker study of GABA-A modulator AZD7325 on cutaneous sensation, contextualizing benzodiazepine-class GABAergic effects and tolerability profile. |

*(7 of 23 registered trials shown, prioritized for direct relevance to lorazepam and GABAergic hypnotic mechanisms; trials focused on benzodiazepine deprescribing/cessation or unrelated psychiatric indications were excluded as not supportive of this indication.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | Journal of Clinical Pharmacology | Double-blind crossover trial in 8 chronic insomniacs: lorazepam 2 mg outperformed flurazepam 30 mg on most sleep parameters over 3 weeks. |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | The Medical Letter on Drugs and Therapeutics | Independent review of pharmacologic options for chronic insomnia, including benzodiazepines. |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohort | International Clinical Psychopharmacology | Evaluated lorazepam 0.5 mg TID vs. 1.5 mg HS in primary insomnia; TID dosing hypothesized to better address daytime fatigue symptoms. |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | Journal of Multidisciplinary Healthcare | Reviews efficacy, safety, and drug-drug interactions of insomnia therapies ("coronasomnia") in COVID-19 patients. |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Medicine | Analysis of hypnotic prescribing patterns (including benzodiazepines) in a large managed-care population. |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Preclinical | Drug Delivery | Developed a microemulsion-based intranasal delivery system for lorazepam (with diazepam and alprazolam) and demonstrated sleep-induction efficacy in a rat model. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacokinetics of anxiolytic drugs, the most widely prescribed psychoactive drug class, relevant to sedative-hypnotic dosing. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquilizer use (dose, efficacy, adverse effects) in elderly patients with chronic non-communicable disease. |
| [41392764](https://pubmed.ncbi.nlm.nih.gov/41392764/) | 2026 | RCT (preclinical) | Food & Function | Mouse-model RCT showing a probiotic strain ameliorates insomnia via GABA/serotonin signaling — supports the GABAergic mechanism relevant to insomnia broadly, though not lorazepam-specific. |
| [39315391](https://pubmed.ncbi.nlm.nih.gov/39315391/) | 2024 | Cohort | BMJ Neurology Open | Characterizes benzodiazepine prescribing patterns, including for sleep-related complaints, in a US clinical population. |

---

## Canada Market Information

Lorazepam currently has **no active Health Canada market authorization** under this evidence pack (`market_status: 未上市` / Not Marketed, `total_licenses: 0`). No Drug Identification Numbers (DINs) or product listings are available to summarize.

---

## Safety Considerations

Please refer to the Health Canada product monograph for safety information. No key warnings, contraindications, or drug-drug interaction data were returned in this evidence pack (all fields flagged as Data Gap DG001 — a **Blocking**-severity gap that prevents formal S1 safety pre-screening).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insomnia has the strongest evidentiary support in this evidence pack — one completed Phase 3 RCT and several supporting Phase 1/2 trials directly testing a lorazepam-containing combination product, plus literature dating back to 1988 establishing lorazepam's hypnotic efficacy — combined with a mechanistically direct (not speculative) link via GABA-A receptor potentiation. However, benzodiazepine-class dependence, tolerance, and withdrawal risks, the complete absence of safety/contraindication data (DG001, Blocking), and the lack of any current Canadian market authorization mean this cannot proceed as an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph warnings, contraindications, and precautions (DG001 — Blocking, must be resolved before any S1 safety evaluation)
- Formal DrugBank-sourced mechanism-of-action documentation (DG002 — High priority)
- Drug-drug interaction data (current query status: not found)
- Clarification of regulatory pathway given zero current Canadian DINs (research-use classification vs. new submission)
- A dependence/withdrawal risk assessment specific to chronic (vs. transient) insomnia use, given benzodiazepines' well-documented long-term safety concerns in this population
- Follow-up on NCT04396327 (not yet recruiting) and re-evaluation of why NCT03338764 (Phase 3) was withdrawn, as both affect confidence in the L1 evidence rating
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

