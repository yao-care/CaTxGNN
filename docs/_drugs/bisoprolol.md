---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a beta-1 selective blocker, generally known as a cardiovascular drug for hypertension. The Evidence Pack does not list its approved indication.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but there are **0 clinical trials** and **0 publications** for this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data (generally known as an antihypertensive) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Bisoprolol is generally known as a beta-1 selective blocker that lowers blood pressure and reduces renin release. An antihypertensive rationale for hypertension-related kidney disease is therefore plausible.

However, malignant hypertension is a hypertensive emergency. It is usually managed with titratable parenteral agents, and oral bisoprolol is not an established option. The dataset offers no support for it.

The very high score most likely reflects the drug's general antihypertensive links in the knowledge graph, not evidence specific to this disease. A second prediction, malignant renovascular hypertension, has an identical score, which suggests both come from the same knowledge-graph pathway. It is not independent support.

The other predictions are pulmonary hypertension (two categories) and Braddock syndrome. All are L5 with no trials and no relevant literature. Beta-blockade in pulmonary hypertension also raises a right ventricular safety question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 20 licenses in total. Five main products are shown below. Dosage form and approved indication text are not available in the data.

| DIN | Product Name |
|---------|------|
| 02465620 | MINT-BISOPROLOL |
| 02518805 | JAMP BISOPROLOL |
| 02267489 | TEVA-BISOPROLOL |
| 02256134 | APO-BISOPROLOL |
| 02544245 | SANDOZ BISOPROLOL TABLETS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials and no relevant literature. Oral bisoprolol is not an established treatment for a hypertensive emergency such as malignant hypertension.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Mechanism of action data (for example, from DrugBank)
- A targeted search for trials and literature on bisoprolol in malignant hypertension and hypertensive nephropathy
- Approved indication text for the Canadian licenses, to confirm the original indication
- A safety review for any pulmonary hypertension indication, focused on right ventricular function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

