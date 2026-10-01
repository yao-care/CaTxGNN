---
layout: default
title: Yellow Fever Vaccine
parent: Model Prediction Only (L5)
nav_order: 980
evidence_level: L5
indication_count: 10
---

# Yellow Fever Vaccine
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

# Yellow Fever Vaccine: From Yellow Fever Prevention to Plasma Cell Myeloma

## One-Sentence Summary

Yellow Fever Vaccine (YF-VAX) is a live attenuated vaccine used to prevent yellow fever.
The TxGNN model predicts it may be effective for **plasma cell myeloma**, but there are **0 clinical trials** and only **1 publication**, a case report on vaccine safety rather than anti-myeloma activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Yellow fever prevention (immunization). The license record has no indication text, so this is inferred from the product type. |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 97.98% |
| Evidence Level | L4 (as assigned in the Evidence Pack; the only study is a safety case report, so the practical level is close to L5) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Yellow Fever Vaccine is a live attenuated viral vaccine (17D strain) that induces immunity against yellow fever virus. Its efficacy in yellow fever prevention is established, but no mechanism links it to treating plasma cell myeloma.

The only related literature describes a patient with myeloma who received the vaccine safely after a bone marrow transplant. This shows the vaccine can be given in some immunocompromised patients. It does not show any anti-myeloma effect. The high TxGNN score (97.98%) is a graph-based prediction with no clinical support. The same applies to the other top-ranked predictions, such as indolent plasma cell myeloma, heart disease and the sickle cell disease variants. Several of the sickle cell variants share an identical score, which suggests a graph artifact rather than a disease-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15089771](https://pubmed.ncbi.nlm.nih.gov/15089771/) | 2004 | Case report | European Journal of Haematology | A patient vaccinated 2.5 years after bone marrow transplantation for myeloma responded to the live attenuated 17D yellow fever vaccine without adverse effects. This is a safety observation, not evidence of treatment benefit. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 428833 | YF-VAX | Not specified | Not specified |

The license number comes from the regulatory record in the Evidence Pack, which lists no dosage form, manufacturer or indication text.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this product.

The case report involved a live attenuated vaccine given to a patient who was not severely immunosuppressed. Any use in myeloma patients would need careful review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, and the single publication is a safety case report with no efficacy signal. No plausible mechanism has been identified for a live attenuated vaccine to treat a plasma cell neoplasm.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess any biological link to myeloma
- Package insert warnings and contraindications from Health Canada, especially for immunocompromised patients
- Preclinical or clinical studies that test anti-myeloma activity, if the hypothesis is pursued
- Confirmation of the original indication, dosage form and manufacturer in the license record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

