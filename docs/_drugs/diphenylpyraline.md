---
layout: default
title: Diphenylpyraline
parent: Moderate Evidence (L3-L4)
nav_order: 290
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Diphenylpyraline: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis"
---

# Diphenylpyraline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Diphenylpyraline: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Diphenylpyraline is a first-generation antihistamine originally used for allergic and vasomotor rhinitis, the common cold, pharyngitis, allergic conjunctivitis, and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **no clinical trials and no publications** were found to support this prediction.
Allergic urticaria falls close to an existing indication (urticaria), so this is closer to an on-label use than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (the Canadian license records contain no indication text; the original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known drug class information, diphenylpyraline is a first-generation H1 antihistamine with anticholinergic activity. Blocking H1 receptors reduces the histamine-driven wheal and flare seen in urticaria, and the anticholinergic effect may reduce nasal secretions.

The knowledge graph already lists urticaria and angioedema among the drug's original indications. Allergic urticaria is therefore essentially a subtype of an existing indication. The high score (0.996) is consistent with this overlap, but it mostly reflects near-label use rather than a new therapeutic direction.

Two other predictions were also generated, both with model support only and no trials or literature:
- **Acute laryngopharyngitis** (score 99.23%): Related to the labeled pharyngitis and common cold indications. Most cases are infectious, so antihistamines would give symptom relief at best.
- **Nasal cavity disease** (score 99.15%): A broad category that overlaps with allergic and vasomotor rhinitis. It is too general to form a specific, testable hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00299561 | CREO-RECTAL ADULTES/ADULTS | Not specified | Not specified |
| 00299596 | CREO-RECTAL ENFANTS/CHILDREN | Not specified | Not specified |

Both products are valid single-ingredient licenses, and none are cancelled.

---

## Safety Considerations

**Contraindications from the knowledge graph** (derived from drug-disease relationships in the knowledge graph, not from package insert text):
- Hypertensive disorder / hypertension
- Peptic ulcer disease
- Benign prostatic hyperplasia
- Ocular hypertension, angle-closure glaucoma, closed-angle glaucoma
- Hyperthyroidism, Graves disease, thyrotoxicosis
- Bladder neck obstruction

No drug interaction records were found. Please refer to the package insert for warnings and other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials or publications for any of the three predicted indications. Allergic urticaria largely overlaps with an existing indication, so the prediction adds little new information. Safety screening cannot proceed because the Canadian package insert data are missing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications) for both DINs
- Mechanism of action data from DrugBank
- Dosage form and route information for the Canadian products, so route compatibility can be assessed (the products appear to be rectal formulations)
- A literature and trial search specific to diphenylpyraline in urticaria
- Review of the knowledge-graph contraindications against the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

