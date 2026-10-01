---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 2
---

# Nimodipine
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

# Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a brain-selective calcium channel blocker, marketed for subarachnoid hemorrhage.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid hemorrhage (the Canadian license record does not list an indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Nimodipine is a dihydropyridine L-type calcium channel blocker with brain-selective activity, and its efficacy in subarachnoid hemorrhage is established.

Homozygous familial hypercholesterolemia is caused by loss of function of the LDL receptor (LDLR). Nimodipine has no known action on LDLR, PCSK9, or hepatic LDL clearance, so no direct mechanistic link has been established. Dihydropyridine calcium channel blockers have been reported to have modest anti-atherosclerotic or vascular effects. These would not address the underlying lipid defect.

The high score of 0.993 comes from a knowledge-graph prediction. It may reflect network proximity to cardiovascular drugs rather than a real biological mechanism, so it should be treated as a hypothesis only.

The model also ranked a second candidate, **nephrogenic syndrome of inappropriate antidiuresis** (score 99.05%). This condition is caused by gain-of-function mutations in the vasopressin V2 receptor gene (AVPR2). Nimodipine has no known V2 receptor antagonism or effect on the downstream cAMP-AQP2 pathway. This candidate is also L5 with no trials or literature, and carries a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2325926 | NIMOTOP | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). There are no registered trials or publications, and no plausible mechanistic link between L-type calcium channel blockade and the LDLR defect underlying homozygous familial hypercholesterolemia.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to test for any biological link
- Preclinical or clinical evidence linking nimodipine to LDL metabolism
- Confirmation of the dosage forms and approved indication for the Canadian license (DIN 2325926)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

