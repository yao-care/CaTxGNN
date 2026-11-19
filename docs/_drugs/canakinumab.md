---
layout: default
title: Canakinumab
parent: Model Prediction Only (L5)
nav_order: 150
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Canakinumab: predicted new indication Hepatic infarction (evidence level L5). Approved use: Gout, cryopyrin-associated periodic syndrome…"
monitor_inn: "Canakinumab"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
---

# Canakinumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Canakinumab: From Gout and Periodic Fever Syndromes to Hepatic Infarction
{: .text-alpha }

## One-Sentence Summary

Canakinumab is an interleukin-1β (IL-1β) antibody, originally used for autoinflammatory conditions such as cryopyrin-associated periodic syndrome (CAPS), familial Mediterranean fever and juvenile arthritis.
The TxGNN model predicts it may be effective for **hepatic infarction**.
**No clinical trials and no publications** currently support this specific prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout, cryopyrin-associated periodic syndrome, systemic-onset juvenile idiopathic arthritis, juvenile idiopathic arthritis, mevalonate kinase deficiency, familial Mediterranean fever (the Canadian licence text is not available, so these come from the model's knowledge base) |
| Predicted New Indication | Hepatic infarction |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for canakinumab: "Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)." ([DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e), label version 2026-06-08; accessed 2026-11-19.) Based on known information, canakinumab is a monoclonal antibody directed at the IL-1β pathway. Its efficacy in autoinflammatory diseases is established, and mechanistically it may be applicable to inflammation-driven conditions.

The only link to hepatic infarction is speculative. IL-1β-driven inflammation may contribute to ischemic tissue injury, and blocking it could dampen that injury. Nothing in the data compiled for this report tests this idea. The high score is a model output, not evidence of benefit.

The original indications are immune-mediated inflammatory diseases. Hepatic infarction is a vascular and ischemic liver injury. The similarity between the two is not yet established.

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
| 02460351 | ILARIS |

The licence is valid and single-ingredient. Dosage form and approved indication text are not available in the compiled data.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded, and the main ones are listed below.
  - **Moderate**:
    - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone.
    - Anticoagulants: warfarin, apixaban, rivaroxaban, dicoumarol.
    - Statin: simvastatin.
    - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, tositumomab, iobenguane (I-131).
  - **Minor**: zinc salts (acetate, gluconate, sulfate).

Warning and contraindication data from the product label are not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials, no publications and only a speculative mechanism. This is the lowest evidence level (L5), so it cannot support a repurposing decision now.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic case for IL-1β involvement in hepatic ischemic injury
- Preclinical or case-level evidence of canakinumab effect in hepatic infarction
- Package insert warnings and contraindications from Health Canada, for safety screening
- A review of the other predictions, since several have more support. For example, the autosomal dominant familial Mediterranean fever prediction (rank 6) has three completed Phase 3 trials and several systematic reviews. However, it overlaps with an already listed indication and is therefore largely confirmatory.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

