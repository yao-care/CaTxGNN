---
layout: default
title: Osilodrostat
parent: Model Prediction Only (L5)
nav_order: 689
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Osilodrostat: predicted new indication Familial generalized lentiginosis (evidence level L5). Approved use: Cushing disease due to pituitary adenoma"
monitor_inn: "Osilodrostat"
predicted_indications: ["familial generalized lentiginosis", "acromelanosis", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "gastrocutaneous syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "Moynahan syndrome", "rhabdoid tumor", "X-linked lymphoproliferative disease due to SH2D1A deficiency", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "peripheral nerve schwannoma"]
---

# Osilodrostat
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

## Osilodrostat: From Cushing Disease to Familial Generalized Lentiginosis
{: .text-alpha }

## One-Sentence Summary

Osilodrostat was originally developed to treat Cushing disease and other forms of Cushing syndrome (cortisol excess).
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cushing disease due to pituitary adenoma; ACTH-dependent Cushing syndrome; Cushing syndrome |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 98.19% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, osilodrostat inhibits 11-beta-hydroxylase (CYP11B1), the enzyme that performs the final step of cortisol synthesis. This lowers cortisol, which is why it is used in Cushing syndrome.

A link between this mechanism and familial generalized lentiginosis (a pigmentation disorder) is doubtful. Blocking cortisol production removes the negative feedback on the pituitary, so ACTH rises. ACTH acts on the melanocortin-1 receptor (MC1R) pathway, which drives skin pigmentation. That would tend to worsen pigmentation rather than improve it.

The high TxGNN score most likely reflects proximity in the knowledge graph rather than a pharmacological rationale. The other top-ranked predictions (acromelanosis, café-au-lait syndrome, Moynahan syndrome, rhabdoid tumor, peripheral nerve schwannoma and others) also have no supporting evidence and no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02558920 | ISTURISA | Not specified | Not specified |
| 02558912 | ISTURISA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interacting drugs. Examples from the 20 shown:
  - **Major**: Clarithromycin, Dolasetron
  - **Moderate**: Famotidine, Alosetron, Loperamide, Aprepitant, Omeprazole, Dexamethasone, Budesonide, Cimetidine, Levofloxacin, Palonosetron, Metreleptin, and others
  - **Minor**: Naloxegol

Package insert warnings and contraindications were not available. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature. The known mechanism (cortisol lowering with a compensatory ACTH rise) runs counter to a benefit in pigmentation disorders. The remaining top-ranked predictions are similarly unsupported.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank to allow a proper mechanistic analysis
- Health Canada package insert warnings and contraindications for safety screening
- Preclinical or mechanistic evidence that cortisol synthesis inhibition affects melanocyte biology in this condition
- Approved indication text and dosage forms for the two DINs
- A review of whether the ACTH rise could aggravate pigmentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

