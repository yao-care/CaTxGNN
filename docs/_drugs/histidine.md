---
layout: default
title: Histidine
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Histidine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the licence data (the products are amino acid solutions…"
monitor_inn: "HISTIDINE"
predicted_indications: ["gastroparesis (disease)", "sclerosing cholangitis"]
---

# Histidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Histidine: From Parenteral Nutrition Component to Gastroparesis

## One-Sentence Summary

Histidine is an essential amino acid used as a component of parenteral nutrition (amino acid infusion) products in Canada. The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 publication**, which does not test histidine as a treatment. This prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (the products are amino acid solutions for parenteral nutrition) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, histidine is an essential amino acid supplied in amino acid and parenteral nutrition products. Its nutritional role is established, but no data compiled for this report links it to gastroparesis.

The only publication retrieved (PMID 42668409) describes gastric amyloid pathology and mucosal denervation in hereditary ATTR amyloidosis. It does not evaluate histidine or any histidine-related pathway as a treatment. One could speculate that histamine made from histidine influences gastric motility or secretion, but this has not been tested in the supplied data. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Cohort/preclinical | Amyloid | Gastric amyloid pathology and mucosal denervation in ATTRv amyloidosis, studied in patients and mice. Histidine was not evaluated. |

---

## Canada Market Information

All 20 licences are valid single-ingredient products. Dosage form and approved indication text are not available in the data compiled for this report. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not available | Not available |
| 02013932 | CLINIMIX | Not available | Not available |
| 02013940 | CLINIMIX | Not available | Not available |
| 00872296 | TRAVASOL | Not available | Not available |
| 02013886 | CLINIMIX | Not available | Not available |

---

## Safety Considerations

No package insert warnings, contraindications or drug interaction records were found in the data compiled for this report. Please refer to the package insert for safety information.

The TxGNN knowledge graph, which is not label text, links histidine to contraindication edges with several conditions. These are signals only and need verification against the labelling:
- **Kidney disease:** chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Calcium and phosphorus disorders:** hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
- **Cardiac conditions:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
- **Phenylalanine metabolism disorders:** phenylketonuria

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.55%), but there are no clinical trials, and the only publication does not study histidine. No mechanistic link to gastroparesis is supported by the data, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for histidine
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Preclinical or clinical evidence that histidine or its metabolites affect gastric motility
- Route and formulation compatibility assessment, since the current products are parenteral nutrition solutions

---

## Additional Note: Second Predicted Indication (Sclerosing Cholangitis)

The model's second prediction is **sclerosing cholangitis** (score 99.27%, evidence level L4, recommendation: Research Question). It has no clinical trials and 8 publications, none of which tests histidine as a treatment.

- **Histamine pathway:** Histidine is the precursor of histamine, made by L-histidine decarboxylase. Mouse studies (PMIDs 27351144, 35799467, 32054995, 29601088) show that mast cell-derived histamine promotes biliary proliferation and fibrosis in primary sclerosing cholangitis. Blocking histamine signalling or removing the enzyme reduced damage.
- **Direction of effect:** These findings suggest that supplying more histidine could worsen the disease rather than improve it, which is the opposite of a therapeutic benefit.
- **Other papers:** The remaining papers cover diagnostic biomarkers, genetics and post-transplant biliary lesions.

This prediction is not recommended for progression without evidence that the direction of effect is favourable.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

