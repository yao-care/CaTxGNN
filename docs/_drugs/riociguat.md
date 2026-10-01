---
layout: default
title: Riociguat
parent: Model Prediction Only (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Riociguat is a soluble guanylate cyclase (sGC) stimulator marketed in Canada, and the pack's rationale text places it in pulmonary arterial hypertension (PAH).
The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-growth disorder.
**No clinical trials and no publications** support this prediction, so it is a model output only and likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (taken from the pack's rationale text; the Canadian licence records contain no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 94.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Riociguat is described as an sGC stimulator that restores NO-sGC-cGMP signaling, which causes pulmonary vasodilation and antiproliferative effects. Its efficacy in PAH is the basis for its marketed use.

The supplied data show **no plausible pathway** linking sGC stimulation to a congenital hair-growth disorder. The high score most likely reflects graph proximity to other hypertrichosis-related entries rather than a true therapeutic signal. The same applies to the other hair and malformation predictions (rank 3 to 5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02533588 | SANDOZ RIOCIGUAT |
| 02533561 | SANDOZ RIOCIGUAT |
| 02412764 | ADEMPAS |
| 02533618 | SANDOZ RIOCIGUAT |
| 02533596 | SANDOZ RIOCIGUAT |

Five of the 10 DINs are listed above. Dosage form and approved indication text are not available in the records.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no mechanistic plausibility. It should not be pursued as a repurposing candidate on this evidence.

**Other predictions in the same run:**
Two PAH subtypes have much stronger support and are rated "Proceed with Guardrails" (L1):
- **PAH associated with congenital heart disease (rank 6, score 92.58%):** supported by a post hoc subgroup analysis of the Phase 3 PATENT-1/2 trials (PMID 26135803). The subgroup is small, and Eisenmenger/shunt physiology and specialist PAH-centre management need attention.
- **PAH associated with connective tissue disease (rank 10, score 91.55%):** supported by a prospectively planned subgroup analysis of PATENT-1 (PMID 27457511) and open-label switching data from a PDE5 inhibitor (PMID 28671485). Riociguat must not be combined with PDE5 inhibitors or nitrates.

Both fall within the already approved PAH (Group 1) population, so they are closer to extensions of the existing indication than to new repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text, dosage forms and manufacturers for the Canadian licences
- For the Ambras prediction: any disease-specific mechanistic or preclinical evidence, without which it should stay on hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

