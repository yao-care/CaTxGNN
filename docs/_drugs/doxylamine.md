---
layout: default
title: Doxylamine
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Doxylamine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis (other known indications include vasomotor rhinitis…"
---

# Doxylamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Doxylamine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Doxylamine is a first-generation H1 antihistamine, originally used for allergic rhinitis, the common cold and related upper-airway and allergic conditions.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone, and because urticaria is already among the drug's known indications, it adds little novelty.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other known indications include vasomotor rhinitis, pharyngitis, common cold, urticaria and angioedema) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, doxylamine is a first-generation H1 antihistamine. It blocks H1 receptors on cutaneous vessels and sensory nerves, and it also has an anticholinergic (drying) effect.

Urticaria and angioedema are already among doxylamine's known indications, and allergic urticaria is a subtype of urticaria. This closeness to existing indications probably explains the very high TxGNN score (99.85%). The prediction is therefore largely a relabeling of an existing use rather than a truly new repurposing opportunity.

Other predicted indications follow the same pattern:
- **Nasal cavity disease** (99.36%): a broad category that overlaps with the allergic and vasomotor rhinitis indications. It is too nonspecific to support a defined hypothesis.
- **Acute laryngopharyngitis** (99.34%): any benefit would likely be symptomatic only, from reduced secretions. The condition is mostly infectious, and the drying effect could irritate the airway.
- **Cold urticaria** (99.26%): H1 antihistamines are a plausible class. Guidelines generally prefer second-generation agents because of their better sedation profile, so any evaluation would need to be compared against them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Doxylamine has 20 valid single-ingredient authorizations in Canada. Dosage form and approved indication text were not available for these products. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 00609129 | DICLECTIN |
| 02413248 | APO-DOXYLAMINE/B6 |
| 02552574 | ALOG-DOXYLAMINE/PYRIDOXINE |
| 02485443 | ROBITUSSIN HONEY COUGH & COLD NIGHTTIME |
| 02406187 | PMS-DOXYLAMINE-PYRIDOXINE |

---

## Safety Considerations

**Drug Interactions** (100 interactions found; main ones shown):
- **Major**: potassium chloride and potassium citrate.
- **Moderate**: several anticholinergic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, clidinium, propantheline, methscopolamine, mepenzolate), opioids (morphine, opium, loperamide), cannabinoids (dronabinol, nabilone), metoclopramide and eluxadoline.

**Disease-related cautions** (from knowledge-graph contraindication associations, not from label text):
- Cardiovascular: hypertension, coronary artery disease, myocardial infarction, atherosclerosis and ventricular tachycardia.
- Eye: angle-closure glaucoma and ocular hypertension.
- Urinary: benign prostatic hyperplasia and bladder neck obstruction.
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism and thyrotoxicosis.
- Liver and digestive: liver disease, liver failure, pancreatitis, gallbladder disease and peptic ulcer disease.
- Other: substance abuse/dependence, paracetamol poisoning and hemoglobinopathy.

Package insert warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or publications for allergic urticaria. Urticaria is already a known indication, so the repurposing value is limited. A sedating first-generation antihistamine would also have to be justified against second-generation alternatives.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or literature evidence specific to allergic urticaria
- Comparison with second-generation H1 antihistamines
- Dosage form and approved indication details for the Canadian products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

