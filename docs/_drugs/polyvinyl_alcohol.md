---
layout: default
title: Polyvinyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 4
---

# Polyvinyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Polyvinyl Alcohol: From Eye Care Products to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polyvinyl alcohol is marketed in Canada in over-the-counter eye care products (REFRESH, MURINE, CLEAR EYES TRIPLE ACTION RELIEF). The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**, a rare inherited scaling skin disorder. **No clinical trials and no publications** currently support this prediction, which rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available data; the product names suggest ophthalmic use |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

Three other ichthyosis-spectrum conditions were also predicted, each with no trials or literature:

| Predicted Indication | TxGNN Score |
|------|------|
| Self-healing collodion baby | 99.83% |
| Lamellar ichthyosis | 99.72% |
| Bathing suit ichthyosis | 99.54% |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. DrugBank lists no original indications and no mechanism for polyvinyl alcohol. What is known is that it is a hydrophilic, film-forming polymer used as a lubricant in eye products. In theory, a polymer like this could act as a topical occlusive or humectant on a defective, scaling skin barrier. This is speculation, and no clinical or preclinical data support it.

All four predicted conditions are forms of congenital ichthyosis, so they likely share the same weak rationale. The score probably reflects the compound's proximity to ichthyosis-related nodes in the knowledge graph, not a validated mechanism. Polyvinyl alcohol has no known keratolytic activity and no known effect on the genetic pathways involved, such as transglutaminase-1 in lamellar ichthyosis.

Self-healing collodion baby is a neonatal, self-limiting condition normally managed with emollients and supportive care. Any new agent would need particular safety caution in newborns, and its added value is unclear.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02138670 | REFRESH |
| 02247538 | MURINE |
| 02301687 | CLEAR EYES TRIPLE ACTION RELIEF |

Dosage form and approved indication text were not provided for these authorizations.

## Safety Considerations

- **Drug Interactions**: No interactions were found in the DDI query.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it (Evidence Level L5), with no trials, no literature and no verifiable mechanism. The available products are ophthalmic, so route compatibility with a skin or neonatal use is also unestablished. Safety screening cannot proceed without the Canadian package insert warnings and contraindications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (for example, via the DrugBank API)
- The original approved indication, dosage forms and routes for the three DINs
- A route compatibility assessment (ophthalmic products versus a topical skin use)
- Preclinical or literature evidence for barrier hydration or occlusion in ichthyosis models
- A neonatal safety assessment before any consideration for self-healing collodion baby

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

