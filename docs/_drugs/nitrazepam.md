---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 3
---

# Nitrazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nitrazepam: From Benzodiazepine Sedative-Hypnotic to Insomnia

## One-Sentence Summary

Nitrazepam is a benzodiazepine internationally known as a sedative-hypnotic (brand name Mogadon), though it currently holds no marketing authorization in Canada. The TxGNN model predicts it may be effective for **insomnia (sleep disorder, initiating and maintaining sleep)** — a use that aligns directly with its established pharmacological class — supported by **20 publications**, including one randomized controlled trial, though **no registered clinical trials** exist for this specific candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — Nitrazepam is not currently marketed in Canada; internationally it is a recognized benzodiazepine sedative-hypnotic (Mogadon) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep (Insomnia) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Nitrazepam is a benzodiazepine that enhances GABA-A receptor chloride-channel activity, producing sedative and hypnotic effects — this is its internationally recognized core indication (marketed abroad as Mogadon).

Unlike many TxGNN candidates that link a drug to a genuinely novel disease area, this prediction essentially reconstructs the drug's own well-established therapeutic identity: a benzodiazepine hypnotic predicted to be useful for insomnia. The mechanistic link is therefore direct and pharmacologically self-evident rather than a speculative extrapolation, which is reflected in the relatively strong evidence level (L2) despite the absence of trials registered specifically against this candidate pairing.

The main gap is regulatory, not mechanistic: Nitrazepam has no current Canadian market presence (0 DINs), so this evidence pack should be read as confirming a known pharmacological identity for a product that would need a fresh regulatory pathway in Canada rather than as a repurposing discovery in the traditional sense.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT (double-blind cross-over) | Acta Psychiatrica Scandinavica | Nitrazepam 5mg compared with triazolam 0.25mg in 26 geriatric inpatients; similar sleep quantity/quality and psychomotor performance between drugs |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Cohort/Review | British Medical Journal | Nitrazepam (Mogadon) shown safe even in acute overdosage (up to 80 tablets, only drowsiness observed); double-blind trial found it as effective as butobarbitone as a hypnotic |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | PK study | Clinical Pharmacokinetics | Review of the clinical pharmacokinetic profile of nitrazepam |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report/Review | The British Journal of Psychiatry | Describes dependence associated with long-term nitrazepam (Mogadon) use |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Reviews hypnotic drug efficacy in the context of sleep physiology and pathology (REM/NREM cycling) |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults experience insomnia; prevalence rises with age, with psychological stress and hyperarousal as key risk factors |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskrift for den Norske Laegeforening | Reviews classification, diagnosis, and treatment approaches for insomnia |
| [20467592](https://pubmed.ncbi.nlm.nih.gov/20467592/) | 2010 | Review | Drugs of Today | Notes that benzodiazepine and non-benzodiazepine hypnotics improve sleep induction and maintenance, with differing effects on slow-wave and REM sleep |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Descriptive | British Medical Journal | Early observational report on nitrazepam's effects |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem review noting its hypnotic efficacy is comparable to benzodiazepines including nitrazepam, flurazepam, temazepam, and triazolam |

---

## Canada Market Information

Nitrazepam is not currently marketed in Canada — no DIN records exist in the Health Canada database.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: this evidence pack flags Canadian labeling warnings/contraindications and DDI data as outstanding data gaps — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between nitrazepam's GABA-A agonism and insomnia is well-established pharmacologically and supported by one RCT plus a body of literature spanning five decades, justifying evidence level L2. However, the complete absence of Canadian market authorization, safety labeling, and DDI data means this cannot proceed without further regulatory and safety work.

**To proceed, the following is needed:**
- Canadian (or comparable jurisdiction) product labeling — key warnings, contraindications, and dosing guidance (currently a Blocking data gap)
- Formal drug interaction (DDI) profile
- Confirmed mechanism-of-action documentation from DrugBank or equivalent primary source
- A regulatory pathway assessment given the drug currently holds zero DINs in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

