---
layout: default
title: Levomilnacipran
parent: Model Prediction Only (L5)
nav_order: 540
evidence_level: L5
indication_count: 6
---

# Levomilnacipran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Levomilnacipran: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Levomilnacipran (marketed in Canada as FETZIMA) is a serotonin-norepinephrine reuptake inhibitor (SNRI) used to treat major depressive disorder (MDD) in adults.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but there are **0 clinical trials** and **0 publications** for this indication. The high score is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder in adults (from the literature; the Canadian licence records in the pack have no indication text) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. The literature describes levomilnacipran as an SNRI, and it is approved for MDD in adults. It inhibits norepinephrine reuptake with about twice the potency of its serotonin reuptake inhibition. Its efficacy in MDD is supported by systematic reviews and network meta-analyses.

**This prediction is not mechanistically plausible.** Benign paroxysmal torticollis of infancy is a self-limiting infantile condition, usually linked to CACNA1A channelopathy. Monoamine reuptake inhibition has no known effect on this pathophysiology, and no link to MDD or to the drug's mechanism was found. The high score (rank 8,819 in the model) likely reflects a knowledge-graph artifact rather than real biology.

The condition also affects infants, and levomilnacipran is not established in pediatric patients. Antidepressants carry a suicidality warning in young people.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Worth Noting

The model's other top predictions are more relevant to levomilnacipran's known use. None has an indication-specific trial.

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Agoraphobia | 99.53% | L5 | Class-level rationale only, since other SNRIs are used in panic and anxiety disorders. No trials or literature. |
| Dysthymic disorder | 99.24% | L5 | Biologically plausible, but MDD efficacy cannot be extrapolated without direct data. |
| Melancholia | 99.20% | L4 | A severe MDD subtype. Supported indirectly by MDD reviews and by preclinical models of neuroinflammation and synaptic plasticity, with 20 publications retrieved. Largely a label-scope question, not true repurposing. |
| Neurotic depression | 99.20% | L4 | An obsolete term that maps to dysthymia or milder depression. It should be re-mapped to a current diagnosis before evaluation. |
| Neurotic disorder | 99.19% | L5 | An obsolete, non-specific category. Too broad to evaluate. |

## Canada Market Information

Indication text, dosage form and manufacturer are not recorded in the licence data.

| DIN | Product Name |
|---------|------|
| 02440989 | FETZIMA |
| 02441004 | FETZIMA |
| 02440970 | FETZIMA |
| 02440997 | FETZIMA |

## Safety Considerations

- **Pediatric use**: Levomilnacipran is not established in pediatric patients, and this prediction concerns infants. Antidepressants carry a suicidality warning in young people.
- No drug interaction records were found.

Please refer to the Health Canada product monograph for full warnings, contraindications and interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link. The target condition is a self-limiting infantile disorder in a population where the drug is not established. The safety documentation for the Canadian product is also incomplete.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications
- Mechanism of action data from DrugBank
- A biological rationale connecting SNRI pharmacology to CACNA1A-related channelopathy, if this indication is to be pursued at all
- For the depression-related candidates (melancholia, neurotic depression, dysthymic disorder), re-map obsolete terms to current diagnoses and treat them as research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

