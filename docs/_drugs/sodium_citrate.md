---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 848
evidence_level: L5
indication_count: 9
---

# Sodium Citrate
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

# Sodium Citrate: From Anticoagulant Solutions (Labelled Indication Not Recorded) to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate is marketed in Canada mainly as anticoagulant citrate solutions, but the data provided do not record a formal approved indication.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data (product names indicate anticoagulant citrate solutions) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication text was recorded for any Canadian licence. The Canadian products are anticoagulant citrate solutions, but the data do not say what they are approved to treat. Nothing in the data links sodium citrate to papillary conjunctivitis.

The 99.95% score is a model output (rank 1,535 in the TxGNN ranking), not clinical evidence. No trials or publications were retrieved to support or test the prediction. The model's own similarity assessment to the original indication is still pending. In its current form, the prediction should be treated as a hypothesis for screening, not a finding.

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
| 2529637 | Anticoagulant Sodium Citrate Solution, USP |
| 60313 | Anticoagulant Sod Citrate Soltn 4gm/100ml |
| 2377411 | Anticoagulant Sodium Citrate 4% W/V Solution, USP |
| 2496755 | Regiocit |
| 2469731 | Anticoagulant Citrate Dextrose Solution USP (ACD) Formula A |

Dosage form and approved indication text are not recorded for these licences. These are 5 of the 12 licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for this drug in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis has no supporting trials or literature, and neither the original indication nor the mechanism of action is available to build a mechanistic argument. The score alone is not enough to justify moving forward.

Among the other predicted indications, only "stomach disease" has any evidence at all. It is preclinical (in vitro studies combining 3-bromopyruvate with sodium citrate in gastric cancer cells), and the retrieved trials are largely unrelated to sodium citrate. That is not enough to change this decision.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Mechanism of action data (e.g., from DrugBank)
- Targeted searches for sodium citrate in ocular surface or conjunctival conditions, to find any real trials or literature
- Assessment of route compatibility, since the current products are not ophthalmic formulations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

