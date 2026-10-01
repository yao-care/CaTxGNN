---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 956
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Valproic acid is an established antiseizure medication, and the Canadian license records supplied here do not state an approved indication.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are currently **0 clinical trials** and **1 publication** (which does not address this tumour type), so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the general approved use of this drug class; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, valproic acid is a widely used antiseizure drug. Its effect in epilepsy is established, and the one mechanism that could theoretically apply to tumours is histone deacetylase (HDAC) inhibition.

The evidence review found no credible mechanistic link between valproic acid and trigeminal nerve tumours. The score of 99.97% is a model output only. The one paper retrieved concerns Sturge-Weber syndrome, a neurocutaneous vascular disorder, not a trigeminal neoplasm. The relationship between epilepsy treatment and this tumour indication is therefore unsupported by the data provided.

Other predictions for this drug have much stronger support, for example trigeminal neuralgia and several reflex epilepsies (reading seizures, startle epilepsy). These are more plausible repurposing directions than the tumour indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years (clinical features, course, treatment response). It is not about trigeminal nerve neoplasm and offers no efficacy evidence. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02239699 | APO-DIVALPROEX |
| 02458926 | MYLAN-DIVALPROEX |
| 00596418 | EPIVAL |
| 02236807 | PMS-VALPROIC ACID |
| 02458934 | MYLAN-DIVALPROEX |

Dosage form and approved indication text were not provided in the license records, so these columns are omitted. The DINs above are as supplied (leading zeros restored).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). There are no registered trials, and the single publication retrieved is unrelated to trigeminal nerve tumours. No credible mechanism links valproic acid to this indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for valproic acid, including any HDAC-inhibition evidence in nervous-system tumours
- Preclinical or clinical studies specifically in trigeminal nerve or related cranial nerve tumours
- Approved indication text for the Canadian licenses, to confirm the original indication
- Consider prioritising better-supported predictions for this drug (such as trigeminal neuralgia and reading seizures) over this one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

