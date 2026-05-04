---
layout: default
title: Buserelin
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 5
---

# Buserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Buserelin: From Hormone Regulation (GnRH Agonist) to Hypertrichosis

## One-Sentence Summary

Buserelin is a gonadotropin-releasing hormone (GnRH) agonist that works by suppressing the LH/FSH axis to reduce sex hormone levels, and is used in conditions such as hormone-sensitive cancers and endocrine disorders.
The TxGNN model predicts it may be effective for **Hypertrichosis (disease)**, with **0 clinical trials** and **1 publication** currently supporting this direction — and the mechanistic rationale for this prediction is considered weak.
This report recommends a **Hold** decision pending further mechanistic and clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset (GnRH agonist class; typically used for hormone-sensitive conditions) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Buserelin is a synthetic GnRH agonist. When administered continuously, it causes desensitization of pituitary GnRH receptors, leading to suppression of LH and FSH secretion, and consequently a reduction in sex hormone (androgen and estrogen) production. This mechanism has a theoretical connection to androgen-driven excess hair growth (hirsutism), as lowering androgen levels can reduce hair follicle stimulation in androgen-sensitive skin areas.

However, it is critical to distinguish between **hirsutism** and **hypertrichosis** — the predicted indication in this report. Hirsutism refers to androgen-dependent excess hair growth in hormone-sensitive areas (e.g., face, chest) and has a clear mechanistic rationale for GnRH agonist intervention. **Hypertrichosis**, by contrast, is a generalized excess hair growth that is typically non-androgen-dependent, arising instead from genetic mutations, drug side effects, or systemic conditions. The underlying biology is fundamentally different, and suppressing the GnRH/sex hormone axis would not be expected to address hypertrichosis.

The sole supporting publication (PMID 31743099) describes a case of Cantu syndrome — a rare genetic disorder characterized by hypertrichosis among other features — complicated by hypopituitarism, and discusses the need for endocrine monitoring. It does not mention buserelin or any GnRH agonist as a treatment, and serves only as distant background literature. The TxGNN prediction likely reflects semantic proximity in the knowledge graph between GnRH signalling pathways and hair-related phenotypes, rather than a genuine therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Buserelin in Hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Case Report | Endocrinology, Diabetes & Metabolism Case Reports | A case of Cantu syndrome (characterized by hypertrichosis among other features) presenting with multiple pituitary hormone deficiencies at age 13; authors recommend inclusion of endocrine monitoring in clinical surveillance. No buserelin or GnRH agonist treatment discussed. |

> **Note:** This publication is indirect background evidence only. It does not evaluate buserelin for hypertrichosis, and its relevance to the predicted repurposing indication is minimal.

---

## Canada Market Information

Buserelin is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are registered.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) are not available in the current dataset. As buserelin is not marketed in Canada, no Canadian product monograph is available for reference.

Please consult the European product labelling or published pharmacopoeia monographs for comprehensive safety information, including risk of initial testosterone flare in oncology settings, bone density loss with prolonged use, and hypersensitivity reactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (99.75%) to this prediction, but the underlying evidence base is essentially absent — there are no clinical trials and only one tangentially related case report that does not assess buserelin's efficacy. More critically, the mechanistic link between GnRH agonism and hypertrichosis is conceptually fragile: hypertrichosis is a non-androgen-dependent condition, making the biological rationale for this repurposing direction weak. This prediction is assessed as a likely knowledge graph false positive arising from semantic adjacency between the GnRH pathway and hair-related phenotypes.

**To proceed, the following would be needed:**

- **Mechanistic validation:** Establish whether any subtype of hypertrichosis has a demonstrable androgen or GnRH-axis component that could respond to buserelin
- **Preclinical data:** In vitro or animal model evidence showing buserelin's effect on non-androgen-dependent hair follicle biology
- **Clinical case series or observational data:** Documented observations of hypertrichosis improvement in patients receiving buserelin for other indications (e.g., prostate cancer, endometriosis)
- **MOA clarification:** Full DrugBank mechanism-of-action data to rule in or out any non-GnRH effects relevant to hair biology
- **Regulatory data:** Obtain Canadian product monograph or equivalent safety documentation if clinical investigation is considered

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

