---
layout: default
title: Guanfacine
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
monitor_inn: "GUANFACINE"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "manic bipolar affective disorder", "restless legs syndrome", "Tourette syndrome"]
description: "Guanfacine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Guanfacine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Guanfacine: Faciodigitogenital syndrome
{: .text-alpha }

## One-Sentence Summary

Guanfacine is an alpha-2A adrenergic agonist, originally used for hypertension and attention deficit hyperactivity disorder (ADHD).
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome** (Aarskog-Scott syndrome), but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 12 of 12) |
| Number of DINs | 12 (valid: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, guanfacine is an alpha-2A adrenergic agonist. It strengthens prefrontal cortex signalling and is established in ADHD and hypertension.

Faciodigitogenital syndrome is an X-linked developmental disorder caused by FGD1 mutations. No plausible pharmacological link to alpha-2A adrenergic agonism has been identified. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should therefore be treated as a model artifact until proven otherwise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Twelve valid single-ingredient licences are listed. The main ones are shown below.

| DIN | Product Name |
|---------|------|
| 02523736 | APO-GUANFACINE XR |
| 02409127 | INTUNIV XR |
| 02523558 | JAMP GUANFACINE XR |
| 02523574 | JAMP GUANFACINE XR |
| 02523582 | JAMP GUANFACINE XR |

---

## Safety Considerations

The package-insert warnings and contraindications were not available in the compiled data. Please refer to the Health Canada package insert for the authoritative safety information.

- **Contraindication and caution signals from the knowledge graph (not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, myocardial infarction, coronary thrombosis, coronary artery disease, cerebrovascular disorder, chronic kidney disease, end stage renal failure, hemoglobinopathy, constipation disorder, atrioventricular block and heart block.
- **Drug interactions:** 100 interactions were identified, and 20 are detailed in the compiled data.
  - **Major:** aprepitant, dexamethasone, clarithromycin.
  - **Moderate (examples):** hydrocortisone, prednisone, prednisolone, triamcinolone, betamethasone, budesonide, metformin, cimetidine, miconazole, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), dronabinol, nabilone, mannitol, metreleptin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanism. It is most likely a network-proximity artefact, so there is no basis to advance it.

**To proceed, the following is needed:**
- Evidence of a biological link between alpha-2A adrenergic signalling and the FGD1-related pathway
- Mechanism of action data and package-insert warnings and contraindications from Health Canada
- Any preclinical or clinical data in faciodigitogenital syndrome

**Note on other predictions:** The data compiled for this report includes a much better-supported prediction for guanfacine, **Tourette syndrome**. It has one completed Phase 3 randomized, placebo-controlled trial (NCT00004376, n=35), one completed Phase 4 study (NCT01547000, n=34), and European guideline and systematic review coverage. It was rated L1 with a recommendation of Proceed with Guardrails. Those guardrails are monitoring of blood pressure and heart rate, watching for sedation, and avoiding abrupt discontinuation. If the goal is to find a viable repurposing direction for guanfacine, a separate report on Tourette syndrome is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

