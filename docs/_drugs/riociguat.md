---
layout: default
title: Riociguat
parent: Model Prediction Only (L5)
nav_order: 811
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

Riociguat is originally used to treat pulmonary arterial hypertension (PAH) and chronic thromboembolic pulmonary hypertension (CTEPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital hair disorder.
This prediction currently has **no clinical trials and no publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension; chronic thromboembolic pulmonary hypertension |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 94.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Riociguat is generally known as a soluble guanylate cyclase (sGC) stimulator. It sensitises sGC to endogenous nitric oxide and raises cGMP, which relaxes pulmonary vessels and slows vascular remodelling. Its efficacy in PAH and CTEPH is established.

The link to the predicted indication is weak. Ambras syndrome is a genetic disorder of hair growth, and no established connection exists between NO-sGC-cGMP signalling and its underlying cause. The high score comes from relationships in the knowledge graph, not from biological or clinical evidence.

Some vasodilators, such as minoxidil, are known to cause excess hair growth. If anything, this hints at a possible side-effect signal rather than a treatment benefit. This is speculative, and no data support it here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 10 valid single-ingredient authorisations for riociguat (5 shown below). Dosage form and approved indication text were not available in the compiled data.

| DIN | Product Name |
|---------|------|
| 02533588 | SANDOZ RIOCIGUAT |
| 02533561 | SANDOZ RIOCIGUAT |
| 02412764 | ADEMPAS |
| 02533618 | SANDOZ RIOCIGUAT |
| 02533596 | SANDOZ RIOCIGUAT |

---

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified. The 20 listed in the compiled data are all rated Moderate:
  - Proton pump inhibitors: omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
  - Antacids and mineral products: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Others: clarithromycin, dexamethasone, mannitol, papaverine

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and no plausible mechanism links sGC stimulation to this congenital hair disorder. The possible hypertrichosis signal from vasodilators further argues against pursuing it.

**To proceed, the following is needed:**
- Confirmation of any biological link between the NO-sGC-cGMP pathway and the genetic basis of Ambras syndrome
- Mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications
- Any preclinical or case-level evidence in this condition

**Note on other predictions:**
Two lower-ranked predictions have real supporting literature, but both are subgroups of the already approved PAH class, so they are not true repurposing.
- **PAH associated with connective tissue disease** is rated L2, with a proposed recommendation of Proceed with Guardrails. It is supported by PATENT-1 subgroup analyses (PMID 27457511), a 2024 systematic review and a 2025 prospective observation study.
- **PAH associated with congenital heart disease** is rated L3, supported by a PATENT-1/2 subgroup analysis (PMID 26135803).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

