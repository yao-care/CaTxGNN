---
layout: default
title: Tetryzoline
parent: Model Prediction Only (L5)
nav_order: 904
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Tetryzoline: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis, common cold"
monitor_inn: "Tetryzoline"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Tetryzoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Tetryzoline: From Pharyngitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Tetryzoline is a topical vasoconstrictor that, according to the knowledge graph used for this report, is associated with pharyngitis and the common cold. It is marketed in Canada in eye-drop products.
The TxGNN model predicts it may be effective for **nasal cavity disease**, with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tetryzoline belongs to the imidazoline class of alpha-adrenergic agonists and works as a topical vasoconstrictor. It narrows blood vessels in the mucosa, which reduces redness, swelling and congestion.

That effect fits conditions of the nasal cavity, such as rhinitis and nasal congestion. The knowledge graph already links the drug to the common cold and pharyngitis, which involve the same upper-airway mucosa. The predicted indication is therefore close to the drug's existing use. It may be an extension of an existing indication rather than a truly new repurposing opportunity.

This mechanistic link is inferred from the drug class, not from evidence supplied for this report. The high TxGNN score is a computational prediction only.

A second prediction, **acute laryngopharyngitis** (score 99.98%), is probably driven by the existing pharyngitis association. No evidence was found that vasoconstriction benefits laryngeal involvement, and it also remains at Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

All 10 licences are valid single-ingredient products. Dosage form and approved indication text are not available in the data compiled for this report.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01942425 | VISINE ORIGINAL | Not available | Not available |
| 02273446 | ORIGINAL EYE DROPS | Not available | Not available |
| 02338602 | VISINE MULTI-SYMPTOM | Not available | Not available |
| 02290596 | ALLERGY EYE DROPS | Not available | Not available |
| 02448955 | 8-SYMPTOM RELIEF | Not available | Not available |

The product names suggest the Canadian products are ophthalmic (eye-drop) formulations. A nasal or pharyngeal use would therefore likely need a different route of administration, and route compatibility has not yet been assessed.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): diabetes mellitus, diabetic ketoacidosis, cardiovascular disease, heart disease, hyperthyroidism, Graves disease, thyrotoxicosis. These are consistent with the systemic effects of alpha-adrenergic agonists, but they should be confirmed against the official product labelling.
- **Drug interactions**: No interaction records were found.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and a drug-class argument, with no clinical trials or publications behind it (Evidence Level L5). The package insert safety information is missing, which blocks safety screening. The Canadian products are eye drops, so route compatibility with a nasal or throat use is unresolved.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings and contraindications
- Obtain mechanism of action data (for example from DrugBank)
- Confirm approved indications and dosage forms for the Canadian licences
- Assess route compatibility (ophthalmic vs. nasal or oropharyngeal use)
- Search for clinical and literature evidence of tetryzoline in nasal congestion or rhinitis
- Clarify whether the predicted indications are genuinely new or already covered by existing nasal or cold-symptom uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

