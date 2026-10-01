---
layout: default
title: Modafinil
parent: Moderate Evidence (L3-L4)
nav_order: 622
evidence_level: L4
indication_count: 1
---

# Modafinil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Modafinil: From Excessive Sleepiness Disorders to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting drug marketed in Canada. The Canadian approved-indication text is not in the data provided, but the trial records describe it as approved for sleepiness and fatigue in narcolepsy, sleep apnea and shift work sleep disorder.
The TxGNN model predicts it may be effective for **insomnia**, but the score looks like a knowledge-graph artifact rather than a real therapeutic signal.
**29 clinical trials** are linked to this prediction, mostly on armodafinil or on fatigue and sleepiness. Only one modafinil trial in primary insomnia was found, and **0 publications** are available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data; trial records describe sleepiness/fatigue in narcolepsy, sleep apnea and shift work disorder |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, modafinil is a wake-promoting agent. It inhibits the dopamine transporter and also affects orexin, histamine and norepinephrine signaling. Its established use is to reduce excessive sleepiness in sleep-wake disorders.

The very high TxGNN score (0.998) most likely reflects modafinil's dense links to sleep-wake disorders in the knowledge graph, not a rationale for treating insomnia itself. A wake-promoting drug would not be expected to help people sleep, and insomnia is a labeled adverse effect of modafinil.

The only defensible link is indirect. Modafinil might treat residual daytime fatigue or sleepiness in people with insomnia, for example alongside cognitive behavioral therapy for insomnia (CBT-I). That is a different indication from treating insomnia. The trials below fit this pattern: most pair armodafinil (the R-enantiomer of modafinil) with CBT-I and target daytime function.

---

## Clinical Trial Evidence

29 trials were retrieved. The 10 most relevant are listed below, prioritizing trials that name insomnia or sleep outcomes. None has reported efficacy results in the data provided. Several trials test armodafinil, not modafinil.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | Modafinil alone or with CBT-I in primary insomnia, assessing daytime functioning and insomnia severity. This is the only modafinil trial directly in insomnia; no results were provided |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I with or without armodafinil for insomnia and fatigue after chemotherapy in breast cancer patients. Armodafinil is an adjunct |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Randomized study of CBT-I with or without armodafinil for insomnia and fatigue in cancer survivors after chemotherapy |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot of brief behavioral therapy or CBT-I, with or without armodafinil 150 mg/day, for insomnia in breast cancer patients |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil, CBT-I, or both for insomnia comorbid with sleep apnea; outcomes are sleep continuity and adherence to CBT-I and CPAP |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for sleep/wake disturbances in older adults. Only 2 participants enrolled, so no inference is possible |
| [NCT00582491](https://clinicaltrials.gov/study/NCT00582491) | N/A | Completed | 44 | Modafinil, sleep and cognition in cocaine dependence, with objective sleep and sleepiness testing |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | Placebo-controlled trial of modafinil for circadian and cognitive dysfunction in stable bipolar disorder |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform protocol for sleep disturbances after COVID-19. The specific intervention is not confirmed from the data provided |
| [NCT00233090](https://clinicaltrials.gov/study/NCT00233090) | Phase 2 | Terminated | 21 | Modafinil vs placebo for fatigue after traumatic brain injury. The condition is fatigue, not insomnia |

Most of the remaining 19 trials cover armodafinil in bipolar depression, schizophrenia and shift work disorder. They also include fatigue in cancer, inflammatory bowel disease and Parkinson's disease, and unrelated studies. They are not direct evidence for insomnia.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

7 licenses are on record; 5 are shown. Dosage form and approved-indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 02430487 | AURO-MODAFINIL |
| 02432560 | MAR-MODAFINIL |
| 02530244 | MODAFINIL |
| 02239665 | ALERTEC |
| 02503727 | JAMP MODAFINIL |

---

## Safety Considerations

Please refer to the package insert for safety information.

Health Canada warnings and contraindications were not available in the Evidence Pack, and no drug-interaction records were found. The one safety point supported by the pack is that insomnia is a labeled adverse effect of modafinil. This runs against use of the drug for insomnia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by a plausible mechanism or by efficacy evidence. No literature was found, and the trials are mostly armodafinil adjunct studies or unrelated conditions. Insomnia is also a labeled adverse effect of the drug. The evidence level is L4.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications, which block safety screening
- Mechanism of action data, from DrugBank or another source
- Results and manual review of NCT00124384 (modafinil in primary insomnia) and the trials whose relevance grade is still pending
- A literature search on modafinil or armodafinil in insomnia and on residual daytime dysfunction alongside CBT-I
- A decision on whether the real target is insomnia itself or daytime sleepiness and fatigue in patients with insomnia. Only the second has any rationale.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

