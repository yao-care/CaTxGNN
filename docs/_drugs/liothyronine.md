---
layout: default
title: Liothyronine
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "Liothyronine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "angiomyxoma", "myxoma", "hypotrichosis simplex of the scalp"]
description: "Liothyronine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). In Canada: 8 DINs (8 marketed)"
---

# Liothyronine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Liothyronine: Renal hypodysplasia/aplasia
{: .text-alpha }

## One-Sentence Summary

Liothyronine is a synthetic thyroid hormone (T3) originally used to treat hypothyroidism and other thyroid diseases such as goiter and thyroid cancer.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but this is a TxGNN model (deep learning) prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 8) |
| Number of DINs | 8 (marketed: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for liothyronine: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3), label version 2026-05-18; accessed 2026-11-19.) Based on known information, liothyronine is the active form of thyroid hormone (triiodothyronine). Its efficacy in replacing thyroid hormone in hypothyroidism is well established, and mechanistically it might be relevant to renal hypodysplasia/aplasia.

Thyroid hormone is known to play a role in organ development, including the kidney, which is the only biological link suggested by the data compiled for this report. However, no trial or publication supports this link. The very high TxGNN score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or demonstrated clinical benefit.

Renal hypodysplasia/aplasia is a structural congenital malformation. It is difficult to see how an adult-type thyroid hormone replacement could reverse a developmental defect, so the prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern. Bilateral renal agenesis and Potter sequence are closely related renal terms. Carney complex, angiomyxoma and myxoma form another cluster. Peripheral dysostosis and acrodysostosis form a third. Nodular goiter is already within the drug's labelled thyroid indications, so it is not a true repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for renal hypodysplasia/aplasia.

(The literature retrieved for other predicted indications was found through the drug name and does not address this disease, so it is not listed here.)

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01919458 | CYTOMEL | Not specified | Not specified |
| 01919466 | CYTOMEL | Not specified | Not specified |
| 02494337 | TEVA-LIOTHYRONINE | Not specified | Not specified |
| 02494345 | TEVA-LIOTHYRONINE | Not specified | Not specified |
| 02549999 | AURO-LIOTHYRONINE | Not specified | Not specified |

Eight valid single-ingredient licences are held in total; the five shown above are the main ones.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
- Cardiovascular: hypertension, coronary artery disease, myocardial infarction
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, and hypopituitarism or pituitary hormone deficiency (including Sheehan syndrome and Kallmann syndrome)
- Bone: osteoporosis, postmenopausal osteoporosis
- Other: thymus gland disease

**Drug Interactions:** 100 interactions were recorded. All 20 shown in the data are of Moderate severity. Main groups:
- Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide, linagliptin)
- Proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole)
- Calcium and magnesium products (calcium phosphate, calcium acetate, magnesium oxide)
- Sympathomimetics (epinephrine, isometheptene, diethylpropion)

Please also refer to the package insert for warnings and contraindications, because label-based safety data have not yet been compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model (deep learning) score (Evidence Level L5). There are no clinical trials or disease-specific publications. Renal hypodysplasia/aplasia is a congenital structural malformation, so a therapeutic role for thyroid hormone replacement is biologically doubtful.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data for liothyronine (for example from DrugBank)
- Preclinical or epidemiological evidence linking thyroid hormone signalling to renal development or renal agenesis
- Indication text, dosage forms and manufacturers for the Canadian licences
- A review of whether another predicted indication with more indirect evidence deserves priority over this one

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

