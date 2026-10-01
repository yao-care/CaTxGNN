---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Colistin
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

# Colistin: From Gram-Negative Bacterial Infection to Postinfectious Vasculitis

## One-Sentence Summary

Colistin is a polymyxin antibiotic, used mainly against serious Gram-negative bacterial infections.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but **0 clinical trials** and **0 publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records. Colistin (as colistimethate) is generally used for Gram-negative bacterial infections. |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Colistin disrupts the outer membrane of Gram-negative bacteria. Detailed mechanism-of-action data are not available in the current dataset.

There is no known immunomodulatory action that would be relevant to immune-complex vasculitis. The only plausible link is indirect: treating the infection that triggers the vasculitis. That is a different rationale from treating the vasculitis itself.

The prediction is therefore best read as a model output without mechanistic support. No trials or literature were found to back it.

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
| 2244849 | COLISTIMETHATE FOR INJECTION U.S.P. |
| 476420 | COLY-MYCIN M |
| 2403544 | COLISTIMETHATE FOR INJECTION, USP |

---

## Safety Considerations

Please refer to the package insert for safety information.

Nephrotoxicity and neurotoxicity are the main concerns noted across the colistin evidence reviewed for this drug. Kidney involvement is common in vasculitis, so renal risk would need particular attention in this setting.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials, no literature, and no plausible mechanism linking colistin to vasculitis. Its known nephrotoxicity is an added concern.

**To proceed, the following is needed:**
- Any published or registered evidence for colistin in postinfectious vasculitis
- A mechanistic rationale beyond treating the triggering infection
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank

**Other predictions for this drug:** Among the lower-ranked predictions, **chronic rhinosinusitis** (Evidence Level L3) has the most support. It rests on a small 2008 pilot study of nebulised bacitracin/colimycin and on cystic-fibrosis-related literature, with no RCTs. Any follow-up work would be better directed there than at postinfectious vasculitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

