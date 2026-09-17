---
layout: default
title: Tisagenlecleucel
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 10
---

# Tisagenlecleucel
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

# Tisagenlecleucel: From B-Cell Malignancies to Crohn's Colitis

## One-Sentence Summary

> Tisagenlecleucel (Kymriah) is an anti-CD19 CAR-T cell therapy originally developed to eliminate CD19+ B cells in B-cell malignancies.
> The TxGNN model predicts a possible application in **Crohn's Colitis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-generated hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell malignancies (CD19+) — derived from mechanistic description in evidence pack; not confirmed by Canadian regulatory filing |
| Predicted New Indication | Crohn's Colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug-level record (`original_moa: [Data Gap]`). Based on the mechanistic description attached to the prediction itself, tisagenlecleucel is an anti-CD19 CAR-T cell therapy whose core mechanism is the elimination of CD19-expressing B cells, and it is used clinically in B-cell malignancies.

B cells do play a contributory role in some autoimmune conditions, which is the general biological rationale offered for CAR-T repurposing into immune-mediated disease. However, Crohn's colitis is primarily driven by Th1/Th17 T-cell activity and intestinal barrier dysfunction — B cells are not considered a core pathogenic pathway. The evidence pack itself flags this mechanistic link as "weak and purely inferential" (機轉關聯薄弱且純屬推論).

No clinical trials, ICTRP registrations, or literature currently exist to support this specific indication. This places the candidate firmly at evidence level L5 (model prediction only), and it should be treated as a hypothesis-generation signal rather than a repurposing lead ready for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Tisagenlecleucel currently has **0 DINs** and is **not marketed** in Canada per the available regulatory dataset. No authorized product, dosage form, or approved indication text is on file.

---

## Cytotoxicity (Antineoplastic Drugs Only)

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (autologous anti-CD19 CAR-T cell therapy) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by an unvalidated knowledge-graph score (L5), with no clinical trials or literature evidence, and the evidence pack's own mechanistic assessment describes the biological link to Crohn's colitis as weak. A blocking data gap (missing regulatory warnings/contraindications) also prevents this candidate from entering even a preliminary safety review (S1).

**To proceed, the following is needed:**
- TFDA/Health Canada label data — package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action and original approved indication from DrugBank (DG002)
- At least preclinical or observational evidence directly linking anti-CD19 B-cell depletion to Crohn's colitis pathophysiology
- Drug interaction (DDI) profile, currently unqueried/not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

