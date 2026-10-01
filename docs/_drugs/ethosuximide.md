---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 362
evidence_level: L5
indication_count: 1
---

# Ethosuximide
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

# Ethosuximide: From Absence Seizures to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ethosuximide is an anti-seizure drug, used mainly for absence seizures. The approved-indication text is not in the supplied data, so this comes from general pharmacology.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, and no mechanistic link was identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence seizures (general knowledge; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on general pharmacology, ethosuximide is an anti-absence agent that mainly blocks T-type calcium channels (Cav3.x) in thalamic neurons. Its efficacy is established in absence seizures, not in any kidney or water-balance disorder.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor gene (*AVPR2*, e.g., R137C/R137L). These mutations make the receptor signal constantly, so the kidney retains water even without vasopressin. Nothing about T-type calcium channel blockade connects to V2 receptor signaling or renal water handling.

Antiepileptics such as carbamazepine and oxcarbazepine are more often linked to causing hyponatremia than to treating it. The very high TxGNN score is a knowledge-graph prediction only. Without clinical or literature support, the prediction should be treated as a hypothesis with no supported mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2545772 | MAR-ETHOSUXIMIDE |
| 23485 | ZARONTIN SYRUP |
| 22799 | ZARONTIN |
| 2547171 | ODAN-ETHOSUXIMIDE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no publications, and no plausible mechanistic link between T-type calcium channel blockade and V2 receptor-driven water retention. Evidence remains at L5 and the decision stays at the earliest screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Confirmed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence showing an effect on V2 receptor signaling or renal water handling
- Any published case reports or trials in NSIAD, or in related hyponatremia or antidiuresis disorders
- Consideration of hyponatremia risk in the safety assessment, since some antiepileptics are associated with it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

