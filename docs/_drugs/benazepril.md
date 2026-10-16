---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Benazepril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
---

# Benazepril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Benazepril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Benazepril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the Health Canada licence records contain no indication text, so this comes from the knowledge-graph indication edges |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benazepril is an angiotensin-converting enzyme (ACE) inhibitor, its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-related kidney disease.

Malignant hypertensive renal disease is kidney damage caused by severe, accelerated hypertension. Blocking the renin-angiotensin-aldosterone system (RAAS) lowers blood pressure and may reduce pressure inside the kidney's filtering units and protein leakage in the urine, so the prediction is biologically coherent.

However, this is largely an extension of the existing hypertension indication rather than a distinct repurposing signal. The high score is not backed by any trial or publication in the data compiled for this report.

### Other Predicted Indications (all model prediction only)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.65% | L5 | RAAS involvement is coherent, but ACE inhibitors can cause acute kidney injury in bilateral renal artery stenosis or a solitary stenotic kidney, a significant safety concern |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.60% | L5 | Weak link; ACE inhibitors are not an established therapy and systemic vasodilation risks hypotension |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.60% | L5 | Theoretical link only; the retrieved papers do not involve benazepril or pulmonary hypertension |
| 5 | Braddock syndrome | 99.44% | L5 | Extremely rare; no plausible mechanistic rationale identified, and the score is likely a graph artifact |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no directly related literature available for the top predicted indication.

For rank 4 (pulmonary hypertension owing to lung disease and/or hypoxia), three publications were retrieved, but they are not relevant: they are animal or preclinical studies of traditional Chinese medicine formulas in renal failure, renal fibrosis and myocardial fibrosis, and they involve neither benazepril nor pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38803876](https://pubmed.ncbi.nlm.nih.gov/38803876/) | 2024 | Preclinical | Heliyon | Modified Zhenwu Tang and oxidative stress/hypoxic responses in chronic renal failure (herbal formula; not relevant) |
| [31007700](https://pubmed.ncbi.nlm.nih.gov/31007700/) | 2019 | Preclinical | Evid Based Complement Alternat Med | Danggui Shaoyao San and hypoxia/autophagy in rat renal fibrosis (herbal formula; not relevant) |
| [31317035](https://pubmed.ncbi.nlm.nih.gov/31317035/) | 2019 | Preclinical | Biomed Res Int | Tongxinluo and myocardial fibrosis after infarction in rats (herbal formula; not relevant) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02290332 | BENAZEPRIL | Not listed | Not listed |
| 02273918 | BENAZEPRIL | Not listed | Not listed |
| 02290340 | BENAZEPRIL | Not listed | Not listed |

All three are valid single-ingredient licences; none are cancelled.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, liver disease, hepatic coma/encephalopathy, kidney disease, anuria, pancreatitis, gallbladder disease, angioedema (including hereditary, acquired and RAAS-blocker-induced forms), systemic lupus erythematosus and other connective tissue diseases, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, neutropenia, agranulocytosis, hypotensive disorder, hyperparathyroidism and osteitis fibrosa, bone and cartilage disease, neonatal jaundice, and others. These are graph-derived associations and must be checked against the Health Canada product monograph.
- **Drug Interactions**: 100 interactions were found in total. The first 20 returned are all Moderate level and mostly involve blood-glucose-lowering agents, which may have their effect enhanced alongside ACE inhibitors. They include insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro, isophane), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), alogliptin, dapagliflozin and exenatide, as well as hydrocortisone and glycerin.
- **Indication-specific concern**: ACE inhibitors can precipitate acute kidney injury in bilateral renal artery stenosis or a solitary stenotic kidney, which is relevant to the renovascular hypertension prediction.

Please also refer to the package insert, as warning and contraindication text from the Health Canada label was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.65%), but there are no clinical trials and no relevant publications, so the evidence level is L5. The indication is also largely an extension of benazepril's existing hypertension use and is not a distinct repurposing signal. Label safety information is missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap)
- Mechanism of action data (for example from DrugBank)
- A targeted search for clinical studies of ACE inhibitors in malignant hypertensive nephrosclerosis
- Indication text and dosage forms for the three DINs
- A renal safety assessment (renal artery stenosis, hyperkalaemia, acute kidney injury) before any renovascular indication is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

