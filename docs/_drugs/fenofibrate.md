---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridaemia and hyperlipidaemia"
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fenofibrate: From Hyperlipidaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug whose relations recorded in the knowledge graph centre on hypertriglyceridaemia and hyperlipidaemia.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, but **no clinical trials** and only **3 preclinical or mechanistic publications** support this direction, and none studies the disease itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia and hyperlipidaemia (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Number of approvals | 10 licences (all single-ingredient products) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge and the submitted literature, fenofibrate is a PPARα agonist that lowers triglycerides and raises HDL cholesterol. The papers provided suggest PPARα agonism upregulates the phospholipid transfer protein (PLTP) gene, which contributes to HDL enlargement in mice.

The link to CETP deficiency is weak. CETP deficiency is a condition in which HDL cholesterol is already markedly elevated and HDL remodelling is impaired. Raising HDL further offers no clear therapeutic rationale and could even be undesirable. The very high TxGNN score most likely reflects network proximity within lipid-metabolism pathways rather than a validated treatment benefit. No fenofibrate-specific clinical evidence in CETP-deficient patients was identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical (mouse) | Journal of Cardiovascular Pharmacology and Therapeutics | In human ApoB100/CETP transgenic mice, CETP inhibition (torcetrapib) combined with PPARα agonism (fenofibrate) changed HDL and LDL cholesterol. This is not a CETP-deficiency model. |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclinical (mouse) | Journal of Biological Chemistry | Fenofibrate induced the PLTP gene, which accounts for HDL enlargement in treated mice. |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mechanistic/translational | Frontiers in Physiology | Plasma HDL did not correlate with faecal cholesterol or cholesterol efflux capacity, suggesting HDL function matters more than HDL level. |

None of these studies directly examines CETP deficiency as a disease in patients treated with fenofibrate.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02269082 | LIPIDIL EZ | Not listed | Not listed |
| 02390701 | SANDOZ FENOFIBRATE E | Not listed | Not listed |
| 02246859 | AA-FENO-SUPER | Not listed | Not listed |
| 02246860 | AA-FENO-SUPER | Not listed | Not listed |
| 02390698 | SANDOZ FENOFIBRATE E | Not listed | Not listed |

These are 5 of the 10 valid single-ingredient licences; the remainder include AA-FENO-MICRO (2), SPC-FENOFIBRATE E, LIPIDIL SUPRA and a second LIPIDIL EZ.

## Safety Considerations

**Contraindication-type relations recorded in the knowledge graph** (not label text): liver failure and liver disease, pancreatitis, gallbladder disease (including cholelithiasis), muscle disorders (myopathy, rhabdomyolysis), thrombocytopenia, anaemia, impaired renal function, and leukopenia/neutropenia-related conditions.

**Drug Interactions**: 100 interactions were found. The ones listed are all rated Moderate, and include:
- Sulfonylureas: acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide
- Many insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro and others)
- Chenodeoxycholic acid
- Esomeprazole

Please refer to the package insert for authoritative warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No clinical trials exist, and no cited study addresses CETP deficiency directly. In addition, CETP deficiency already involves high HDL-C, so the expected pharmacological effect is not clearly beneficial.

**To proceed, the following is needed:**
- Evidence that studies fenofibrate in CETP-deficient patients or a validated disease model
- A clear clinical rationale for any benefit when HDL-C is already elevated
- Detailed mechanism of action data
- Health Canada product monograph warnings, contraindications and indication text, which are missing from the compiled data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

