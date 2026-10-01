---
layout: default
title: Ergometrine
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Ergometrine
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

# Ergometrine: From Uterotonic Use to Hypertrichosis

## One-Sentence Summary

Ergometrine (ergonovine) is an ergot-derived uterotonic, marketed in Canada as an injection.
The TxGNN model predicts it may be effective for **hypertrichosis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uterotonic use (the Health Canada licence record does not state an approved indication text) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on known information, ergometrine is an ergot alkaloid uterotonic that acts as a partial agonist at serotonergic, adrenergic and dopaminergic receptors.

**This prediction is not mechanistically supported.** No known mechanism links these receptor actions to hair growth disorders. The high TxGNN score reflects graph proximity only, and no trials or literature back it.

The same applies to the other top-ranked predictions:
- **Ambras-type congenital hypertrichosis** is a rare genetic disorder.
- **Isolated genetic hair shaft abnormality** is a genetic structural defect.
- **Nephrogenic syndrome of inappropriate antidiuresis** is caused by activating AVPR2 mutations.
- **Dandy-Walker malformation syndrome** is a congenital brain malformation.
- **Leprosy** has no established antimycobacterial or immunomodulatory link.

Among the ten predictions, **migraine disorder** (rank 7) has the most plausible rationale. Ergot alkaloids act on serotonin receptors to constrict cranial vessels, and this is the same class mechanism as ergotamine and methysergide. Small studies report benefit with ergonovine and methylergonovine, but the designs are open-label or retrospective. Most of the data come from the close analog methylergonovine, and there are no registered trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2441241 | ERGONOVINE MALEATE INJECTION USP |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the queried data.

Literature retrieved for other predicted indications flags vasoconstrictive risks with ergot alkaloids and oxytocics, including coronary vasospasm, Prinzmetal angina, QT prolongation and raised pulmonary vascular resistance. Ergometrine is generally cautioned against in cardiac disease and pulmonary hypertension.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hypertrichosis prediction rests on a model score alone (L5), with no trials, no literature and no plausible pharmacological link.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For a more promising direction, a separate evaluation of **migraine** (evidence level L3, "Research Question"). This would need:
  - a review of the small ergonovine and methylergonovine studies, such as [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/), [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) and [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/)
  - a vasospasm and cardiovascular safety assessment before any further work

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

