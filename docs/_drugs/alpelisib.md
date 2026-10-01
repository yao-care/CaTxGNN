---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Alpelisib
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

# Alpelisib: From HR+/HER2- Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (marketed in Canada as PIQRAY) is a PI3Kα-selective inhibitor, used in HR+/HER2- breast cancer with a PIK3CA mutation according to the trials in this Evidence Pack.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but the evidence is prediction only: **1 registered trial** (breast cancer, not pulmonary hypertension) and **2 publications**, both raising safety concerns rather than showing benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records; the related trials point to HR+/HER2- advanced breast cancer with a PIK3CA mutation |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database. Alpelisib is known to be a PI3Kα-selective inhibitor. PI3K/AKT signaling is implicated in the proliferation and remodeling of pulmonary vascular smooth muscle, so a mechanistic link to pulmonary hypertension is plausible in principle.

However, the retrieved evidence does not show any clinical benefit. It points the other way:

- A case report describes alpelisib-induced interstitial lung disease in a patient with advanced breast cancer.
- A preclinical study found that PI3Kα pathway inhibition combined with doxorubicin caused biventricular atrophy and right ventricular dysfunction.

Both signals are concerning for a disease that involves the pulmonary vasculature and the right heart. The high TxGNN score reflects a knowledge-graph association and has not been backed by any study of alpelisib in pulmonary hypertension.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A (observational) | Completed | 435 | REASSURE: European real-world retrospective cohort of ribociclib or alpelisib in HR+/HER2- advanced or metastatic breast cancer. It does not evaluate pulmonary hypertension (relevance grade C). |

No registered trial tests alpelisib in pulmonary hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer, a pulmonary safety signal |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical (animal) | J Am Heart Assoc | PI3Kα inhibition with doxorubicin caused biventricular atrophy, remodeling and right ventricular dysfunction, a cardiac safety signal |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2497085 | PIQRAY |
| 2497077 | PIQRAY |
| 2497069 | PIQRAY |

Dosage form, manufacturer and approved-indication text were not available in the license records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kα inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood glucose monitoring is relevant, since hyperglycemia is an on-target toxicity (see the metformin prevention study NCT04300790); otherwise refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Formal warnings, contraindications and interaction data were not available. Please refer to the package insert for safety information.

Signals from the retrieved evidence:
- **Pulmonary:** alpelisib-associated interstitial lung disease has been reported.
- **Cardiac:** preclinical data show right ventricular dysfunction when PI3Kα inhibition is combined with doxorubicin.
- **Metabolic:** hyperglycemia is a known on-target toxicity, and metformin has been studied to prevent it.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is prediction only (L5). There are no relevant trials, and the only literature points to pulmonary and cardiac safety risks rather than benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism-of-action data from DrugBank
- Preclinical evidence that PI3Kα inhibition improves pulmonary vascular remodeling, with an assessment of pulmonary and right-heart toxicity
- Original approved-indication text from the Canadian license records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

