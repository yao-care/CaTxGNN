---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 916
evidence_level: L5
indication_count: 9
---

# Topiramate
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is an antiseizure medication. The Canadian license records provided carry no indication text, so this is inferred from the supporting literature in the Evidence Pack. The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **0 clinical trials** and **0 publications** support this direction, so the prediction is not backed by any evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (inferred from the literature; no approved indication text in the license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Topiramate is generally described as blocking voltage-gated sodium channels, enhancing GABA-A receptor activity, antagonizing AMPA/kainate glutamate receptors, and weakly inhibiting carbonic anhydrase. This is general pharmacology, not data from the Evidence Pack.

None of these actions is an established antitumour mechanism. Epilepsy and a tumour of the trigeminal nerve are different disease types, and no credible mechanistic link is identified for this indication. The very high score (99.70%) is most likely a knowledge-graph proximity artifact, possibly from shared neuro-anatomical or trigeminal-related nodes. It should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Topiramate is marketed in Canada under 20 DINs. The records provided do not include dosage form or approved indication text. Five authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 2279614 | APO-TOPIRAMATE |
| 2345269 | JAMP TOPIRAMATE TABLETS |
| 2544377 | JAMP TOPIRAMATE TABLETS |
| 2262991 | PMS-TOPIRAMATE |
| 2287781 | GLN-TOPIRAMATE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature, and no plausible antitumour mechanism, which places it at evidence level L5. There is no basis to move it forward.

**To proceed, the following is needed:**
- Any independent evidence (preclinical or clinical) that topiramate affects trigeminal nerve tumours
- Mechanism of action data from DrugBank, to test whether any mechanistic link exists
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Approved indication text and dosage forms for the Canadian DINs

Other predictions for this drug (visual epilepsy, thinking seizures, reading seizures) are mostly narrower forms of epilepsy, which is already topiramate's original use, so they are not true repurposing signals. Reviewing them would be a better use of effort than pursuing this one.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

