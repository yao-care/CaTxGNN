---
layout: default
title: Clobetasone
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Clobetasone
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

# Clobetasone: From Topical Corticosteroid Use (Inflammatory Skin Conditions) to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Clobetasone is a low-to-moderate potency topical corticosteroid. The Canadian product on record is an eczema-care medicated cream, but no approved indication text is available.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**.
Currently **0 clinical trials** and **0 publications** support this prediction, so it is a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the regulatory record (the product name suggests eczema) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for clobetasone is not currently available. As a topical corticosteroid, it is expected to act through the glucocorticoid receptor, producing anti-inflammatory and anti-lymphocytic effects. Topical corticosteroids as a class are used as skin-directed therapy in early-stage cutaneous T-cell lymphoma (CTCL). This is class-level plausibility only and is not evidence for clobetasone itself.

The main reservation is potency. Clobetasone is low-to-moderate potency, whereas skin-directed CTCL therapy typically relies on stronger agents. Any follow-up would need a targeted literature search on this point.

The other top-ranked predictions are weaker:
- **Related lymphomas:**
  - Primary cutaneous T-cell non-Hodgkin lymphoma largely overlaps with the lead prediction, so it is not an independent signal.
  - Sezary syndrome, primary cutaneous B-cell lymphoma and granulomatous slack skin disease are extensions of the same idea with no supplied evidence.
- **Systemic conditions:** Crohn's colitis, adrenocortical insufficiency and nephrotic syndrome reflect the systemic corticosteroid class. There is no evidence that a topical product achieves relevant exposure.
- **Likely graph artifacts:** Cystic teratoma and spinal cord dermoid cyst have no plausible mechanistic link.

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
| 2214415 | SPECTRO ECZEMACARE MEDICATED CREAM | Cream (per product name) | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there is no supporting trial or literature evidence (L5, model prediction only). Clobetasone's low-to-moderate potency also makes disease-modifying activity in lymphoma doubtful.

**To proceed, the following is needed:**
- A targeted literature search on clobetasone or comparable-potency topical corticosteroids in early-stage CTCL
- Mechanism of action data (for example from DrugBank)
- The Health Canada package insert, for warnings, contraindications and the approved indication
- Route and formulation compatibility assessment for skin-directed use in CTCL
- A safety review of long-term or extensive topical use, including HPA-axis suppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

