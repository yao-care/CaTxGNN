---
layout: default
title: Evinacumab
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Evinacumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not stated in the Canadian licence record"
---

# Evinacumab
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

# Evinacumab: From Lipid Disorder Therapy to Diabetic Cataract

## One-Sentence Summary

Evinacumab (marketed in Canada as EVKEEZA) is an anti-ANGPTL3 monoclonal antibody that lowers blood lipids. The TxGNN model predicts it may be effective for **diabetic cataract** with a very high score, but **no clinical trials and no publications** currently support this specific prediction. The only related signal in the data compiled for this report is one preclinical paper on **diabetic retinopathy**, a neighbouring eye condition that ranks 10th among the predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Evinacumab blocks ANGPTL3, a protein that restrains lipoprotein lipase and endothelial lipase. By blocking it, the drug lowers LDL-C, triglycerides and HDL-C. Detailed mechanism data were not available in the drug record itself, so this description comes from the mechanistic assessment compiled for the prediction.

The link to diabetic cataract is weak. No direct mechanistic connection between ANGPTL3 inhibition and lens opacification has been shown. A hypothetical path through lipid or metabolic changes in diabetes is speculative. The high score is a graph-based prediction, and the same pattern appears across many cataract types (tetanic, mature, immature, senile, nuclear, cortical and others), which suggests the model is spreading its signal across the cataract disease cluster rather than reflecting specific biology.

The more interesting finding sits just below the top predictions. A 2026 paper (PMID 41555340) reports that an ANGPTL3–integrin α5 axis drives retinal vascular leakage in diabetic retinopathy. If confirmed, blocking ANGPTL3 could plausibly reduce vascular permeability in the retina. This is a preclinical finding, and the study design could not be verified from the data provided.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for diabetic cataract. The one relevant publication below concerns diabetic retinopathy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41555340](https://pubmed.ncbi.nlm.nih.gov/41555340/) | 2026 | Preclinical/Mechanistic (to be confirmed) | Journal of Translational Medicine | ANGPTL3 is a clinical predictor of diabetic retinopathy. The study examines its causal role in breaking down the blood-retinal barrier, through the ANGPTL3–integrin α5 axis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02541769 | EVKEEZA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

For any eye-related use, evinacumab is a systemically given antibody, so how well it reaches the eye, the route of delivery and its safety in that setting would all need investigation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The diabetic cataract prediction rests on the model score alone (Evidence Level L5), with no trials, no literature and no plausible mechanism. The related diabetic retinopathy finding (Evidence Level L4) is more promising but is a single preclinical paper, so it is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Verification of the study design and findings of PMID 41555340
- Preclinical evidence on ANGPTL3 blockade in lens or retinal models, including ocular penetration
- An assessment of whether diabetic retinopathy, rather than cataract, should be the priority indication to investigate
- Route and delivery compatibility assessment for any eye indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

