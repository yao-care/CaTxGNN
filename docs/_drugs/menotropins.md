---
layout: default
title: Menotropins
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Menotropins
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

# Menotropins: From Infertility Treatment to Peptic Esophagitis

## One-Sentence Summary

Menotropins is a gonadotropin preparation (FSH/LH activity) used in fertility treatment, marketed in Canada as MENOPUR.
The TxGNN model predicts it may be effective for **peptic esophagitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no plausible mechanism identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data; menotropins is generally used for ovarian stimulation in infertility |
| Predicted New Indication | Peptic esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, menotropins is a gonadotropin product with FSH and LH activity, used to stimulate the ovaries. Its efficacy in fertility treatment is established, but that does not extend to the esophagus.

The current assessment finds no plausible mechanism linking gonadotropin activity to esophageal mucosal injury or acid reflux. The high score (0.984) is a graph-based prediction only, and it most likely reflects a graph-neighborhood artifact rather than a real biological signal.

The other top predictions (esophageal disease, esophageal ulcer, esophageal malformation, and a cluster of cardiac conduction disorders) show the same pattern. None has any supporting trial or literature, so they should not be read as independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For reference, the only literature item found among all the predictions is a 1987 report of Raynaud's phenomenon in infertile women treated with bromocriptine (PMID [3117594](https://pubmed.ncbi.nlm.nih.gov/3117594/)). It concerns a different drug and a different predicted disease, so it is not evidence for menotropins in peptic esophagitis.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2283093 | MENOPUR |

Dosage form and approved indication text were not available in the input.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for menotropins in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials or publications, and no plausible mechanism links a gonadotropin to peptic esophagitis. The evidence level is L5, and the safety data needed for screening is missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Approved indication text and dosage form for the MENOPUR licence
- Any independent preclinical or clinical evidence showing a biological link between FSH/LH activity and esophageal mucosal disease
- Confirmation of route compatibility, which is currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

