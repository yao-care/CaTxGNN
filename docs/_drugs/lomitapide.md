---
layout: default
title: Lomitapide
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "LOMITAPIDE"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "platelet storage pool deficiency"]
description: "Lomitapide: predicted new indication Marcothrombocytopenia with mitral valve insufficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Lomitapide
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

## Lomitapide: Marcothrombocytopenia with mitral valve insufficiency
{: .text-alpha }

## One-Sentence Summary

Lomitapide is an oral drug approved for homozygous familial hypercholesterolemia (HoFH), a severe inherited form of high LDL cholesterol.
The TxGNN model predicts it may be effective for **macrothrombocytopenia with mitral valve insufficiency**, with a very high score (0.9992).
However, there are **0 clinical trials** and **0 publications** for this prediction, and no plausible mechanistic link, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Marcothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in the compiled data. From known pharmacology, lomitapide inhibits microsomal triglyceride transfer protein (MTP). MTP is needed in liver and intestinal cells to assemble ApoB-containing lipoproteins (VLDL and chylomicrons). Blocking it lowers LDL cholesterol, which is why the drug works in HoFH.

This mechanism has **no known relationship** to macrothrombocytopenia (a platelet-count and platelet-size disorder) or to mitral valve pathology. Nothing in the data suggests lomitapide acts on platelet production or valve disease. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related platelet disorders, not biological evidence.

This is not an isolated result. The other top-ranked predictions are mostly platelet or bleeding disorders, including hereditary thrombocytopenia with normal platelets, dense granule disease, Glanzmann thrombasthenia and pseudo-von Willebrand disease. They share the same weakness: no trials, no literature and no mechanistic rationale. This pattern suggests the TxGNN model (deep learning) is picking up similarities it learned between related diseases, not independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|------|
| 02420341 | JUXTAPID | Valid (single-ingredient) |
| 02420376 | JUXTAPID | Valid (single-ingredient) |
| 02420384 | JUXTAPID | Valid (single-ingredient) |

Approved indication text and dosage form details were not available in the compiled data.

---

## Safety Considerations

- **Drug Interactions**: The data lists 100 potential interactions. Examples flagged as **Major** include:
  - Acarbose
  - Pioglitazone
  - Doxycycline, minocycline and tetracycline
  - Clarithromycin
  - Aprepitant
  - Bupropion
  - Naltrexone
  - Chenodeoxycholic acid
  - Oxandrolone and oxymetholone

  Moderate interactions include ranitidine, cimetidine, loperamide, budesonide, saxagliptin, linagliptin and eliglustat.
- **Known class concerns** (from general pharmacology, not from the label data compiled here): liver fat accumulation and transaminase elevation, gastrointestinal side effects, CYP3A4-related interactions, and teratogenicity precautions.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no trials, no publications and no plausible mechanism linking MTP inhibition to platelet or valve disease. Lomitapide's liver toxicity and interaction burden make it hard to justify exposing patients without supporting evidence.


**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking MTP inhibition to platelet production or function
- Preclinical or in vitro data supporting such a link
- Retrieval of the Canadian package insert warnings and contraindications
- Formal mechanism of action data
- A risk-benefit assessment for any non-lipid population, given the hepatic and interaction risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

