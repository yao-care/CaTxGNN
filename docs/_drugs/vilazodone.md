---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 968
evidence_level: L5
indication_count: 10
---

# Vilazodone
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

# Vilazodone: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Vilazodone is an antidepressant (a serotonin reuptake inhibitor with 5-HT1A partial agonist activity) marketed for major depressive disorder (MDD).
The TxGNN model predicts it may be effective for **dysthymic disorder** (persistent mild depression) with a score of 99.79%, but **no clinical trials and no publications** were retrieved to support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (based on the literature and rationale text; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From the pharmacology described in the retrieved material, vilazodone combines serotonin reuptake inhibition with 5-HT1A partial agonism. It was designed so that the 5-HT1A component might offset the feedback inhibition that limits the effect of conventional SSRIs.

Dysthymic disorder is a chronic, lower-intensity form of depression. It is closely related to MDD, vilazodone's established indication, and serotonergic drugs are already used across chronic depressive conditions. That makes the model's prediction biologically plausible.

However, plausibility is the only support here. No study in the retrieved data tests vilazodone specifically in dysthymia, so this remains a research question rather than a validated repurposing candidate.

**Other predictions for this drug (for context):**
- **Melancholia (rank 4)** has the strongest evidence: 1 completed Phase 4 study and about 20 publications, which yields an L1 grade. Melancholia maps to MDD, so this is effectively an on-label use rather than true repurposing, and the L1 grade rests on reviews of the pivotal RCTs. It should be confirmed against the current Canadian label.
- **Obsessive-compulsive disorder (rank 5)** has only class-level SSRI reviews and no vilazodone-specific data (L4).
- **Neurotic disorder, neurotic depression and agoraphobia** have plausible serotonergic links but no evidence.
- **Benign paroxysmal torticollis of infancy, Keppen-Lubinsky syndrome, Ohdo syndrome and schizotypal personality disorder** have no credible mechanistic link and are likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder.

---

## Literature Evidence

Currently no related literature available for dysthymic disorder.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2551810 | APO-VILAZODONE |
| 2443732 | VIIBRYD |
| 2443740 | VIIBRYD |
| 2551837 | APO-VILAZODONE |
| 2551829 | APO-VILAZODONE |

Six licences are on record in total; five are listed above. Dosage form and approved indication text were not provided for any of them.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there is no trial or literature evidence for dysthymic disorder (L5). Safety data from the Canadian label is also not yet available, so the candidate cannot move forward on current information.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications and approved indication text) to confirm the current labelled use and enable safety screening
- Detailed mechanism of action data from DrugBank
- A targeted search for trials and publications on vilazodone in dysthymia or persistent depressive disorder, using current diagnostic terms
- If the aim is to find a genuinely new use, review the OCD and anxiety-spectrum predictions, since the highest-evidence prediction (melancholia) is effectively on-label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

