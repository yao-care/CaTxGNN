---
layout: default
title: Deoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 260
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Deoxycholic Acid: From an Unspecified Original Indication to Diabetic Nephropathy

## One-Sentence Summary

Deoxycholic acid is a secondary bile acid with cell-membrane-disrupting (cytolytic) activity, marketed in Canada as a single-ingredient product (BELKYRA). The approved indication text is not available in the data compiled for this report.
The TxGNN model gives its highest-ranked predictions to two rare COL4A1-related vascular disorders, but these have no supporting studies. The most actionable lead is **diabetic nephropathy**, which has **0 clinical trials** and **4 publications**, all indirect (bile acid metabolism studies, none testing deoxycholic acid as a treatment).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian license record has no indication text) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (rank 1); diabetic nephropathy is the only prediction with literature (rank 3) |
| TxGNN Prediction Score | 99.49% (rank 1); 99.32% for diabetic nephropathy (rank 3) |
| Evidence Level | L5 for rank 1 (model prediction only); L4 for diabetic nephropathy |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Deoxycholic acid is a secondary bile acid with known cytolytic, membrane-disrupting activity. Because the original indication is not recorded in the compiled data, the link between its established use and the predicted indications cannot be assessed.

**Rank 1 and rank 2 predictions (COL4A1-related disorders).** The top prediction is a rare monogenic disorder of the vascular basement membrane (collagen IV), and rank 2 (brain small vessel disease 1 with or without ocular anomalies) is also COL4A1-related. No known pathway connects deoxycholic acid to this pathology. The two high scores (both about 99.5%) likely reflect a shared neighbourhood in the knowledge graph rather than a biological rationale.

**Rank 3 prediction (diabetic nephropathy).** The retrieved publications link altered bile acid metabolism to diabetic kidney disease. Bile acid signalling through FXR and TGR5 is plausibly relevant to renal inflammation, lipid handling and fibrosis. None of the publications tests deoxycholic acid as a treatment. It may be a biomarker or pathway participant, and whether its effect is protective or harmful is unresolved. Its role as a cytolytic injectable agent also raises a safety question for systemic use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature exists only for diabetic nephropathy (rank 3). Ranks 1 and 2 have no publications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | Clinical observational | Nutrition & Diabetes | Metabolomic profiling of bile acids in patients with diabetic kidney disease, showing step-wise changes in bile acid metabolism as the disease progresses |
| [38377553](https://pubmed.ncbi.nlm.nih.gov/38377553/) | 2024 | Preclinical | ACS Biomaterials Science & Engineering | Nanoparticles absorbed through the intestine to reduce oxidative stress and vasoconstriction in diabetic nephropathy |
| [36996678](https://pubmed.ncbi.nlm.nih.gov/36996678/) | 2023 | Preclinical | Biomedicine & Pharmacotherapy | Relaxin showed renoprotective effects in diabetic mice, accompanied by increased bile acid levels |
| [33378964](https://pubmed.ncbi.nlm.nih.gov/33378964/) | 2021 | Preclinical | Biomedicine & Pharmacotherapy | QiDiTangShen granules altered gut microbiome composition and improved bile acid profiles in a diabetic nephropathy mouse model |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02443910 | BELKYRA | Not recorded | Not recorded |

## Safety Considerations

**Drug Interactions**: 67 interactions were identified. The 20 listed in the compiled data are all rated Moderate, and most involve agents that affect bleeding or clotting:
- Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, abciximab, cangrelor, caplacizumab
- Anticoagulants: apixaban, betrixaban, dalteparin, fondaparinux, danaparoid, argatroban, bivalirudin, desirudin, antithrombin III human
- Thrombolytics: alteplase, anistreplase
- Radiolabelled antibodies: ibritumomab tiuxetan, tositumomab, tositumomab (I-131)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top two predictions have no supporting studies and no plausible mechanism. The diabetic nephropathy prediction has only indirect, mostly preclinical evidence on bile acid metabolism, and none of it tests deoxycholic acid. The package insert safety data and the original indication are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications and approved indication)
- Mechanism of action data for deoxycholic acid (for example, from DrugBank)
- Studies directly testing deoxycholic acid, or its FXR/TGR5 signalling, in diabetic kidney disease models
- A safety assessment of systemic exposure, given the drug's cytolytic activity and its route of administration
- Route compatibility assessment for the predicted indications (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

