---
layout: default
title: Tralokinumab
parent: Model Prediction Only (L5)
nav_order: 919
evidence_level: L5
indication_count: 10
---

# Tralokinumab
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

# Tralokinumab: From Anti-IL-13 Antibody Therapy to Diabetic Cataract

## One-Sentence Summary

Tralokinumab is an anti-IL-13 monoclonal antibody marketed in Canada as ADTRALZA.
The TxGNN model predicts it may be effective for **diabetic cataract**, but **no clinical trials and no publications** currently support this prediction.
The prediction rests on the model score alone, and the supplied data give no mechanistic support for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.69% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tralokinumab is an antibody that blocks IL-13, a cytokine of type 2 inflammation. The record lists no original indication text, so the link between its approved use and the predicted indication cannot be assessed.

The data do not support a direct connection between IL-13 and diabetic cataract. Diabetic cataract is mainly driven by the polyol pathway and oxidative stress in the lens. Tralokinumab is also a large antibody with limited ocular penetration, so an effect on the lens is not plausible without further evidence. The high score (98.69%) most likely reflects closeness between cataract and diabetes nodes in the knowledge graph, not a validated mechanism.

The other nine top predictions fall into two groups, all at evidence level L5 with a Hold recommendation:
- **Cataract subtypes (eight):** immature, type 2 diabetes-associated, tetanic, mature, craniostenosis, cortical, nuclear senile and senile cataract. Scores are 98.5–98.6%.
- **Diabetic retinopathy (one):** score 98.4%. This is the most biologically plausible of the ten, because retinal inflammation and cytokine signalling are involved in the disease. It is still a hypothesis, with no supporting evidence and an unresolved question of intravitreal versus systemic delivery.

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
| 2540193 | ADTRALZA |
| 2521288 | ADTRALZA |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no trials, no literature and no plausible mechanistic link to the lens. Of the ten predictions reviewed, diabetic retinopathy is the only one worth a closer look.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. These are currently missing and block safety screening.
- Mechanism of action data from DrugBank, to test any IL-13 link to lens or retinal disease.
- Original (approved) indication text for both DINs.
- A literature and trial search for IL-13 or type 2 inflammation in cataract and diabetic eye disease.
- An assessment of ocular delivery routes (route compatibility is pending).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

