---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Disopyramide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report (disopyramide is gene…"
monitor_inn: "DISOPYRAMIDE"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
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

## Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Disopyramide is a class Ia antiarrhythmic drug that is marketed in Canada (as RYTHMODAN). The TxGNN model predicts it may be effective for **Tourette syndrome**, with a very high model score. However, there are currently **no clinical trials and no publications** supporting this prediction, so it rests on computational inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (disopyramide is generally known as an antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Canada Market Status | Approved but not marketed (approvals on record: 1) |
| Number of DINs | 1 (valid: 0) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, disopyramide is a class Ia antiarrhythmic that blocks sodium channels and has anticholinergic activity.

Tourette syndrome involves dysfunction of dopaminergic signalling and cortico-striato-thalamo-cortical circuits. No plausible mechanistic link to sodium channel blockade has been established. The high score (0.9986) comes from the TxGNN model (deep learning) and is not backed by any trial or literature evidence. It may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions show the same pattern. ADHD (and its inattentive subtype), trichotillomania, faciodigitogenital syndrome, specific developmental disorder, chondromyxoid fibroma and trigeminal nerve neoplasm have no identifiable mechanistic rationale. Two cardiac predictions are more biologically plausible:
- **Idiopathic neonatal atrial flutter** (rank 7): disopyramide is used for atrial and ventricular arrhythmias, but neonatal safety is a concern (anticholinergic effects, negative inotropy, proarrhythmia).
- **Multifocal atrial tachycardia** (rank 9): the only related literature concerns a different drug (lorcainide), so it is indirect evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Tourette syndrome.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02224801 | RYTHMODAN | Not specified | Not specified |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug–disease relationships in a knowledge graph, not from label text): long QT syndrome (including familial), kidney disease, liver disease, gallbladder disease, potassium deficiency, benign prostatic hyperplasia, atrial fibrillation, atrial flutter, hypotensive disorder, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, hypoglycemia, atrioventricular block, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, myocardial disorder, myocarditis, pyoureter.
- **Drug Interactions**: 100 interactions were identified in total. Examples:
  - **Major**: potassium citrate, clarithromycin, picosulfuric acid
  - **Moderate**: famotidine, hydrocortisone, dexamethasone, amphotericin B, atropine, hyoscyamine, glycopyrronium, loperamide, aprepitant, chlorpropamide, and others
  - **Minor**: cimetidine

The package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Tourette syndrome is supported only by a model score. There are no trials or literature, no plausible mechanistic link, and a substantial safety profile (QT prolongation, anticholinergic effects, cardiac contraindications) that would be hard to justify in a neurodevelopmental indication. Of the predictions listed, the cardiac arrhythmia indications (neonatal atrial flutter, multifocal atrial tachycardia) are mechanistically more reasonable but still lack direct evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Original approved indication text for the Canadian license
- Direct preclinical or clinical evidence for any predicted indication, with priority on arrhythmia-related ones
- A review of neonatal and paediatric safety if atrial flutter is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

