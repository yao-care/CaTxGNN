---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 980
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "perinatal disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
description: "Vitamin A: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Vitamin A
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

## Vitamin A: Congenital prothrombin deficiency
{: .text-alpha }

## One-Sentence Summary

Vitamin A is an essential fat-soluble vitamin, originally used to treat vitamin deficiency disorders, including vitamin A deficiency.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.
Of the other predicted indications, "perinatal disease" has the most support: several Cochrane reviews on vitamin A in very low birth weight infants.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, vitamin A is a nutrient and the parent compound of the retinoids. Its efficacy in correcting vitamin A deficiency is well established, and it acts through retinoic acid receptor signalling.

For congenital prothrombin deficiency, a plausible mechanism is **not apparent**. This is a genetic coagulation factor disorder. Prothrombin synthesis depends on the vitamin K pathway, and vitamin A has no established role in it. The very high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of efficacy.


- **Perinatal disease (score 0.9963)**: vitamin A supports lung epithelial development, and deficiency in very low birth weight infants is linked to bronchopulmonary dysplasia risk. This is the best-supported direction, and it is consistent with vitamin A's existing nutritional role rather than a wholly new use.
- **Injury (score 0.9969)**: retinoids support epithelial regeneration and wound healing, but the trials are limited to extremely-low-birth-weight neonates.
- **Cell proliferation disorder** and **radiation or chemically induced disorder**: mechanistically plausible through retinoid receptor signalling and photoprotection, but the categories are too broad to test.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for congenital prothrombin deficiency.

For reference, the trials below were found for the lower-ranked predictions "injury" and "perinatal disease". They are not direct evidence for the top prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01203488](https://clinicaltrials.gov/study/NCT01203488) | Phase 1/2 | Completed | 807 | Randomized trial of higher-dose vitamin A in extremely-low-birth-weight infants, assessing survival without bronchopulmonary dysplasia and sepsis risk |
| [NCT02102711](https://clinicaltrials.gov/study/NCT02102711) | NA | Completed | 62 | Oral vitamin A in neonates under 1500 g to prevent bronchopulmonary dysplasia and retinopathy of prematurity |
| [NCT01115478](https://clinicaltrials.gov/study/NCT01115478) | NA | Completed | 2500 | Zinc and/or vitamin A supplementation to reduce placental malaria in pregnancy (only tangentially relevant) |
| [NCT04000789](https://clinicaltrials.gov/study/NCT04000789) | NA | Unknown | 96 | Vitamin A/E/sodium hyaluronate eye drops in diabetic retinopathy with dry eye (little direct relevance) |

---

## Literature Evidence

Currently no related literature is available for congenital prothrombin deficiency.

The strongest literature in the data compiled for this report concerns "perinatal disease":

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | Cochrane systematic review | Cochrane Database Syst Rev | Vitamin A supplementation to prevent mortality and morbidity in very low birth weight infants |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier version of the same review; low vitamin A status at birth is linked to chronic lung disease |
| [17943744](https://pubmed.ncbi.nlm.nih.gov/17943744/) | 2007 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier version of the same review |
| [22742601](https://pubmed.ncbi.nlm.nih.gov/22742601/) | 2012 | Systematic review and meta-analysis | Paediatr Perinat Epidemiol | Vitamin A and carotenoid supplementation in pregnancy and maternal, neonatal and infant outcomes |
| [34105132](https://pubmed.ncbi.nlm.nih.gov/34105132/) | 2021 | Meta-analysis | J Spec Oper Med | Association between high vitamin A intake and bone fracture risk (a safety signal) |
| [40901583](https://pubmed.ncbi.nlm.nih.gov/40901583/) | 2025 | Review | World J Hepatol | Vitamin A toxicity and liver damage at excessive intake (a safety signal) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00586315 | MULTI 1000 | Not specified | Not specified |
| 02100606 | MULTI 12 | Not specified | Not specified |
| 02242529 | MULTI-12/K1 PEDIATRIC | Not specified | Not specified |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: kidney disease, liver disease, gallbladder disease, peptic ulcer disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, hemolytic anemia, sickle cell anemia, hereditary hemochromatosis, Wilson disease, inflammatory bowel disease, ulcerative colitis, hypervitaminosis, and others.
- **Drug Interactions**: 68 interactions were recorded. The main **Major** ones are:
  - Other retinoids: isotretinoin, acitretin, tretinoin
  - Tetracycline-class antibiotics: doxycycline, tetracycline, minocycline, omadacycline, demeclocycline, eravacycline, oxytetracycline, sarecycline
- **Moderate** interactions include bexarotene, bile acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer and selpercatinib. Orlistat is **Minor**.
- **Literature safety signals**: high vitamin A intake is associated with bone fracture risk and liver toxicity.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, congenital prothrombin deficiency, has no trials or literature and no plausible mechanism (the pathway is vitamin K-dependent). The score is a model output only (evidence level L5). Among the lower-ranked predictions, the perinatal and very-low-birth-weight infant direction has the strongest evidence, in Cochrane reviews, but it largely reflects vitamin A's existing nutritional role.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text and dosage forms for the three Canadian licences (all currently blank)
- If pursuing this prediction, a mechanistic hypothesis linking vitamin A to prothrombin deficiency, which is currently lacking
- Consider re-prioritising toward the perinatal disease or neonatal lung injury direction, supported by a focused review of the Cochrane evidence and the safety risks (hepatic toxicity, bone effects, teratogenic retinoid interactions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

