---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "LEVOFLOXACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Levofloxacin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial marketed in Canada in multiple single-ingredient products.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 clinical trials** and only **1 publication** (an outbreak report on a different, microsporidial cause of keratoconjunctivitis), so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 17 of 17) |
| Number of DINs | 17 (valid: 17) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Levofloxacin belongs to the fluoroquinolone class of antibacterials, which act by inhibiting bacterial DNA replication. The model likely scored this disease highly because of its similarity to other ocular infections and inflammatory eye conditions.

The link is weak. The only retrieved paper describes an outbreak of microsporidial keratoconjunctivitis from contaminated swimming-pool water. Fluoroquinolones have no established activity against microsporidia, so that report does not support a benefit from levofloxacin. The high score reflects computational proximity, not clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis linked to swimming-pool water contamination in Taiwan; no levofloxacin treatment data |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02442302 | QUINSAIR |
| 02537079 | LEVOFLOXACIN IN 5% DEXTROSE INJECTION |
| 02298651 | SANDOZ LEVOFLOXACIN |
| 02315440 | TEVA-LEVOFLOXACIN |
| 02325942 | APO-LEVOFLOXACIN |

All 17 licences in the local records are valid single-ingredient products. Only five are listed here.

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 entries. Major-level interactions include tramadol and hydrocortisone. Many moderate-level interactions were also found, including with antidiabetic agents (acarbose, alogliptin, metformin, pioglitazone, albiglutide), NSAIDs (ibuprofen, ketorolac), famotidine, abiraterone, adenosine, alfuzosin, amifampridine, ethinylestradiol, formoterol and salbutamol.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the single retrieved publication concerns a microsporidial outbreak that levofloxacin is not expected to treat. The high TxGNN score is not backed by direct clinical evidence, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or preclinical studies of levofloxacin in punctate epithelial keratoconjunctivitis, including the ocular route and formulation
- Mechanism of action data and an analysis of the likely causative organisms in this condition
- Package insert warnings and contraindications from Health Canada

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

