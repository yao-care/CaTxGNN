---
layout: default
title: Polatuzumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Polatuzumab Vedotin: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Not available in the Health Canada license data compiled for this rep…"
monitor_inn: "POLATUZUMAB VEDOTIN"
predicted_indications: ["HER2 positive breast carcinoma"]
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From B-Cell Malignancy (Original Indication Not Listed) to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an antibody-drug conjugate that is marketed in Canada under the brand name POLIVY. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Health Canada license data compiled for this report |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, polatuzumab vedotin is an antibody-drug conjugate that targets CD79b and delivers the microtubule-disrupting payload monomethyl auristatin E (MMAE). CD79b is a B-cell receptor component found on mature B cells and B-cell malignancies.

The link to HER2-positive breast carcinoma is weak. CD79b is not a recognized target in this cancer, and no connection to HER2 signaling or to CD79b expression in breast tumors is established. The high score (0.993) is a knowledge-graph prediction. It may reflect the shared MMAE payload class, which other antibody-drug conjugates use, or general network proximity to microtubule-targeting agents used in breast cancer. A high score does not by itself indicate a mechanistic basis.

HER2-positive breast cancer also already has effective approved HER2-directed therapies, including trastuzumab, pertuzumab and trastuzumab deruxtecan. Any new agent would have to show a clear advantage over these options.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02515431 | POLIVY | Not specified | Not specified |
| 02499614 | POLIVY | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic microtubule-disrupting payload (MMAE) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically includes CBC with differential, and liver and renal function) |
| Handling Protection | Please refer to the package insert; follow institutional cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total, and the first 20 are included in the data compiled for this report. All are rated Moderate or Major.
  - **Major**: Clarithromycin, Cobicistat, Deferiprone, Samarium (153Sm) lexidronam
  - **Moderate** (examples): Aprepitant, Cimetidine, Metronidazole, Miconazole, Rosuvastatin, Simvastatin, Ticagrelor, Chloroquine, Hydroxychloroquine, Disulfiram

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5). There is also no established mechanistic link between CD79b targeting and HER2-positive breast carcinoma, and effective HER2-directed therapies already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before safety screening can proceed
- Mechanism of action data from DrugBank
- Evidence of CD79b or other relevant target expression in HER2-positive breast tumors
- Preclinical studies of polatuzumab vedotin in HER2-positive breast cancer models
- Approved indication text for each DIN, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

