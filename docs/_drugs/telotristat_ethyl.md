---
layout: default
title: Telotristat Ethyl
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
---

# Telotristat Ethyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Telotristat ethyl: From Carcinoid Syndrome Diarrhea to Cauda Equina Syndrome

## One-Sentence Summary

Telotristat ethyl (marketed as XERMELO) is a peripheral serotonin-synthesis inhibitor, known for treating carcinoid syndrome diarrhea. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **0 clinical trials** and **0 publications** support this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Carcinoid syndrome diarrhea (from general product knowledge; the supplied license record has no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Telotristat ethyl inhibits peripheral tryptophan hydroxylase (TPH1), which lowers gut-derived serotonin. It has minimal central nervous system penetration. Detailed mechanism of action data is not included in the structured drug record. This description comes from the repurposing rationale in the evidence pack.

The link between the original and predicted indications is weak. Cauda equina syndrome is a compressive or structural neurological emergency that is managed surgically. Nothing in the supplied data shows a pharmacological pathway from peripheral TPH1 inhibition to this condition. The high score (0.994) most likely reflects the structure of the knowledge graph, not a pharmacological rationale.

The other top predictions are similarly unsupported. They include obsolete neurogenic bladder, postural orthostatic tachycardia syndrome, restless legs syndrome, endolymphatic hydrops, dry eye syndrome, Meniere disease, His bundle tachycardia, neurocirculatory asthenia and active cochleovestibular Meniere disease. All have scores above 97% and none has any trial or literature evidence. Several appear to be graph neighbors of one another, so they are not independent signals. For postural orthostatic tachycardia syndrome, lowering peripheral serotonin could plausibly worsen symptoms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2481553 | XERMELO | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no identifiable mechanism, so it stays at evidence level L5. The pharmacology (peripheral action with minimal CNS penetration) does not fit a compressive neurological condition like cauda equina syndrome.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the Canadian license details (dosage form, approved indication, manufacturer). The pack's inputs are labelled TFDA and DrugBank, so the Health Canada record needs verifying.
- Structured mechanism of action data from DrugBank
- A literature and trial search for any mechanistic or clinical link to cauda equina syndrome
- Mapping the obsolete neurogenic bladder term to a current ontology term before any further review
- If cauda equina syndrome stays unsupported, re-prioritizing the other predictions only if independent evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

