---
layout: default
title: Hyaluronidase
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Hyaluronidase"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
description: "Hyaluronidase: predicted new indication Esotropia (evidence level L5)."
---

# Hyaluronidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Hyaluronidase: From Its Current Marketed Use to Esotropia
{: .text-alpha }

## One-Sentence Summary

Hyaluronidase is an enzyme marketed in Canada under the product name HYQVIA, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **esotropia** (inward-turning eye misalignment), but there are **0 clinical trials** and **1 publication**, and that publication describes a surgical complication rather than a benefit.
This prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 (model prediction only; the single related report is a complication case series, not supporting evidence) |
| Canada Market Status | Marketed (valid licenses: 5 of 5) |
| Number of DINs | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hyaluronidase is an enzyme that breaks down hyaluronan, a component of connective tissue. It is commonly used to help other injected drugs spread through tissue. No therapeutic mechanism linking it to esotropia has been established.

The only linked report (PMID 16934027) describes persistent double vision and strabismus after cataract surgery under local anesthesia. Hyaluronidase is sometimes added to the anesthetic block in that setting. This points to a possible adverse-effect association, such as local anesthetic toxicity to the eye muscles or spread of the anesthetic. It does not show a treatment benefit.

The high TxGNN score is therefore not supported by clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | Case report/series | Binocular Vision & Strabismus Quarterly | Describes the clinical features and treatment of persistent double vision and strabismus after cataract surgery under local anesthesia. This is a surgical complication, not a therapeutic use. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02524368 | HYQVIA |
| 02524376 | HYQVIA |
| 02524384 | HYQVIA |
| 02524392 | HYQVIA |
| 02524406 | HYQVIA |

All five authorizations are valid single-ingredient licenses. Dosage form and approved indication text are not available in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions**: 63 interactions were identified, and all of the 20 listed in the data are graded **Minor**. Examples include:
  - corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone)
  - antihistamines (promethazine, chlorpheniramine, loratadine, cetirizine)
  - local anesthetics (lidocaine, articaine)
  - estrogens (estradiol, ethinylestradiol, conjugated estrogens)
  - aspirin

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, and the sole publication reports strabismus as a complication of eye surgery, which argues against a therapeutic role.

**To proceed, the following is needed:**
- Evidence that hyaluronidase treats esotropia, such as controlled clinical or mechanistic studies. None currently exists.
- Mechanism of action data and package insert warnings and contraindications from Health Canada.
- Approved indication and dosage form details for the five HYQVIA licenses.

**Note on better-supported predictions for this drug:** Among its other predicted indications, **diabetic retinopathy** (TxGNN rank 6) has by far the strongest support. It has two completed Phase 3 trials of intravitreal ovine hyaluronidase for vitreous hemorrhage (NCT00198497, n=510; NCT00198510, n=750) and one completed Phase 2 study (NCT00198471, n=10) in non-proliferative disease. Trial results were not in the data compiled for this report, so a review of the actual outcomes is needed before any decision on that indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

