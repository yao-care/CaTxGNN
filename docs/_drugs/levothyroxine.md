---
layout: default
title: Levothyroxine
parent: Moderate Evidence (L3-L4)
nav_order: 542
evidence_level: L4
indication_count: 10
---

# Levothyroxine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levothyroxine: From Thyroid Hormone Replacement to Endemic Goiter

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone (T4). The Canadian label text was not included in the data supplied, so its original indication is not confirmed here.
The TxGNN model predicts it may be useful for **endemic goiter**.
Only **1 clinical trial** (which tests dill, not levothyroxine) and **20 publications** (mostly epidemiological or physiological, with one small levothyroxine study) are linked to this prediction, so the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Endemic goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Levothyroxine replaces or supplements the body's own thyroid hormone. It would be expected to lower TSH (thyroid-stimulating hormone), the signal that drives the thyroid to grow.

Endemic goiter is mainly caused by iodine deficiency. Low thyroid hormone output raises TSH, and the thyroid enlarges in response. A cohort study in the pack (PMID 6304776) found higher baseline TSH in people living in iodine-deficient areas. Giving levothyroxine to lower TSH is therefore biologically plausible.

However, the first-line intervention for endemic goiter is iodine repletion, not thyroid hormone. The retrieved literature is mostly about iodine prophylaxis and thyroid physiology, and only one item (PMID 3278876) tested levothyroxine. The link is a plausible hypothesis, not a demonstrated benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | Not applicable | Completed | 68 | Placebo-controlled study of dill (*Anethum graveolens*) in thyroiditis and nodular goiter, measuring hormone levels, inflammatory markers and nodule size over 90 days. It does not test levothyroxine and was not in an iodine-deficient setting. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | RCT | Curr Med Res Opin | Maternal iodine supplementation in 460 pregnant women from non-goiter and goiter-endemic areas, examining thyroid function and birth outcomes. Iodine was tested, not levothyroxine. |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Clinical study | Dtsch Med Wochenschr | Multicenter study in 74 patients with diffuse endemic goiter. Levothyroxine 150 µg daily was compared with levothyroxine 100 µg plus iodide for 6 months, then iodide alone. This is the only item that tests levothyroxine directly. |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World J Surg | Iodine deficiency is the established primary cause, and iodine supplementation is the established prevention and treatment. The review also discusses other causative factors. |
| [7704809](https://pubmed.ncbi.nlm.nih.gov/7704809/) | 1994 | Review | Curr Ther Endocrinol Metab | Overview of endemic goiter (no abstract available). |
| [36839362](https://pubmed.ncbi.nlm.nih.gov/36839362/) | 2023 | Overview | Nutrients | Update on iodine deficiency and iodine prophylaxis. |
| [6304776](https://pubmed.ncbi.nlm.nih.gov/6304776/) | 1983 | Cohort | Prog Clin Biol Res | Patients in iodine-deficient areas had higher basal TSH and TRH response than controls. TSH correlated inversely with T4. |
| [3090091](https://pubmed.ncbi.nlm.nih.gov/3090091/) | 1986 | Cohort | J Clin Endocrinol Metab | Thyroid function study of 1,218 people in an endemic area of northern Italy (65% goiter prevalence). |
| [6309889](https://pubmed.ncbi.nlm.nih.gov/6309889/) | 1983 | Clinical study | J Clin Endocrinol Metab | Iodized oil given to 58 goitrous patients in mildly iodine-deficient Greece. Goiter size decreased. |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Observational | J Clin Endocrinol Metab | Maternal and newborn thyroid status in severe endemic goiter (Zaire), related to fetal hypothyroidism. |
| [6863473](https://pubmed.ncbi.nlm.nih.gov/6863473/) | 1983 | Survey | J Clin Endocrinol Metab | Survey of endemic goiter in Vietnam, which affects about 15% of the population. Goitrogenic cassava in the diet was one contributing factor. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02550792 | APO-LEVOTHYROXINE |
| 02461714 | LEVOTHYROXINE SODIUM FOR INJECTION |
| 02172119 | SYNTHROID |
| 02172089 | SYNTHROID |
| 02172135 | SYNTHROID |

*Showing 5 of 20 authorizations. Dosage form and approved-indication text were not provided for these entries.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.81%), but the supporting evidence is indirect. No registered trial tests levothyroxine for endemic goiter, and iodine repletion is already the established first-line approach. This is best treated as a research question.

**To proceed, the following is needed:**
- Health Canada monograph text (approved indications, warnings, contraindications) and mechanism of action data
- Controlled studies of levothyroxine, alone or with iodine, in iodine-deficient populations
- A comparison against iodine repletion alone

**Other predictions for this drug:** In this Evidence Pack, **nodular goiter** is the best-supported prediction (L1 per the pack's label, Proceed with Guardrails). It has randomized trials of levothyroxine, including NCT00277589 (Phase 4, placebo-controlled, 1,024 patients). Its L1 label counts Phase 4 randomized evidence as equivalent to the Phase 3 criterion. It may be a better candidate to pursue first. Renal hypodysplasia/aplasia, bilateral renal agenesis and Potter sequence have no plausible mechanism and are likely graph artifacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

