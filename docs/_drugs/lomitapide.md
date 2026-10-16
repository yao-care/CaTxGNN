---
layout: default
title: Lomitapide
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lomitapide: predicted new indication Macrothrombocytopenia with mitral valve insufficiency (evidence level L5). Approved use: Homozygous familial hypercholesterolemia"
---

# Lomitapide
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

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Lomitapide is an oral drug approved for homozygous familial hypercholesterolemia (HoFH), a severe inherited form of high LDL cholesterol.
The TxGNN model predicts it may be effective for **macrothrombocytopenia with mitral valve insufficiency**, with a very high score (99.92%).
However, there are **0 clinical trials** and **0 publications** for this prediction, and no plausible mechanistic link, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous familial hypercholesterolemia |
| Predicted New Indication | Macrothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in the compiled data. From known pharmacology, lomitapide inhibits microsomal triglyceride transfer protein (MTP). MTP is needed in liver and intestinal cells to assemble ApoB-containing lipoproteins (VLDL and chylomicrons). Blocking it lowers LDL cholesterol, which is why the drug works in HoFH.

This mechanism has **no known relationship** to macrothrombocytopenia (a platelet-count and platelet-size disorder) or to mitral valve pathology. Nothing in the data suggests lomitapide acts on platelet production or valve disease. The high score most likely reflects closeness among platelet-related disorders in the knowledge graph rather than a drug-specific signal.

This is not an isolated result. The other top-ranked predictions are mostly platelet or bleeding disorders, including hereditary thrombocytopenia, dense granule disease, Glanzmann thrombasthenia and pseudo-von Willebrand disease. They share the same weakness: no trials, no literature and no mechanistic rationale. This pattern points to a common artifact in the graph neighborhood rather than independent signals.

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

All three licenses are active, with none cancelled. Approved indication text and dosage form details were not available in the compiled data.

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
The prediction rests only on a knowledge-graph score. There are no trials, no publications and no plausible mechanism linking MTP inhibition to platelet or valve disease. Lomitapide's liver toxicity and interaction burden make it hard to justify exposing patients without supporting evidence.

**Other predictions:** The only prediction with real evidence is **hyperlipoproteinemia** (rank 9, L1, Proceed with Guardrails). It is supported by completed Phase 3 single-arm studies in HoFH, including a pediatric study, and the published pediatric HoFH results. However, it largely overlaps the already approved indication, so it is not a true repurposing finding. Any extension should stay within that evidence base.

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

