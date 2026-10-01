---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a widely used beta-lactam antibacterial, marketed in Canada under 20 licences.
The TxGNN model predicts it may be relevant to **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** were retrieved for this prediction.
This is a model-only signal with no supporting evidence, and no plausible mechanism is apparent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (general antibacterial use; licence indication text was not provided in the evidence pack) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for amoxicillin in this evidence pack. Amoxicillin is a beta-lactam antibacterial. Its efficacy against susceptible bacterial infections is well established.

Polyclonal hyperviscosity syndrome is a condition of raised serum viscosity from excess polyclonal immunoglobulins. Amoxicillin has no known action on serum viscosity or immunoglobulin levels, so no mechanistic link can be proposed. The high score (99.63%) most likely reflects proximity in the knowledge graph rather than a biological effect. Several other top-ranked predictions (hyperamylasemia, congenital analbuminemia, premalignant haematological disease) share the same limitation.

Among the other predicted indications, monoclonal gammopathy (rank 6) is the only one with a plausible biological thread. Case reports describe antibiotic-responsive regression of immunoproliferative small intestinal disease, including after *H. pylori* eradication regimens that typically contain amoxicillin. That is bacterial-driven lymphoproliferation, and it does not show that amoxicillin treats monoclonal gammopathy itself. The rest of the retrieved material for that indication is about infections in myeloma patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and approved indication text were not provided for these licences.

| DIN | Product Name |
|---------|------|
| 2477726 | AG-AMOXICILLIN |
| 2532042 | PRZ-AMOXICILLIN |
| 628158 | APO-AMOXI |
| 2388073 | AURO-AMOXICILLIN |
| 406724 | NOVAMOXIN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials or publications, and amoxicillin has no plausible effect on serum viscosity or polyclonal immunoglobulin excess. This is a hypothesis without support, not an actionable repurposing candidate.

**To proceed, the following is needed:**
- Amoxicillin mechanism of action data (for example from DrugBank), to allow any mechanistic-link analysis
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Any independent biological or clinical rationale linking amoxicillin to hyperviscosity or polyclonal hypergammaglobulinemia
- If the team wants a more tractable direction, a separate review of monoclonal gammopathy (rank 6), restricted to antigen-driven lymphoproliferative contexts such as IPSID and *H. pylori*-associated disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

