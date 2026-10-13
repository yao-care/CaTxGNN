---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a long-established mood stabiliser, originally used for bipolar disorder and manic affective disorders.
The TxGNN model predicts it may be effective for **pseudoachondroplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder (also listed in the knowledge graph: major affective disorder, manic bipolar affective disorder, and several arthritis-related conditions) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lithium is a long-used mood-stabilising agent whose efficacy in bipolar disorder is well established. Its pharmacology is commonly linked to inhibition of glycogen synthase kinase-3 (GSK-3) and modulation of Wnt/beta-catenin signalling, which may in principle be relevant to skeletal biology.

Pseudoachondroplasia is caused by mutations in the COMP gene, leading to endoplasmic reticulum stress in chondrocytes and defects in the cartilage extracellular matrix. The link to lithium is speculative: Wnt pathway modulation could theoretically influence chondrocyte behaviour, but no data compiled for this report show a therapeutic effect.

The very high TxGNN score most likely reflects proximity in the knowledge graph to other skeletal and joint disorders (several arthritis-related conditions are already linked to lithium there), rather than a validated biological connection. The other top-ranked predictions are also rare skeletal dysplasias with similarly sparse evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

(For context, one general review on genetic skeletal disorders, [31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/), Orphanet J Rare Dis, 2019, was retrieved for a different lower-ranked prediction, brachyolmia-amelogenesis imperfecta syndrome. It covers therapeutic approaches to genetic skeletal disorders in general and is not specific to lithium.)

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02011239 | CARBOLITH | Not specified | Not specified |
| 00236683 | CARBOLITH | Not specified | Not specified |
| 02216132 | PMS-LITHIUM CARBONATE - CAP 150MG | Not specified | Not specified |
| 02242837 | APO-LITHIUM CARBONATE | Not specified | Not specified |
| 00461733 | CARBOLITH | Not specified | Not specified |

Nine valid single-ingredient licences exist in total; the five above are shown.

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text):** kidney disease, hypothyroidism (including myxedema and congenital hypothyroidism), diabetes insipidus (central and neurohypophyseal), cognitive disorder, psoriasis and parapsoriasis, sudden cardiac arrest, heart conduction disease, and pyoureter.
- **Drug Interactions:** 100 interactions were identified. Examples of those listed:
  - **Major:** bupropion, lorcaserin
  - **Moderate:** metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, chlorpropamide, acarbose, famotidine, loperamide, mesalazine, balsalazide, morphine, metronidazole, clarithromycin, potassium citrate
  - **Minor:** doxycycline, epinephrine, acetylsalicylic acid
- **Additional consideration:** Lithium is known to be teratogenic in some contexts, which matters for any developmental or paediatric skeletal indication. It also has a narrow therapeutic window requiring serum level monitoring.

Please refer to the package insert for the full warnings and contraindications, as the label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a model score, with no clinical trials, no supporting publications, and only a speculative mechanistic link. Lithium's known renal, thyroid and cardiac risks, along with its narrow therapeutic index, raise the bar for justifying any new use, especially in a paediatric rare-disease setting.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to assess a credible link to COMP-related chondrocyte pathology
- Preclinical evidence (for example, cell or animal models of pseudoachondroplasia) showing a lithium effect
- A targeted literature search on lithium and skeletal dysplasia or chondrocyte ER stress
- A paediatric safety and teratogenicity risk assessment before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

