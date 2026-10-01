---
layout: default
title: Alimemazine
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 6
---

# Alimemazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Alimemazine: From Phenothiazine Antihistamine to Allergic Urticaria

## One-Sentence Summary

Alimemazine is a phenothiazine-class first-generation H1 antihistamine, but the supplied data does not list an original approved indication.
The TxGNN model predicts it may be effective for **allergic urticaria** (score 99.98%),
but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| Market Status | ✓ Marketed |
| Number of Licenses | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Based on general class knowledge, alimemazine is a phenothiazine-class H1 antihistamine. Blocking H1 receptors is a plausible way to relieve histamine-mediated conditions such as urticaria. This link comes from class knowledge and the model score, not from trial or literature data in the pack.

The pack lists no original indication, so the relationship between the old and new use cannot be assessed from the data. The drug may already be labelled for urticaria or itch in some jurisdictions, so the local label must be checked before this is treated as true repurposing.

The other predictions are weaker or less well defined:
- **Cold urticaria** (99.96%) is also histamine-driven, but guideline-preferred agents are second-generation antihistamines.
- **Atopic IgE responsiveness** (99.60%) is a phenotype, not a clinical indication. An antihistamine would only relieve symptoms.
- **Nasal cavity disease** (99.60%) is too broad and needs narrowing, for example to allergic rhinitis.
- **Recalcitrant atopic dermatitis** (99.59%) is a weak fit, because antihistamines mainly help itch and sleep, and biologics and JAK inhibitors are the relevant comparators.
- **Acute laryngopharyngitis** (99.54%) is usually infectious, and any benefit would be indirect symptom relief.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Regulatory and Market Information

| License Number | Product Name |
|---------|------|
| 1926306 | PANECTYL |
| 1926292 | PANECTYL |

The pack does not state dosage form or approved indication for either license. The pack's listed inputs are TFDA and DrugBank, and no Health Canada data was supplied, so the licensing jurisdiction of these entries should be confirmed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the model score, with no clinical trials or literature. Key data on approved indications, mechanism and safety is also missing, so the candidate stays at the research-question stage.

**To proceed, the following is needed:**
- Approved indication and dosage form for the marketed PANECTYL licenses, and the jurisdiction of those licenses
- Package insert warnings and contraindications, since the safety screen cannot proceed without them
- Mechanism of action data (for example, from DrugBank)
- A literature and trial search for alimemazine in urticaria, and a check of whether urticaria is already a labelled use
- For weaker candidates, a narrower indication definition (for example, allergic rhinitis instead of "nasal cavity disease")
- A rationale for using a first-generation sedating antihistamine, given that guidelines prefer second-generation agents

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

