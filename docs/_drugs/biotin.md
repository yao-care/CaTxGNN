---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Biotin: predicted new indication Dyspepsia (evidence level L5). Approved use: Nutritional biotin deficiency"
monitor_inn: "BIOTIN"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
---

# Biotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Biotin: From Nutritional Biotin Deficiency to Dyspepsia

## One-Sentence Summary

Biotin is a B-vitamin originally used to treat nutritional biotin deficiency.
The TxGNN model predicts it may be effective for **dyspepsia**, but this rests on a computational prediction alone: there are **0 registered clinical trials** and only **6 publications**, none of which tests biotin as a treatment for dyspepsia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional biotin deficiency |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, biotin is a cofactor for carboxylase enzymes involved in carbohydrate, fat and amino acid metabolism. Its efficacy in correcting biotin deficiency is established, and it may be applicable to dyspepsia only indirectly.

The link between the original and predicted indications is plausible but not direct. Biotin deficiency can cause gastrointestinal symptoms such as nausea and anorexia, so correcting a deficiency might relieve some digestive complaints. This is not evidence that biotin treats dyspepsia in people who are not deficient.

The high TxGNN score (99.43%) is a computational output and should not be read as clinical proof. The second-ranked prediction, gastroparesis (score 99.42%), has no supporting trials or literature, and biotin has no known prokinetic or gastric-motility mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | Biotin deficiency in an infant fed only an amino acid formula after a neonatal diagnosis of dyspepsia; a deficiency case, not a treatment study for dyspepsia |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Stomach antral endocrine cells in 76 IBS patients compared with healthy controls; no biotin intervention |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Endocrine cells in the oxyntic stomach mucosa of IBS patients; no biotin intervention |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/Other | Eksp Klin Gastroenterol | A prebiotic supplement containing several vitamins, including biotin, for gut microbiota disorders in patients with lung disease on antibiotics; biotin is not studied on its own |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathol | Interleukin-10 localisation in H. pylori gastritis; no biotin intervention |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney Int | Small bowel T cells and stress protein in IgA nephropathy; not related to biotin treatment |

None of these publications shows that biotin improves dyspepsia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02100606 | MULTI 12 | Not specified | Not specified |
| 02242529 | MULTI-12/K1 PEDIATRIC | Not specified | Not specified |

---

## Safety Considerations

Disease associations flagged in the knowledge graph (not taken from label text) suggest caution in patients with:

- Kidney disease, nephrolithiasis (including susceptibility caused by SLC26A1), nephrocalcinosis, and acute urate nephropathy
- Pyoureter
- Calcium and phosphorus disorders: hypercalcemia, hyperparathyroidism, osteitis fibrosa, and phosphorus metabolism disease
- Sarcoidosis
- Lytic metastatic bone lesions
- Constipation disorder

These associations probably reflect other components of multivitamin products (such as vitamin D or calcium) rather than biotin itself, so they should be checked against the package insert. No drug interaction records were found.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a model score. There are no clinical trials, and the literature does not test biotin for dyspepsia. The mechanistic link is indirect, and the available Canadian products are multi-ingredient vitamin formulations.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before any safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Evidence that biotin improves dyspepsia symptoms, such as clinical studies in patients with dyspepsia, with or without documented biotin deficiency
- Approved indication text and dosage forms for the two Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

