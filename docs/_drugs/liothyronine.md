---
layout: default
title: Liothyronine
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Liothyronine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Liothyronine: From Thyroid Hormone Replacement to Nodular Goiter

## One-Sentence Summary

Liothyronine (synthetic T3, DrugBank DB00279) is a thyroid hormone with no supporting original-indication data in the current evidence pack and no marketing presence in Canada.
Among TxGNN's top 10 predictions, only **Nodular Goiter** is backed by real-world evidence — the other 9 candidates (including the two highest-scoring, renal hypodysplasia/aplasia and bilateral renal agenesis) have no clinical trials or literature at all, so this report focuses on Nodular Goiter as the only scientifically actionable signal, supported by **2 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (drug not marketed in Canada; no license record). Classically, liothyronine is a thyroid hormone replacement used for hypothyroidism. |
| Predicted New Indication | Nodular Goiter (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, liothyronine is a synthetic form of triiodothyronine (T3), a direct thyroid hormone receptor agonist with rapid onset and short half-life.

Exogenous thyroid hormone suppresses pituitary TSH secretion, which is the established mechanism behind "TSH-suppressive therapy" — a standard approach used to shrink or control benign nodular goiter and prevent regrowth after thyroid surgery. This is exactly the mechanistic link the TxGNN model is capturing.

In clinical practice, however, this suppressive role is almost always filled by **levothyroxine (T4)**, not liothyronine (T3), precisely because T3's short half-life makes it poorly suited for stable long-term TSH suppression. One of the retrieved papers (PMID 10426591) directly demonstrates suppressive therapy with levothyroxine — not liothyronine — for euthyroid nodular goiter, reinforcing that the mechanism is real but the specific drug substitution (T3 for T4) is not yet clinically validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02665325](https://clinicaltrials.gov/study/NCT02665325) | N/A | Unknown | 100 | Evaluates cognitive function and mood in differentiated thyroid carcinoma patients undergoing TSH-suppressive therapy with L-thyroxine — same suppressive mechanism, but studies thyroid carcinoma (not nodular goiter) and does not specify liothyronine use. |
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | N/A | Completed | 68 | Randomized placebo-controlled trial of Anethum graveolens (dill) extract in thyroiditis and nodular goiter patients, evaluating hormone levels and nodule size — unrelated to liothyronine itself. |

Neither trial directly tests liothyronine in nodular goiter; both are mechanism-adjacent only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38278171](https://pubmed.ncbi.nlm.nih.gov/38278171/) | 2024 | Review | Lancet | Comprehensive review of hyperthyroidism, including toxic nodular goitre pathophysiology and TSH-based diagnosis. |
| [36818930](https://pubmed.ncbi.nlm.nih.gov/36818930/) | 2022 | Review | Acta Clinica Croatica | Reviews amiodarone-induced thyroid dysfunction, noting T4-to-T3 conversion pathways relevant to thyroid hormone pharmacology. |
| [28915531](https://pubmed.ncbi.nlm.nih.gov/28915531/) | 2017 | Review | Hormone and Metabolic Research | Reviews subclinical hyperthyroidism (the state induced by TSH-suppressive dosing) and its cardiovascular risk. |
| [23998691](https://pubmed.ncbi.nlm.nih.gov/23998691/) | 2014 | Review | Climacteric | Reviews thyroid-reproductive axis interactions; background context on thyroid hormone physiology in women. |
| [5067818](https://pubmed.ncbi.nlm.nih.gov/5067818/) | 1972 | Review | The Medical Clinics of North America | Historical review of hyperthyroidism presentation and management. |
| [37434815](https://pubmed.ncbi.nlm.nih.gov/37434815/) | 2023 | Cohort | American Journal of Translational Research | Correlates urinary iodine levels with thyroid function indices in nodular goiter patients. |
| [34980104](https://pubmed.ncbi.nlm.nih.gov/34980104/) | 2022 | Case-Control | Environmental Health | Case-control study of perchlorate and iodine exposure as risk factors for nodular goiter and thyroid tumors. |
| [11453524](https://pubmed.ncbi.nlm.nih.gov/11453524/) | 2001 | Cohort | Journal of Pediatric Endocrinology & Metabolism | Compares serum cytokine levels between Graves' disease and non-toxic nodular goiter in children/adolescents. |
| [16776143](https://pubmed.ncbi.nlm.nih.gov/16776143/) | 2006 | Case Report | Nihon Rinsho | Case report of T3 toxicosis, relevant to liothyronine's own toxicity profile. |
| [25297557](https://pubmed.ncbi.nlm.nih.gov/25297557/) | 2014 | Animal Study | The Journal of Endocrinology | Feline hyperthyroidism as an animal model mechanistically similar to human toxic nodular goiter. |

---

## Canada Market Information

Liothyronine currently has **no Health Canada market authorization** in this dataset (0 DINs, market status: 未上市/Not marketed). No product license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available (all fields flagged as data gaps, including a **Blocking**-severity gap for TFDA/Health Canada label warnings — DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TSH-suppression mechanism is pharmacologically coherent and supported by L3-level observational/review evidence, but no study directly tests liothyronine (as opposed to levothyroxine) in nodular goiter, the drug is not marketed in Canada, and a Blocking-severity safety data gap (missing label warnings/contraindications) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) to clear the S1 safety gate (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Evidence specifically evaluating liothyronine (not levothyroxine) for TSH-suppressive therapy in nodular goiter, or an explicit pharmacologic justification for extrapolating from T4 data to T3
- Clarification of Canada market/import status given zero current DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

