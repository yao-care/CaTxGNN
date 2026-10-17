---
layout: default
title: Ziprasidone
parent: Model Prediction Only (L5)
nav_order: 994
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ziprasidone: predicted new indication Trichotillomania (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "ZIPRASIDONE"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
---

# Ziprasidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ziprasidone: From Schizophrenia and Bipolar Disorder to Trichotillomania

## One-Sentence Summary

Ziprasidone is an atypical antipsychotic originally used for schizophrenia and bipolar disorder (including manic episodes).
The TxGNN model predicts it may be effective for **trichotillomania** (compulsive hair pulling), but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; bipolar disorder (including manic episodes). The Canadian licence records contain no indication text, so this comes from the TxGNN knowledge graph. |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ziprasidone is generally known to block dopamine D2 and serotonin 5-HT2A receptors. Both pathways are involved in repetitive and compulsive behaviours, which are the core features of trichotillomania. This link is plausible, but none of the data compiled for this report supports it.

Schizophrenia and bipolar disorder are psychotic and mood disorders, while trichotillomania is a repetitive-behaviour disorder. The overlap is mainly in the neurotransmitter systems involved, and nothing in the compiled data confirms that ziprasidone works in this condition. The high score reflects a pattern in the knowledge graph, not clinical proof.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ziprasidone has 8 valid single-ingredient authorizations in Canada and no cancelled ones. The records contain no dosage form or approved indication text. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02298597 | ZELDOX |
| 02298619 | ZELDOX |
| 02449544 | AURO-ZIPRASIDONE |
| 02449552 | AURO-ZIPRASIDONE |
| 02449579 | AURO-ZIPRASIDONE |

---

## Safety Considerations

Label warnings and contraindications from the Canadian package insert are not available in the compiled data. Please refer to the package insert for these.

- **Contraindication signals from the knowledge graph** (these are database associations, not label text): long QT syndrome and familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, orthostatic hypotension, liver failure, kidney disease, epilepsy, neutropenia, agranulocytosis, diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, obesity disorder, potassium deficiency, and several movement disorders (basal ganglia disease, focal hand dystonia, blepharospasm). The cardiac signals matter most because ziprasidone is known to prolong the QT interval.
- **Drug Interactions**: 100 interactions were found in total. The major-level interactions in the first 20 reviewed are:
  - Hydrocortisone
  - Amphotericin B (including the lipid complex)
  - Bupropion
  - Morphine

  Moderate-level examples include metformin, pioglitazone, acarbose, alogliptin, albiglutide, epinephrine, famotidine, atropine and loperamide. Because the interaction count is high, a full review is advised before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.83%), but no trials or publications support ziprasidone for trichotillomania. The pharmacological reasoning is plausible but unproven. Meanwhile, ziprasidone carries known cardiac (QT) risks and many drug interactions.

**To proceed, the following is needed:**
- A systematic literature search for ziprasidone or other D2/5-HT2A antagonists in trichotillomania and related repetitive-behaviour disorders
- Mechanism of action data to support the proposed link
- The Canadian package insert warnings and contraindications for safety screening
- A comparison against established treatments for trichotillomania
- A cardiac safety plan (QTc monitoring) and an interaction review if any study is planned

**Note on other predictions:** In the same candidate list, **major affective disorder** (rank 3) has much stronger support. It has several randomized, placebo-controlled phase 2 trials of ziprasidone as add-on or single therapy in depression and mixed states, plus systematic reviews, giving an L1 evidence level and a "Proceed with Guardrails" recommendation. **Tourette syndrome** (rank 7) has a small paediatric pilot study and guideline reviews (L3), and is considered a research question. If the aim is to find the most promising repurposing direction for ziprasidone, these two deserve priority over trichotillomania.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

