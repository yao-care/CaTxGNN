---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 538
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor, used to replenish dopamine in dopamine-deficiency states such as Parkinson's disease. The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (general pharmacology; the approved-indication text is not recorded in the source data) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Levodopa is a dopamine precursor, and its approved use is to replenish dopamine in dopaminergic deficit states.

Rasmussen encephalitis is a rare, chronic, unilateral neuroinflammatory disease. It is driven mainly by T-cell (CD8+) cytotoxicity and microglial activation, and it presents with intractable focal seizures, progressive hemiparesis and cognitive decline. **No direct mechanistic link between the two is established.** Dopaminergic modulation has no known role in this immune-mediated pathology.

The very high TxGNN score most likely reflects knowledge-graph proximity, such as shared neurological or movement-disorder gene and phenotype nodes, rather than a validated pharmacological rationale. Levodopa could also lower the seizure threshold in some patients, which would be a concern in a seizure-dominant disease. This prediction should therefore be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved-indication text are not recorded for these authorizations. Five of the 20 are shown.

| DIN | Product Name |
|---------|------|
| 2531593 | AURO-LEVOCARB |
| 2546396 | JAMP LEVOCARB |
| 2292165 | DUODOPA |
| 2531607 | AURO-LEVOCARB |
| 2244495 | TEVA-LEVOCARBIDOPA |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no registered trials or publications, no plausible mechanistic link to a T-cell-mediated disease, and a possible seizure-threshold concern in a seizure-dominant condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (e.g., from DrugBank)
- A literature and trial search for dopaminergic agents in Rasmussen encephalitis or related neuroinflammatory epilepsies
- A mechanistic rationale showing how dopamine replenishment could affect immune-mediated neuroinflammation
- An assessment of seizure risk in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

