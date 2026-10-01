---
layout: default
title: Lurbinectedin
parent: Model Prediction Only (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: From Small Cell Lung Cancer to Multiple Endocrine Neoplasia

## One-Sentence Summary

Lurbinectedin is a cytotoxic anticancer drug approved for small cell lung cancer, a neuroendocrine carcinoma.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it so far.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung cancer (per the Evidence Pack's mechanistic rationale; the Canadian licence record has no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Lurbinectedin is generally described as an alkylating agent that binds the DNA minor groove and inhibits oncogenic transcription. Its efficacy in small cell lung cancer is established, and mechanistically it may be applicable to other neuroendocrine tumours.

Small cell lung cancer is a neuroendocrine carcinoma. Tumours associated with multiple endocrine neoplasia (pancreatic neuroendocrine tumours, pituitary tumours and parathyroid tumours) are also neuroendocrine in origin. This gives a loose biological rationale for the prediction.

This link is speculative. No trial or publication in the dataset supports it. The high TxGNN score reflects knowledge-graph proximity, not clinical proof. The other nine predictions for this drug have the same evidence gap, and several are veterinary diseases, which suggests graph-propagation artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2520834 | ZEPZELCA | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating-type agent that inhibits transcription) |
| Myelosuppression Risk | Present. The Evidence Pack notes myelosuppression and neutropenia risk, but no grading is available. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential) and liver function, based on the neutropenia and hepatotoxicity concerns noted in the pack |
| Handling Protection | Please refer to the package insert warnings and precautions. Cytotoxic drug handling regulations would be expected to apply. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no registered trials or publications, and the only mechanistic support is a loose neuroendocrine-lineage analogy. The drug's cytotoxic and myelosuppressive profile also raises the bar for any new use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or case-level evidence in MEN-associated neuroendocrine tumours
- A literature and trial search for lurbinectedin in neuroendocrine tumours, to confirm whether any evidence exists
- Route compatibility and similarity-to-original-indication assessments (both currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

