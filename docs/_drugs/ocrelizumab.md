---
layout: default
title: Ocrelizumab
parent: Model Prediction Only (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is a humanized anti-CD20 monoclonal antibody originally used to deplete CD20+ B cells in the treatment of Multiple Sclerosis. The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure embedding-similarity signal with no mechanistic or clinical evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (MS) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data for ocrelizumab is not yet available in this evidence pack (DrugBank MOA field is unpopulated). Based on the information captured in the repurposing rationale, ocrelizumab works by binding CD20 on B lymphocytes and depleting them — the mechanism underlying its efficacy in Multiple Sclerosis, an autoimmune disease driven partly by B-cell activity.

The link to HER2 positive breast carcinoma is considerably weaker. B cells and tumour-infiltrating lymphocytes do play a role in the breast cancer immune microenvironment, but there is no established causal or subtype-specific connection between CD20+ B-cell depletion and HER2-driven oncogenic signaling. The evidence pack's own rationale explicitly characterizes the TxGNN score as an artifact of embedding-space disease similarity rather than a mechanism-driven hypothesis.

Notably, all ten of the top predicted indications for this drug (ranks 1–10) are scored at the same L5 evidence level with a "Hold" recommendation, and none have supporting clinical trials. One candidate (rank 4, "breast tumor luminal A or B") returned 19 PubMed hits, but manual review found these to be keyword false positives — matches on "B cell development," "hepatitis B," and "HLA-B typing" rather than genuine breast-cancer-relevant literature. This pattern suggests the current prediction set for ocrelizumab is largely graph-topology noise rather than a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are zero clinical trials, zero literature citations, and no mechanistic rationale specific to HER2 positive breast carcinoma — the evidence pack's own scoring (S0/L5) and rationale text flag this as an embedding-similarity artifact rather than a credible repurposing hypothesis. Regulatory safety data (warnings, contraindications) is also missing (data gap DG001, Blocking severity), which independently precludes any progression toward safety review.

**To proceed, the following is needed:**
- Formal DrugBank/label-sourced mechanism-of-action documentation (DG002)
- TFDA/health authority label safety data — warnings and contraindications (DG001, blocking)
- Preclinical or mechanistic studies establishing a specific link between CD20+ B-cell depletion and HER2-driven breast cancer pathogenesis
- Re-screening of other ranked candidates for this drug to rule out further keyword false positives before any candidate advances past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

