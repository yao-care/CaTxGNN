---
layout: default
title: Catridecacog
parent: Model Prediction Only (L5)
nav_order: 161
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# Catridecacog: From Congenital Factor XIII A-Subunit Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog (recombinant coagulation factor XIII A-subunit) is approved for congenital FXIII A-subunit deficiency.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on knowledge-graph proximity alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital FXIII A-subunit deficiency (from the prediction rationale; the Canadian license record lists no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, catridecacog replaces the FXIII A-subunit. This enzyme cross-links fibrin and stabilizes the clot, and its efficacy in FXIII A-subunit deficiency is established.

The link to the predicted indication is weak. FXIII acts downstream of platelet plug formation. A platelet release (secretion) defect is a primary hemostasis problem, and FXIII does not correct granule secretion or platelet activation. Any benefit would be a speculative adjunct effect on clot stability.

The high TxGNN score (99.29%) most likely reflects proximity within the bleeding and coagulation cluster of the knowledge graph, not a validated mechanism. The model also ranks two other platelet or von Willebrand-related disorders highly, pseudo-von Willebrand disease (99.29%) and Glanzmann thrombasthenia (99.15%). Both have the same problem: only a nonspecific, downstream fibrin-stabilization rationale, with no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2389975 | TRETTEN | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no trials or publications, and the mechanism is hypothetical because FXIII acts downstream of the platelet secretion defect. Safety data for the Canadian product are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that FXIII supplementation improves clot stability or hemostasis in platelet secretion defects
- A literature search, including case reports, for FXIII use in platelet function disorders
- Comparison against current standard management (platelet transfusion, antifibrinolytics, recombinant FVIIa) to define any realistic role

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

