---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is an androgen receptor blocker, best known for treating prostate cancer. The Evidence Pack does not include its label indication text, so this original indication comes from general knowledge.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but there are **0 clinical trials** and only **1 publication** (a comment on a retrospective study) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (general knowledge; Canadian licence indication text was not provided in the pack) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L3 (as graded in the pack; the support is a single comment article, so this is at the weak end of L3) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bicalutamide is a nonsteroidal androgen receptor antagonist. Androgen signaling drives hair follicle growth, so blocking the receptor could plausibly reduce androgen-dependent hair growth. This is the link between its original use, where it blocks androgen-driven tumor growth, and the predicted use in excess hair growth.

The one linked record is a comment on a retrospective review of 35 patients. That review reported bicalutamide improving minoxidil-induced hypertrichosis in female pattern hair loss. This suggests possible relevance, but the primary data are not in the pack.

Two caveats apply. The predicted disease, hypertrichosis, is broader than the minoxidil-induced setting in that paper. Also, detailed mechanism of action data from DrugBank is not currently available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment | J Am Acad Dermatol | Comment on a retrospective review of 35 patients on bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. No abstract is available, so the comment's own arguments cannot be summarized. |

---

## Canada Market Information

Six licences are recorded. The five main ones are listed below. Dosage form and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 02270226 | TEVA-BICALUTAMIDE |
| 02519178 | BICALUTAMIDE |
| 02357216 | JAMP-BICALUTAMIDE |
| 02325985 | ACH-BICALUTAMIDE |
| 02275589 | PMS-BICALUTAMIDE |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (antiandrogen) therapy, not a conventional cytotoxic |
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
The prediction score is high, but the only supporting item is a comment article. There are no registered trials, and the primary study is not in the pack. This is a research question rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- Retrieve and appraise the primary retrospective study of 35 patients (bicalutamide for minoxidil-induced hypertrichosis) and the comment's arguments
- Search for prospective or controlled studies of antiandrogens in hypertrichosis
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Safety review for any non-oncology use, including dose, duration and patient population, especially in women

Among the other top predictions, only female breast carcinoma has meaningful support: a Phase 2 combination trial and preclinical and case literature. It may be a stronger repurposing direction than hypertrichosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

