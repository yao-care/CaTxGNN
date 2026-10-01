---
layout: default
title: Ripretinib
parent: Model Prediction Only (L5)
nav_order: 805
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: From Gastrointestinal Stromal Tumour (GIST) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib is a kinase inhibitor that targets KIT and PDGFRA. It is approved for gastrointestinal stromal tumour (GIST), although the approved indication text is missing from the licensing data supplied.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | GIST (taken from the mechanistic note; the licence record has no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ripretinib is a switch-control inhibitor of the KIT and PDGFRA kinases, which drive GIST. Detailed mechanism-of-action data is not available in the supplied record, so this description comes from the mechanistic notes only.

The link to the predicted indication is weak. MEN syndromes are driven mainly by RET activation (MEN2) or loss of MEN1 function. Ripretinib has no established RET activity. The prediction therefore rests only on a high graph-model score, not on a known biological connection. Both conditions are tumour disorders, but that is a broad similarity and not a mechanistic argument.

Other predictions for this drug (HER2-positive breast carcinoma, several breast cancer subtypes, cytomegalovirus infection, amenorrhea, and two veterinary diseases) are also L5 and Hold. Several look like graph-topology artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2500833 | QINLOCK |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. The drug-interaction query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials, no relevant literature, and no plausible link between ripretinib's KIT/PDGFRA inhibition and the RET/MEN1-driven biology of MEN. There is also no safety data on file.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Preclinical evidence of ripretinib activity in RET- or MEN1-driven models
- A properly constructed literature search for ripretinib and MEN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

