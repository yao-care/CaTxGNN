---
layout: default
title: Estrone
parent: Model Prediction Only (L5)
nav_order: 356
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Estrone: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
---

# Estrone
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

# Estrone: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Estrone is a weak estrogen, and in the knowledge base used for this report its original indication is acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are **0 clinical trials** and only **1 loosely related publication** supporting this direction.
The prediction is purely computational and has no clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

*Note: The approved-indication text for the Canadian product is not available, so the original indication is taken from the knowledge graph's indication records.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, estrone is a weak estrogen and a precursor/metabolite of estradiol. Estrogens can modestly influence circulating trace metals, for example through changes in binding proteins such as albumin and ceruloplasmin.

However, there is no evidence that estrone raises, lowers or treats elevated plasma zinc. The high TxGNN score (0.998) is a network-based prediction without clinical support. In addition, elevated plasma zinc is a laboratory finding rather than a treatable clinical condition, which further limits its therapeutic relevance.

A second prediction, **pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome** (score 99.30%), also has no clinical trials or literature. It is an autoinflammatory disorder driven by PSTPIP1 mutations and excess IL-1β. The link to estrone appears to come only from the shared "acne" phenotype. Established treatments target IL-1 or TNF, not estrogens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Clinical intervention study | The American Journal of Clinical Nutrition | Soy protein intake in perimenopausal women and its effect on iron indexes and antioxidant status. Only indirectly related to estrogens and trace metals, and it does not address estrone or zinc. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00727369 | ESTRAGYN VAGINAL CREAM | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The knowledge graph links estrone with a wide range of conditions, including:
  - Cardiovascular and metabolic: hypertension, diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypertriglyceridemia, hypercalcemia, nephrocalcinosis, humoral hypercalcemia of malignancy
  - Hepatic and biliary: liver failure, liver disease, gallbladder disease
  - Neurological and psychiatric: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, anxiety disorder, neurotic disorder, dysthymic disorder
  - Porphyrias: inherited porphyria, porphyrin metabolism disease, porphyria
  - Endocrine: hypothyroidism, myxedema, congenital hypothyroidism
  - Immune and respiratory: systemic lupus erythematosus (including pediatric), asthma (including intrinsic and allergic)
- **Drug Interactions:** 100 interactions were found in total. The 20 reviewed are mostly Moderate, with one Minor (cimetidine). The main ones are:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - Antidiabetic agents: acarbose, metformin, chlorpropamide, and the GLP-1, DPP-4 and SGLT2 classes (albiglutide, dulaglutide, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin)
  - Others: aprepitant, clarithromycin, chenodeoxycholic acid, topical calcitriol

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials, the only publication is indirectly related, and no credible mechanistic link exists. The target "elevated plasma zinc" is a laboratory finding rather than a disease that requires treatment. The PAPA syndrome prediction is equally unsupported.

**To proceed, the following is needed:**
- Mechanism of action data for estrone
- Health Canada package insert warnings and contraindications, which are needed before safety screening can proceed
- Clear justification that the predicted indication is a clinically meaningful treatment target
- Preclinical or clinical evidence linking estrone to the predicted indication
- Route compatibility assessment (the Canadian product is a vaginal cream)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

