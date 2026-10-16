---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Diltiazem: predicted new indication Obsolete susceptibility to ischemic stroke (evidence level L5). Approved use: Hypertensive disorder / hypertension, atrial fibrillation…"
monitor_inn: "Diltiazem"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Hypertension to Obsolete Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete susceptibility to ischemic stroke**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (Health Canada indication text is not available, so these come from the knowledge graph) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diltiazem is a non-dihydropyridine L-type calcium channel blocker with antihypertensive effects. Its efficacy in hypertension and cardiac rhythm disorders is established, and mechanistically it may be applicable to stroke risk reduction.

Blood pressure control is a recognized way to lower stroke risk, so an indirect rationale exists. However, this is already covered by the existing hypertension indication and does not show a distinct repurposing benefit.

The predicted disease term is also labelled "obsolete", which suggests a deprecated ontology entry that may map to a broader or renamed concept (for example, ischemic stroke risk). The high score (99.08%) is a model prediction only and is not backed by any trial or publication in the data compiled for this report. The term should be clarified before further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Diltiazem has 20 valid single-ingredient licences in Canada and no cancelled ones. Dosage form and approved indication text are not available in the data compiled for this report. Five main authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02528061 | JAMP DILTIAZEM CD |
| 02546450 | M-DILTIAZEM T |
| 02271656 | TEVA-DILTIAZEM HCL ER |
| 02370492 | TEVA-DILTIAZEM T |
| 02256770 | TIAZAC XC |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** Several disease associations are recorded, including:
  - Cardiac conduction and rhythm: atrioventricular block, sick sinus syndrome, Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia
  - Structural and haemodynamic: aortic stenosis, hypertrophic cardiomyopathy, hypotensive disorder, renal artery obstruction
  - Blood: neutropenia, agranulocytosis
  - Angioedema (several forms)
  - Organ disease: kidney disease, liver disease, gallbladder disease
  - Other: connective tissue, bone and cartilage disease

  These are database associations and must be verified against the official label.
- **Drug Interactions:** 100 interactions were recorded. The only one rated Major in the sample is **loperamide**. Moderate-level interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Other drugs: pioglitazone, canagliflozin, bupropion, aprepitant, morphine, acetylsalicylic acid
  - Calcium salts: carbonate, chloride, citrate, acetate and others

Label warnings and contraindications from the Health Canada package insert are not available, so please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), the target disease term is obsolete and unclear, and the only plausible mechanism (blood pressure lowering) is already covered by the existing hypertension indication. The safety review also cannot proceed without the package insert.

**To proceed, the following is needed:**
- Clarify which current disease concept the obsolete term maps to (e.g., ischemic stroke or stroke risk)
- Mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications
- A literature and trial search on diltiazem and stroke prevention or outcomes
- Evidence that any benefit is independent of blood pressure lowering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

