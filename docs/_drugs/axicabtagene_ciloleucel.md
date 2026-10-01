---
layout: default
title: Axicabtagene Ciloleucel
parent: Model Prediction Only (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Axicabtagene Ciloleucel
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

# Axicabtagene ciloleucel: From Large B-Cell Lymphoma to Crohn's Colitis

## One-Sentence Summary

Axicabtagene ciloleucel (Yescarta) is an autologous anti-CD19 CAR-T cell therapy, generally used for relapsed or refractory B-cell lymphoma. The TxGNN model predicts it may be effective for **Crohn's colitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Large B-cell lymphoma (general drug knowledge; the local record contains no approved indication text) |
| Predicted New Indication | Crohn's colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, axicabtagene ciloleucel is an autologous CD19-directed CAR-T cell therapy. Its efficacy in B-cell malignancies rests on eliminating CD19-expressing B cells, and mechanistically that deep B-cell depletion may be relevant to immune-mediated disease.

The link to Crohn's colitis is only conceptual. CD19 CAR-T is being explored more broadly in autoimmune disease, but B-cell-directed therapy has shown limited benefit in Crohn's disease. The 0.914 TxGNN score is a graph-based prediction, and no trial or publication in the data supports it.

Lymphodepletion and cytokine release syndrome are major safety concerns for a non-malignant indication, so the risk-benefit balance is currently unfavorable.

**Other candidates in the same prediction list** (all L5, all Hold):
- The most plausible other candidate is rheumatoid vasculitis (86.24%), where B-cell depletion is biologically relevant, but no specific evidence exists.
- Ankylosing spondylitis has only a weak link, because its disease drivers are the TNF and IL-17/IL-23 axes.
- Several candidates have no plausible CD19 link and likely reflect graph-topology artifacts. These are multiple endocrine neoplasia, adrenal gland hyperfunction, HER2-positive breast carcinoma, and the mastocytosis-related diseases.
- Idiopathic aplastic anemia is a particular concern, because CAR-T-related prolonged cytopenias would be dangerous in bone marrow failure.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2485648 | YESCARTA | Not listed | Not listed in the local record |

---

## Cytotoxicity

The record has no DrugBank category or toxicity data, so this classification is inferred from the drug type.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (autologous CAR-T cell therapy) |
| Myelosuppression Risk | Prolonged cytopenias are a recognized concern with CAR-T therapy |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; at minimum, CBC and monitoring for cytokine release syndrome and neurotoxicity |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

Safety concerns noted in the candidate rationale, which are not sourced from the label:
- Cytokine release syndrome
- Neurotoxicity
- Prolonged cytopenias
- Lymphodepletion-related risks

No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, literature, or established mechanism for Crohn's colitis. The serious toxicity profile of CAR-T therapy is hard to justify for a non-malignant indication without supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any clinical or preclinical evidence of CD19 CAR-T in Crohn's disease, and a comparison against approved biologics
- Approved indication text, dosage form, and manufacturer for the Canadian license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

