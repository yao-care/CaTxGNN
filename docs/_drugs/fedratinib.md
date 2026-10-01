---
layout: default
title: Fedratinib
parent: Model Prediction Only (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib is a JAK2-selective kinase inhibitor, marketed in Canada as INREBIC and generally used for myelofibrosis.
The TxGNN model predicts it may be effective for **benign PEComa** with a very high score (99.84%), but the prediction currently has **0 clinical trials** and **0 publications** behind it.
It rests on model output alone, and the mechanistic link is speculative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelofibrosis (general knowledge of fedratinib's labelling; the Evidence Pack contains no approved-indication text) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% (model rank 3847) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, fedratinib is a JAK2-selective inhibitor with additional activity against FLT3 and BRD4. Its efficacy in myelofibrosis comes from suppressing JAK/STAT signaling.

The link to PEComa is weak. PEComa biology is driven mainly by loss of TSC1/2 and hyperactivation of mTOR, and mTOR inhibitors are the established approach. Any connection to fedratinib would be indirect, through crosstalk between the JAK/STAT and mTOR pathways. The high score likely reflects similarity in the knowledge-graph neighbourhood rather than a validated mechanism.

The other nine top predictions do not strengthen the case:
- Lymphangiomyoma, uterine PEComa and lymphangioleiomyomatosis are in the same TSC/mTOR family, where JAK2 dependency is not established.
- The two rhabdoid tumor predictions are correlated with each other and rest only on hypothetical BRD4-related epigenetic effects.
- The two hemophagocytic syndromes carry an identical score, so they are not independent evidence. They are the most mechanistically plausible, because JAK/STAT drives their cytokine storm, but no fedratinib-specific data were supplied.

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
| 2502445 | INREBIC |

Dosage form, manufacturer and approved-indication text were not supplied for this authorization.

---

## Safety Considerations

- **Key Warning (from the mechanism notes, not a package-insert extract)**: Fedratinib carries a boxed warning for encephalopathy, including Wernicke's encephalopathy. This would need careful weighing in critically ill patients, such as those with hemophagocytic syndromes.

Please refer to the package insert for full warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. No trials or publications exist, and the disease biology (mTOR-driven) does not point to JAK2 inhibition. The drug also has a significant toxicity profile, so there is no basis to advance.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence, such as cell-line or animal data, for fedratinib in PEComa or another top-ranked disease
- A literature and trial search extended to JAK inhibitor class effects, especially for hemophagocytic lymphohistiocytosis, which is the most plausible of the ten predictions
- Route compatibility and similarity-to-original-indication assessments, both still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

