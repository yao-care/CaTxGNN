---
layout: default
title: Pinaverium
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 1
---

# Pinaverium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Pinaverium: From Gastrointestinal Smooth Muscle Disorders to Benign Prostatic Hyperplasia

## One-Sentence Summary

Pinaverium is marketed in Canada under the brand name Dicetel and as generics. The Canadian licence records give no indication text, but from general pharmacology it is a gut-selective antispasmodic used for functional gastrointestinal disorders.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**.
This rests on the model score alone: **0 clinical trials** and **0 publications** currently support the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (general pharmacology: functional gastrointestinal disorders) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From general pharmacology, which the input data does not confirm, pinaverium is a gastrointestinal-selective L-type calcium channel blocker. It relaxes gut smooth muscle by limiting calcium entry into the cells.

A possible but unverified link to BPH is that calcium channel blockade could also relax smooth muscle in the prostate and lower urinary tract. That could ease lower urinary tract symptoms. The model's high score may reflect this kind of shared smooth muscle pharmacology, but no study in the Evidence Pack tests it.

There is also a significant pharmacokinetic doubt. Pinaverium is poorly absorbed systemically and acts mainly in the gut. Whether it reaches prostate or bladder tissue at pharmacologically relevant concentrations is unknown. This prediction should be treated as a hypothesis only.

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
| 1950592 | DICETEL |
| 2230684 | DICETEL |
| 2469677 | PINAVERIUM |
| 2469685 | PINAVERIUM |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high TxGNN score, with no clinical trials or literature behind it. The mechanism of action is not documented in the record, and pinaverium's poor systemic absorption makes it doubtful that it reaches the prostate.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to test the link between calcium channel blockade and prostate or bladder smooth muscle
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Approved indication text and dosage forms for the four DINs
- Preclinical or pharmacokinetic evidence on whether the drug reaches prostatic or bladder tissue
- A literature and trial search specifically on pinaverium and lower urinary tract symptoms or BPH

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

