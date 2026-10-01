---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 5
---

# Benazepril
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

# Benazepril: From Its Marketed Use (Indication Not Recorded) to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Benazepril is an ACE inhibitor that is already marketed in Canada, but the supplied data does not record its approved indications.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a very high score.
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (all Canadian license entries have blank indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. From general pharmacology, not from the evidence pack, benazepril belongs to the ACE inhibitor class. These drugs block the renin-angiotensin-aldosterone system (RAAS), which plays a central role in blood pressure control and kidney haemodynamics.

Malignant hypertensive renal disease is kidney injury driven by severely elevated blood pressure. RAAS blockade is therefore a plausible mechanism, and it fits the drug class. The evidence pack itself supports none of this: it has no trials, no literature and no recorded original indications. Because benazepril is already marketed and its approved indications are blank, we cannot tell whether this is genuine repurposing or overlap with existing hypertension use.

The other four predictions are weaker still:

- Malignant renovascular hypertension has the same score and the same evidence gap.
- The pulmonary hypertension predictions have no supportive evidence. The 20 literature hits for the hypoxia-related one are keyword matches on "hypoxia" (brain aging, keloid fibroblasts, gastric cancer and similar topics). None concerns benazepril or ACE inhibitors.
- Braddock syndrome is likely a knowledge-graph artifact and needs independent expert review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2290332 | BENAZEPRIL |
| 2273918 | BENAZEPRIL |
| 2290340 | BENAZEPRIL |

Dosage form, manufacturer and approved indication are not recorded for these licenses.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.65%), but there are no clinical trials or relevant publications, so the evidence level is L5. Key data on original indications, mechanism and safety is also missing, so this candidate should not advance beyond screening yet.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications) for the three DINs; this is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A targeted literature search on benazepril or ACE inhibitors in malignant hypertension and hypertensive nephrosclerosis
- Clarification of whether this prediction goes beyond benazepril's existing hypertension use
- A clinical trial registry search for this drug-disease pair
- Independent expert review of the lower-ranked predictions (pulmonary hypertension, Braddock syndrome) before any follow-up

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

