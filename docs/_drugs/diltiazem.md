---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
---

# Diltiazem
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

# Diltiazem: From Cardiovascular Use to Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a non-dihydropyridine calcium channel blocker marketed in Canada, and the supplied data does not list its approved indications.
The TxGNN model predicts it may be relevant to **susceptibility to ischemic stroke**, but the ontology flags this disease term as **obsolete**.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied data |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Diltiazem is a non-dihydropyridine calcium channel blocker. The approved indications are also missing from the supplied data, so the relationship between the original and predicted indications cannot be assessed directly.

At the class level, calcium channel blockade could plausibly relate to ischemic stroke through blood pressure lowering, vasodilation, and reduced calcium-mediated neuronal injury. This is a general class rationale, not evidence for diltiazem itself.

The predicted disease term is marked "obsolete" in the ontology, so the prediction may map to a deprecated or merged concept. It should be re-mapped to a current stroke or cerebrovascular disease term before any further review. A high score alone (99.08%) cannot support a recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Diltiazem has 20 licences in Canada. The supplied data lists the five below and does not include dosage forms or approved indication text.

| DIN | Product Name |
|---------|------|
| 2528061 | JAMP DILTIAZEM CD |
| 2546450 | M-DILTIAZEM T |
| 2271656 | TEVA-DILTIAZEM HCL ER |
| 2370492 | TEVA-DILTIAZEM T |
| 2256770 | TIAZAC XC |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). The target disease term is obsolete, so the prediction may point to a deprecated concept. Mechanism and safety data are also missing.

**To proceed, the following is needed:**
- Re-map the obsolete disease term to a current stroke or cerebrovascular disease term and re-evaluate
- Obtain diltiazem's approved indications and mechanism of action (e.g., from DrugBank)
- Obtain Health Canada package insert warnings and contraindications for safety screening
- Search for clinical trials and literature on diltiazem in ischemic stroke or cerebrovascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

