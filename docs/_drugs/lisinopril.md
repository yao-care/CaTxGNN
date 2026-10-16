---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lisinopril: predicted new indication Posteroinferior myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "LISINOPRIL"
predicted_indications: ["posteroinferior myocardial infarction", "posterolateral myocardial infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant renovascular hypertension", "malignant hypertensive renal disease", "septal myocardial infarction", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lisinopril: From Hypertension and Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used for hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**,
but **no clinical trials and no publications** currently support this specific prediction. The high score largely reflects the existing myocardial infarction indication rather than a new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge-graph indication list; Canadian label text was not available) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lisinopril belongs to the ACE inhibitor class. Its efficacy in hypertension and myocardial infarction is established, and ACE inhibition is known to reduce remodeling after a heart attack.

Posteroinferior myocardial infarction is an anatomical subtype of myocardial infarction, which is already an existing indication. The high TxGNN score therefore mostly reflects overlap with the current label, not a genuinely new use.

Other top predictions follow a similar pattern. Posterolateral and septal myocardial infarction, malignant renovascular hypertension and malignant hypertensive renal disease are subtypes of conditions already treated with the drug. A few predictions are more distinct (pulmonary hypertension, chronic pulmonary heart disease, and a rare genetic syndrome), and these are discussed below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posteroinferior myocardial infarction, or for any of the other top 10 predicted indications.

---

## Literature Evidence

No related literature is available for posteroinferior myocardial infarction. The literature retrieved for other predicted indications is summarized below for reference.

**Pulmonary hypertension owing to lung disease and/or hypoxia (rank 4):** most retrieved items are off-target and none provides clinical evidence for lisinopril in this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10456287](https://pubmed.ncbi.nlm.nih.gov/10456287/) | 1999 | Preclinical (isolated vessels) | Fundam Clin Pharmacol | In rat pulmonary arteries, endothelin rather than angiotensin II drove the hypoxic contractile response, which argues against an ACE-inhibitor benefit |
| [8016291](https://pubmed.ncbi.nlm.nih.gov/8016291/) | 1994 | Not classified | P R Health Sci J | Acute sublingual ACE inhibitors, including lisinopril, transiently raised pulmonary artery pressure and vascular resistance during catheterization |
| [8405086](https://pubmed.ncbi.nlm.nih.gov/8405086/) | 1993 | Not classified | Eur J Pharmacol | Lisinopril improved recovery during reoxygenation in cultured cardiomyocytes |

**Chronic pulmonary heart disease (rank 9):** the only lisinopril-specific clinical papers, both small and of unconfirmed design.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (small, design unconfirmed) | Kardiologiia | Lisinopril 10 mg/day attenuated pulmonary hypertension and improved right ventricular function in heart failure patients with ischemic heart disease and COPD |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (small, design unconfirmed) | Probl Tuberk Bolezn Legk | Lisinopril treatment in chronic cor pulmonale (no abstract available) |
| [26895877](https://pubmed.ncbi.nlm.nih.gov/26895877/) | 2016 | Review/Commentary | Eur J Pediatr | Argues that ACE inhibitors, beta-blockers and mineralocorticoid antagonists should be used in children with chronic heart failure despite limited data |

**Septal myocardial infarction (rank 7):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | ACE inhibitor plus coenzyme Q10 as adjunctive treatment in a patient with ventricular septal rupture after myocardial infarction; relevance to lisinopril specifically cannot be confirmed |

---

## Canada Market Information

Lisinopril is marketed in Canada with 20 valid single-ingredient authorizations. Dosage form and approved indication text were not available in the data compiled for this report. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02049333 | ZESTRIL | Not available | Not available |
| 02386232 | LISINOPRIL | Not available | Not available |
| 02394499 | AURO-LISINOPRIL | Not available | Not available |
| 02394480 | AURO-LISINOPRIL | Not available | Not available |
| 02386240 | LISINOPRIL | Not available | Not available |

---

## Safety Considerations

Package insert warnings and contraindications were not available. The following comes from the knowledge graph and drug-interaction databases and is not label text.

- **Disease-level contraindication signals (knowledge graph):** angioedema (including hereditary, acquired and ACE-inhibitor-induced forms), kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, aortic stenosis and aortic valve disease, hypotensive disorders, neutropenia and agranulocytosis, systemic lupus erythematosus and connective tissue disease, potassium deficiency, hyperparathyroidism, and bone disease.
- **Drug interactions:** 100 interactions were identified. The two **Major** ones in the sample reviewed are potassium citrate and potassium bicarbonate (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel-preparation products (picosulfuric acid, polyethylene glycol with electrolytes).
- **Pulmonary hypertension signal:** one paper reported that acute sublingual lisinopril transiently raised pulmonary artery pressure and resistance, which warrants caution if this direction is explored.
- **Renal artery stenosis:** ACE inhibitors carry risk in bilateral renal artery stenosis, which is relevant to the renovascular hypertension predictions.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are mostly anatomical subtypes of conditions where lisinopril is already used, so they offer little new repurposing value. For the genuinely new directions (pulmonary hypertension, chronic pulmonary heart disease), the evidence is limited to small studies of unconfirmed design and animal data, and no trials are registered. The evidence level is L5 for the lead prediction, and chronic pulmonary heart disease reaches only L4 as a research question.

**To proceed, the following is needed:**
- Canadian package insert warnings, contraindications and approved indication text (currently a blocking gap for safety screening)
- Mechanism of action data (DrugBank)
- Confirmation of whether the subtype predictions are already covered by the existing myocardial infarction and hypertension labels, which would make them non-incremental
- For chronic pulmonary heart disease, retrieval and appraisal of the full text of PMID 14524095 and 17047621 to confirm study design and size, followed by a controlled trial if the signal holds
- No further work is suggested for Braddock syndrome or the COL4A1-related familial hematuria syndrome, where no mechanistic link or evidence was found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

