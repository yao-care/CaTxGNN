---
layout: default
title: Mogamulizumab
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
---

# Mogamulizumab
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is an anti-CCR4 antibody marketed in Canada as POTELIGEO, and its approved use is in cutaneous T-cell lymphoma.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (from the Evidence Pack's mechanistic notes; the Canadian licence record has no indication text) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Mogamulizumab is an anti-CCR4 monoclonal antibody. It depletes CCR4-positive cells, including regulatory T cells (Tregs), through antibody-dependent cellular cytotoxicity (ADCC).

The only plausible link to urothelial carcinoma is a speculative one. Tregs and the CCR4 ligands CCL17/CCL22 are implicated in immunosuppressive tumour microenvironments in general. Depleting Tregs might therefore boost antitumour immunity in urothelial tumours. No CCR4 involvement in this tumour type is documented in the supplied data.

Several other top predictions are urothelial variants (kidney pelvis sarcomatoid, bladder sarcomatoid, renal pelvis papillary). They are likely near-duplicates that reflect a shared graph neighbourhood rather than independent signals. The high score should therefore be read as a hypothesis, not as evidence of efficacy.

Two lower-ranked predictions are worth noting as research questions:
- **Transitional cell carcinoma (rank 9):** the broadest urothelial category. Combining CCR4 blockade with checkpoint inhibitors is a plausible hypothesis-generating question.
- **Richter syndrome (rank 10):** a lymphoid transformation, which loosely fits the drug's use in a lymphoid malignancy. CCR4 expression on the tumour cells is unverified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| Licence Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2527715 | POTELIGEO | Not listed in the record | Not listed in the record |

---

## Cytotoxicity

The original indication is a lymphoma, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: No interactions were found in the queried data.
- **Immune-related toxicity**: Depleting Tregs could worsen immune-related toxicity, which is a theoretical concern in any new setting.

Please refer to the package insert for full safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are supported by the model score alone, with no registered trials or publications. The mechanistic link to urothelial carcinoma is speculative, and the top-ranked entries are likely redundant with one another.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism-of-action data (for example, from DrugBank)
- Evidence of CCR4 or CCR4-ligand (CCL17/CCL22) expression and Treg infiltration in urothelial tumours
- Preclinical or early-phase data, prioritising broad transitional cell carcinoma with checkpoint-inhibitor combinations as the first research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

