---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 2
---

# Brompheniramine
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

# Brompheniramine: From an Unrecorded Original Indication to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation antihistamine marketed in Canada in a cough and cold product. The Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the one Canadian licence has no indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. The reasoning below comes from general pharmacology, not from the supplied data. Brompheniramine belongs to the first-generation H1-receptor antagonist class. In allergic urticaria, histamine released from mast cells drives wheals and itching, so blocking the H1 receptor is biologically plausible.

The original indication is not recorded. The only Canadian product is named "Robitussin Children's Cough & Cold Bedtime", which suggests a symptomatic cough and cold combination. This is an inference from the product name, not from indication text. Allergic symptoms such as itching and histamine-mediated reactions are a plausible bridge between that use and urticaria.

A second prediction, **cold urticaria** (score 99.55%), rests on the same class-level reasoning. Cold exposure triggers mast-cell degranulation and histamine release, and H1 blockade could plausibly help. For both conditions, there are no drug-specific trials or literature in the record. Any class-effect evidence would need to be retrieved separately.

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
| 2394707 | ROBITUSSIN CHILDREN'S COUGH & COLD BEDTIME | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records for this drug. This does not confirm the absence of interactions.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.87%), but the evidence level is L5, with no clinical trials or literature. The original indication, the mechanism data, and the warnings and contraindications are also missing, so the candidate cannot advance to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication), needed for safety screening
- Mechanism of action data from DrugBank
- A search for clinical trials and literature on brompheniramine or H1-antihistamine class effects in allergic urticaria and cold urticaria
- Dosage form and route information to check route compatibility with the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

