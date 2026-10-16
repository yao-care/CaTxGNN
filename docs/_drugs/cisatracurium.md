---
layout: default
title: Cisatracurium
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cisatracurium: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not specified in the Canadian license records"
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocker, used as a muscle relaxant during anesthesia and intensive care.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **no clinical trials and no publications** currently support this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license records |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, cisatracurium is a non-depolarizing neuromuscular blocker that acts on nicotinic acetylcholine receptors at the neuromuscular junction, relaxing skeletal muscle.

A plausible therapeutic link to cauda equina syndrome is hard to find. Cauda equina syndrome is a compressive neurological emergency, usually treated by urgent surgical decompression. Blocking neuromuscular transmission does not relieve nerve root compression. The very high TxGNN score (99.99%, rank 254) reflects a pattern in the knowledge graph, not clinical or mechanistic support.

Other predicted indications show the same pattern. For example, the preeclampsia-related literature describes cisatracurium only as part of anesthesia during cesarean section, not as treatment of the disease. Likewise, the thrombotic disease paper is about anesthesia for pediatric liver transplantation. These are peri-procedural uses, not new therapeutic indications.

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For reference, the second-ranked prediction, preeclampsia, has two loosely related papers on anesthesia during cesarean section:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Cohort | Anesthesiology and Pain Medicine | Compared serum interleukin-6, leptin and adiponectin after cesarean section under general vs spinal anesthesia |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case series | Revista Espanola de Anestesiologia y Reanimacion | Remifentanil bolus for hemodynamic control during cesarean section in 12 high-risk patients |

Neither paper tests cisatracurium as a treatment for preeclampsia.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02563266 | Cisatracurium Besylate Injection USP Multi-Dose | Not listed | Not listed |
| 02408813 | Cisatracurium Besylate Injection USP Multidose | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: 61 interactions were recorded. The 20 reviewed include the following.
  - **Major**: kanamycin, neomycin, paromomycin, polymyxin B, streptomycin. These are aminoglycoside and polypeptide antibiotics that may potentiate neuromuscular blockade.
  - **Moderate**: amphotericin B (including lipid, cholesteryl sulfate and liposomal forms), doxycycline, minocycline, tetracycline, vancomycin, magnesium chloride, magnesium sulfate, mannitol, metoclopramide, topical neomycin.
  - **Minor**: ranitidine, ranitidine (bismuth citrate).
- Magnesium sulfate is especially relevant in obstetric settings such as preeclampsia, because it potentiates neuromuscular blockade.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or supporting literature, and no plausible mechanism links neuromuscular blockade to cauda equina syndrome. The other nine predicted indications (including preeclampsia, migraine, irritable bowel syndrome and thrombotic disease) are also on Hold and show the same lack of mechanistic plausibility.

**To proceed, the following is needed:**
- Health Canada package insert data (warnings, contraindications, approved indications)
- Mechanism of action data from DrugBank
- A credible biological rationale linking neuromuscular blockade to the predicted disease
- Preclinical or clinical evidence specific to the predicted indication
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

