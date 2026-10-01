---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 900
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

# Theophylline: From Airway Disease (Bronchodilator) to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator used for airway diseases such as asthma and COPD. The TxGNN model predicts it may be effective for **thrombotic disease** with a very high score (99.6%). However, there are currently **0 clinical trials** and **18 retrieved publications**, none of which directly tests theophylline for thrombosis, so the prediction is not yet supported by real evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records. Literature describes theophylline as a bronchodilator for asthma, bronchitis and emphysema. |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Theophylline is a non-selective phosphodiesterase (PDE) inhibitor. Its efficacy in airway disease is well established.

The link to thrombosis is theoretical. PDE inhibition raises cAMP in platelets, which could reduce platelet aggregation. This is the same pathway that prostacyclin uses to suppress platelet clumping. A related study of milrinone (another PDE inhibitor) and adenosine in human platelets (PMID 8981060) shows that this pathway is biologically relevant.

There is a counterweight. Theophylline also blocks adenosine receptors, and adenosine itself inhibits platelet aggregation, so this effect may offset the benefit. The high TxGNN score reflects a network-based prediction only. The retrieved literature is largely off-target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications tests theophylline as a treatment for thrombotic disease. Most are reviews or assay and methods papers that mention platelets or theophylline incidentally. They are listed in order of closeness to the hypothesis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone (a PDE inhibitor) lowers platelet aggregation and interacts with adenosine through platelet cAMP. This is indirect mechanistic support only. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Describes how prostacyclin raises platelet cAMP to prevent aggregation, which is the pathway PDE inhibitors could influence. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet drug. Not about theophylline. |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Laboratory study | Journal of Nutrition | Aged garlic extract inhibits platelet aggregation via cAMP/cGMP signalling. Not about theophylline. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational | Cor et Vasa | T-lymphocyte subsets in vascular disease patients, measured with a theophylline-resistance assay. Not a treatment study. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay method | British Journal of Haematology | Platelet factor 4 assay that uses theophylline as an anticoagulant additive. Not a treatment study. |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Assay method | Platelets | Soluble CLEC-2 as a marker of platelet activation. Not about theophylline. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | Aptasensor for detecting theophylline. Not about thrombosis. |
| [7307205](https://pubmed.ncbi.nlm.nih.gov/7307205/) | 1981 | Clinical series | Chirurgia Italiana | Diagnosis and treatment of Raynaud's phenomenon in 120 patients. Not specific to theophylline. |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | Clinical article | Z Gesamte Inn Med | Chronic cor pulmonale resulting from thromboembolic disease. No abstract available. |

---

## Canada Market Information

Dosage form and approved indication text are not recorded for these licences. Six licences are registered in total; five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 692700 | AA-THEO LA | Not listed | Not listed |
| 627410 | ELIXIR DE THEOPHYLLINE | Not listed | Not listed |
| 2360101 | THEO ER | Not listed | Not listed |
| 2360128 | THEO ER | Not listed | Not listed |
| 692697 | AA-THEO LA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a speculative platelet cAMP mechanism that adenosine antagonism may cancel out. There are no trials, and the retrieved literature does not test theophylline in thrombosis.

Other predicted indications in the pack are better supported:
- **Obstructive lung disease:** this is likely on-label use rather than true repurposing.
- **Nasal cavity disease:** one completed Phase 2 trial of nasal theophylline irrigation for post-viral olfactory loss (NCT03990766, n=27).

**To proceed, the following is needed:**
- A targeted literature search for theophylline and platelet aggregation or thrombosis (in vitro, animal and human data)
- Mechanism of action data to resolve the PDE inhibition versus adenosine antagonism question
- The approved indication and warnings from the Health Canada package insert
- Safety review, given theophylline's narrow therapeutic index, before any thrombosis-related use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

