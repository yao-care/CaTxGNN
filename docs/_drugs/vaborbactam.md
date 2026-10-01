---
layout: default
title: Vaborbactam
parent: Model Prediction Only (L5)
nav_order: 954
evidence_level: L5
indication_count: 10
---

# Vaborbactam
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

# Vaborbactam: From Complicated Urinary Tract Infection to Osteoarthritis

## One-Sentence Summary

Vaborbactam is a beta-lactamase inhibitor given together with meropenem, originally used for complicated urinary tract infections.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **0 clinical trials** and **0 publications** currently support this prediction. It is a computational finding only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated urinary tract infection (the Canadian licence record has no indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank. Based on known information, vaborbactam is a cyclic boronic acid serine beta-lactamase inhibitor. It is combined with meropenem to treat complicated urinary tract infections. Its role is to protect the antibiotic from bacterial enzymes.

**No mechanistic link has been established** between this activity and osteoarthritis. Vaborbactam has no known effect on cartilage, joint inflammation, or musculoskeletal targets. The high score (98.52%) most likely reflects the structure of the knowledge graph, not pharmacology.

The other top predictions point the same way. They include osteoarthritis susceptibility, rheumatoid arthritis, gout, and several rare skeletal dysplasias. All are L5 with no supporting trials or literature. The cluster of musculoskeletal diseases suggests the model is following shared neighbours in the graph, not a real drug effect.

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
| 2554151 | VABOMERE |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanistic link. A beta-lactamase inhibitor has no known pharmacological connection to osteoarthritis, so this is not actionable at present.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic hypothesis connecting beta-lactamase inhibition to joint pathology, supported by preclinical data
- Any registered clinical trials or publications on vaborbactam in osteoarthritis

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

