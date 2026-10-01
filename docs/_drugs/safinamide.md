---
layout: default
title: Safinamide
parent: Model Prediction Only (L5)
nav_order: 825
evidence_level: L5
indication_count: 3
---

# Safinamide
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

# Safinamide: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Safinamide is marketed in Canada as ONSTRYV and is used as add-on therapy in Parkinson's disease. The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (add-on therapy; the Canadian licence records contain no indication text) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the curated drug record. From known pharmacology, safinamide is a reversible MAO-B inhibitor that also blocks voltage-gated sodium channels and reduces glutamate release. In Parkinson's disease, MAO-B inhibition enhances dopaminergic signalling. The sodium channel and glutamate effects could plausibly dampen seizure activity.

Rasmussen encephalitis is a rare, progressive brain disorder characterised by intractable focal seizures. It is driven mainly by T-cell-mediated autoimmune inflammation, and none of safinamide's known mechanisms address that process. At best, safinamide might help with seizure symptoms. There is no basis to expect it to affect the underlying disease. The high score is therefore not corroborated by any clinical or mechanistic evidence.

Two other diseases were also predicted, and neither has any trials or publications:
- **Myelitis** (score 99.46%): the rationale is speculative neuroprotection. Myelitis covers many inflammatory, infectious and autoimmune causes that safinamide does not treat, so a specific cause would need to be defined first.
- **PLA2G6-associated neurodegeneration** (score 99.22%): this is the most biologically plausible of the three. It often presents with dystonia-parkinsonism, so safinamide might help parkinsonian symptoms, though there is no evidence it changes disease progression. It is flagged as a research question, and a preclinical or case-series study would be a reasonable first step.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02484641 | ONSTRYV |
| 02484668 | ONSTRYV |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trials or publications support it, and safinamide's known mechanisms do not target the autoimmune inflammation that drives Rasmussen encephalitis. Safety information is also incomplete.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Curated mechanism-of-action data from DrugBank
- A literature and trial search with disease-specific terms for Rasmussen encephalitis
- Preclinical or case-series evidence, with PLA2G6-associated neurodegeneration (symptomatic parkinsonism) as a possible first test case

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

