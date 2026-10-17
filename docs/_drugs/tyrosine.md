---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 956
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not specified in the Canadian license data"
monitor_inn: "Tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma"]
---

# Tyrosine
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

# Tyrosine: From an Unspecified Nutritional Indication to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid used as a nutrient component in parenteral nutrition products marketed in Canada. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but the data compiled for this report contain **no clinical trials and no publications** supporting this prediction. This is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is a precursor of catecholamines (dopamine, norepinephrine) and thyroid hormones. Its Canadian products are amino acid solutions for parenteral nutrition, but no approved indication text is recorded.

Nothing in the data compiled for this report connects tyrosine to compressive injury of the lumbosacral nerve roots, which is the basis of cauda equina syndrome. The high TxGNN score reflects a model output and is not supported by any trial or publication, so the prediction should be treated as a hypothesis only.

**Other predictions reviewed (all Hold, L5 unless noted):**

| Predicted Indication | TxGNN Score | Observation |
|------|------|------|
| Obsolete neurogenic bladder | 99.55% | No supporting evidence; the disease term is obsolete |
| Angle-closure glaucoma | 99.54% | Only associative biomarker data (plasma amino acid changes); no therapeutic evidence |
| Hyperthyroidism | 99.51% | Safety concern: tyrosine is a thyroid hormone substrate and could theoretically worsen thyrotoxicosis |
| Postural orthostatic tachycardia syndrome | 99.46% | Plausible indirect link via catecholamines (L4); the only paper is a case report of a drug with the opposite action |
| Hyperthyroxinemia | 99.46% | Supplementation could theoretically raise thyroxine |
| Resistance to thyroid hormone (THRB mutation) | 99.40% | Receptor defect that a precursor would not correct |
| Traumatic glaucoma, aqueous misdirection, neovascular glaucoma | 99.35–99.32% | No credible mechanism or supporting evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

For reference, one trial was found for the rank 4 prediction (hyperthyroidism):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Placebo-controlled trial of a zinc, selenium, and L-tyrosine supplement to prevent thyrotoxicosis in adults with elevated TPO antibodies and the SEPP1 polymorphism. Tyrosine is not the sole evaluated agent, so it provides no direct evidence for tyrosine. |

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For reference, the most relevant publications retrieved for other predictions are listed below. None tests tyrosine as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Frontiers in Medicine | Plasma amino acid alterations in early primary angle-closure glaucoma (biomarker observation only) |
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome case treated with alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor that acts opposite to tyrosine; indirect relevance to POTS |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism causes, diagnosis, and management |
| [30886364](https://pubmed.ncbi.nlm.nih.gov/30886364/) | 2019 | Review | Nat Rev Endocrinol | Role of thyroglobulin tyrosine residues in thyroid hormone synthesis (background mechanism) |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Preclinical | Endocrinology | Thyroid hormone receptor beta mutations impairing ligand binding (background mechanism) |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma causes and treatment |

---

## Canada Market Information

All 20 licenses are valid single-ingredient products. Dosage form and approved indication text are not recorded in the data compiled for this report. The first five are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not recorded | Not recorded |
| 02013932 | CLINIMIX | Not recorded | Not recorded |
| 02013940 | CLINIMIX | Not recorded | Not recorded |
| 00872296 | TRAVASOL | Not recorded | Not recorded |
| 02013886 | CLINIMIX | Not recorded | Not recorded |

Other marketed products include CLINIMIX E, ESSEPNA, 20% PROSOL, PRIMENE 10%, OLIMEL 5.7% and 7.6%, and SMOFKABIVEN electrolyte-free formulations.

---

## Safety Considerations

- **Theoretical thyroid concern:** Tyrosine is a substrate for thyroid hormone synthesis. For hyperthyroidism and hyperthyroxinemia, supplementation could in theory worsen the condition rather than treat it.
- **Drug interactions:** No interaction records were found.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome rests solely on a model score, with no trials, no publications, and no identified mechanism. The other top predictions are likewise unsupported, and several (hyperthyroidism, hyperthyroxinemia) raise theoretical safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism of action data for tyrosine
- Original approved indication text for the Canadian products
- A plausible biological rationale linking tyrosine to cauda equina syndrome, followed by preclinical or clinical studies
- Consideration of the rank 5 prediction (postural orthostatic tachycardia syndrome), which has a plausible catecholamine link, as a better-motivated alternative, although direct evidence is still absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

