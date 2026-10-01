---
layout: default
title: Cantharidin
parent: Model Prediction Only (L5)
nav_order: 150
evidence_level: L5
indication_count: 1
---

# Cantharidin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Cantharidin: From an Unspecified Original Indication to Amenorrhea

## One-Sentence Summary

Cantharidin is generally described as a topical vesicant, but no original approved indication is recorded in the data provided.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on a knowledge-graph score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available, and the graph path behind the prediction was not provided. The only support is the high TxGNN score (0.994), so the prediction cannot be checked against a specific mechanism.

Cantharidin is generally described as a protein phosphatase 2A (PP2A) inhibitor and a topical vesicant. No established pathway links this activity to hypothalamic-pituitary-ovarian regulation or menstrual function. Any mechanistic link to amenorrhea is speculative.

Systemic cantharidin is also known to be highly toxic, with renal and gastrointestinal injury. That is a strong argument against systemic use for a non-life-threatening condition. Route compatibility between the marketed product and the predicted indication has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 772011 | CANTHARONE PLUS | Not recorded | Not recorded |

The metadata lists TFDA as the regulatory input source, so the jurisdiction of this license record should be confirmed before it is treated as a Health Canada authorization.

## Safety Considerations

- **Systemic toxicity (from the literature-based rationale):** systemic cantharidin is associated with renal and gastrointestinal injury.
- **Drug Interactions:** no interaction records were found in the query.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link. The known systemic toxicity of cantharidin makes use in amenorrhea difficult to justify without strong new evidence.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication, dosage form)
- Mechanism of action data from DrugBank
- The TxGNN graph path behind the amenorrhea prediction
- Evidence that the marketed product's route is compatible with the proposed use
- A literature and trial search for any biological link between cantharidin and menstrual regulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

