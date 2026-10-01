---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 909
evidence_level: L5
indication_count: 10
---

# Tipiracil
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

# Tipiracil: From Metastatic Colorectal Cancer (Trifluridine/Tipiracil Combination) to Cecum Villous Adenoma

## One-Sentence Summary

Tipiracil is a component of the trifluridine/tipiracil combination (LONSURF), approved for refractory metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but **0 clinical trials** and **0 publications** support this specific prediction.
This is a model-only (L5) signal, and the high score most likely reflects knowledge-graph proximity to colorectal terms rather than real therapeutic potential.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Refractory metastatic colorectal cancer (as the trifluridine/tipiracil combination; license indication text not provided) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tipiracil is known to be a thymidine phosphorylase inhibitor. It has no cytotoxic activity on its own. Its role in the approved combination is to raise exposure to trifluridine, the cytotoxic partner.

Cecum villous adenoma is a benign, premalignant lesion, and a cytotoxic combination is not a recognised treatment for it. Such lesions are normally managed by endoscopic or surgical removal. The model's score most likely reflects the closeness of "cecum" and "adenoma" to colorectal cancer terms in the knowledge graph, not a genuine mechanistic link. We therefore consider the prediction weak and do not recommend treating it as a repurposing lead.

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
| 2472104 | LONSURF |
| 2472112 | LONSURF |

Dosage form and approved indication text were not provided for these licenses.

---

## Cytotoxicity

Tipiracil itself is not cytotoxic. This section applies because it is used only in combination with the cytotoxic agent trifluridine, for colorectal cancer.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Combination product with a conventional cytotoxic partner (trifluridine, a nucleoside antimetabolite); tipiracil acts as an enzyme inhibitor |
| Myelosuppression Risk | Leukopenia and neutropenia are reported for the combination (PMID 30677817) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential at minimum; please refer to the package insert for full monitoring requirements |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

Adverse effects reported for the combination in the literature include leukopenia, neutropenia, fatigue, diarrhoea and vomiting. A case of leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura has also been described. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or publications for cecum villous adenoma, and the lesion is benign and not a plausible target for a cytotoxic combination. Several other top-ranked predictions are also benign colonic lesions with no mechanistic rationale. "Rectosigmoid junction neoplasm" largely restates the existing colorectal cancer indication, and "cecal disease" is supported only by case reports of the approved use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence specific to adenoma or premalignant colorectal lesions
- Approved indication text and dosage form for the two LONSURF licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

