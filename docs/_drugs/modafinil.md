---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Modafinil: From Wakefulness Disorders to Insomnia

## One-Sentence Summary

Modafinil is a wakefulness-promoting agent (eugeroic) widely approved internationally for excessive daytime sleepiness associated with narcolepsy, obstructive sleep apnea, and shift work sleep disorder — but it has not received marketing approval in Canada.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **99.85%** — however, this prediction direction runs **counter to the drug's known mechanism**, and the model likely reflects topological proximity between sleep-related disease nodes in the knowledge graph rather than a genuine therapeutic relationship.
Among the 29 clinical trials identified, none directly validate modafinil as a primary treatment for insomnia; **0 relevant publications** were retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy / Obstructive Sleep Apnea / Shift Work Sleep Disorder (no Canadian DIN on record) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 — mechanism-level / indirect evidence only; no direct RCT for insomnia |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Modafinil's primary mechanism involves inhibition of the dopamine transporter (DAT), reducing dopamine reuptake and thereby promoting wakefulness. Secondary effects on histamine, norepinephrine, and orexin pathways further reinforce its alerting activity. This places modafinil in the eugeroic class — a drug that increases arousal, not sedation.

The prediction of efficacy in insomnia is **mechanistically paradoxical**: insomnia is a disorder of excess arousal or difficulty initiating/maintaining sleep, while modafinil actively promotes wakefulness. Indeed, insomnia is a well-documented **adverse effect** of modafinil itself (reported in up to 5% of patients in controlled trials). A meaningful therapeutic signal in insomnia would require either a completely different mechanism than currently understood, or a very specific clinical subtype (e.g., chronic sleep-restriction fatigue leading to paradoxical rebound insomnia) that no current trial has evaluated.

The TxGNN high score (0.9985, rank 3,576 overall) most plausibly reflects **topological proximity** in the knowledge graph between modafinil and sleep-related disease nodes. Both narcolepsy and insomnia share biological annotations (orexin signalling, circadian rhythm genes, polysomnographic phenotypes), which the graph-based model treats as proximity — but proximity in a disease network does not translate to therapeutic equivalence. This is a known limitation of graph-based repurposing models when the drug's action is directionally opposite to the disease pathophysiology. Clinicians should interpret this as a **flag for caution**, not an actionable signal.

---

## Clinical Trial Evidence

The 29 trials retrieved span a wide range of conditions and mostly involve armodafinil (the R-enantiomer of modafinil) rather than modafinil itself. Only a small subset directly address insomnia. The most relevant trials are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | **Most directly relevant.** Phase 4 RCT of modafinil alone or combined with CBT-I in patients with **primary insomnia**. Assessed daytime functioning and insomnia severity — results would clarify whether modafinil's alerting effect indirectly reduces insomnia via homeostatic sleep pressure |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I ± armodafinil for insomnia and fatigue in female breast cancer survivors post-chemotherapy. Armodafinil used as adjunct; insomnia was a secondary endpoint. Evidence grade B — indirect and in a specific oncology population |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot study of brief behavioural therapy for insomnia (BBT-I) ± armodafinil 150 mg/day in breast cancer patients. Insomnia was the primary management target. Evidence grade B — oncology-specific; armodafinil, not modafinil |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil vs. CBT-I vs. combination for insomnia comorbid with obstructive sleep apnea. Directly studies insomnia as primary outcome, though drug is armodafinil and population has comorbid SDB |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform protocol for sleep disturbances in Long COVID (PASC). Flexible multi-intervention design; modafinil may be one arm but intervention allocation is appendix-specific |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | 8-week RCT of modafinil vs. placebo in stable bipolar disorder to address sleep dysregulation and cognitive impairment. Circadian and sleep outcomes included, but not insomnia as isolated endpoint |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for sleep/wake disturbances in older adults. Enrolled only 2 participants before termination — no usable data |
| [NCT01121536](https://clinicaltrials.gov/study/NCT01121536) | Phase 3 | Terminated | 867 | 6-month open-label extension of armodafinil as adjunctive therapy for bipolar I depression. Large scale but terminated; primary safety study, not directed at insomnia |
| [NCT03620253](https://clinicaltrials.gov/study/NCT03620253) | Phase 3 | Terminated | 9 | Modafinil for residual cognitive impairment in remitted depression. Terminated after enrolling only 9 of expected participants. Insomnia was not the target endpoint |
| [NCT00917748](https://clinicaltrials.gov/study/NCT00917748) | Phase 3 | Completed | 84 | Modafinil vs. placebo for fatigue and quality of life in patients with metastatic breast or prostate cancer on docetaxel chemotherapy. Sleep disturbance was one secondary outcome but insomnia treatment was not the primary aim |

> **Note:** The majority of trials in this dataset use **armodafinil** (not modafinil), target **fatigue or excessive sleepiness** (not insomnia), or involve highly specific disease populations (cancer, Parkinson's, bipolar disorder). No trial was identified where modafinil was tested as a primary pharmacotherapy for idiopathic insomnia in a general adult population.

---

## Literature Evidence

Currently no related literature available.

> PubMed query for modafinil + insomnia returned 0 results on the data retrieval date (2026-03-25). This absence is itself informative: despite decades of clinical use, modafinil has not generated a body of literature supporting its use as an insomnia treatment.

---

## Canada Market Information

Modafinil is **not approved and not marketed in Canada** (no DIN on record). There are no Health Canada licences to list.

> For reference: modafinil (brand name Provigil) holds approved indications in the United States (narcolepsy, OSA-related sleepiness, shift work sleep disorder) and many other jurisdictions. Its Schedule IV controlled substance status in the US and controlled/prescription-only status in most countries would apply to any future Canadian regulatory pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No Canadian product monograph is available (drug not marketed). Based on international product labelling, clinicians should be aware that insomnia is a commonly reported **adverse event** of modafinil, not an indication — a critical distinction for this repurposing hypothesis. Prescribers considering off-label use in any sleep context should consult the most recent prescribing information from a jurisdiction where the product is approved (e.g., US FDA label).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high-confidence prediction (99.85%) for modafinil in insomnia is mechanistically inconsistent — modafinil is a wakefulness-promoting agent whose primary pharmacology would be expected to **worsen** insomnia, and insomnia is in fact listed as a known adverse effect. The evidence base consists entirely of indirect signals (trials targeting fatigue/sleepiness in oncology or psychiatric patients, using armodafinil rather than modafinil, with insomnia as a secondary or absent endpoint). No literature evidence was retrieved. This prediction should be flagged as a likely **false positive arising from knowledge graph topology** and deprioritised relative to other TxGNN candidates.

**To proceed, the following would be needed:**
- Mechanistic re-evaluation: identify any proposed secondary mechanism (e.g., orexin system normalisation, circadian entrainment) that could plausibly benefit insomnia without exacerbating arousal
- Review results from NCT00124384 (the only Phase 4 trial of modafinil in primary insomnia) to determine whether daytime alerting indirectly improved night-time sleep architecture
- Clarify whether the prediction may apply to a specific insomnia subtype (e.g., hypersomnia-insomnia syndrome, insomnia secondary to shift work disorder) where daytime function normalisation could be a therapeutic strategy
- Obtain full MOA data from DrugBank and Canadian/US product monograph safety sections before any clinical translation discussion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

