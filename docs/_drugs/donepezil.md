---
layout: default
title: Donepezil
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is an acetylcholinesterase inhibitor, widely known as a treatment for Alzheimer's disease (the supplied Canadian licence records do not list indication text).
The TxGNN model predicts it may be effective for **psychogenic movement disorders**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (from general drug knowledge; not stated in the supplied licence data) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on general pharmacology, donepezil is a cholinesterase inhibitor that raises central cholinergic tone. Its efficacy in Alzheimer's disease is established, and cholinergic signalling interacts with basal ganglia circuits, which is why a movement-related prediction is not implausible.

However, no rationale specific to functional (psychogenic) movement disorders is supported by the supplied data. The link is inferred from general donepezil pharmacology, and the similarity to the original indication has not been assessed. The high TxGNN score should be read as a model-derived hypothesis, not as evidence of benefit.

For context, other TxGNN predictions for this drug have more supporting material than this top-ranked one. Examples are chronic tic disorder (small human reports and mouse studies) and lingual-facial-buccal dyskinesia (Cochrane reviews of cholinergic drugs as a class). Both are still at the research-question stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

20 licences are on record; the 5 main ones are listed below. Dosage form, manufacturer and approved indication text were not provided in the supplied data.

| DIN | Product Name |
|---------|------|
| 02362279 | APO-DONEPEZIL |
| 02475278 | DONEPEZIL |
| 02328682 | SANDOZ DONEPEZIL |
| 02340615 | TEVA-DONEPEZIL |
| 02322331 | PMS-DONEPEZIL |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no registered trials, no supporting literature, and no disease-specific mechanistic rationale. Donepezil is marketed in Canada, but that does not add evidence for this new indication.

**To proceed, the following is needed:**
- A systematic literature search for cholinesterase inhibitors in functional/psychogenic movement disorders
- Mechanism of action data (MOA), for example from DrugBank
- Health Canada package insert warnings and contraindications for safety screening
- Consideration of the counter-signal that cholinesterase inhibitors can cause or worsen movement disorders (a 2025 systematic review examines this in Alzheimer's patients)
- Consideration of moving resources to better-supported predictions for this drug, such as chronic tic disorder or tardive dyskinesia

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

