---
layout: default
title: Sodium Zirconium Cyclosilicate
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 10
---

# Sodium Zirconium Cyclosilicate
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

# Sodium Zirconium Cyclosilicate: From Hyperkalaemia to Breast Fibrocystic Disease

## One-Sentence Summary

Sodium zirconium cyclosilicate is a non-absorbed potassium binder that acts in the gut and is used to lower high blood potassium (hyperkalaemia).
The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but **0 clinical trials** and **0 publications** support this, and no plausible biological link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperkalaemia (general drug knowledge; the Canadian label text was not provided) |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 93.41% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, sodium zirconium cyclosilicate is a selective potassium binder that works in the gastrointestinal tract. It is barely absorbed into the body and has no known effect on breast tissue.

The prediction does not appear to be biologically grounded. The top 8 predicted indications are all breast or lactation conditions: benign mammary dysplasia, blunt duct adenosis, apocrine adenosis, fat necrosis, breast abscess, lactation disease and breast adenosis. Blunt duct adenosis and apocrine adenosis have identical scores (91.85%). This points to a cluster of related disease terms in the knowledge graph rather than independent signals. Ranks 9 and 10 (heparin cofactor 2 deficiency and antithrombin deficiency type 2) are coagulation disorders, which a potassium binder does not act on either.

The TxGNN score is a graph-based prediction only. It does not show that the drug works for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2490722 | LOKELMA |
| 2490714 | LOKELMA |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism. The drug is a non-absorbed GI potassium binder with no known effect on breast tissue.

**To proceed, the following is needed:**
- The Health Canada package insert, for warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to assess any mechanistic link
- Any independent preclinical or clinical evidence linking the drug to benign breast conditions
- A review of why the model ranks the breast cluster highly, since the correlated scores suggest redundant graph signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

