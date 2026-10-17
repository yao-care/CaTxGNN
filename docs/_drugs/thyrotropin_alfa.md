---
layout: default
title: Thyrotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Thyrotropin Alfa: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the available Canadian license data"
monitor_inn: "Thyrotropin alfa"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
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

# Thyrotropin alfa: From Its Original Use to Migraine Disorder

## One-Sentence Summary

Thyrotropin alfa (Thyrogen) is a recombinant thyroid-stimulating hormone (TSH) that is marketed in Canada, but the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on a graph-based model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Canadian license data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thyrotropin alfa is a recombinant form of human TSH, so it would be expected to act by stimulating the TSH receptor on thyroid tissue. The indication text for its Canadian license is also empty, so the original indication cannot be confirmed from the data compiled for this report.

No established mechanism links TSH receptor stimulation to migraine. The very high TxGNN score (99.98%, rank 691) reflects associations in a knowledge graph, not clinical or mechanistic evidence. The lack of any trial or publication means the prediction is a hypothesis only.

The other top predictions are similarly unsupported. Several are subtypes or variants of migraine (migraine with brainstem aura, migraine susceptibility), which probably inherit the same graph signal rather than add independent evidence. Others, such as Raynaud disease, pulmonary hypertension and postural orthostatic tachycardia syndrome, have only speculative, indirect links. The prediction of hyperthyroidism is biologically implausible, since TSH receptor stimulation would be expected to worsen it.

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
| 02246016 | THYROGEN | Not stated | Not stated |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening completed and found 45 interactions in total. The 20 listed in the data compiled for this report are all rated Moderate. They are almost all with glucose-lowering drugs, including:
  - Metformin
  - Acarbose
  - Sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide)
  - DPP-4 inhibitors (alogliptin, saxagliptin)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - GLP-1 receptor agonists (albiglutide, dulaglutide, exenatide, semaglutide)
  - Insulins (human, aspart)

  Blood glucose control may need closer monitoring in patients using these drugs.
- **Theoretical concern**: Exogenous TSH can transiently raise thyroid hormone levels and heart rate. This is relevant to the predicted indications of postural orthostatic tachycardia syndrome and hyperthyroidism, where it could cause harm rather than benefit.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, publications or established mechanism. The original indication and mechanism of action are also missing from the data compiled for this report, and the package insert safety information has not been reviewed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication and the dosage form for DIN 02246016
- Mechanism of action data, for example from DrugBank
- A literature and trial search to find any link between thyroid or TSH signalling and migraine
- A mechanistic rationale for why TSH receptor agonism could help migraine, which is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

