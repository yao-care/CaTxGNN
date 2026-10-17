---
layout: default
title: Ponatinib
parent: Model Prediction Only (L5)
nav_order: 753
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Ponatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
monitor_inn: "PONATINIB"
predicted_indications: ["fibromatosis, gingival", "liposarcoma"]
---

# Ponatinib
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

# Ponatinib: From BCR-ABL1-Positive Chronic Myelogenous Leukemia to Fibromatosis, Gingival

## One-Sentence Summary

Ponatinib was originally used to treat BCR-ABL1-positive chronic myelogenous leukemia.
The TxGNN model predicts it may be effective for **gingival fibromatosis** (top-ranked prediction), but there are currently **0 clinical trials** and **0 publications** supporting this direction.
A second prediction, **liposarcoma**, has **0 clinical trials** and **1 preclinical publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ponatinib is a multi-targeted tyrosine kinase inhibitor (targeting BCR-ABL, FGFR, PDGFR, VEGFR, SRC and KIT). Its efficacy in BCR-ABL1-positive chronic myelogenous leukemia has been established, and mechanistically it may be applicable to conditions driven by kinase signaling.

For **gingival fibromatosis**, the only support is the high TxGNN score (99.04%). Kinase signaling in fibroblast proliferation and extracellular matrix deposition could plausibly relate to fibrotic overgrowth, but this link is speculative and not backed by clinical or literature evidence. Gingival fibromatosis is a rare and mostly benign condition, and ponatinib's cardiovascular and vascular occlusive toxicity would be hard to justify for it.

**Secondary prediction: liposarcoma** (score 99.00%). Ponatinib inhibits several receptor tyrosine kinases (FGFR, PDGFR, KIT, SRC, RET) that may drive sarcoma biology. One 2017 preclinical study identified druggable kinase targets in liposarcoma. From the available information, I cannot confirm that ponatinib itself was tested or found active, so this evidence is indirect and preclinical (L4).

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either gingival fibromatosis or liposarcoma.

---

## Literature Evidence

For gingival fibromatosis, currently no related literature available.

For liposarcoma (secondary prediction), one publication is available:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinical (kinase profiling / RNAi and drug screening) | Journal of Hematology & Oncology | Kinase profiling of liposarcomas identified druggable kinase targets; liposarcoma is an understudied cancer with limited progress in treating metastatic disease |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02437333 | ICLUSIG | Not available | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine monitoring typically includes CBC, liver function and cardiovascular status |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples from the first 20 reviewed):
- **Major**: Acetylsalicylic acid, Clarithromycin
- **Moderate**: Loperamide, Aprepitant, Dexamethasone, Naldemedine, Naltrexone, Metronidazole, Miconazole
- **Minor**: Famotidine, Ranitidine, Cimetidine, Nizatidine, Rabeprazole, Omeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole, Magnesium oxide, Naloxegol

Warnings and contraindications from the Canadian package insert were not available in the data compiled for this report. Please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gingival fibromatosis prediction rests only on a model score, with no clinical trials or literature (L5). Ponatinib's vascular occlusive and cardiovascular toxicity makes the risk-benefit profile unfavourable for a mostly benign condition. Liposarcoma is a more plausible research question (L4, preclinical only) but does not yet justify clinical advancement.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Confirmation of whether ponatinib was specifically tested in the liposarcoma kinase screening study
- Preclinical evidence (e.g., fibroblast or cell-line studies) for gingival fibromatosis
- Approved indication text and dosage form for DIN 02437333
- A risk-benefit assessment of cardiovascular and vascular occlusive toxicity for the proposed indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

