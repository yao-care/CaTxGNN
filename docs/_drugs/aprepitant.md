---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Nausea and Vomiting Prevention to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is an NK1 (substance P) receptor antagonist, marketed in Canada as EMEND and EMEND TRI-PACK. The Evidence Pack does not list its approved indication, but it is generally known as an antiemetic for chemotherapy-induced nausea and vomiting. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (generally known: prevention of chemotherapy-induced nausea and vomiting) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Aprepitant blocks the NK1 receptor, the target of substance P. Detailed mechanism-of-action data from DrugBank are not available in the Evidence Pack, so this description relies on the mechanistic assessment supplied with the prediction.

NSIAD is caused by gain-of-function mutations in the AVPR2 gene. These make the vasopressin V2 receptor constitutively active, so the kidney keeps retaining water. The disease therefore sits in a different signaling pathway from NK1 blockade, and no established link connects the two.

The very high TxGNN score (99.97%, rank 1010 overall) most likely reflects proximity in the knowledge graph, not a demonstrated pharmacological rationale. The prediction should be treated as a hypothesis, not a supported candidate.

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
| 2298813 | EMEND TRI-PACK |
| 2298805 | EMEND |
| 2298791 | EMEND |

Dosage forms and approved indication text were not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry or literature support. The mechanism is also implausible: NK1 antagonism does not act on the constitutively active V2 receptor that drives NSIAD. A high model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking NK1 antagonism to water balance, vasopressin signaling or renal function
- Mechanism-of-action data from DrugBank, to support a mechanistic analysis
- Health Canada package insert warnings and contraindications, so safety screening can begin
- The Health Canada approved indication and dosage forms for each DIN

**Other top-10 predictions:**
- None of the other top-10 predictions has aprepitant-specific clinical evidence.
- Pulmonary hypertension and subarachnoid hemorrhage are marked "Research Question" because a plausible NK1 mechanism exists in preclinical models, but neither has clinical support.
- The publications retrieved for pulmonary hypertension and for the periodontal-related malformation syndrome are unrelated to aprepitant and should not be counted as evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

