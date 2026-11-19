---
layout: default
title: Granisetron
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). In Canada: 3 DINs (3 marketed)"
---

# Granisetron
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

## Granisetron: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist that is marketed in Canada. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but this is a computational prediction only: **0 clinical trials** and **0 publications** were found to support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for granisetron: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), label version 2026-04-30; accessed 2026-11-19.) Granisetron is generally known as a selective 5-HT3 receptor antagonist.

One hypothesis is that modulating 5-HT3 receptors could influence the dopaminergic and serotonergic signaling involved in mood regulation. This is a speculative link. No direct clinical evidence was found, and the high score (0.9962) reflects a network-based computational prediction rather than demonstrated efficacy.

Because the original indication is not listed in the available regulatory data, the relationship between the original and new indications cannot be assessed here.

Other top-ranked predictions include Tourette syndrome (0.9952) and trichotillomania (0.9923), which have a more plausible serotonergic and dopaminergic rationale. Several others, such as acute contagious conjunctivitis, nephrogenic syndrome of inappropriate antidiuresis and bronchitis, have no clear mechanistic basis and are likely network artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02322765 | GRANISETRON HYDROCHLORIDE INJECTION | Not specified | Not specified |
| 02452359 | NAT-GRANISETRON | Not specified | Not specified |
| 02308894 | APO-GRANISETRON | Not specified | Not specified |

All three authorizations are valid single-ingredient products.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not from label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest, heart conduction disease. These point to a cardiac conduction/QT concern.
- **Drug Interactions**: The query found 100 interactions in total. Examples from the 20 reviewed:
  - **Major**: fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide
  - **Moderate**: abametapir, abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol
  - The major interactions suggest particular attention to QT-prolonging drugs and serotonergic drugs.

Please refer to the package insert for warnings and contraindications, as label data was not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the mechanism data is missing, and the mechanistic link to manic bipolar affective disorder is speculative. Cardiac (QT-related) signals and many interactions with serotonergic and QT-prolonging drugs also call for caution in a psychiatric population.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication and dosage form details for the Canadian products
- Preclinical or clinical evidence for 5-HT3 antagonism in mood disorders
- Comparison of the predicted indications with better-supported candidates, such as Tourette syndrome and trichotillomania

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

