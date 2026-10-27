---
layout: default
title: Siponimod
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Siponimod: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not specified in the licence data compiled for this report"
monitor_inn: "Siponimod"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "Prinzmetal angina", "rheumatoid arthritis", "atrophoderma vermiculata", "ulerythema ophryogenesis", "myelodysplastic syndrome"]
---

# Siponimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Siponimod: From Its Approved Use to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Siponimod is a selective S1P1/S5 receptor modulator marketed in Canada under the brand name MAYZENT. The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the licence data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Siponimod is known as a selective modulator of the S1P1 and S5 receptors. S1P signalling affects lymphocyte trafficking, vascular endothelial barrier function and vascular remodelling, so a biological rationale for pulmonary vascular disease is conceivable.

However, this link is speculative. S1P1 modulators are associated with bradycardia and other cardiovascular effects, which is a concern in a cardiopulmonary condition. The high TxGNN score reflects network-based computational similarity and is not evidence of clinical benefit.

Other top-ranked predictions for this drug are also worth noting. Rheumatoid arthritis (rank 7, score 99.16%) is the most biologically plausible, because S1P signalling regulates immune cell trafficking. A 2021 review supports this mechanism. It is a research question only, and no rheumatoid arthritis trials exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

For context, the migraine-related predictions (ranks 2, 4 and 5) are linked only to indirect literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35382764](https://pubmed.ncbi.nlm.nih.gov/35382764/) | 2022 | Review (case report) | BMC Anesthesiology | A patient with multiple sclerosis had remission of comorbid migraine after starting interferon β1a. Siponimod is discussed only as an immunomodulator therapy, and this is not evidence of efficacy. |
| [28703543](https://pubmed.ncbi.nlm.nih.gov/28703543/) | 2017 | Review | Revue Médicale Suisse | A general neurology annual update. No specific link to siponimod in migraine. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02496429 | MAYZENT | Not specified | Not specified |
| 02496437 | MAYZENT | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interacting drugs in total. The 20 reviewed for this report include many rated Major, such as:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- Acid reducers: famotidine, ranitidine, cimetidine
- Antiemetics and related drugs: aprepitant, dolasetron, palonosetron
- Anti-infectives: clarithromycin, levofloxacin
- Anabolic steroid: oxandrolone

Moderate-level interactions include loperamide, bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate and naltrexone.

**Class-related concern:** S1P1 modulators are associated with bradycardia and cardiac conduction effects. This is relevant to cardiovascular conditions such as pulmonary hypertension. Lymphopenia is also expected, and it is relevant for infection risk.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pulmonary hypertension rests only on a computational score. There are no clinical trials or publications, and the drug's known cardiovascular effects raise a safety concern. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are a blocking gap for safety screening
- Original approved indication text and dosage form for the two DINs
- Mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic studies of S1P1/S5 modulation in pulmonary vascular disease
- A cardiovascular safety assessment, especially for heart rate and conduction effects
- Consider prioritising rheumatoid arthritis for exploratory preclinical investigation, as it has the most plausible mechanistic rationale among the predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

