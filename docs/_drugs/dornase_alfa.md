---
layout: default
title: Dornase Alfa
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase alfa: From Cystic Fibrosis to Paroxysmal Hemicrania

## One-Sentence Summary

Dornase alfa (recombinant human DNase I, marketed in Canada as PULMOZYME) cleaves extracellular DNA, for example in airway secretions rich in neutrophil extracellular traps (NETs).
The TxGNN model lists **paroxysmal hemicrania** as its top predicted new indication, but with a score of only **50%**, which is uninformative, and **0 clinical trials** and **0 publications** support it.
This is a model-only prediction with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian record (Pulmozyme is generally known for cystic fibrosis, per general knowledge rather than the Evidence Pack) |
| Predicted New Indication | Paroxysmal hemicrania |
| TxGNN Prediction Score | 50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Based on known information, dornase alfa is a recombinant human DNase I that breaks down extracellular DNA. Its established use is in thick, DNA-rich airway secretions.

The prediction is difficult to support mechanistically. Paroxysmal hemicrania is an indomethacin-responsive trigeminal autonomic headache disorder involving trigeminal-autonomic and hypothalamic circuits. No extracellular-DNA component is known. The TxGNN score of 0.5 (rank 1,924,906) carries no discriminating information, so this is a weak graph-based association.

The other nine predictions look similar. All have a score of 0.5, evidence level L5 and a "Hold" recommendation:

| Rank | Predicted Indication | Mechanistic Assessment |
|------|------|------|
| 2 | Xanthoma disseminatum | No established link; DNase mechanism is speculative |
| 3 | Xanthogranuloma | No established link; extrapolation from inflammatory-cell and NET biology only |
| 4 | Benign cephalic histiocytosis | No established link; graph association only |
| 5 | Generalized eruptive histiocytosis | No established link |
| 6 | Langerhans cell histiocytosis | Speculative only; extracellular DNA and NETs could be a secondary inflammatory contributor, but standard therapy targets the MAPK pathway |
| 7 | Trigeminal autonomic cephalalgia | No plausible link |
| 8 | Phacolytic glaucoma | No established link; the process is protein-driven and treated surgically |
| 9 | Congenital epulis | No established link; treated by surgical excision |
| 10 | Necrobiotic xanthogranuloma | Speculative only; necrobiosis could theoretically involve extracellular DNA |

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
| 2046733 | PULMOZYME |

Dosage form, manufacturer and approved indication text are not available in the retrieved record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on an uninformative model score (0.5) with no clinical, preclinical or literature support. No plausible mechanistic link to paroxysmal hemicrania was identified.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text and dosage form for the Canadian license
- Any preclinical or clinical evidence linking DNase activity to the predicted disease
- Route compatibility assessment (available and required routes are currently unassessed)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

