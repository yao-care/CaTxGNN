---
layout: default
title: Triethylenetetramine
parent: Model Prediction Only (L5)
nav_order: 944
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Triethylenetetramine: predicted new indication Thyroid gland undifferentiated (anaplastic) carcinoma (evidence level L5). Approved use: Wilson disease"
---

# Triethylenetetramine
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

# Triethylenetetramine: From Renal Cell Carcinoma and Wilson Disease to Anaplastic Thyroid Carcinoma

## One-Sentence Summary

Triethylenetetramine (trientine) is a copper chelator, listed for Wilson disease, iron metabolism disorders and several renal cell carcinoma subtypes in the knowledge graph used for this report.
The TxGNN model predicts it may be effective for **thyroid gland undifferentiated (anaplastic) carcinoma**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wilson disease (the Canadian licence records contain no approved indication text; the indications listed come from the knowledge graph) |
| Predicted New Indication | Thyroid gland undifferentiated (anaplastic) carcinoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trientine is a copper chelator. Its efficacy in Wilson disease, a disorder of copper accumulation, is established, and mechanistically it may be applicable to other conditions in which copper plays a role.

Copper is a cofactor in angiogenic and signalling pathways, such as VEGF and MEK1/2-BRAF signalling (sometimes called "cuproplasia"). Depleting copper is therefore a plausible antitumour concept. The knowledge graph also lists several renal cell carcinoma indications for this drug, which may partly explain why the model connects it to other tumours.

This reasoning is hypothetical. No trials or literature were found for anaplastic thyroid carcinoma, and the high TxGNN score is a computational prediction, not clinical evidence.

**Other predicted indications (all prediction only, no trials or literature):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hepatopulmonary syndrome | 99.77% | L5 | No direct mechanistic link; speculative connection through chronic liver disease |
| 3 | Early-onset familial noncirrhotic portal hypertension | 99.77% | L5 | Linked to the hepatic vascular network shared with Wilson disease |
| 4 | Hepatoportal sclerosis | 99.77% | L5 | Indirect link to copper chelation |
| 5 | Primitive portal vein thrombosis | 99.77% | L5 | No clear rationale; likely graph proximity |
| 6 | Idiopathic copper-associated cirrhosis | 99.77% | L4 | Most biologically plausible; shares hepatic copper accumulation with Wilson disease; a candidate for focused literature review |
| 7 | Hepatic porphyria | 99.71% | L5 | Heme synthesis is metal-dependent; no direct rationale |
| 8 | Disorder of tyrosine metabolism | 98.78% | L5 | Weak link through copper-dependent tyrosinase |
| 9 | Renal cell carcinoma associated with neuroblastoma | 98.78% | L5 | Likely driven by existing renal cell carcinoma indications |
| 10 | Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 98.78% | L5 | Likely driven by existing renal cell carcinoma indications |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02515067 | WAYMADE-TRIENTINE | Not specified | Not specified |
| 02504855 | MAR-TRIENTINE | Not specified | Not specified |

Both products are valid single-ingredient licences.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** The knowledge graph links the drug to a broad set of conditions, including:
- Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary thrombosis, peripheral vascular disease, intermittent claudication
- Liver and bilirubin: liver failure, drug-induced liver injury, hyperbilirubinaemia (including Gilbert syndrome)
- Endocrine and metabolic: adrenocortical insufficiency, Addison disease, hypothyroidism (including myxedema and congenital hypothyroidism), potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders
- Other: hemoglobinopathy, diarrhoeal disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia

These are database associations and should be verified against the official product monograph.

**Drug Interactions:** 27 interactions were identified in total. The 20 detailed records are all rated Moderate and involve mineral and trace-element products, which is consistent with chelation. They include:
- Calcium salts (phosphate, acetate, carbonate, citrate, glubionate, gluconate, lactate)
- Magnesium salts (oxide, carbonate, chloride, citrate)
- Iron preparations (iron, ferrous fumarate, ferrous gluconate, ferrous sulfate, iron protein succinylate, tetraferric tricitrate)
- Copper gluconate, selenium and manganese sulfate

Please refer to the package insert for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The anaplastic thyroid carcinoma prediction has a very high model score but no clinical trials or literature, so it remains at evidence level L5. The mechanistic argument (copper depletion) is plausible but untested for this indication. Official safety information has not been obtained.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A systematic literature and trial search on copper chelation in anaplastic thyroid carcinoma
- A focused review of idiopathic copper-associated cirrhosis, the most biologically plausible alternative (L4)
- Preclinical or early-phase data showing antitumour activity of trientine in the predicted indication
- A dosage form and indication review for the two Canadian products, whose records are incomplete
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

