---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From an Unrecorded Original Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue that is marketed in Canada. The Evidence Pack does not record its original approved indications.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **0 clinical trials** and **0 publications** support this prediction, and the proposed mechanism is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Desmopressin is generally understood to release von Willebrand factor (VWF) and factor VIII from endothelial stores through V2 receptor signaling.

Congenital prothrombin deficiency is a lack of factor II. Desmopressin does not raise prothrombin, so there is no clear mechanistic route to benefit. The high TxGNN score most likely reflects the drug's proximity to other coagulation-related nodes in the knowledge graph, not a real therapeutic link. This prediction should be treated as unsupported until evidence says otherwise.

Other top-ranked predictions vary in plausibility:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 3 | Glanzmann thrombasthenia | 99.30% | Plausible but unproven; the missing receptor limits any benefit |
| 4 | Primary release disorder of platelets | 99.26% | Plausible; secretion defects are a reasonable class in which to test it |
| 9 | Bleeding diathesis due to a collagen receptor defect | 98.95% | Plausible but speculative |
| 7 | "Flood factor deficiency" | 99.15% | Label looks garbled, probably von Willebrand factor deficiency; mapping needs verification |
| 2, 5, 8 | Inherited thrombophilia, pseudo-von Willebrand disease, thrombocytopenic purpura | 98.9–99.4% | Safety concern: extra VWF release could worsen thrombosis or platelet clumping |
| 6 | Scott syndrome | 99.16% | Any effect would be indirect and weak |
| 10 | Hereditary thrombocytosis with transverse limb defect | 98.95% | No credible mechanistic link |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

For reference, the only publication in the pack is linked to rank 7 ("flood factor deficiency"): [PMID 39054329](https://pubmed.ncbi.nlm.nih.gov/39054329/), a 2024 review titled "von Willebrand disease" in *Nature Reviews Disease Primers*. It is general background and not direct evidence for desmopressin.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2513579 | BIPAZEN |
| 873993 | DDAVP INJ 4MCG/ML |
| 2284030 | APO-DESMOPRESSIN |
| 2024179 | OCTOSTIM LIQ INJ. 15MCG/ML |
| 2242465 | DESMOPRESSIN SPRAY |

Dosage forms and approved indication text were not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the pack.

For some of the other predicted indications, the mechanism suggests a possible risk. In thrombophilia and thrombotic thrombocytopenic purpura, extra VWF and FVIII release could worsen thrombosis. In pseudo-von Willebrand disease, it could increase platelet clumping.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature. Desmopressin does not increase prothrombin, so the high score is probably a graph-proximity artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (currently blocking safety screening)
- Mechanism of action data from DrugBank, to check the mechanistic links properly
- Verification of the "flood factor deficiency" ontology mapping, and confirmation of whether desmopressin is already established for von Willebrand disease
- A targeted literature and trial search for the more plausible candidates (Glanzmann thrombasthenia, platelet release disorders, collagen receptor defects), which are better suited as research questions than the rank 1 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

