---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 769
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Bronchodilator Therapy (Asthma/COPD) to Thrombotic Disease

## One-Sentence Summary

Theophylline is a methylxanthine drug historically used as a bronchodilator for asthma and chronic obstructive pulmonary disease (COPD). The TxGNN model assigns a very high prediction score for a possible association with **Thrombotic Disease**, but this candidate currently has **no clinical trials** and only **20 publications**, none of which directly demonstrate an antithrombotic mechanism or clinical effect for theophylline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Canadian regulatory data (drug is not marketed in Canada). Literature in this evidence pack consistently describes theophylline as a bronchodilator for asthma/COPD. |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for theophylline in this evidence pack. Based on the supporting literature, theophylline is a xanthine derivative long used as a bronchodilator for asthma and COPD, acting primarily through phosphodiesterase inhibition and adenosine receptor antagonism (e.g., PMID 23672674, PMID 14988770).

The TxGNN model assigns a very high score (99.62%) to the thrombotic disease association, but the accompanying literature does not establish a direct pharmacological link. Most publications describe general platelet-activation biomarkers (platelet factor 4, soluble CLEC-2, microRNA signatures) or unrelated inflammatory conditions (Behçet's disease, inflammatory bowel disease) rather than theophylline's effect on coagulation or thrombus formation. Several entries mention theophylline only incidentally — for example, as a component of anticoagulant/sample-preparation buffers used in platelet research (PMID 749930), not as a therapeutic agent.

There is a weak theoretical rationale worth noting: methylxanthines can modulate cAMP-dependent platelet signaling in vitro, and a related paper on milrinone/adenosine interplay (PMID 8981060) illustrates this pathway conceptually. However, this evidence is indirect and has not been confirmed for theophylline specifically. Given the absence of any clinical trial and the lack of a direct mechanistic study, this prediction should be treated as exploratory and unproven at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | General review of thromboxane A2/prostacyclin balance in platelet aggregation and atherosclerosis; no theophylline-specific data. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Platelet/neutrophil activation studied in Behçet's disease patients; theophylline not evaluated as intervention. |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflammatory Bowel Diseases | Platelet-leukocyte aggregate formation studied in IBD; unrelated to theophylline therapy. |
| [29956444](https://pubmed.ncbi.nlm.nih.gov/29956444/) | 2018 | Basic Science | Journal of Thrombosis and Haemostasis | Mechanistic study of Weibel-Palade body exocytosis in endothelial activation; no theophylline link. |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Methodology | Cells | Methodology paper on blood sample processing for microRNA analysis; theophylline mentioned only as an anticoagulant additive. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | pending | Clinical Pharmacokinetics | Pharmacokinetic review of ticlopidine (an antiplatelet drug); theophylline not the subject. |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | pending | Platelets | Assay development for soluble CLEC-2 as a platelet-activation biomarker; no drug intervention studied. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | pending | British Journal of Haematology | Radioimmunoassay for platelet factor 4; theophylline used only as part of sample anticoagulant. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | pending | General Pharmacology | Milrinone/adenosine interaction inhibiting platelet aggregation via cAMP — offers indirect mechanistic analogy to methylxanthine action. |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | pending | The Journal of Nutrition | Aged garlic extract inhibits platelet aggregation via cAMP/cGMP signaling; unrelated to theophylline. |

---

## Canada Market Information

Theophylline is currently **not marketed in Canada** under this evidence pack — no Drug Identification Numbers (DINs) or product licenses are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there are no registered clinical trials and no literature directly demonstrating a pharmacological or clinical link between theophylline and thrombotic disease. The evidence level is L5 (model prediction only), which does not support progression.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for theophylline (currently a data gap; DrugBank query needed)
- Canadian/TFDA-equivalent label warnings and contraindications (currently a data gap; blocking safety review)
- Targeted mechanistic or preclinical studies examining theophylline's direct effect on coagulation/platelet pathways
- If mechanistic signal is confirmed, at minimum an observational or case-control study before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

