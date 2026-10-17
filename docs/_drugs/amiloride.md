---
layout: default
title: Amiloride
parent: Moderate Evidence (L3-L4)
nav_order: 50
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Amiloride: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Amiloride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Amiloride: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but the evidence is thin: **no clinical trials** and only **1 publication** (a general review of mineralocorticoid hypertension) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (the approved indication text for the Canadian licences is not available, so this comes from the knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, amiloride blocks the epithelial sodium channel (ENaC) in the distal nephron, which reduces sodium reabsorption and spares potassium. Its efficacy in hypertension and heart failure is established.

Renovascular hypertension is driven by activation of the renin-angiotensin-aldosterone axis. Amiloride is also used in mineralocorticoid-driven hypertension, so a mechanistic link is plausible. However, malignant renovascular hypertension is an acute, severe condition normally managed by revascularization and parenteral agents. The fit is therefore plausible but not specific. The high TxGNN score most likely reflects the drug's existing hypertension indication rather than new evidence.

Other predictions for this drug are also weakly supported:
- **Malignant hypertensive renal disease** (99.82%): no trials or literature (L5). Hyperkalaemia risk in renal impairment is a major concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.81%): L4 evidence, mostly preclinical. It suggests a possible role for ENaC/ASIC1/NHE1 inhibition, but several retrieved papers are off-topic and the therapeutic direction is unclear.
- **Chronic pulmonary heart disease** (99.68%): L3 evidence, indirect, from general congestive heart failure studies. This is the most clinically grounded of the alternatives and may be worth a closer look.
- **Pulmonary hypertension with unclear multifactorial mechanism** and **Braddock syndrome**: model prediction only (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Overview of investigating mineralocorticoid hypertension. Hypokalaemic hypertension with low plasma renin is typical, and primary aldosteronism is the most frequent cause. It is not specific to renovascular hypertension. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02249510 | MIDAMOR | Not specified | Not specified |
| 00784400 | AA-AMILZIDE | Not specified | Not specified |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are not label text): kidney disease, anuria, liver disease, hepatic coma/encephalopathy, diabetes mellitus, diabetic ketoacidosis, diabetic nephropathy, gout, potassium deficiency disease, acidosis disorders (including lactic acidosis), pancreatitis, gallbladder disease, systemic lupus erythematosus, hyperparathyroidism, and others.
- **Drug Interactions**: 100 interactions were identified. Those listed include:
  - *Moderate*: metformin; corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone); SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin); exenatide; bupropion; dronabinol; and laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose).
  - *Minor*: doxycycline, amoxicillin, cimetidine.
- **Hyperkalaemia**: a published case report describes severe hyperkalaemia in an elderly patient (with trimethoprim-sulfamethoxazole). This is especially relevant for renal indications.

Please also refer to the package insert, as the label warnings were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a general review. There are no clinical trials, and the mechanistic link is plausible but nonspecific. The clinical setting (an acute, severe condition managed with other approaches) and the hyperkalaemia and renal risks do not favour advancing at this stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Direct clinical or mechanistic evidence in renovascular hypertension
- Consideration of chronic pulmonary heart disease as a better-supported alternative, with indication-specific evidence beyond general heart failure studies
- A hyperkalaemia and renal function monitoring plan for any renal-involved population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

