---
layout: default
title: Cabergoline
parent: Moderate Evidence (L3-L4)
nav_order: 140
evidence_level: L4
indication_count: 5
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Cabergoline: From Hyperprolactinemic Disorders to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a dopamine D2 agonist, widely used for prolactin-secreting pituitary tumours (prolactinomas) and hyperprolactinemia.
The TxGNN model predicts it may be effective for **pituitary adenocarcinoma**, but there are **0 clinical trials** and only **3 publications** (all case reports, none directly on pituitary carcinoma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinemic disorders / prolactin-secreting pituitary adenomas (taken from trial descriptions; Health Canada indication text was not supplied) |
| Predicted New Indication | Pituitary adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in the supplied data. Cabergoline is known to be a D2 dopamine receptor agonist. D2 activation suppresses hormone secretion and cell proliferation in lactotroph tumours and some corticotroph tumours.

Pituitary adenocarcinoma (carcinoma) is a rare malignant counterpart of the pituitary adenomas that cabergoline already treats. If the tumour cells express D2 receptors, the same mechanism could plausibly apply. That is the basis of the model's prediction.

The support is indirect. The only relevant item is a case report of ectopic ACTH hypersecretion managed with octreotide or cabergoline, and that patient did not have pituitary carcinoma. The very high TxGNN score is a knowledge-graph prediction and is not backed by clinical data for this specific disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case report | Endocr Pract | Long-term octreotide or cabergoline in a patient with ectopic corticotropin secretion after adrenalectomy; not pituitary carcinoma, so indirect evidence |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case report | Rev Esp Enferm Dig | Duodenal lymphangiectasia as the first sign of pancreatic adenocarcinoma in a patient with a pituitary adenoma on cabergoline; off-target |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case report | Medicine | Multiple endocrine neoplasia with an atypical course and a MEN1 variant of uncertain significance; only indirectly related |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2455897 | APO-CABERGOLINE |
| 2549611 | JAMP CABERGOLINE |
| 2242471 | DOSTINEX |

---

## Safety Considerations

Health Canada warnings and contraindications were not available in the supplied data, and no drug interactions were found. Please refer to the package insert for safety information.

Related literature in the Evidence Pack reports the following signals for cabergoline:
- **Cardiac valvulopathy**: debated, but monitoring is advised at high or long-term doses.
- **Impulse control disorders**: a recent study reports a prevalence of up to 59.8%.
- **Angle-closure glaucoma**: reported in a case report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and a mechanistic argument only. There are no trials and no publications directly on pituitary carcinoma, and the three case reports are indirect or off-target.

**To proceed, the following is needed:**
- Clinical data specific to pituitary carcinoma, such as case series or D2 receptor expression studies in carcinoma tissue
- Detailed mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications
- Review of the closely related prediction **pituitary cancer** (rank 3), which has an L2 evidence level and a Proceed with Guardrails recommendation. It is supported by Phase 3 and Phase 4 trials and a meta-analysis in pituitary adenomas (adenoma-level, not carcinoma-level evidence). It should be labelled as extrapolated from adenoma data and would need cardiac valve monitoring and specialist endocrine and oncology oversight.

This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

