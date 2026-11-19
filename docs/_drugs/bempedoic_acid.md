---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 9
monitor_inn: "Bempedoic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
last_modified_at: 2026-11-05
description: "Bempedoic Acid: predicted new indication hyperthyroidism (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Bempedoic Acid
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

## Bempedoic acid: ATP-citrate lyase inhibitor → hyperthyroidism
{: .text-alpha }

## One-Sentence Summary

Bempedoic acid is an oral lipid-lowering drug that inhibits ATP-citrate lyase (ACL) and is marketed in Canada as NILEMDO.
The TxGNN model predicts it may be relevant to **hyperthyroidism**, but this is a model prediction only,
with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperthyroidism |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bempedoic acid: "Bempedoic acid is an adenosine triphosphate-citrate lyase (ACL) inhibitor that lowers LDL-C by inhibition of cholesterol synthesis in the liver. ACL is an enzyme upstream of 3-hydroxy-3-methyl-glutaryl-coenzyme A (HMG-CoA) reductase in the cholesterol biosynthesis pathway." ([DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9), label version 2026-06-25; accessed 2026-11-19.) From general pharmacology, bempedoic acid inhibits ACL, an enzyme upstream of HMG-CoA reductase in hepatic cholesterol synthesis, and thereby lowers LDL cholesterol.

No clear mechanistic link to hyperthyroidism has been identified. Thyroid hormone status influences lipid metabolism, but that does not imply that an ACL inhibitor would treat excess thyroid hormone production. The high score is a model-based prediction only and is not backed by any trial or publication. The prediction should be treated as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02562782 | NILEMDO | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 23 interactions were recorded in total; the 20 listed in the compiled data include:
  - **Major**: systemic corticosteroids (hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, deflazacort, fludrocortisone), levofloxacin, and simvastatin.
  - **Moderate**: rosuvastatin, empagliflozin, glyburide, repaglinide, rifaximin, selexipag, fexofenadine, and revefenacin.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trials or publications address hyperthyroidism, and no plausible mechanistic link exists, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking ACL inhibition to thyroid hormone excess
- Any clinical or observational data on bempedoic acid in thyroid disease
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data and a review of the interaction profile

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

