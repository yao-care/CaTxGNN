---
layout: default
title: Lodoxamide
parent: Model Prediction Only (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lodoxamide: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Vernal conjunctivitis, papillary conjunctivitis…"
monitor_inn: "Lodoxamide"
predicted_indications: ["rosacea conjunctivitis", "punctate epithelial keratoconjunctivitis", "infectious anterior uveitis", "idiopathic uveitis", "nail infection", "neurotrophic keratopathy", "blepharoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture"]
---

# Lodoxamide
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

# Lodoxamide: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Lodoxamide is a mast cell stabilizer used as an eye drop for allergic conjunctival diseases, including vernal keratoconjunctivitis and atopic and papillary conjunctivitis.
The TxGNN model predicts it may be useful for **rosacea conjunctivitis**,
but **no clinical trials and no publications** currently support this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vernal conjunctivitis, papillary conjunctivitis, atopic conjunctivitis, vernal keratoconjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (treat as a research question) |

## Why is This Prediction Reasonable?

Lodoxamide is a mast cell stabilizer. Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology sources note that the precise primary molecular target of mast cell stabilizers is not fully resolved. One in vitro finding shows lodoxamide inhibits the migration of THP-1 cells in a GPR35-dependent manner, and GPR35 is a candidate target.

Ocular rosacea involves inflammation of the lid margin and conjunctiva, so there is some overlap with the ocular surface inflammation in lodoxamide's approved indications. The topical ophthalmic route would also be the same.

The link is indirect, however. The main drivers of rosacea (meibomian gland dysfunction, Demodex, and innate immune dysregulation) are not mast cell-dominated. The high score is a computational prediction only and has not been validated.

### Other Predicted Indications

The model also ranks other conditions. Their support is as follows:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Punctate epithelial keratoconjunctivitis | 97.51% | Adjacent ocular surface inflammation with the same route; plausible but unvalidated (Research Question) |
| 3 | Infectious anterior uveitis | 96.11% | Intraocular disease; topical drug is unlikely to reach adequate concentrations; weak link (Hold) |
| 4 | Idiopathic uveitis | 96.09% | T cell and cytokine-driven; penetration concern (Hold) |
| 5 | Nail infection | 95.34% | No antimicrobial activity; likely a knowledge-graph artifact (Hold) |
| 6 | Neurotrophic keratopathy | 94.69% | Nerve damage is not addressed by mast cell stabilization (Hold) |
| 7 | Blepharoconjunctivitis | 93.44% | Allergic subtypes overlap with approved uses; plausible but unvalidated (Research Question) |
| 8 | Postinfectious vasculitis | 93.36% | Systemic condition; minimal systemic exposure from topical use (Hold) |
| 9 | Post-bacterial disorder | 93.24% | Vague category with no defined pathophysiology (Hold) |
| 10 | Infective urethral stricture | 93.09% | Fibrotic condition; route incompatible (Hold) |

Among these, punctate epithelial keratoconjunctivitis and blepharoconjunctivitis (allergic forms) are the most biologically plausible.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00893560 | ALOMIDE | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: No drug-drug interaction records were found. One pharmacology record lists GPR35 as a target of lodoxamide (a target association, not a drug interaction).

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rosacea conjunctivitis is supported only by the model score (Evidence Level L5), with no clinical trials or publications. The mechanistic link is indirect, and the original mechanism of action data is unavailable. It is best treated as a research question rather than a candidate ready for development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before any safety screening
- Mechanism of action data (for example from DrugBank), including confirmation of the role of GPR35
- A literature and trial search focused on ocular rosacea, punctate epithelial keratoconjunctivitis, and allergic blepharoconjunctivitis
- Confirmation of the approved indication text, dosage form, and route of administration for the Canadian product
- Preclinical or small exploratory studies to test whether mast cell stabilization has any benefit in ocular rosacea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

