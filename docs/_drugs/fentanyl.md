---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 381
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Fentanyl: From an Opioid Analgesic to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist marketed in Canada in injectable, patch and buccal forms. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis** (a second prediction, Tourette syndrome, is also noted below). There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (Canadian license records contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is generally known as a mu-opioid receptor agonist used for pain relief and anaesthesia. Opioids can influence vasopressin release and produce antidiuretic effects, which may be the reason the model links fentanyl to antidiuresis-related conditions.

However, nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2) in the kidney. It occurs independently of vasopressin secretion, so an opioid acting on vasopressin release has no clear therapeutic role. The prediction may be a network artifact, for example a link through shared water-balance nodes in the knowledge graph. Opioid-associated antidiuresis could also worsen hyponatraemia, which is a possible safety concern.

**Second prediction: Tourette syndrome (score 99.05%, evidence level L5).** Tourette syndrome involves dysregulation of cortico-striato-thalamo-cortical circuits and dopamine signalling. The endogenous opioid system has been proposed to modulate tics, and a few small studies have explored opioid-system modulators. There are no supporting data for fentanyl itself, a potent, short-acting agonist with abuse liability, respiratory depression risk and tolerance. Any further consideration would need preclinical or mechanistic support and a favourable risk-benefit case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Fentanyl has 20 valid single-ingredient licences in Canada. Dosage form, manufacturer and approved indication text are not available for these records. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02408015 | FENTORA | Not available | Not available |
| 02496186 | FENTANYL INJECTION BP | Not available | Not available |
| 02506963 | FENTANYL CITRATE INJECTION | Not available | Not available |
| 02282976 | TEVA-FENTANYL | Not available | Not available |
| 02327163 | SANDOZ FENTANYL PATCH | Not available | Not available |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links fentanyl to contraindication-type relationships with many conditions, including:
  - Cardiovascular: hypertension, hypotensive disorder, orthostatic hypotension, long QT syndrome, torsades de pointes.
  - Respiratory: chronic obstructive pulmonary disease, asthma.
  - Hepatic, renal and digestive: liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, inflammatory bowel disease.
  - Neurological and psychiatric: basal ganglia disease, anxiety disorder, substance abuse/dependence.
  - Other: benign prostatic hyperplasia, potassium deficiency disease.

  These come from model data and should be verified against the official product monograph.
- **Drug Interactions:** The interaction query returned 100 records. Among those listed, the **Major** interactions are alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dexfenfluramine, dolasetron, fenfluramine, granisetron and lorcaserin. **Moderate** interactions include atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycerol phenylbutyrate, glycopyrronium and hyoscyamine.
- **Indication-specific concern:** Opioid-associated antidiuresis could worsen hyponatraemia in the predicted nephrogenic SIAD setting.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions (nephrogenic SIAD and Tourette syndrome) are supported only by graph-based scores, with no clinical trials or literature. The mechanistic link for nephrogenic SIAD is implausible, and fentanyl's safety profile (abuse liability, respiratory depression, tolerance, many interactions) raises the bar for any repurposing case.

**To proceed, the following is needed:**
- Official Health Canada product monograph warnings, contraindications and approved indications. This is currently a blocking gap for safety screening.
- Mechanism of action data (for example from DrugBank).
- Preclinical or mechanistic evidence supporting a therapeutic role in the predicted indications.
- A documented risk-benefit rationale, particularly regarding hyponatraemia (nephrogenic SIAD) and abuse and respiratory risks (Tourette syndrome).
- Assessment of route and formulation compatibility with the proposed indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

