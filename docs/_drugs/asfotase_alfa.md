---
layout: default
title: Asfotase Alfa
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Asfotase Alfa: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies (evidence level L5). Approved use: Hypophosphatasia"
monitor_inn: "Asfotase alfa"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Steel syndrome", "exocrine pancreatic insufficiency", "Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "familial apolipoprotein C-II deficiency", "esophageal varices with bleeding", "esophageal varices without bleeding", "cystinosis"]
---

# Asfotase Alfa
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

## Asfotase alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies
{: .text-alpha }

## One-Sentence Summary

Asfotase alfa is an enzyme replacement therapy originally used to treat hypophosphatasia.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypophosphatasia |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for asfotase alfa: "HPP is caused by a deficiency in TNSALP enzyme activity, which leads to elevations in several TNSALP substrates, including inorganic pyrophosphate (PPi). TNSALP is a metallo-enzyme that catalyzes the hydrolysis of phosphomonoesters with release of inorganic phosphate and alcohol." ([DailyMed: Strensiq (asfotase alfa) prescribing information, Alexion Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3387574f-5eaa-4501-a71d-4cbfbd563031), label version 2025-12-12; accessed 2026-11-19.) Based on known information, asfotase alfa is a recombinant tissue-nonspecific alkaline phosphatase (TNAP) enzyme replacement. It breaks down inorganic pyrophosphate (PPi), pyridoxal-5'-phosphate (PLP) and phosphoethanolamine, which supports bone mineralization in hypophosphatasia.

Mitochondrial oxidative phosphorylation disorders arise from defects in cellular energy metabolism. The TNAP mechanism does not address these defects, so no clear mechanistic link was identified. The high score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis, not as evidence of efficacy.

**Other predictions reviewed (all L5, all Hold):**

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Steel syndrome | 0.9991 | Collagen XXVII defect; TNAP replacement does not correct it. Only a loose skeletal-phenotype overlap. |
| 3 | Exocrine pancreatic insufficiency | 0.9989 | Only an "enzyme replacement" similarity learned by the TxGNN model (deep learning); no digestive enzyme activity. |
| 4 | Scheie syndrome | 0.9985 | Alpha-L-iduronidase deficiency is not addressed. |
| 5 | Hurler syndrome | 0.9975 | Approved therapies differ; no target relevance. |
| 6 | Lysosomal storage disease with skeletal involvement | 0.9973 | Different pathology from the PPi-mediated mineralization defect. |
| 7 | Familial apolipoprotein C-II deficiency | 0.9971 | No known effect on lipoprotein metabolism. |
| 8–9 | Esophageal varices (with / without bleeding) | 0.9968 | Portal hypertension; no plausible link. Identical scores suggest a shared ontology-based prediction. |
| 10 | Cystinosis | 0.9965 | Cystine transport defect; only a superficial renal and bone overlap. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02444623 | STRENSIQ | Not specified | Not specified |
| 02444615 | STRENSIQ | Not specified | Not specified |
| 02444631 | STRENSIQ | Not specified | Not specified |
| 02444658 | STRENSIQ | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, and the mechanism of asfotase alfa (TNAP enzyme replacement for bone mineralization) does not address mitochondrial energy metabolism defects. The high TxGNN score alone is not sufficient to justify moving forward. The other nine top-ranked predictions are likewise unsupported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A plausible biological rationale linking TNAP replacement to mitochondrial OXPHOS disorders, such as preclinical or mechanistic studies
- Any clinical or observational evidence (trials, case reports) in the predicted indication
- Route and dosage-form compatibility assessment for the new indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Strensiq (asfotase alfa) prescribing information, Alexion Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3387574f-5eaa-4501-a71d-4cbfbd563031) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

