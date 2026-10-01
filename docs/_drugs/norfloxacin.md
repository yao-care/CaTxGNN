---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 661
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibacterial that is currently marketed in Canada. The TxGNN model predicts it may be effective for **hyperamylasemia**, but **0 clinical trials** and **0 publications** support this prediction. It is a model-only signal with no plausible biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (antibacterial class; the licence indication text is not available) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Norfloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. This mechanism is relevant to bacterial infections.

Hyperamylasemia is a laboratory finding (elevated serum amylase), not an infectious disease. It has no clear antibacterial target, and no plausible mechanistic link to norfloxacin was identified. The high TxGNN score most likely reflects the topology of the knowledge graph rather than real pharmacology. Taken alone, it is not a reason to pursue this indication.

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
| 2229524 | NORFLOXACIN | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried sources.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no trials, no literature, and no plausible mechanism. Hyperamylasemia is a laboratory finding rather than a treatable disease target for an antibacterial.

**Other candidates in this prediction set:**
- **Septicemic plague** is biologically plausible, since fluoroquinolones are a recognised class for plague. The evidence is only preclinical and not specific to norfloxacin. Norfloxacin's poor systemic exposure also makes it a weak candidate for septicaemia.
- **Punctate epithelial keratoconjunctivitis** has only indirect case-series evidence, which concerns microsporidial infection and does not establish norfloxacin efficacy.
- Both are classed as Research Questions (L4), not as candidates ready to proceed.

**To proceed, the following is needed:**
- The Health Canada package insert, for approved indications, warnings and contraindications
- Mechanism of action data
- Any clinical or preclinical evidence specific to norfloxacin for the target condition
- Dosage form and route information, to assess route compatibility
- A re-ranking of candidates by biological plausibility, rather than by TxGNN score alone

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

