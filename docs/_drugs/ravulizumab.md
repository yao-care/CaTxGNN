---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ravulizumab: predicted new indication Autosomal recessive severe congenital neutropenia due to G6PC3 defici… (evidence level L5). Approved use: Paroxysmal nocturnal hemoglobinuria"
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
---

# Ravulizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ravulizumab: From Paroxysmal Nocturnal Hemoglobinuria to Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency
{: .text-alpha }

## One-Sentence Summary

Ravulizumab is a long-acting complement C5 inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria (PNH).
The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on a graph-based model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria (from the TxGNN knowledge graph; no approved indication text is available from Health Canada) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ravulizumab is a long-acting inhibitor of complement component C5. It blocks terminal complement activation, and its efficacy in PNH, a complement-mediated hemolytic disease, is established.

G6PC3 deficiency is a metabolic and neutrophil-function disorder with no established complement-driven pathology. The link to PNH is therefore weak. The prediction is a graph-based association only, with no supporting mechanistic or clinical data. In this case, the high score should be read as a model signal, not as biological evidence.

The other top-ranked predictions show the same pattern. They are mostly congenital neutropenias and platelet or bleeding disorders (cyclic hematopoiesis, severe congenital neutropenia, CXCR2 deficiency, pseudo-von Willebrand disease and others). Each has an evidence level of L5 and a recommendation of Hold. Primary hyperoxaluria has only a speculative secondary link through complement involvement in oxalate crystal-induced renal inflammation, and no clinical evidence supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02533456 | ULTOMIRIS | Not specified | Not specified |
| 02533448 | ULTOMIRIS | Not specified | Not specified |

Both authorizations are valid single-ingredient products.

## Safety Considerations

- **Contraindications (knowledge graph)**: The knowledge graph lists meningococcal infection as a contraindicated condition. This comes from graph edges, not from package insert text.
- **Drug Interactions**: Four minor interactions were identified, all with human immunoglobulin G products (intravenous, subcutaneous, intramuscular, and combined intravenous/subcutaneous).
- **Infection risk**: Complement C5 blockade increases susceptibility to meningococcal and other encapsulated bacterial infections. This is a particular concern in neutropenic patients, who are already at high infection risk.

Package insert warnings and contraindications were not available for this report. Please refer to the Health Canada package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link between C5 inhibition and G6PC3-related neutropenia. Complement blockade could also add infection risk in an already vulnerable population. Evidence is at level L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanistic evidence that complement activation contributes to G6PC3 deficiency pathology
- Mechanism of action data for ravulizumab (DrugBank)
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form details for the two DINs
- Preclinical or clinical data in neutropenia models, plus a risk assessment for meningococcal infection and other infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

