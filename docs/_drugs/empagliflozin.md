---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 324
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

*Note: the supplied Canadian licence records list no approved indication text. The original indication above reflects the drug's general use as an SGLT2 inhibitor and is not taken from the Evidence Pack.*

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor marketed in Canada as JARDIANCE and, in combination, as SYNJARDY.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

Two other predictions have equally thin support:
- Focal stiff limb syndrome: 99.06%, L5, Hold
- Opsismodysplasia: 99.03%, L5, Hold

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Empagliflozin is an SGLT2 inhibitor that acts on renal glucose reabsorption. Its efficacy is established in its original metabolic indication, but nothing in the supplied data ties SGLT2 inhibition to the biology of stiff person syndrome.

Classic stiff person syndrome is an autoimmune disorder of GABAergic and glutamic acid decarboxylase (GAD65) neurotransmission. The only plausible link is indirect: the disease is often comorbid with autoimmune diabetes. That is a comorbidity association, not a therapeutic rationale. The high score should be read as a model signal that has not been corroborated.

The related predictions are no stronger:
- **Focal stiff limb syndrome** is a localized variant of the same disease spectrum. Its score is identical (0.9906), which suggests both predictions come from the same graph neighbourhood rather than from independent signals.
- **Opsismodysplasia** is a rare skeletal dysplasia, typically linked to INPPL1 (SHIP2) variants affecting PI3K/insulin-related signaling. No evidence connects SGLT2 inhibition to this pathway or to skeletal development. It is a paediatric genetic disease, and the safety of SGLT2 inhibitors in children adds further concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2443945 | JARDIANCE |
| 2443937 | JARDIANCE |
| 2456591 | SYNJARDY |
| 2456575 | SYNJARDY |
| 2456605 | SYNJARDY |

Eight DINs are registered in total, and the five main authorizations are shown above. Dosage form and approved indication text are not included in the supplied records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to an SGLT2 inhibitor. The identical scores for the two stiff-person-spectrum predictions suggest correlated rather than independent signals.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (for example, from the DrugBank API) to test whether any biological link exists to GAD65/GABAergic pathways or INPPL1/PI3K signaling
- Independent preclinical or clinical evidence for the predicted indication
- For opsismodysplasia, a paediatric safety assessment before any further consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

