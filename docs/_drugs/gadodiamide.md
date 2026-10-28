---
layout: default
title: Gadodiamide
parent: Model Prediction Only (L5)
nav_order: 422
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Gadodiamide: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Not specified in the available licence data (gadodiamide is a diagnos…"
monitor_inn: "Gadodiamide"
predicted_indications: ["rheumatoid arthritis"]
---

# Gadodiamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Gadodiamide: From a Diagnostic MRI Contrast Agent to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Gadodiamide is a gadolinium-based contrast agent used in magnetic resonance imaging (MRI), marketed in Canada as OMNISCAN. The TxGNN model predicts it may be associated with **rheumatoid arthritis**, but there are **no registered clinical trials** and only **3 publications**, all of which used gadodiamide as an imaging tool rather than as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data (gadodiamide is a diagnostic MRI contrast agent) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9916 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gadodiamide is a gadolinium-based contrast agent. It enhances MRI images and has no recognised therapeutic anti-inflammatory activity.

The three publications found (2001–2002) used gadodiamide-enhanced MRI to visualize synovitis, bone marrow edema and bone erosions in patients with rheumatoid arthritis and other inflammatory joint diseases. This is a **diagnostic** use, not a therapeutic one. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At present there is no sound mechanistic reason to consider gadodiamide a treatment for rheumatoid arthritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Cohort | The Journal of Rheumatology | MRI features of wrist and finger joints compared across early RA, established RA, other arthritis and arthralgia |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Cohort | European Radiology | In 84 patients, MRI synovial volume and bone marrow oedema were assessed for predicting bone erosion progression at 1 year |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Cohort | European Radiology | Compared low-field extremity MRI (0.2 T) with high-field MRI (1.5 T) in 103 patients with arthritic small joints |

All three studies concern diagnostic imaging, not treatment.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02172771 | OMNISCAN | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 potential interacting drugs, almost all with an unclassified severity level. The only one with a graded severity is **acebutolol (Moderate)**. Others with unclassified severity include calcitriol, pantoprazole, omeprazole, lansoprazole, vancomycin, prednisone, simvastatin, potassium chloride, dexamethasone and acetylsalicylic acid.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The supporting literature describes gadodiamide as an imaging agent, not a therapy, and there are no clinical trials. No therapeutic mechanism is known.

**To proceed, the following is needed:**
- Mechanism of action data showing a plausible therapeutic pathway
- Health Canada package insert warnings and contraindications, needed for any safety screening
- Approved indication and dosage form details for the Canadian licence
- Preclinical or clinical evidence of a therapeutic effect, not just diagnostic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

