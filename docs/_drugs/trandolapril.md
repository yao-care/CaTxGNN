---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 922
evidence_level: L5
indication_count: 6
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Trandolapril: From ACE Inhibitor Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an ACE inhibitor that is marketed in Canada under 20 licences.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **0 clinical trials** and **0 publications** currently support this prediction.
The result is a model-only prediction (Evidence Level L5) and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, trandolapril belongs to the ACE inhibitor class. ACE inhibitors block the formation of angiotensin II, which lowers blood pressure and reduces pressure inside the kidney's filtering units (glomeruli).

Malignant hypertensive renal disease is kidney injury driven by severe, sustained high blood pressure. Lowering systemic and glomerular pressure through ACE inhibition is biologically plausible for this condition.

The 99.92% TxGNN score reflects a knowledge-graph association, not clinical proof. No trials or publications were found for this drug–disease pair, so the mechanistic argument is still unverified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

The table shows 5 of the 20 authorizations. Dosage form, manufacturer and approved indication text were not provided for these entries.

| DIN | Product Name |
|---------|------|
| 2325756 | SANDOZ TRANDOLAPRIL |
| 2526581 | TRANDOLAPRIL |
| 2325748 | SANDOZ TRANDOLAPRIL |
| 2239267 | MAVIK |
| 2471868 | AURO-TRANDOLAPRIL |

---

## Safety Considerations

Please refer to the package insert for safety information.

One class-level concern relates to the related prediction for malignant renovascular hypertension. ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis. This should be weighed carefully before any use in renal vascular disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature, and the safety and mechanism data are incomplete. The mechanistic argument is reasonable, but it is not yet evidence.

**Other predictions in this pack:**
- Malignant renovascular hypertension, pulmonary hypertension (two variants) and Braddock syndrome are also L5 / Hold.
- The 10 papers retrieved for pulmonary hypertension owing to lung disease and/or hypoxia are general hypoxia biology (brain aging, cancer, keloid, multiple sclerosis, altitude). None concerns trandolapril, so they should not be counted as support.
- Chronic pulmonary heart disease (score 99.19%) is the only prediction with any drug-specific study: a 1996 rat study of long-term trandolapril on vasoconstriction in chronic heart failure ([PMID 8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/)). It is preclinical only and indirect, so it is rated L4 and labelled a Research Question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic search for human clinical evidence on trandolapril in hypertensive renal disease
- A similarity assessment against the original indication and a route-of-administration compatibility check
- Confirmation of the animal model in PMID 8989645 if the chronic pulmonary heart disease direction is pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

