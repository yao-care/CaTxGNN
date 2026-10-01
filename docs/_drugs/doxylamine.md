---
layout: default
title: Doxylamine
parent: Model Prediction Only (L5)
nav_order: 304
evidence_level: L5
indication_count: 4
---

# Doxylamine
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

# Doxylamine: From Marketed Antihistamine Products to Allergic Urticaria

## One-Sentence Summary

Doxylamine is a first-generation H1 antihistamine that is marketed in Canada in single-ingredient and combination products, including doxylamine/pyridoxine and cough-and-cold formulations.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but **no clinical trials and no publications** were supplied to support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (the Canadian licence records have no indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Doxylamine is known from general pharmacology as a first-generation H1 antihistamine with anticholinergic and sedating effects. This background knowledge is not confirmed by the supplied data.

Allergic urticaria is driven largely by histamine release from mast cells, so H1 blockade is biologically consistent with the prediction. Most of the plausibility is a class effect. H1 antagonists are already standard treatment for urticaria, so the prediction is not a new discovery.

Second-generation antihistamines are the usual first-line choice, and doxylamine's sedation and anticholinergic burden limit its appeal. Any further work would need to show a benefit over those agents.

Three other predictions also scored above 99%: nasal cavity disease (99.36%), acute laryngopharyngitis (99.34%) and cold urticaria (99.26%). None has supporting trials or literature. The first two are broad or symptom-level targets that would need narrowing. Cold urticaria has the same class-effect logic as allergic urticaria.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

The Evidence Pack lists 20 authorizations in total. The five main ones are shown below. Dosage form and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 609129 | DICLECTIN |
| 2413248 | APO-DOXYLAMINE/B6 |
| 2552574 | ALOG-DOXYLAMINE/PYRIDOXINE |
| 2485443 | ROBITUSSIN HONEY COUGH & COLD NIGHTTIME |
| 2406187 | PMS-DOXYLAMINE-PYRIDOXINE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trials or publications support the prediction. The mechanistic link is a generic antihistamine class effect, and existing second-generation antihistamines already fill this role. It is a research question, not an actionable candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for doxylamine in urticaria
- Comparative evidence against second-generation antihistamines, covering sedation and anticholinergic burden
- Narrowing of the broad predicted indications (nasal cavity disease, acute laryngopharyngitis) to specific conditions before they are assessed

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

