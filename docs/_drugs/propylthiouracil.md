---
layout: default
title: Propylthiouracil
parent: Moderate Evidence (L3-L4)
nav_order: 780
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Propylthiouracil: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone re… (evidence level L4). Approved use: Hyperthyroidism, Graves disease, thyrotoxicosis, t…"
monitor_inn: "PROPYLTHIOURACIL"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Propylthiouracil (PTU) is an antithyroid drug originally used to treat hyperthyroidism, Graves disease, thyrotoxicosis and thyroid crisis.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but there are **0 clinical trials** and only **4 publications** (mouse models and case reports), none of which tests PTU as a treatment.
The mechanistic rationale is weak, and the high score most likely reflects network proximity to the original indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism, Graves disease, thyrotoxicosis, thyroid crisis (approved indication text is not available in the Canadian licence records) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, PTU inhibits thyroid peroxidase and reduces thyroid hormone synthesis. At high doses it also reduces peripheral conversion of T4 to T3. This underlies its use in hyperthyroidism.

In resistance to thyroid hormone beta (RTH-beta), thyroid hormone levels are high and TSH is not suppressed, because the receptor responds poorly to the hormone. Lowering hormone levels with an antithyroid drug would raise TSH further and risks goiter and over-stimulation of the thyroid. The mechanistic link is therefore weak and may be counterproductive. Case reports in the literature describe patients with RTH who were mistakenly treated with PTU for suspected thyrotoxicosis and whose goiter worsened.

The high TxGNN score most likely reflects the network closeness of RTH to hyperthyroidism-related conditions, not a real therapeutic connection.

### Other Predictions Reviewed

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Neonatal thyrotoxicosis | 99.40% | L4 | Mechanistically close to Graves disease. The evidence is mostly reviews on hyperthyroidism in pregnancy (maternal treatment), not direct neonatal treatment. It is a reasonable research question, but hepatotoxicity is a major concern in children. |
| Hyperthyroxinemia | 99.08% | L4 | This is a laboratory finding with many causes. It would need to be split into specific causes, because non-thyrotoxic forms would not benefit and could be harmed. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | Neonatal thyrotoxicosis and maternal infertility in a family with a TRβ mutation (M313T). |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocr J | Thai woman with a de novo TRβ L330S mutation. Her goiter enlarged after 9 months of PTU given for presumed thyrotoxicosis. |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Animal model (mouse) | Endocrinology | Role of TSH in thyroid carcinoma development in mice carrying a TRβ mutation. |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Animal model (mouse) | Oncogene | Thyroid hormone activates tumour cell proliferation in a mouse model of follicular thyroid carcinoma. |

None of these studies evaluates PTU as a treatment for RTH.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02523019 | PROPYLTHIOURACIL TABLETS | Not listed | Not listed |
| 02521059 | HALYCIL | Not listed | Not listed |

---

## Safety Considerations

- **Disease-related contraindication signals (from the knowledge graph, not label text)**:
  - Blood disorders: thrombocytopenia, leukopenia, pancytopenia, agranulocytosis, neutropenia and several congenital neutropenia syndromes.
  - Thyroid: hypothyroidism, myxedema, congenital hypothyroidism.
  - Liver and bilirubin: drug-induced liver injury, hyperbilirubinemia, Gilbert syndrome.
  - Lung: interstitial lung disease.
- **Drug Interactions**: 83 interacting drugs were identified. Examples:
  - Major: deferiprone.
  - Moderate: warfarin, dicoumarol, theophylline, aminophylline, oxtriphylline, naltrexone, radioactive iodide (I-131, I-123), macimorelin.
  - Many others (including corticosteroids, omeprazole, pantoprazole, rosuvastatin and clopidogrel) have no assigned severity level.
- **Pediatric and neonatal use**: The literature on neonatal thyrotoxicosis raises a significant hepatotoxicity concern for PTU.

Please refer to the Health Canada package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the literature contains only mouse models and case reports. The mechanism points the wrong way: lowering thyroid hormone in RTH would raise TSH and risk goiter. The high TxGNN score is not backed by evidence of benefit.

**To proceed, the following is needed:**
- A clear mechanistic argument for why an antithyroid drug would help in RTH-beta, or confirmation that this prediction should be dropped.
- Official Health Canada package insert warnings and contraindications, which are missing and block safety screening.
- Detailed mechanism of action data from DrugBank.
- Approved indication text and dosage forms for the two Canadian licences.
- For the lower-ranked predictions: neonatal thyrotoxicosis could be explored as a research question with a dedicated pediatric hepatotoxicity risk assessment, and hyperthyroxinemia would need to be split into specific causes before any evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

