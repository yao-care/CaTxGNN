---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 608
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Metolazone: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension / hypertensive disorder"
monitor_inn: "METOLAZONE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Metolazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metolazone: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (from the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, metolazone is a thiazide-like diuretic that inhibits the sodium-chloride cotransporter in the distal convoluted tubule. This reduces sodium and fluid volume, and its efficacy in hypertension is established.

Reducing volume and sodium load is plausibly relevant to renovascular hypertension. However, malignant renovascular hypertension is driven mainly by activation of the renin-angiotensin system due to renal artery stenosis, and thiazide-type diuretics can further stimulate renin release. This is a mechanistic concern rather than a supporting argument.

The very high score (99.84%) most likely reflects the close ontology relationship between this condition and the already approved hypertension indication, not independent evidence of benefit.

Other predicted indications show the same pattern. Their scores are all above 99.7%, and none has supporting trials:

| Predicted Indication | Score | Comment |
|------|------|------|
| Malignant hypertensive renal disease | 99.84% | Indirect link. Metolazone retains efficacy at reduced GFR, but malignant hypertension is an emergency needing rapid titratable parenteral therapy, so an oral diuretic is not suitable as primary treatment. |
| Pulmonary hypertension, unclear multifactorial mechanism | 99.83% | Diuretics may relieve volume overload (supportive care only). Metolazone does not act on pulmonary vascular pathways. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.83% | Possible symptomatic benefit for edema. One preclinical paper retrieved, judged non-informative. |
| Braddock syndrome | 99.78% | No mechanistic rationale identified. Likely a knowledge-graph artifact. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For reference, one publication was retrieved for a lower-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia). It is a preclinical study and is not informative for the top prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Preclinical | Am J Physiol | In rats, thiazide diuretic receptors (measured by [3H]metolazone binding) in the kidney were rapidly and reversibly reduced after acute renal ischemia. It describes receptor biology only, with no demonstrated relevance to pulmonary hypertension. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00888400 | ZAROXOLYN | Not specified | Not specified |

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
The drug-disease contraindication links in the knowledge graph include:
- Liver and metabolic: liver failure, hepatic coma, hepatic encephalopathy, pancreatitis, diabetes mellitus, diabetic ketoacidosis, gout
- Electrolyte and mineral: potassium deficiency disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
- Renal: anuria
- Blood pressure regulation: orthostatic hypotension, multiple system atrophy, postural orthostatic tachycardia syndrome
- Autoimmune and pregnancy-related: systemic lupus erythematosus (including pediatric), HELLP syndrome

**Drug Interactions:** The interaction screening returned 100 interacting drugs in total. The 20 listed in the compiled data were mostly Moderate, with a few Minor. Examples:
- **Moderate:** acarbose, alogliptin, albiglutide (possible effect on glucose control); hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone (corticosteroids); amphotericin B; rabeprazole, omeprazole; bupropion; morphine; bisacodyl; cholecalciferol; calcium phosphate
- **Minor:** doxycycline, hyoscyamine, atropine

Please refer to the package insert for key warnings and label contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or relevant publications (Evidence Level L5). There are also mechanistic concerns: thiazide-type diuretics may increase renin release, and malignant hypertension needs rapid parenteral therapy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for metolazone
- A literature and trial search specific to renovascular and malignant hypertension
- Expert review of whether the high score reflects true biology or only ontology proximity to hypertension
- Approved indication text and dosage form for the Canadian licence (DIN 00888400)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

