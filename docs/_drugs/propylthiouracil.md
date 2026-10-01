---
layout: default
title: Propylthiouracil
parent: Moderate Evidence (L3-L4)
nav_order: 773
evidence_level: L4
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Propylthiouracil (PTU) is an antithyroid drug that lowers thyroid hormone production. The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but there are **0 clinical trials** and **6 publications**, and none of the publications show PTU helping in this condition. This prediction is a graph-based association only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided data (PTU is generally known as an antithyroid drug for hyperthyroidism) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. PTU is known to inhibit thyroid peroxidase and so reduce thyroid hormone synthesis. It also inhibits peripheral conversion of T4 to T3.

In resistance to thyroid hormone (RTH), a THRB mutation makes tissues respond poorly to thyroid hormone. Serum T4 and T3 are high, and TSH is inappropriately normal or high. A drug that lowers hormone levels looks related to this picture on the surface. That is probably why the graph model scores it highly.

Mechanistically, however, the fit is poor. Lowering hormone output in RTH would be expected to raise TSH further and risk worsening goiter. No retrieved record shows a clinical benefit from PTU in this condition. The link is a statistical association in the knowledge graph, not a demonstrated treatment effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review | Endocrinology | Role of the TR-beta isoform in thyroid hormone resistance in the heart; describes the RTH syndrome and its elevated T4/T3. Not about PTU treatment. |
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case report | Exp Clin Endocrinol Diabetes | Turkish family (mother and son) with a THRB P453A mutation and RTH. No PTU treatment evidence. |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | Neonatal thyrotoxicosis and maternal infertility in a family with a THRB M313T mutation. Describes the disease, not PTU benefit. |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocr J | Thai woman with a de novo THRB L330S mutation. She was misdiagnosed with thyrotoxicosis and treated with PTU for 9 months, and her goiter became more enlarged. |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Animal study | Endocrinology | Role of TSH in spontaneous thyroid carcinoma in a THRB-mutant mouse model. Preclinical, not about PTU. |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Animal study | Oncogene | Thyroid hormone drives tumour cell proliferation in a mouse model of follicular thyroid carcinoma with a dominant-negative THRB mutation. Preclinical, not about PTU. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2523019 | PROPYLTHIOURACIL TABLETS |
| 2521059 | HALYCIL |

Dosage form and approved indication text were not provided for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the provided data.

The review of a related predicted indication (neonatal thyrotoxicosis) noted that PTU carries a hepatotoxicity warning. A safety review is needed before any further work.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.66%), but the evidence is L4. The literature describes the disease itself (THRB mutations, family case reports, mouse models), and no study shows PTU benefit. The one case report involving PTU suggests it may worsen goiter. Mechanistically, suppressing thyroid hormone synthesis is not expected to help in RTH.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to support or refute a mechanistic link
- Original approved indication text and dosage forms for the two licenses
- Any clinical evidence of PTU outcomes in confirmed THRB-mutation RTH, rather than misdiagnosed thyrotoxicosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

