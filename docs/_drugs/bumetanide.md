---
layout: default
title: Bumetanide
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "BUMETANIDE"
predicted_indications: ["acute pulmonary heart disease"]
description: "Bumetanide: predicted new indication Acute pulmonary heart disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Bumetanide: Acute pulmonary heart disease
{: .text-alpha }

## One-Sentence Summary

Bumetanide is a loop diuretic used to relieve fluid overload in heart failure and related conditions. The TxGNN model predicts it may be useful for **acute pulmonary heart disease**, but the evidence level is **L5**: there are no registered clinical trials and no study that tests bumetanide in this disease. The literature compiled for this report concerns left-sided heart failure and general diuretic use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bumetanide is a loop diuretic that inhibits the Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb of the loop of Henle. This produces rapid sodium and water excretion, which reduces preload, venous congestion and fluid overload in the lungs and body.

Acute pulmonary heart disease (acute cor pulmonale, for example after a massive pulmonary embolism) involves right ventricular pressure overload and dilation, with systemic venous congestion. Decongestive diuresis is therefore mechanistically plausible as supportive care for right-sided volume overload.

There are important limits. Bumetanide does not treat the underlying cause (obstruction of the pulmonary vessels or raised pulmonary vascular resistance). Aggressive diuresis can also lower right ventricular preload and cardiac output when the right ventricle depends on preload, which creates a risk. The high score most likely reflects the drug's close relationship to heart failure treatment rather than disease-specific evidence. Detailed mechanism-of-action data were not available in the data compiled for this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these studies tests bumetanide in acute pulmonary heart disease. They address heart failure and diuretics in general.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Small haemodynamic study | Br J Clin Pharmacol | IV bumetanide in 24 patients with coronary disease and acute or chronic left-sided heart failure raised blood pressure and vascular resistance, and lowered cardiac index and pulmonary artery occluded pressure |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Bumetanide is a potent loop diuretic for oedema from heart failure, liver and kidney disease, and acute pulmonary congestion |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews treatment of acute heart failure, where diuretics are the mainstay for most patients |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Compares pharmacokinetics, safety, efficacy and cost of loop diuretics |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohort | Am J Emerg Med | Epidemiology of heart failure presentations to US emergency departments, 2016–2023 |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00728284 | BURINEX | Not specified | Not specified |
| 00728276 | BURINEX | Not specified | Not specified |

Both licences are valid single-ingredient products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible for right-sided volume overload, but no study tests bumetanide in acute pulmonary heart disease, so the evidence level is L5. Reducing preload could also harm a patient with a preload-dependent right ventricle, and the high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Studies or case series of loop diuretics in acute cor pulmonale or right ventricular failure
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data
- A haemodynamic safety assessment for patients with preload-dependent right ventricular failure

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

