---
layout: default
title: Pitolisant
parent: Moderate Evidence (L3-L4)
nav_order: 737
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Pitolisant: From Narcolepsy-Related Excessive Daytime Sleepiness to Insomnia

## One-Sentence Summary

Pitolisant (marketed in Canada as WAKIX) is a histamine H3 receptor antagonist/inverse agonist. It is used to promote wakefulness in narcolepsy-related sleepiness.
The TxGNN model predicts it may be effective for **insomnia** with a very high score, but only **1 registered clinical trial** (withdrawn, 0 participants) and **10 publications** were retrieved, and none of them shows efficacy in insomnia.
The predicted direction of effect also conflicts with the drug's mechanism, so this prediction is likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy-related excessive daytime sleepiness (taken from the retrieved literature and mechanism notes; the Health Canada indication text is not available in this pack) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From the literature, pitolisant is a selective histamine H3 receptor antagonist/inverse agonist. By blocking the H3 autoreceptor it increases histamine release in the brain and promotes wakefulness. It has been authorised in Europe and the USA for adults with narcolepsy with or without cataplexy.

The prediction does not hold up well mechanistically. Insomnia is a hyperarousal condition, and a wake-promoting drug pushes in the opposite direction from the therapeutic goal. Insomnia is also a recognised adverse effect of pitolisant. The high TxGNN score most likely reflects the drug's close knowledge-graph link to sleep-wake disorders in general, not a plausible therapeutic effect.

The retrieved literature covers narcolepsy, obstructive sleep apnea (OSA) and pediatric sleep disorders. None of it demonstrates a benefit in insomnia. Evidence is indirect only, and the direction of effect is unfavourable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Randomised, double-blind, placebo-controlled trial of pitolisant in alcohol use disorder, with sleep among the secondary outcomes. It was withdrawn before enrolment, so it produced no efficacy or safety data. It is not an insomnia trial. |

---

## Literature Evidence

None of these publications studies insomnia as a treatment target. They are listed as the closest available context (RCTs first).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet. Neurology | Phase 3 double-blind, placebo-controlled trial of pitolisant safety and efficacy in children aged 6 or older with narcolepsy, with or without cataplexy |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Randomised trial in OSA patients adhering to CPAP who still have residual excessive daytime sleepiness |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Double-blind, placebo-controlled trial of daytime sleepiness in moderate-to-severe OSA patients who refuse CPAP |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurologia | Real-life WAKE study of effectiveness and safety in type 1 narcolepsy patients unresponsive to or intolerant of prior treatments |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Cohort | Neurological Sciences | Retrospective single-center study of 40 Chinese pediatric narcolepsy patients treated with pitolisant |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Overview of histamine receptors, agonists and antagonists in health and disease |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Histaminergic changes in neuropsychiatric disorders. Pitolisant is cited for excessive sleepiness in narcolepsy, and doxepin (an H1 antagonist) for insomnia. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Profile of pitolisant in narcolepsy: design, development and place in therapy |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurology and Therapy | Narrative review of current and emerging therapies for pediatric sleep disorders, including OSA, insomnia and narcolepsy |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Pitolisant as an alternative stimulant for narcolepsy-cataplexy in teenagers with refractory sleepiness |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2516268 | WAKIX |
| 2516241 | WAKIX |

Dosage form and approved indication text are not available in the current data.

---

## Safety Considerations

- **Known adverse effect relevant to this prediction**: Insomnia is a recognised adverse effect of pitolisant, which makes use in insomnia counterintuitive.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered trial was withdrawn with zero enrollment, and no retrieved publication supports efficacy in insomnia. The wake-promoting mechanism runs opposite to the therapeutic goal, and insomnia is a known adverse effect. The high TxGNN score is best read as a model artifact.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication and dosage form)
- Mechanism of action data from DrugBank
- Any direct clinical evidence in insomnia, which is unlikely given the mechanism

For context, the second TxGNN prediction, attention deficit-hyperactivity disorder (score 99.36%), has a more coherent mechanistic rationale. H3 blockade raises dopamine, norepinephrine and acetylcholine release in attention-related cortical areas. It is supported only by reviews and preclinical work, so it is better treated as a research question for an exploratory study than as a ready candidate. The third prediction, faciodigitogenital syndrome, has no clinical or mechanistic support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

