---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Seizure Control to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a long-established anticonvulsant and sedative.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **1 loosely related publication**, so this is effectively a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; known as an anticonvulsant/sedative |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Phenobarbital enhances GABA-A receptor inhibition (a positive allosteric modulator). This gives it anticonvulsant and sedative effects. It has no known antineoplastic activity.

The prediction is hard to justify mechanistically. A GABAergic anticonvulsant has no established link to tumours of the trigeminal nerve. The very high TxGNN score is most likely a graph artifact, driven by neighbouring trigeminal and neurological nodes in the knowledge graph rather than by pharmacology. The only retrieved publication is a case series on Sturge-Weber syndrome, a neurocutaneous disorder, not a neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years, covering clinical features, course and treatment response. It does not address trigeminal nerve neoplasm or show phenobarbital efficacy for it. |

## Canada Market Information

Approved indication text and dosage forms are not recorded in the licence data. Five of the 7 licences are listed below.

| DIN | Product Name |
|---------|------|
| 2304090 | PHENOBARBITAL SODIUM INJECTION, USP |
| 645575 | PHENOBARB ELIXIR |
| 2304082 | PHENOBARBITAL SODIUM INJECTION, USP |
| 178799 | PHENOBARB |
| 178810 | PHENOBARB |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials, the single publication is off-topic, and there is no plausible antitumour mechanism. Other predictions for this drug in this pack are seizure-related (for example, reflex seizure subtypes) and are mechanistically more coherent. They remain indirect, class-level evidence.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence of antitumour activity, if the neoplasm direction is to be pursued
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Approved indication text for the Canadian licences
- Consideration of the seizure-related predictions as a more plausible research direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

