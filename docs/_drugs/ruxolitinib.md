---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 822
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

# Ruxolitinib: From Its Marketed Uses to Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa)

## One-Sentence Summary

Ruxolitinib is a JAK1/2 inhibitor marketed in Canada under the brand names Jakavi and Opzelura. The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

The supplied data do not include approved indication text for the Canadian licences, so the original indication is not listed.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the Evidence Pack. Ruxolitinib is known as a JAK1/2 inhibitor, which blocks JAK/STAT signalling downstream of many cytokines.

The link to the predicted indication is weak. PEComa is driven mainly by loss of TSC1/2 and hyperactivation of mTORC1, not by JAK/STAT signalling. Nothing in the supplied data connects ruxolitinib to this tumour type. The high TxGNN score (99.73%, model rank 5842) reflects a knowledge-graph pattern, not mechanistic or clinical support.

The same pattern appears for the other PEComa-spectrum predictions: benign PEComa, lung PEComa, lymphangiomyoma and lymphangioleiomyomatosis. For these, mTOR inhibitors are the established mechanistic class.

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
| 02552434 | OPZELURA |
| 02388022 | JAKAVI |
| 02388014 | JAKAVI |
| 02434814 | JAKAVI |
| 02388006 | JAKAVI |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. There are no trials or publications, and the known biology of PEComa (mTORC1-driven) does not point to JAK/STAT inhibition.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking JAK/STAT signalling to PEComa
- Mechanism of action data (DrugBank)
- Health Canada product monograph warnings and contraindications

**Better-supported alternatives for this drug:**
- **Hemophagocytic syndrome associated with infection** (rank 9, evidence level L3): HLH is driven by IFN-γ and cytokine signalling through JAK1/2, and the evidence includes:
  - Multiple cohort studies and case reports, including EBV-associated and paediatric HLH.
  - A consensus guideline.
  - A Phase 1 trial in immune effector cell-associated HLH-like syndrome (NCT07424222, not yet recruiting).
- **Liposarcoma** (rank 5, evidence level L4): two preclinical papers link JAK-STAT signalling to myxoid liposarcoma, with no clinical data.

These candidates warrant prioritisation over the PEComa-spectrum predictions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

