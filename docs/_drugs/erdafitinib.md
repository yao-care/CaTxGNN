---
layout: default
title: Erdafitinib
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Erdafitinib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Erdafitinib"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia", "Mills syndrome"]
---

# Erdafitinib
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

## Erdafitinib: From Its Marketed Use to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Erdafitinib is a pan-FGFR (FGFR1-4) tyrosine kinase inhibitor marketed in Canada as BALVERSA. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, erdafitinib is a pan-FGFR (FGFR1-4) tyrosine kinase inhibitor.

FGF/FGFR signaling has been implicated in pulmonary vascular remodeling and smooth muscle proliferation. This offers a plausible but unvalidated rationale for pulmonary hypertension. The TxGNN score is very high (0.994, rank 10,953), but it is a model prediction only.

Safety is a concern. FGFR inhibitors are known to cause hyperphosphatemia, ocular toxicity, and nail and skin effects. The net benefit in a cardiopulmonary population is unknown.

Other predictions in the top 10 are weaker or lack a clear mechanistic link:
- **Rheumatoid arthritis** is the only one with any literature. That literature is a general kinase inhibitor review, not RA-specific evidence.
- **Kyphoscoliotic heart disease, amenorrhea, ALS (and related entries), brachydactyly-syndactyly syndrome, axial spondylometaphyseal dysplasia, and Mills syndrome** have no supporting trials or literature.
- **For several of these**, inhibiting FGFR could be ineffective or even harmful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

The only literature in the top 10 predictions is for rheumatoid arthritis (rank 4). It is general context, not evidence of efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Review | Pharmacological Research | 2020 update on properties of FDA-approved small molecule kinase inhibitors, including erdafitinib. It has no RA-specific clinical data. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02493233 | BALVERSA | Not specified | Not specified |
| 02493225 | BALVERSA | Not specified | Not specified |
| 02493217 | BALVERSA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor, FGFR1-4) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Serum phosphate, ocular examination, and skin and nail assessment, based on the known class effects of FGFR inhibitors. Please also refer to the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen was completed and returned 100 interacting drugs. The 20 entries reviewed include:
  - **Major**: cholecalciferol, calcitriol, calcifediol, calcium phosphate, calcium acetate, dexamethasone, clarithromycin, magnesium oxide, magnesium sulfate, magnesium chloride.
  - **Moderate**: metformin, loperamide, saxagliptin, linagliptin, empagliflozin, eliglustat, naldemedine, naloxegol, prucalopride, rifaximin.
- **Class-related concerns**: Hyperphosphatemia, ocular toxicity, and nail and skin effects are known with FGFR inhibitors. The interactions with vitamin D and calcium or phosphate-containing products are consistent with the phosphate-related concern.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pulmonary hypertension has a very high model score but no clinical trials or literature behind it (evidence level L5). The mechanistic rationale is plausible but unvalidated. The known toxicity profile of FGFR inhibitors adds uncertainty for a cardiopulmonary population.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical evidence for FGFR inhibition in pulmonary vascular remodeling
- A benefit-risk assessment of hyperphosphatemia, ocular, and skin and nail toxicity in patients with pulmonary hypertension
- Review of the major drug interactions, particularly with vitamin D, calcium, and magnesium products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

