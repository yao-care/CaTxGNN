---
layout: default
title: Fluorescein
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein: From Ophthalmic Diagnostic Dye to Prinzmetal Angina

## One-Sentence Summary

Fluorescein is a fluorescent dye used in ophthalmology for angiography and corneal staining. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Fluorescein is a diagnostic dye. It is used to visualise blood vessels in the eye and to reveal damage on the corneal surface. It is not known to act on the smooth muscle of blood vessels.

Prinzmetal angina is caused by spasm of the coronary arteries. No pharmacological link has been identified between fluorescein and vasospasm modulation, and no experimental or clinical data connect the two. The very high TxGNN score is most likely an artefact of the knowledge graph rather than a real therapeutic signal.

Other predictions for this drug show a similar pattern. Trials and papers retrieved for rheumatoid arthritis, hyperthyroidism, hemoglobinopathy, thrombophilia and beta-thalassemia mostly involve eye conditions, where fluorescein is used as a staining or imaging tool. None of them tests fluorescein as a treatment.

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
| 505005 | FLUORESCITE |
| 2160773 | DIOFLUOR STRIPS |
| 2148390 | MINIMS FLUORESCEIN SODIUM |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic rationale, no trials and no literature (L5). Fluorescein has no known vasospasm-modulating activity, and the high score is likely a knowledge-graph artefact.

**To proceed, the following is needed:**
- Independent preclinical or mechanistic evidence that fluorescein affects coronary vasospasm
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism of action data from DrugBank
- Confirmation of the approved indications and dosage forms for the three Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

