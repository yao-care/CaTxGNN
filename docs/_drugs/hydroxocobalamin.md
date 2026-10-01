---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Hydroxocobalamin: From Vitamin B12 Deficiency and Cyanide Poisoning to Esophageal Varices

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, used for B12 deficiency and cyanide poisoning (marketed in Canada as CYANOKIT).
The TxGNN model predicts it may be effective for **esophageal varices without bleeding** and **esophageal varices with bleeding**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Esophageal varices without bleeding (a second prediction, esophageal varices with bleeding, has an identical score) |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hydroxocobalamin is a vitamin B12 form, and its efficacy in B12 deficiency and cyanide poisoning is established. No established mechanistic link to esophageal varices has been identified.

One speculative angle is that hydroxocobalamin scavenges nitric oxide and can raise blood pressure. Nitric oxide signaling plays a role in portal hypertension, which drives varices. This pathway is unvalidated, and the direction of effect is uncertain and could be harmful, especially in an acute bleeding setting.

The high score (99.23%) may simply reflect knowledge-graph connectivity, such as shared neighbours among vitamin, liver disease and vascular nodes, rather than real biology. The bleeding and non-bleeding variants have identical scores, which suggests both terms map to the same graph neighbourhood. The score is therefore not independent evidence.

Acute variceal bleeding is currently managed with vasoactive drugs (terlipressin, octreotide), endoscopic band ligation and antibiotic prophylaxis. Nothing in the available data suggests hydroxocobalamin adds to these.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2375370 | CYANOKIT |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no clinical trials or publications, and the mechanistic link is speculative and possibly unfavourable. The Canadian marketing authorization does not cover this use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank, to assess the nitric oxide and portal hypertension hypothesis
- Preclinical or clinical literature on hydroxocobalamin in portal hypertension or variceal disease
- Confirmation of route compatibility and similarity to the original indication (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

