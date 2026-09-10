---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Propylthiouracil (PTU): From Hyperthyroidism to Neonatal Thyrotoxicosis and Related Thyroid Hormone Disorders

## One-Sentence Summary

Propylthiouracil (PTU, DB00550) is a classic thionamide antithyroid agent, established for treating hyperthyroidism (most notably Graves' disease). TxGNN generated three predicted indications for this drug — **resistance to thyroid hormone (THRB mutation)**, **neonatal thyrotoxicosis**, and **hyperthyroxinemia** — but only **neonatal thyrotoxicosis** is backed by a directly matching mechanism, **1 clinical trial** and **20 supporting publications**; the other two candidates show a mechanistic mismatch and are not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism (Graves' disease) — established pharmacological use; not currently found in the Canadian licensing dataset for this drug |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Number of Predicted Indications Evaluated | 3 |
| Lead Predicted Indication | Neonatal thyrotoxicosis |
| TxGNN Prediction Score (lead) | 99.40% |
| Evidence Level (lead) | L3 |
| Recommended Decision (lead) | Proceed with Guardrails |

### Predicted Indications Comparison

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Resistance to thyroid hormone (THRB mutation) | 99.66% | L5 | S0 | Hold |
| 2 | Neonatal thyrotoxicosis | 99.40% | L3 | S2 | Proceed with Guardrails |
| 3 | Hyperthyroxinemia | 99.08% | L4 | S1 | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available in the evidence pack for PTU. Based on well-established pharmacology, propylthiouracil inhibits thyroid peroxidase (TPO), blocking iodide organification and the coupling of iodotyrosines, thereby reducing synthesis of T4 and T3. It also inhibits peripheral type 1 deiodinase (D1), reducing conversion of T4 to the more biologically active T3. This dual action (synthesis blockade + peripheral conversion blockade) is the pharmacological basis for its established use in hyperthyroidism, particularly Graves' disease, where it is frequently the preferred agent in the first trimester of pregnancy.

**Neonatal thyrotoxicosis** is mechanistically the best match. This condition most commonly arises when maternal Graves' disease TSH-receptor-stimulating antibodies (TRAb) cross the placenta and stimulate the fetal/neonatal thyroid. Thionamides (PTU or methimazole) are the standard pharmacological approach to controlling maternal and, indirectly, fetal/neonatal hyperthyroidism in this setting — the mechanism directly addresses the excess hormone production driving the disease.

**Hyperthyroxinemia** is only a partial match. Where the elevated T4 is driven by true thyroid hyperfunction (e.g., Graves' disease, amiodarone-induced hyperthyroidism), PTU's synthesis-blocking mechanism is directly applicable, as seen in one of the supporting cohort studies. However, several of the underlying literature cases involve non-hyperfunctional causes such as familial dysalbuminemic hyperthyroxinemia (an albumin-binding artifact) or thyroid hormone receptor resistance — conditions PTU cannot correct, since the hormone level itself is not pathologically elevated in the way PTU is designed to reduce.

**Resistance to thyroid hormone (THRB mutation)** is mechanistically the weakest fit. This condition is caused by a THRB receptor mutation that reduces target-tissue responsiveness to thyroid hormone, with compensatory elevation of TSH/T4/T3. The pathology lies in receptor signaling, not in excess hormone synthesis. PTU can only reduce hormone *synthesis*, which does not correct receptor-level resistance — none of the six supporting publications actually evaluate PTU treatment outcomes in this condition; all are genetic/mechanistic characterization or animal-model studies.

---

## Clinical Trial Evidence

### Neonatal Thyrotoxicosis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03066076](https://clinicaltrials.gov/study/NCT03066076) | Phase 3 | Unknown | 60 | Compared total thyroidectomy vs. thionamide (antithyroid drug) therapy in Graves' ophthalmopathy patients; relevant as an indirect maternal-management trial for pregnancy-related thyrotoxicosis rather than a direct neonatal-thyrotoxicosis treatment trial. Follow-up status is uncertain (marked UNKNOWN). |

### Resistance to Thyroid Hormone (THRB mutation) / Hyperthyroxinemia

Currently no related clinical trials registered.

---

## Literature Evidence

### Neonatal Thyrotoxicosis (lead candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25747892](https://pubmed.ncbi.nlm.nih.gov/25747892/) | 2015 | Cohort | Thyroid | Gestational thyrotoxicosis and antithyroid drug use analyzed against neonatal outcomes in an integrated healthcare system |
| [36680759](https://pubmed.ncbi.nlm.nih.gov/36680759/) | 2023 | Cohort | Thyroid | Incidence/risk factors for neonatal hypothyroidism in Graves' patients treated with antithyroid drugs until delivery |
| [33349844](https://pubmed.ncbi.nlm.nih.gov/33349844/) | 2021 | Review | J Clin Endocrinol Metab | Testing, monitoring and treatment of thyroid dysfunction in pregnancy |
| [31345521](https://pubmed.ncbi.nlm.nih.gov/31345521/) | 2019 | Review | Endocrinol Metab Clin North Am | Overview of hyperthyroidism management in pregnancy, including PTU use in the first trimester |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Hyperthyroidism in pregnancy — maternal/fetal risk overview |
| [32199749](https://pubmed.ncbi.nlm.nih.gov/32199749/) | 2020 | Review | Best Pract Res Clin Endocrinol Metab | Management of thyrotoxicosis during pregnancy |
| [34335902](https://pubmed.ncbi.nlm.nih.gov/34335902/) | 2021 | Review | Exp Ther Med | Hyperthyroidism management during pregnancy and lactation |
| [25185644](https://pubmed.ncbi.nlm.nih.gov/25185644/) | 2014 | Review | J Endocrinol Invest | Update on medical (thionamide) treatment of Graves' hyperthyroidism |
| [18558604](https://pubmed.ncbi.nlm.nih.gov/18558604/) | 2008 | Case Report | Endocr Pract | Persistent neonatal thyrotoxicosis from an activating TSHR mutation |
| [2090674](https://pubmed.ncbi.nlm.nih.gov/2090674/) | 1990 | Case Report | J Endocrinol Invest | Neonatal hepatitis and lymphocyte sensitization following placental transfer of PTU |

### Resistance to Thyroid Hormone (THRB mutation)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case Report | Exp Clin Endocrinol Diabetes | THRB gene mutation (P453A) causing thyroid hormone resistance in a family |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review | Endocrinology | Role of TRβ isoform in cardiac thyroid hormone resistance |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Preclinical | Endocrinology | TSH-driven thyroid carcinoma development in TRβ-mutant mice |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clin Endocrinol | Neonatal thyrotoxicosis and maternal infertility linked to TRβ mutation (M313T) |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case Report | Endocr J | De novo L330S TRβ mutation in a Thai patient previously (unsuccessfully) treated with PTU |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Preclinical | Oncogene | Thyroid hormone-driven tumor proliferation in a TRβ-mutant (PV) mouse model |

### Hyperthyroxinemia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2840057](https://pubmed.ncbi.nlm.nih.gov/2840057/) | 1988 | Cohort | Aust N Z J Med | Amiodarone-induced hyperthyroidism treated with combined PTU and potassium perchlorate |
| [18334584](https://pubmed.ncbi.nlm.nih.gov/18334584/) | 2008 | Case Report | J Clin Endocrinol Metab | Beneficial effect of PTU plus L-thyroxine in a patient with MCT8 mutation |
| [3097618](https://pubmed.ncbi.nlm.nih.gov/3097618/) | 1986 | Review | Pediatrics | Familial partial thyroid hormone resistance — poor response to PTU/thyroidectomy reported |
| [7527990](https://pubmed.ncbi.nlm.nih.gov/7527990/) | 1994 | Review | Acta Med Austriaca | Thyroxine excess and pregnancy |
| [32101523](https://pubmed.ncbi.nlm.nih.gov/32101523/) | 2020 | Case Report | Endocrinol Diabetes Metab Case Rep | Familial dysalbuminemic hyperthyroxinemia confounding autoimmune thyroid disease management |
| [3708869](https://pubmed.ncbi.nlm.nih.gov/3708869/) | 1986 | Other | Clin Endocrinol | Albumin-binding studies in familial dysalbuminemic hyperthyroxinemia |
| [8574290](https://pubmed.ncbi.nlm.nih.gov/8574290/) | 1995 | Preclinical | Endocr J | Long-term PTU/thyroid hormone effects on lymphocyte subsets in mice |
| [3498760](https://pubmed.ncbi.nlm.nih.gov/3498760/) | 1987 | Other | J Immunol | Reduced NK cell activity in hyperthyroxinemic mice, with PTU as hypothyroid comparator |
| [9436485](https://pubmed.ncbi.nlm.nih.gov/9436485/) | 1997 | Case Report | Ann Endocrinol | Fetal cord blood sampling in diagnosis/treatment of fetal hyperthyroidism |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review | Endocrinology | Role of TRβ isoform in cardiac thyroid hormone resistance |

---

## Canada Market Information

No Canadian licenses (DINs) are on file for this drug in the evidence pack (market status: Not marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (neonatal thyrotoxicosis) / **Hold** (resistance to thyroid hormone; hyperthyroxinemia)

**Rationale:**
- Neonatal thyrotoxicosis has a directly matching mechanism (thionamide blockade of hormone synthesis addresses the excess-hormone pathology) and is supported by 1 Phase 3 trial (indirect, maternal-management) plus 20 publications, including cohort-level data — sufficient to proceed cautiously.
- Resistance to thyroid hormone and hyperthyroxinemia (non-hyperfunctional subtypes) show a mechanistic mismatch — PTU cannot correct receptor resistance or protein-binding artifacts — and no publication evaluates PTU treatment outcomes for these conditions directly, so these two remain on Hold.

**To proceed, the following is needed:**
- Product monograph / regulatory safety warnings and contraindications for PTU (currently a Blocking data gap — required before any S1 safety review)
- Detailed mechanism-of-action confirmation from DrugBank (High-priority data gap)
- A direct clinical evaluation of PTU (not just thionamides generally) specifically in confirmed neonatal thyrotoxicosis cases, given current evidence is largely about maternal Graves' disease management
- Route/formulation compatibility assessment for neonatal or pediatric dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

