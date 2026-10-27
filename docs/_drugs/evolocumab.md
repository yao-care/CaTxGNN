---
layout: default
title: Evolocumab
parent: Model Prediction Only (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Evolocumab: predicted new indication Symptomatic form of hemophilia in female carriers (evidence level L5). Approved use: Homozygous familial hypercholesterolemia"
monitor_inn: "Evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity", "hemorrhagic disease of newborn", "ichthyosis, X-linked, without steroid sulfatase deficiency", "inherited thrombophilia", "disorder of other vitamins and cofactors metabolism and transport"]
---

# Evolocumab
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

## Evolocumab: From Homozygous Familial Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers
{: .text-alpha }

## One-Sentence Summary

Evolocumab is a PCSK9-inhibiting antibody originally used to lower cholesterol in homozygous familial hypercholesterolemia and related dyslipidemia.
The TxGNN model predicts it may be effective for **symptomatic form of hemophilia in female carriers**,
but **no clinical trials and no publications** currently support this direction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous familial hypercholesterolemia; syndromic dyslipidemia (the Canadian licence text is not available) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, evolocumab is a monoclonal antibody that targets PCSK9. By blocking PCSK9, it increases the availability of LDL receptors and lowers LDL cholesterol. Its efficacy in hypercholesterolemia is established.

The predicted new indication does not fit this mechanism. Hemophilia carrier symptoms arise from reduced factor VIII or IX activity caused by X-linked variants. This pathway is unrelated to PCSK9 or LDL metabolism. The high score (0.998) reflects a knowledge-graph prediction only and should not be read as biological or clinical support.

Other top-ranked predictions show the same pattern. They are mostly coagulation or haematological disorders, or broad ontology categories, with no plausible link to PCSK9 inhibition. The one exception is familial apolipoprotein C-II deficiency (rank 2, score 99.50%). It involves lipid metabolism, but evolocumab mainly lowers LDL-C and has only modest triglyceride effects, so it is unlikely to correct the core defect. No trials or literature support it either.

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
| 02446057 | REPATHA | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list one pharmacology entry. It is the drug's own target, PCSK9 (gene PCSK9), the protein that evolocumab (also known as AMG-145 or Repatha) binds. It is not a conventional drug-drug interaction, and no interaction severity level was provided.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There is no clinical trial or publication evidence (L5), and the mechanism of PCSK9 inhibition has no plausible connection to hemophilia carrier symptoms. Health Canada safety label information is also missing.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking PCSK9 inhibition to clotting factor VIII or IX function
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, and the approved indication text for DIN 02446057
- Consideration of a more biologically plausible candidate from the list, such as familial apolipoprotein C-II deficiency, supported by literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

