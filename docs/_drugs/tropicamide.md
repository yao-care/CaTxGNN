---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 946
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Ophthalmic Pupil Dilation to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a topical eye-drop medicine, originally used to dilate the pupil (mydriasis) for eye examinations.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic mydriasis (pupil dilation), topical use. The licence records contain no indication text. |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on class knowledge, tropicamide is a muscarinic antagonist (anticholinergic). It is marketed only as a topical ophthalmic mydriatic.

The link to cauda equina syndrome is weak. Cauda equina syndrome is a structural, surgical emergency. An antimuscarinic could at most ease secondary bladder symptoms, not the underlying nerve compression. Systemic exposure from eye drops is also too low to support this use. The high score is most likely a knowledge-graph proximity artifact rather than a real therapeutic signal.

The two next-ranked predictions are also supported only by the model:

- **Neurogenic bladder (score 99.13%)**: Muscarinic antagonists such as oxybutynin are established therapy, so the class mechanism is plausible. However, tropicamide has no systemic or intravesical formulation and no pharmacokinetic data for this use. The disease term is flagged obsolete in the ontology and should be re-mapped to a current neurogenic lower urinary tract dysfunction term. Established antimuscarinics already exist, so the added value is doubtful.
- **Irritable bowel syndrome (score 99.12%)**: Anticholinergic antispasmodics such as dicyclomine and hyoscyamine are used for IBS cramping. Tropicamide has no oral or systemic formulation, its safety in this setting is unknown, and it has no clear advantage over existing agents.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 981 | MYDRIACYL |
| 622885 | ODAN-TROPICAMIDE |
| 1007 | MYDRIACYL |
| 2148536 | MINIMS TROPICAMIDE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no trials or publications. Tropicamide is only available as a topical eye drop, and cauda equina syndrome is a structural, surgical emergency that an antimuscarinic would not treat.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- A pharmacological rationale for tropicamide over existing antimuscarinics, with data on any systemic or intravesical formulation
- Re-mapping of the obsolete neurogenic bladder term to a current ontology term before any further assessment of that candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

