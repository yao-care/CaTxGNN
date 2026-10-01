---
layout: default
title: Abemaciclib
parent: Model Prediction Only (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib (brand name VERZENIO) is a CDK4/6 inhibitor used for hormone receptor-positive, HER2-negative breast cancer.
The TxGNN model predicts it may be effective for **rheumatoid arthritis** with a high score, but there are currently **0 clinical trials** and only **1 publication** (an observational study in breast cancer patients that does not test efficacy in RA).
This prediction rests on the model alone and has no clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- breast cancer (inferred from the trials and literature in the pack; the Canadian license text was not provided) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 (no clinical efficacy data; mechanistic plausibility only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, abemaciclib belongs to the CDK4/6 inhibitor class. Its efficacy in HR+/HER2- breast cancer is established, and mechanistically it may be applicable to rheumatoid arthritis.

The link is plausible but unproven. CDK4/6 inhibition limits the proliferation of lymphocytes and synovial fibroblasts, the cell types that drive joint inflammation in RA. Blocking them could in theory dampen autoimmune inflammation. Some reports also suggest that CDK4/6 inhibitors influence immune function. They may enhance antitumour immunity, but they may also trigger autoimmune reactions.

The only literature hit (PMID 40504547) is an observational study of immune-mediated disease in breast cancer patients on CDK4/6 inhibitors. It looks at disease prevalence and possible flares, so it speaks to safety rather than RA efficacy. The high TxGNN score (97.32%) is not backed by any clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort (observational) | The Oncologist | Investigated the prevalence of pre-existing and emerging autoimmune diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy, to find predictive biomarkers and assess the impact on outcomes. It is not an RA efficacy study. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2487101 | VERZENIO |
| 2487098 | VERZENIO |
| 2487136 | VERZENIO |
| 2487128 | VERZENIO |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral CDK4/6 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential), liver and renal function; QTc and cardiovascular status where relevant |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The Evidence Pack contains no package insert warnings, contraindications or drug interaction data for this drug. The literature retrieved for other predicted indications does show these signals:

- **Cardiovascular**: Meta-analyses and pharmacovigilance studies report QTc prolongation and cardiovascular adverse events with CDK4/6 inhibitors as a class. Ribociclib carries the highest risk, and the risk with abemaciclib is lower. A case report describes myocardial infarction from coronary plaque erosion two weeks after abemaciclib was started.
- **Kidney**: An FDA adverse event database analysis describes abemaciclib-associated kidney injury reports.
- **Immune**: Autoimmune reactions have been reported with CDK4/6 inhibitors, and the effect on people with pre-existing RA has not been established.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only. There are no registered RA trials, and the single publication is an observational safety-oriented study in breast cancer patients. The mechanistic link is plausible but untested, so there is currently no basis for a clinical development step.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking the S1 safety screen)
- Detailed mechanism of action data (MOA), for example from DrugBank
- Preclinical RA data, such as in vitro synovial fibroblast or lymphocyte assays and animal arthritis models
- An assessment of immune-related and cardiovascular safety in RA patients, who are often on concomitant immunosuppressants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

