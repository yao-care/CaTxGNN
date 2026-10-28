---
layout: default
title: Plerixafor
parent: Model Prediction Only (L5)
nav_order: 746
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
description: "Plerixafor: predicted new indication CMM7 (evidence level L5). Approved use: Not recorded in the local data"
---

# Plerixafor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Plerixafor: CMM7
{: .text-alpha }

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist, used in Canada to mobilise stem cells in patients with plasma cell myeloma (multiple myeloma) and non-Hodgkin lymphoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Plerixafor blocks the CXCR4 receptor (it also interacts with ACKR3). Normally, CXCR4 binds the chemokine CXCL12 and keeps blood stem cells anchored in the bone marrow. By disrupting this bond, plerixafor releases stem cells into the bloodstream. This is why it is used to collect stem cells for autologous transplantation in myeloma and lymphoma.

Indolent plasma cell myeloma is a slowly progressing form of the same disease as the original indication. The high TxGNN score most likely reflects this close disease relationship rather than any subtype-specific finding. A plausible biological link is that the CXCR4/CXCL12 axis helps myeloma cells stay in the protective bone marrow niche. However, this has not been demonstrated in the data compiled for this report. Plerixafor's approved role is also stem cell mobilisation, not treating the myeloma itself, so the prediction should not be read as evidence of an anti-myeloma effect.

**Related signal in another disease:** The strongest evidence for plerixafor in the predictions is in myeloid leukaemia (a lower-ranked prediction). There, 27 trials and 20 publications examine plerixafor as a chemosensitiser. It is used to release leukaemia cells from bone marrow niches so that chemotherapy works better. This evidence is early-phase and does not carry over to myeloma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for indolent plasma cell myeloma.

---

## Literature Evidence

Currently no related literature available for indolent plasma cell myeloma.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02529815 | PLERIXAFOR INJECTION |
| 02539454 | PLERIXAFOR INJECTION |

Both authorisations are valid single-ingredient products. Dosage form, manufacturer and approved indication text were not available in the licence records.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links plerixafor to caution in thrombocytopenia, impaired renal function and leukaemia. Treat these as signals to verify against the official label, not as confirmed contraindications.
- **Drug interactions:** No drug–drug interactions were identified. The only interaction data are pharmacological targets (CXCR4 and ACKR3).

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or publications address this subtype, and plerixafor is established as a stem cell mobiliser, not as a treatment for the myeloma itself. The higher-ranked score reflects disease proximity rather than clinical evidence.

**To proceed, the following is needed:**
- Subtype-specific preclinical or clinical evidence that CXCR4 blockade affects indolent myeloma biology or outcomes
- Clear definition of the intended clinical role (disease control versus mobilisation)
- Review of the Health Canada package insert for warnings, contraindications and dosing, with attention to renal impairment and thrombocytopenia
- If the project is redirected, a separate evaluation of the myeloid leukaemia signal, which has early-phase evidence but no Phase 3 randomised data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

