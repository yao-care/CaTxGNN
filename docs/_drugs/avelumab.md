---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
description: "Avelumab: predicted new indication Human herpesvirus 8-related tumor (evidence level L5). Approved use: Cutaneous neuroendocrine carcinoma"
monitor_inn: "Avelumab"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Avelumab
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

## Avelumab: From Cutaneous Neuroendocrine Carcinoma to Human Herpesvirus 8-Related Tumor
{: .text-alpha }

## One-Sentence Summary

Avelumab was originally used to treat cutaneous neuroendocrine carcinoma (Merkel cell carcinoma).
The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumor**,
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous neuroendocrine carcinoma |
| Predicted New Indication | Human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for avelumab: "PD-L1 may be expressed on tumor cells and tumor-infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD-L1 to the PD-1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation, and cytokine production. […] Avelumab binds PD-L1 and blocks the interaction between PD-L1 and its receptors PD-1 and B7.1." ([DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118), label version 2026-09-22; accessed 2026-11-19.) Avelumab is an antibody that blocks PD-L1, a checkpoint inhibitor, and its use in cutaneous neuroendocrine carcinoma is established. Mechanistically, it may be applicable to human herpesvirus 8-related tumors. This reasoning comes from general knowledge, not from the supplied data.

Tumors driven by herpesvirus 8 (for example, Kaposi sarcoma) can express PD-L1. Blocking PD-L1 could restore T-cell antitumour activity. This link is plausible but has not been verified against the record.

Other predictions for this drug are also listed below. They are all supported by model output only:

- **Urothelial sites** (prostatic urethra urothelial carcinoma, score 0.9992; kidney pelvis sarcomatoid transitional cell carcinoma, score 0.9991) have the most plausible rationale, because avelumab is known to be used in advanced urothelial carcinoma. These are flagged as research questions, and checking whether existing urothelial trial populations included these subsites could raise the evidence level.
- **Rare neuroendocrine or cutaneous tumors** (middle ear neuroendocrine tumor, malignant cutaneous granular cell skin tumor, ectomesenchymoma) may reflect similarity to the original indication. PD-L1 relevance is unestablished.
- **Congenital immunodeficiencies** (adenosine deaminase deficiency, reticular dysgenesis, immunoerythromyeloid hypoplasia, non-severe combined immunodeficiency) have no credible mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Immune activation in these settings is a theoretical safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02469723 | BAVENCIO | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: Three Major-level interactions were identified, all with immunomodulatory agents:
  - Lenalidomide
  - Pomalidomide
  - Thalidomide

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9997), but no clinical trials or literature support the prediction, so the evidence level is L5. The mechanistic rationale for the herpesvirus 8-related tumor comes from general knowledge and cannot be checked against the data compiled for this report.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Targeted literature and trial searches for HHV-8-related tumors, such as Kaposi sarcoma, including PD-L1 expression data
- For the urothelial subsite predictions, a review of whether existing urothelial carcinoma trials included these subsites
- Review of the three Major drug interactions (lenalidomide, pomalidomide, thalidomide) before any combination use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

