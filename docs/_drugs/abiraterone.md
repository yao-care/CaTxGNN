---
layout: default
title: Abiraterone
parent: Model Prediction Only (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Abiraterone
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

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone is a CYP17A1 inhibitor that suppresses androgen synthesis. The Canadian license data do not list an approved indication, but the only registered study in the pack concerns castration-resistant prostate cancer.
The TxGNN model predicts it may be effective for **migraine disorder**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (the registered study in the pack concerns castration-resistant prostate cancer) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Abiraterone is known to inhibit CYP17A1 and suppress androgen synthesis. No plausible pathway linking this mechanism to migraine is documented.

The relationship between the original and new indication is not supported by the data. The high TxGNN score is a graph-based model output only.

The lower-ranked prediction "migraine with or without aura, susceptibility to" returned 20 publications. They concern epilepsy and migraine genetics (SCN1A, MTHFR, shared channelopathies) and do not mention abiraterone or androgen pathways. They look like keyword matches and should not be counted as supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage form and approved indication text are not provided in the license records. The five main authorizations are:

| DIN | Product Name |
|---------|------|
| 02371065 | ZYTIGA |
| 02503999 | MAR-ABIRATERONE |
| 02501503 | PMS-ABIRATERONE |
| 02540452 | PRZ-ABIRATERONE |
| 02502305 | JAMP ABIRATERONE |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (CYP17A1 inhibitor); not a conventional cytotoxic agent |
| Other items (myelosuppression, emetogenicity, monitoring, handling protection) | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or literature for migraine disorder, and no mechanistic link between androgen synthesis inhibition and migraine is documented.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- Detailed mechanism of action data (MOA), for example from DrugBank
- Preclinical or mechanistic evidence linking CYP17A1/androgen pathways to migraine
- Original approved indication text from the Canadian license records
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

