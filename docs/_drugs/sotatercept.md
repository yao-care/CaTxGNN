---
layout: default
title: Sotatercept
parent: Model Prediction Only (L5)
nav_order: 866
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sotatercept: predicted new indication Acute lymphoblastic leukemia (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Sotatercept"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
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

## Sotatercept: From an Approved Canadian Product (Indication Not Specified) to Acute Lymphoblastic Leukemia
{: .text-alpha }

## One-Sentence Summary

Sotatercept is an activin receptor type IIA-Fc fusion protein that is currently marketed in Canada as WINREVAIR, although the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **acute lymphoblastic leukemia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Acute lymphoblastic leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on the available description, sotatercept is an activin receptor type IIA-Fc fusion protein. It traps activin and related TGF-beta superfamily ligands, such as activins and GDF8/11.

Activin signaling has been implicated in the regulation of blood cell formation, which is the only loose biological connection to acute lymphoblastic leukemia (ALL). However, the data compiled for this report show no direct mechanistic or clinical link to ALL. The high TxGNN score is a computational prediction, and it likely reflects proximity in the knowledge graph rather than validated biology.

Because the original indication is not available, the relationship between the original and new indications cannot be assessed.

### Other Predicted Indications (All L5, Hold)

The model also ranked the following diseases highly. None has any trial or literature support in the compiled data.

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Severe nonproliferative diabetic retinopathy | 99.77% | Speculative link through retinal vascular remodeling. Ocular and vascular safety of a systemic activin trap is unaddressed. |
| 3 | Diabetic retinopathy | 99.72% | Same rationale as rank 2. |
| 4 | Drug-induced osteoporosis | 99.65% | Activin inhibition is biologically plausible in bone, and preclinical work has shown bone-anabolic effects. This is the most mechanistically coherent candidate, but no clinical evidence was supplied. |
| 5 | Diabetic cataract | 99.49% | TGF-beta signaling is involved in lens epithelial-mesenchymal transition, but there is no evidence linking sotatercept to this condition. |
| 6 | HER2 positive breast carcinoma | 99.43% | Activin and TGF-beta roles in breast cancer are context-dependent, so the direction of effect is uncertain. |
| 7 | Transitional cell carcinoma | 99.39% | No direct rationale. The effect could be beneficial or detrimental. |
| 8 | Prostatic urethra urothelial carcinoma | 99.36% | Likely driven by similarity to related urothelial cancer nodes. |
| 9 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.36% | Likely a graph-proximity artifact. |
| 10 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.34% | The near-identical scores across urothelial subtypes suggest a shared graph-based artifact. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02551306 | WINREVAIR | Not specified | Not specified |
| 02551314 | WINREVAIR | Not specified | Not specified |

Both licenses are single-ingredient products with valid status.

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found. A systemic activin trap in the proposed new indications also raises unaddressed questions, particularly ocular and vascular safety for the diabetic eye conditions, and an uncertain direction of effect in cancers.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials, no publications, and no confirmed mechanistic link to acute lymphoblastic leukemia. Safety and label information are also missing, so the candidate cannot move beyond initial screening.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, and approved indication) to enable safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic studies supporting an activin-pathway role in ALL
- If prioritizing among the predictions, a focused literature and trial review for drug-induced osteoporosis, the most mechanistically coherent candidate
- Assessment of dosage form and route compatibility with any proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

