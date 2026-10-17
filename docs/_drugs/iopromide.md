---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Iopromide: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the Canadian license records compiled for this report"
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
---

# Iopromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent used for diagnostic imaging (marketed in Canada as ULTRAVIST).
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but this is a model prediction only,
with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records compiled for this report (iopromide is known as a radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is an iodinated, non-ionic contrast agent. It is used to enhance visibility of structures on X-ray and CT imaging, not to treat disease.

No mechanistic link to the predicted indication has been established. Iopromide has no known pharmacological action on joint tissue or on genetic susceptibility pathways. The high score is a computational output only. It is likely a knowledge-graph artifact, for example from the shared use of contrast agents in joint imaging (arthrography).

The other top predictions show the same pattern. They include osteoarthritis, rheumatoid arthritis, rare skeletal dysplasias (brachyolmia, acromesomelic dysplasia Hunter-Thompson type, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy. All have scores above 99%, none has any supporting trial or publication, and none has a plausible therapeutic mechanism. The scores therefore appear to reflect network structure rather than biology.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02078619 | ULTRAVIST 370 | Not specified | Not specified |
| 02078600 | ULTRAVIST 300 | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction databases. The main ones listed are as follows:
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, polymyxin B, streptomycin
  - **Moderate**: mannitol
  - **Unknown severity**: clotrimazole, acetylsalicylic acid, bupropion, dexamethasone, pantoprazole

Label warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or publications, no plausible mechanism, and no therapeutic role for a diagnostic contrast agent in the predicted conditions. The Canadian license records also lack indication text and safety label data.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking iopromide to joint or cartilage disease
- Preclinical or clinical evidence for the predicted indication
- Canadian package insert (warnings, contraindications and approved indications) to support safety screening
- Review of whether the prediction is only an artifact of iopromide's use in arthrography
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

