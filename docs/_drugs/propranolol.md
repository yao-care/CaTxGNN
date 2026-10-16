---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Hypertension, atrial fibrillation, hypertrophic cardiomyopathy…"
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "chondroma", "cirrhotic cardiomyopathy", "cardiomyopathy"]
---

# Propranolol
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

# Propranolol: From Hypertension and Cardiac Arrhythmia to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker originally used for hypertension, atrial fibrillation, hypertrophic cardiomyopathy and infantile hemangioma.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific prediction.
The data compiled for this report show somewhat more (indirect) literature for two lower-ranked predictions, cirrhotic cardiomyopathy and cardiomyopathy, which are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, hypertrophic cardiomyopathy, hemangioma (the Canadian licence records contain no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propranolol is a non-selective beta-adrenergic blocker. Its efficacy in cardiovascular conditions such as hypertension, arrhythmia and hypertrophic cardiomyopathy is established, and it also has anti-proliferative and anti-angiogenic effects in vascular tumours such as hemangioma.

For the top-ranked prediction, no plausible mechanistic link is established. Tateyama-type distal myopathy is a rare skeletal muscle disorder, and beta-adrenergic blockade has no known pathophysiological connection to it. The high score (0.994) should therefore be treated as a model output, not as evidence of benefit. The knowledge graph also lists myopathy, muscular disease and skeletal muscle disease as contraindications for propranolol, which points in the opposite direction.

Other predictions have more plausible links:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | No plausible mechanism; no evidence |
| 3 | Hypertrophic cardiomyopathy due to intensive athletic training | 99.17% | L5 | Rationale via heart rate and contractility reduction, but athlete's heart is usually managed by detraining |
| 4 | Chondroma | 99.14% | L5 | No clear link; not angiogenesis-driven like hemangioma |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L4 | Mixed, indirect evidence (3 publications) |
| 6 | Cardiomyopathy | 99.12% | L3 | Largely overlaps with the existing hypertrophic cardiomyopathy use |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the five predictions listed above.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (distal myopathy, Tateyama type).

Indirect literature exists for lower-ranked predictions. For cirrhotic cardiomyopathy (rank 5):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Clinical/cohort study | Frontiers in Pharmacology | Propranolol may correct prolonged QT intervals in patients with cirrhosis |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Clinical study | PLoS One | Beta-blocker cardiovascular effects are blunted in cirrhosis; effect varies with disease severity |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical/observational | Journal of Hepatology | Non-selective beta-blockers may impair circulatory and renal function in refractory ascites |

For cardiomyopathy (rank 6), the most relevant publications are older small haemodynamic studies in hypertrophic cardiomyopathy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical physiology study | European Heart Journal | Effects of IV propranolol and verapamil on diastolic stiffness in HCM |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical haemodynamic study | British Heart Journal | Nifedipine plus propranolol appeared superior to nifedipine alone in 12 patients with obstructive HCM |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical study | American Journal of Cardiology | Propranolol and arrhythmia in HCM |
| [28431779](https://pubmed.ncbi.nlm.nih.gov/28431779/) | 2017 | Review/monograph | Profiles of Drug Substances, Excipients, and Related Methodology | Overview of propranolol uses, including hypertension, arrhythmia and hypertrophic cardiomyopathy |
| [1094291](https://pubmed.ncbi.nlm.nih.gov/1094291/) | 1975 | Review | New England Journal of Medicine | General drug therapy review of propranolol |

Many other records for this prediction are generic "Propranolol" monographs with low specificity.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02491893 | LUPIN-PROPRANOLOL LA | Not specified | Not specified |
| 02550830 | PRZ-PROPRANOLOL | Not specified | Not specified |
| 00740675 | TEVA-PROPRANOLOL | Not specified | Not specified |
| 02225883 | PROPRANOLOL HYDROCHLORIDE INJECTION USP | Injection | Not specified |
| 02457857 | HEMANGIOL | Not specified | Not specified |

All 13 licences are valid single-ingredient products; the five above are shown as examples.

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease links, not label text): myopathy, muscular disease and skeletal muscle disease, familial periodic paralysis, myasthenia gravis, diabetes mellitus and diabetic ketoacidosis, kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, bronchitis, systemic lupus erythematosus, gout, hypercalcemia, hyperparathyroidism, anxiety and neurotic disorders, among others. The muscle disease entries are directly relevant to the top predictions.
- **Drug Interactions**: 100 interactions were recorded. Major: epinephrine. Moderate examples: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, atropine, hyoscyamine, methscopolamine, bupropion, morphine, cimetidine, canagliflozin, chlorpropamide, lorcaserin, calcium acetate and calcium phosphate. Minor examples: aspirin, ascorbic acid and magnesium oxide.
- **Cirrhosis**: the cirrhotic cardiomyopathy literature suggests non-selective beta-blockers may impair circulatory and renal function in refractory ascites.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on model score alone (L5), with no trials, no literature, no plausible mechanism, and a knowledge-graph contraindication in muscle disease. The only predictions with some supporting literature (cirrhotic cardiomyopathy, and general cardiomyopathy) are either mixed in benefit-risk or largely overlap with existing approved use.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text, dosage forms and manufacturers for the Canadian licences
- For distal myopathy, Tateyama type: any preclinical or clinical rationale; otherwise deprioritise
- For cirrhotic cardiomyopathy: a controlled study clarifying benefit-risk (QT correction versus circulatory and renal harm), which may be a more productive research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

