---
layout: default
title: Siponimod
parent: Model Prediction Only (L5)
nav_order: 845
evidence_level: L5
indication_count: 10
---

# Siponimod
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

# Siponimod: From Multiple Sclerosis to Pulmonary Hypertension

## One-Sentence Summary

Siponimod (brand name MAYZENT) is a sphingosine-1-phosphate (S1P) receptor modulator. It is known as a multiple sclerosis treatment, though the Canadian licence records supplied here list no approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied licence data (multiple sclerosis is inferred from the literature) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.68% (rank 6,602) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Siponimod belongs to the S1P receptor modulator class, which acts on S1P1 and S1P5 receptors. Based on the literature, it is used in multiple sclerosis, and its mechanism could in principle be relevant to pulmonary hypertension.

S1P signaling affects both vascular and immune biology, so a link to pulmonary hypertension is conceivable. However, the supplied data show no such link, and any rationale remains speculative.

The class also carries bradyarrhythmia and atrioventricular-conduction warnings. A cardiopulmonary indication would therefore need a dedicated safety review before any further consideration. A high TxGNN score is not evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Candidates

Several lower-ranked predictions have some indirect literature. None has trial data.

| Rank | Predicted Indication | Score | Evidence Level | Decision | Note |
|------|------|------|------|------|------|
| 2 | Migraine disorder | 99.66% | L4 | Research Question | One 2022 case report/commentary ([PMID 35382764](https://pubmed.ncbi.nlm.nih.gov/35382764/)) discusses migraine alongside interferon β1a and siponimod. Its type was inferred from the title and the full text was not reviewed. |
| 7 | Rheumatoid arthritis | 99.16% | L4 | Research Question | A 2021 review of S1P signaling in immune-mediated diseases ([PMID 33983615](https://pubmed.ncbi.nlm.nih.gov/33983615/)) gives a coherent but indirect rationale. No RA-specific efficacy data were found. |
| 4, 5 | Migraine with brainstem aura; migraine susceptibility | 99.56%; 99.49% | L5 | Hold | The only relevant paper concerns migraine in general. The 20 papers retrieved for rank 5 are mostly epilepsy genetics and reflect keyword matching, not evidence of benefit. |
| 3, 6, 8, 9, 10 | Kyphoscoliotic heart disease, Prinzmetal angina, atrophoderma vermiculata, ulerythema ophryogenesis, myelodysplastic syndrome | 98.79–99.56% | L5 | Hold | No trials or literature and no evident mechanism. Siponimod's cardiac conduction warnings and lymphopenia effect are cautions for the cardiac and bone-marrow indications. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2496429 | MAYZENT |
| 2496437 | MAYZENT |

---

## Safety Considerations

Please refer to the package insert for safety information.

Class-level caution: S1P modulators carry bradyarrhythmia and atrioventricular-conduction warnings, and they cause lymphopenia. Both would need specific review for any cardiopulmonary indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction scores high (99.68%) but has no clinical trials, no literature and no identified mechanism. It remains at Evidence Level L5 and Decision Stage S0. Cardiac conduction warnings add further caution for a cardiopulmonary use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from the DrugBank API, to test the S1P-to-pulmonary-vascular link
- The Canadian approved indication, dosage form and manufacturer for each DIN
- A targeted literature search on S1P modulation in pulmonary vascular disease
- Full-text review of PMID 35382764 if the migraine direction is pursued, since migraine and rheumatoid arthritis are the more evidence-supported candidates (both L4, Research Question)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

