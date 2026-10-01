---
layout: default
title: Oxtriphylline
parent: Model Prediction Only (L5)
nav_order: 688
evidence_level: L5
indication_count: 3
---

# Oxtriphylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Oxtriphylline: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Oxtriphylline is a choline salt of theophylline, marketed in Canada in the product CHOLEDYL EXPECTORANT, but its approved indication is not recorded in the available data.
The TxGNN model predicts it may be effective for **migraine disorder**, with a very high score.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available record |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Oxtriphylline is a methylxanthine, the same class as theophylline and caffeine. It is a non-selective adenosine receptor antagonist and phosphodiesterase inhibitor. Adenosine signaling is plausibly linked to migraine through cerebral vasomotor tone and trigeminovascular activation. Caffeine, a related methylxanthine, is already used as an analgesic adjuvant.

This link is indirect and speculative. Methylxanthines can also provoke headache and lower the seizure threshold, so the direction of effect is uncertain. The score of 99.64% is a computational prediction from the knowledge graph, not evidence of efficacy. Because the original indication and mechanism data are missing from the record, the relationship between the original and new indications cannot be assessed.

Two other migraine-related predictions have the same weakness:
- **Migraine with brainstem aura** (score 99.55%): no drug-specific evidence. The high score likely reflects proximity to the parent migraine node in the knowledge graph. A methylxanthine could plausibly worsen aura-related cortical excitability.
- **Migraine with or without aura, susceptibility to** (score 99.32%): this is a genetic susceptibility concept, not a directly treatable condition. The 20 retrieved publications cover epilepsy genetics and epilepsy-migraine shared mechanisms. None study oxtriphylline or theophylline.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 476374 | CHOLEDYL EXPECTORANT | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

As a theoretical class concern only (not drug-specific data), methylxanthines can provoke headache and lower the seizure threshold. This matters for a migraine indication, particularly migraine with aura. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the knowledge-graph score (Evidence Level L5). There are no clinical trials or drug-specific publications. The mechanistic link is indirect, and the known pharmacology of methylxanthines (headache provocation, lowered seizure threshold) could work against the proposed use. Safety data is also missing.

**To proceed, the following is needed:**
- The Health Canada package insert, to establish the approved indication, warnings, and contraindications. This blocks any safety screening.
- Mechanism of action data from DrugBank.
- A literature search specific to oxtriphylline or theophylline and migraine, since the current retrieval matched only on disease terms.
- A mechanistic assessment of whether adenosine antagonism would help or worsen migraine, including the seizure-threshold concern.
- Confirmation of the dosage form and route of the marketed product, to check compatibility with a migraine use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

