---
layout: default
title: Lactulose
parent: Model Prediction Only (L5)
nav_order: 513
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Lactulose: From Established Laxative and Hepatic Encephalopathy Use to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a non-absorbable disaccharide, marketed in Canada under six licenses and widely used as a laxative and for hepatic encephalopathy. The TxGNN model predicts it may be effective for **acute urate nephropathy**, with a very high score. However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acute urate nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

The approved-indication text for the Canadian licenses was not provided, so the original indication is not listed here. The use described above comes from the retrieved literature.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lactulose is known from the retrieved literature as a non-absorbable disaccharide that acidifies the colon and lowers gut-derived ammonia and endotoxin. It is used for constipation and hepatic encephalopathy.

For acute urate nephropathy, the reviewed data support **no plausible mechanistic link**. Lactulose is not known to act on uric acid handling or on urate precipitation in the renal tubules. The high TxGNN score (99.89%) reflects a knowledge-graph association, not any trial or published finding. The prediction should be treated as a hypothesis-generating signal only.

**Better-supported candidates from the same run:** the rank-3 prediction, **obstructive jaundice**, has much stronger support. Gut acidification lowers endotoxaemia and bacterial translocation, which may protect the kidney after biliary obstruction. This is backed by studies from 1986–2003, including a 102-patient randomized trial of preoperative lactulose and bile salts (PMID 2032107). It is evidence level L3, but the pack does not confirm a Phase 3 RCT. Other predictions are weaker:

| Rank | Predicted indication | TxGNN score | Evidence level |
|------|------|------|------|
| 2 | Nephrolithiasis | 99.78% | L5 |
| 3 | Obstructive jaundice | 99.53% | L3 |
| 4 | Bile duct disease | 99.47% | L4 |
| 5 | Biliary tract disease | 99.38% | L4 |
| 6 | Hyperphosphatemia | 99.37% | L4 |
| 7 | Exercise-induced malignant hyperthermia | 99.14% | L5 |
| 8 | Bile duct neoplasm | 99.12% | L4 |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Six licenses are on record; five are listed below. Dosage form, manufacturer and approved-indication text were not provided.

| DIN | Product Name |
|---------|------|
| 02331551 | TEVA-LACTULOSE |
| 02469391 | PMS-LACTULOSE-PHARMA |
| 02247383 | PHARMA-LACTULOSE |
| 00854409 | RATIO-LACTULOSE |
| 02295881 | JAMP-LACTULOSE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute urate nephropathy has no supporting trials or literature and no plausible mechanism. It rests entirely on the model score (evidence level L5), so there is no basis to advance it.

**To proceed, the following is needed:**
- Health Canada package insert data (indications, warnings, contraindications), which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank) to test any link to urate nephropathy
- Any preclinical or clinical signal for lactulose in urate handling or crystal-induced kidney injury; if none emerges, deprioritize this indication
- Consider redirecting effort to **obstructive jaundice**. This would require verifying the interventions in NCT01090193 (the summary does not mention lactulose) and the design and arms of the 1991 multicentre study (PMID 2032107).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

