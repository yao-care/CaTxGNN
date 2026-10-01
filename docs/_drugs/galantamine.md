---
layout: default
title: Galantamine
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 9
---

# Galantamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Galantamine: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Galantamine is a cholinesterase inhibitor used for cognitive impairment in Alzheimer's disease. The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **0 clinical trials** and **0 publications** support this specific prediction, so it is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (taken from the literature in the pack; the license records contain no indication text) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Galantamine is an acetylcholinesterase inhibitor and an allosteric modulator of nicotinic receptors. Structured mechanism-of-action data were not available, so this description comes from the model-generated rationale, not from DrugBank.

The data do not document a plausible link between galantamine and functional (psychogenic) movement disorders. The pack also notes that the score is not a discriminating signal, because nearly all candidates score about 0.999. On its own, the 99.90% figure should not be read as strong support.

Other predictions for this drug have more supporting material, though still indirect. "Lingual-facial-buccal dyskinesia" (related to tardive dyskinesia) has one randomized crossover trial of galantamine in tardive dyskinesia (PMID 17388711), plus Cochrane reviews of cholinergic drugs. "Extrapyramidal and movement disease" has two trials in schizophrenia and a systematic review. Both are still indirect evidence, and both include signals of possible harm (see Safety Considerations). If this drug is pursued, one of these would be a better starting point than the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada lists 12 licenses for galantamine. Dosage form and approved indication text were not supplied in the data. Based on the product names, these appear to be extended-release formulations.

| DIN | Product Name |
|---------|------|
| 02339447 | MYLAN-GALANTAMINE ER |
| 02443031 | GALANTAMINE ER |
| 02443023 | GALANTAMINE ER |
| 02339455 | MYLAN-GALANTAMINE ER |
| 02425165 | AURO-GALANTAMINE ER |

## Safety Considerations

Please refer to the package insert for safety information.

The literature retrieved for other predictions raises movement-related concerns that are relevant if galantamine were considered for any movement disorder:
- A 2025 systematic review examined movement disorders associated with acetylcholinesterase inhibitors, including galantamine, in Alzheimer's dementia.
- A pharmacovigilance study (PMID 24127392) reported a link between cholinesterase inhibitors and Pisa syndrome, a dystonia-type adverse event.

These are signals from the literature, not label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5). No trials or publications were found, and no mechanistic link is documented. Related literature on cholinesterase inhibitors and movement disorders suggests possible harm, not benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Evidence that specifically links galantamine to psychogenic movement disorders, or a switch to a better-supported candidate such as lingual-facial-buccal dyskinesia
- A review of the movement-disorder adverse event signals for cholinesterase inhibitors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

