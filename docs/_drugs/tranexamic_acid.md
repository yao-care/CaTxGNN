---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 923
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Tranexamic Acid: From Antifibrinolytic Use to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic medicine marketed in Canada as injection and tablet products, and it is generally used to reduce bleeding.
The TxGNN model predicts it may be relevant to **amenorrhea**, but there are **0 clinical trials** and only **2 indirect review publications** behind this prediction.
The link is probably a knowledge-graph association with menstrual disorders, not a real therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records provided |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 (as assigned in the Evidence Pack; only indirect narrative reviews, no trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Tranexamic acid is known as an antifibrinolytic that reduces blood loss, including menstrual blood loss. It does not suppress ovulation or the endometrial cycle.

Amenorrhea means the absence of menstruation, which is a different outcome from reducing bleeding. The two retrieved publications cover abnormal uterine bleeding and menses suppression in general. In those settings, tranexamic acid is likely discussed as an adjunct for bleeding reduction, while amenorrhea is achieved with hormonal agents.

The 99.19% score therefore most likely reflects a link between tranexamic acid and menstrual disorders in the knowledge graph. The mechanism does not support inducing amenorrhea, so the prediction should be treated with caution. A more plausible related direction is heavy or abnormal menstrual bleeding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based overview of drug therapy for abnormal uterine bleeding. Nonhormonal options such as NSAIDs reduce bleeding by about 25–35%. Choice of therapy depends on cause, bleeding amount, contraception needs, and side effects. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in premenopausal women with blood cancers. Notes that data comparing these therapies are scarce. The full text was not available, so the study type and content could not be fully confirmed. |

Both papers address menstrual bleeding control in general. Neither shows that tranexamic acid induces amenorrhea.

---

## Canada Market Information

Five of the 12 authorizations are shown below. Dosage form and approved indication text were not provided for these products.

| DIN | Product Name |
|---------|------|
| 02246365 | Tranexamic Acid Injection BP |
| 02409097 | GD-Tranexamic Acid |
| 02466015 | Tranexamic Acid Injection |
| 02531208 | Tranexamic Acid Injection |
| 02401231 | Tranexamic Acid Tablets |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is high, but it is a model prediction with no clinical trial support. The mechanism (reducing bleeding) does not explain amenorrhea, and the two retrieved reviews are only indirectly related. The study of tranexamic acid in menstrual bleeding is better framed as heavy menstrual bleeding than as amenorrhea.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (required before any safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- Full text of the 2024 review (PMID 39043214) to confirm its content and study type
- A re-examination of whether heavy menstrual bleeding, rather than amenorrhea, is the more appropriate target indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

