---
layout: default
title: Tisagenlecleucel
parent: Model Prediction Only (L5)
nav_order: 917
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tisagenlecleucel: predicted new indication Crohn's colitis (evidence level L5). Approved use: Not stated in the available licence data"
---

# Tisagenlecleucel
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

# Tisagenlecleucel: From CD19-Positive B-Cell Malignancy to Crohn's Colitis

## One-Sentence Summary

Tisagenlecleucel (KYMRIAH) is a CD19-directed CAR-T cell therapy that depletes B cells. It is marketed in Canada, but the data compiled for this report do not list an approved indication text.
The TxGNN model predicts it may be effective for **Crohn's colitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Crohn's colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. Based on known information, tisagenlecleucel is a CD19-directed CAR-T cell therapy: the patient's own T cells are engineered to recognise CD19 and eliminate B cells.

The link to Crohn's colitis is only a graph-based prediction. Crohn's disease is driven mainly by T-cell and innate immune pathways, and B-cell depletion has not shown consistent benefit. The mechanistic case is therefore weak.

Safety is also a concern. Lymphodepleting chemotherapy, cytokine release syndrome and infection risk are difficult to justify in a non-life-threatening condition.

The other nine predicted indications were also reviewed. Most have no plausible CD19-related target:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Multiple endocrine neoplasia | 91.34% | No plausible target |
| 3 | Idiopathic aplastic anemia | 89.69% | T-cell-mediated; possible worsening of cytopenias |
| 4 | Adrenal gland hyperfunction | 88.34% | No mechanistic rationale |
| 5 | HER2 positive breast carcinoma | 88.02% | CD19 not expressed; solid tumour barriers |
| 6 | Ankylosing spondylitis | 87.11% | TNF and IL-17/IL-23 driven; safer biologics exist |
| 7 | Lymphoadenopathic mastocytosis with eosinophilia | 87.04% | Not a CD19-expressing B-cell disease |
| 8 | Systemic mastocytosis | 87.00% | KIT-driven; kinase inhibitors are more appropriate |
| 9 | Smouldering systemic mastocytosis | 86.83% | Indolent disease; toxicity unacceptable |
| 10 | Rheumatoid vasculitis | 86.24% | Most plausible (B-cell and autoantibody component), but still only exploratory |

All ten predictions are at evidence level L5 with a Hold recommendation.

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
| 02480514 | KYMRIAH | Not stated | Not stated |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (CAR-T cell therapy) |
| Myelosuppression Risk | High for the regimen: prolonged cytopenias are reported, and the lymphodepleting chemotherapy is myelosuppressive |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, signs of cytokine release syndrome and neurotoxicity, infection surveillance |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 41 interactions were identified. The first 20 records in the compiled data include these major-level interactions:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
  - Leflunomide
  - Natalizumab

  Moderate-level interactions include strontium chloride Sr-89, roflumilast, chloramphenicol, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, dimethyl fumarate, niraparib and ocrelizumab. Many of these are immunosuppressive or myelosuppressive agents.
- **Predicted-indication safety signals**: Lymphodepleting chemotherapy, cytokine release syndrome and infection risk are of particular concern in non-life-threatening conditions. In idiopathic aplastic anemia, prolonged cytopenias could worsen the disease.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Crohn's colitis has a high model score (91.39%) but no clinical trials or literature behind it. The mechanistic link is weak because Crohn's disease is not primarily B-cell driven. The safety burden of CAR-T therapy is hard to justify in this setting.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Approved indication, dosage form and manufacturer details for the Canadian licence
- Preclinical or exploratory evidence of B-cell involvement in Crohn's colitis
- If any autoimmune indication is pursued, rheumatoid vasculitis (rank 10) is the most biologically plausible starting point, at an exploratory or preclinical stage only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

