---
layout: default
title: Glutamic Acid
parent: Model Prediction Only (L5)
nav_order: 436
evidence_level: L5
indication_count: 4
---

# Glutamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Glutamic Acid: From Parenteral Nutrition Amino Acid Component to Postmenopausal Osteoporosis

## One-Sentence Summary

Glutamic acid is an amino acid that is marketed in Canada as a component of parenteral nutrition products. The TxGNN model predicts it may be effective for **postmenopausal osteoporosis**, but there are currently **0 clinical trials** and only **indirect or preclinical literature** behind this prediction. In practice, this is a model-generated research question, not an evidence-backed candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available license data (marketed in Canada as a component of parenteral nutrition products) |
| Predicted New Indication | Postmenopausal osteoporosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (preclinical and mechanistic data only; no clinical studies of glutamic acid itself) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Glutamic acid is a naturally occurring amino acid and also acts as an excitatory neurotransmitter and a precursor of GABA. In Canada it is marketed as an ingredient of amino acid and parenteral nutrition solutions, and its efficacy as a nutritional component, not as a bone treatment, is the basis for its use.

The link to osteoporosis is indirect. Glutamate signalling has been described in bone cells (osteoblasts and osteoclasts). Glutamate residues in vitamin K-dependent proteins such as osteocalcin also undergo gamma-carboxylation, which is relevant to bone metabolism. One preclinical study in ovariectomized mice reported that glutamic acid reduced estrogen-deficiency-induced menopausal-like symptoms. However, none of this shows that giving glutamic acid affects bone density or fracture risk in humans. Many of the retrieved papers are about vitamin K2, vitamin D3 or bisphosphonates, not glutamic acid itself.

The other predicted indications are weaker still:
- **Pregnancy-associated osteoporosis** (score 99.18%): no trials or literature; likely driven by network similarity to other osteoporosis entities, and pregnancy adds a safety constraint.
- **Primary hereditary glaucoma** (score 99.13%): no trials or literature; glutamate excitotoxicity of retinal ganglion cells is a recognized hypothesis in glaucoma, which argues against rather than for supplementation.
- **Gastroparesis** (score 99.11%): the retrieved papers concern antibodies to glutamic acid decarboxylase (GAD65), a different molecule, so this is probably a name-similarity artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized trial of glutamic acid in postmenopausal osteoporosis was found. The table lists the most relevant retrieved publications, and most of them do not test glutamic acid.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26144993](https://pubmed.ncbi.nlm.nih.gov/26144993/) | 2015 | Preclinical (ovariectomized mice) | Nutrition Research | Glutamic acid ameliorated estrogen-deficiency-induced menopausal-like symptoms in mice; the only study that directly tests glutamic acid |
| [18187428](https://pubmed.ncbi.nlm.nih.gov/18187428/) | 2007 | Clinical (small acute study) | J Am Coll Nutr | Poly-gamma-glutamic acid (a different compound) and calcium absorption in post-menopausal women |
| [34529430](https://pubmed.ncbi.nlm.nih.gov/34529430/) | 2021 | Preclinical (drug delivery) | Nano Letters | Bone-targeting polymer vesicles containing glutamic acid units used to deliver estradiol; glutamic acid is a structural material, not the active drug |
| [19172219](https://pubmed.ncbi.nlm.nih.gov/19172219/) | 2009 | Randomized prospective study | J Bone Miner Metab | Menatetrenone (vitamin K2) increased osteocalcin gamma-carboxylation in 109 postmenopausal patients; not a glutamic acid study |
| [14529146](https://pubmed.ncbi.nlm.nih.gov/14529146/) | 2003 | Review | Keio J Med | Vitamin D3 and/or K2 treatment for postmenopausal osteoporosis; not a glutamic acid study |
| [14584089](https://pubmed.ncbi.nlm.nih.gov/14584089/) | 2003 | Clinical/Review | Yonsei Med J | Vitamin K2 combined with bisphosphonates; not a glutamic acid study |
| [29437025](https://pubmed.ncbi.nlm.nih.gov/29437025/) | 2018 | Genetic association | Endocr Metab Immune Disord Drug Targets | VKORC1 polymorphism and osteoporosis in postmenopausal women |
| [40950804](https://pubmed.ncbi.nlm.nih.gov/40950804/) | 2025 | Observational metabolomics | J Diabetes Metab Disord | Amino acid profiles, aging and sex hormones in elderly Iranian adults |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02141450 | 20% PROSOL | Not specified | Not specified |
| 02352540 | OLIMEL 5.7% | Not specified | Not specified |
| 02236875 | PRIMENE 10% | Not specified | Not specified |
| 02477947 | OLIMEL 7.6% | Not specified | Not specified |
| 02352494 | PERIOLIMEL 2.5% E | Not specified | Not specified |

Two further authorizations (OLIMEL 7.6% E, DIN 02477955, and OLIMEL 5.7% E, DIN 02352532) are also valid, bringing the total to 7 single-ingredient DINs.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease relationships in the TxGNN knowledge graph, not label text): kidney disease (including chronic kidney disease, chronic renal failure and end stage renal failure), nephrolithiasis and nephrocalcinosis, hypercalcemia-related conditions (hypercalcemia, humoral hypercalcemia of malignancy, hyperparathyroidism, osteitis fibrosa, sarcoidosis), phosphorus metabolism disease, heart disease and cardiovascular disease, digitalis poisoning, ventricular fibrillation, acute urate nephropathy, phenylketonuria and other disorders of phenylalanine metabolism.
- **Drug interactions** (5 moderate-level interactions): amphetamine, benzphetamine, dextroamphetamine, lisdexamfetamine and metamfetamine.
- **Indication-specific concerns**: glutamate excitotoxicity is a potential concern in glaucoma, and use in pregnancy would need a dedicated safety assessment.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trial or human study of glutamic acid in postmenopausal osteoporosis. The only direct evidence is one mouse study, and most retrieved papers concern vitamin K2, vitamin D3 or bisphosphonates. The kidney, calcium-metabolism and cardiovascular signals in the knowledge graph also overlap with an older osteoporosis population.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical bone studies (bone density, bone turnover markers, fracture endpoints) that test glutamic acid directly
- A review of whether oral or parenteral dosing is feasible and how the bone-relevant exposure would be achieved, given that current Canadian products are parenteral nutrition solutions
- A safety assessment for renal impairment, hypercalcemia-related conditions and cardiovascular disease, which the knowledge graph flags as contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

