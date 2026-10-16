---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 942
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Triamterene: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, hypertensive disorder, congestive heart failure"
monitor_inn: "TRIAMTERENE"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Triamterene
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

# Triamterene: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, congestive heart failure (the Health Canada licence records contain no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron. It promotes sodium and water excretion while retaining potassium. Its efficacy in hypertension and heart failure is established.

The prediction for malignant hypertensive renal disease is plausible only by extension: it is a severe form of hypertension with kidney involvement, and diuresis and volume reduction can lower blood pressure. However, the picture is less favourable than the score suggests:

- Malignant hypertension needs rapid, controlled blood pressure reduction, and triamterene is not a suitable agent for that.
- Hyperkalemia risk is higher in renal impairment, and the knowledge graph lists kidney disease and anuria among contraindications.
- No trials or literature support this use.

Other predictions in the list follow the same pattern:

- **Malignant renovascular hypertension** (99.89%): driven mainly by the renin-angiotensin-aldosterone system, and combining a potassium-sparing diuretic with RAAS-acting agents increases hyperkalemia risk.
- **Pulmonary hypertension** (99.88%): the high scores likely reflect a shared hypertension node in the ontology, not a pulmonary vascular mechanism.
- **Braddock syndrome** (99.84%): no mechanistic rationale is identifiable, and the score is likely a graph-connectivity artifact.
- **Chronic pulmonary heart disease** (99.75%): the most credible secondary candidate, because it involves right-sided heart failure with fluid retention and triamterene is already used as a diuretic in heart failure. It has indirect literature support only (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the top predicted indication. Publications retrieved for lower-ranked predictions are shown below for reference, and all of them are indirect evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Review (as classified; the abstract describes a randomized crossover study) | Dtsch Med Wochenschr | In 16 heart failure patients, a hydrochlorothiazide + triamterene combination was compared with a digitalis glycoside. Relevant to chronic pulmonary heart disease only indirectly. |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Clinical hemodynamic study | Fortschr Med | In 12 patients with chronic heart failure (NYHA II-III), a verapamil/triamterene/hydrochlorothiazide combination over 4 weeks lowered blood pressure and heart rate. It is a combination study and not specific to triamterene. |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Low-pressure pulmonary edema after a triamterene-hydrochlorothiazide tablet, attributed to the hydrochlorothiazide component. This is an adverse event report and not evidence of efficacy. |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Preclinical (animal physiology) | J Physiol | Rat colon electrophysiology study with no clinical relevance to this indication. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00441775 | APO-TRIAZIDE | Not specified | Not specified |
| 00532657 | TEVA-TRIAMTERENE/HCTZ | Not specified | Not specified |

Both products are listed as valid. Their names indicate triamterene/hydrochlorothiazide combination products.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The TxGNN knowledge graph links triamterene to many contraindicated conditions. Key groups are:
  - Kidney and urinary: kidney disease, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
  - Liver: liver failure, liver disease, hepatic coma, hepatic encephalopathy
  - Metabolic: diabetes mellitus (type 1 and type 2), diabetic ketoacidosis, gout, hypercalcemia, acidosis, lactic acidosis, hyperparathyroidism
  - Other: pancreatitis, gallbladder disease, systemic lupus erythematosus, folic acid deficiency anemia, neonatal jaundice
- **Drug Interactions**: 100 interactions were found. The main ones among the 20 detailed entries are:
  - **Major**: potassium citrate (additive hyperkalemia risk)
  - **Moderate**: metformin, bupropion, morphine, dronabinol, canagliflozin, dapagliflozin, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), and laxatives or bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes)
  - **Minor**: famotidine, ranitidine, cimetidine, doxycycline, minocycline

Warnings and contraindications from the Health Canada package insert were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease is supported only by the model score, with no trials or literature, and it conflicts with clinical reality. Triamterene is not suited to the rapid blood pressure control this condition needs, and its hyperkalemia risk is higher with renal impairment. Among the other predictions, chronic pulmonary heart disease (L4, "Research Question") is the more credible lead, but its evidence is indirect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Direct clinical or mechanistic evidence for the predicted indication, or a refocus on chronic pulmonary heart disease with targeted literature review
- Indication text and dosage form details for the two Canadian licences
- A hyperkalemia and renal function risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

