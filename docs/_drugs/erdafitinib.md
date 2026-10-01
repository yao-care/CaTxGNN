---
layout: default
title: Erdafitinib
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is an FGFR (fibroblast growth factor receptor) kinase inhibitor marketed in Canada as BALVERSA for cancer treatment.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The evidence is model-prediction only, so the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records; urothelial carcinoma with FGFR alterations, per general product knowledge |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Erdafitinib is a pan-FGFR inhibitor, a class of drugs that blocks FGF/FGFR signaling. Its efficacy in its original cancer indication is established, and mechanistically it may be applicable to conditions driven by FGFR signaling.

The link to pulmonary hypertension is plausible but unproven. FGF2/FGFR1 signaling has been linked to pulmonary artery smooth muscle proliferation and vascular remodeling, so pan-FGFR inhibition could be relevant in preclinical models. There are no direct pulmonary hypertension data for erdafitinib.

Class toxicities would need to be addressed first: hyperphosphatemia, retinal toxicity and nail toxicity. No safety data exist in pulmonary hypertension populations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

---

## Other Predicted Indications (All Evidence Level L5, Hold)

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Kyphoscoliotic heart disease | 99.27% | No credible mechanistic link; likely a knowledge-graph artifact |
| 3 | Amenorrhea | 99.26% | No supporting link; FGFR1 inhibition would be expected to disturb the reproductive axis |
| 4 | Rheumatoid arthritis | 99.25% | Weak, hypothesis-level link; one indirect paper (see below) |
| 5 | Amyotrophic lateral sclerosis | 99.06% | Doubtful direction of effect; FGF signaling is generally neuroprotective |
| 6 | Brachydactyly-syndactyly syndrome | 99.03% | Congenital malformation; a postnatal kinase inhibitor is not expected to correct it |
| 7 | ALS type 22 | 98.91% | Near-duplicate of ALS; consolidate with the parent assessment |
| 8 | ALS, susceptibility to | 98.88% | Susceptibility-locus entry, not a distinct treatable indication |
| 9 | Axial spondylometaphyseal dysplasia | 98.83% | Loose link only; no evidence FGFR inhibition would help |
| 10 | Mills syndrome | 98.78% | No identifiable rationale; likely network proximity to ALS-related nodes |

The only publication retrieved across all predictions is for rheumatoid arthritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Review | Pharmacological research | General review of FDA-approved small molecule kinase inhibitors, including erdafitinib. It has no RA-specific erdafitinib data and is not counted as clinical evidence. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2493233 | BALVERSA |
| 2493225 | BALVERSA |
| 2493217 | BALVERSA |

Dosage form and approved indication text are not available in the retrieved license records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Class toxicities to monitor include hyperphosphatemia (serum phosphate), retinal toxicity (ophthalmic examination) and nail toxicity; see the package insert for the full schedule |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no clinical trials and no direct literature. The pulmonary hypertension mechanism is plausible but unproven, and the FGFR class toxicity profile has not been assessed in this population. The other nine predictions have weak or doubtful mechanistic links.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to support the FGFR-to-vascular remodeling analysis
- Preclinical evidence for FGFR inhibition in pulmonary hypertension models
- A safety assessment of hyperphosphatemia, retinal toxicity and nail toxicity in a pulmonary hypertension population
- Dosage form, approved indication text and route information for the three DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

