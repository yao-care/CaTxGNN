---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Imipenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the evidence pack's top-ranked candidate (`predicted_indications[0]` = diffuse scleroderma) as required by the report template.

# Imipenem: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Imipenem is a broad-spectrum carbapenem antibiotic; detailed original indication and mechanism-of-action data are not available in this evidence pack. The TxGNN model predicts a possible link to **Diffuse Scleroderma**, but this direction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no indication text on file; drug is not currently marketed in Canada) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for imipenem in this evidence pack. Based on known pharmacology, imipenem is a broad-spectrum carbapenem antibiotic used against serious bacterial infections — a mechanism of bacterial cell-wall synthesis inhibition, not an immunomodulatory or antifibrotic action.

Diffuse scleroderma is an autoimmune, fibrotic connective-tissue disease with no established infectious pathology. There is no known pharmacological or clinical pathway connecting a beta-lactam antibiotic's mechanism to scleroderma pathogenesis.

The evidence pack's own rationale for this pairing states directly: *"No plausible mechanism: imipenem is an antibiotic and diffuse scleroderma is an autoimmune fibrotic disease with no infectious pathology link; there are no trials or literature supporting this pairing — it is assessed as noise from TxGNN embedding similarity."* This assessment, combined with the complete absence of clinical trials or literature (confirmed by 3 independent zero-result queries in the query log), indicates this specific prediction should not be treated as a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Imipenem is not currently marketed in Canada — no DIN (Drug Identification Number) records are on file, and no product licenses are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for imipenem in diffuse scleroderma, no plausible mechanistic link (antibacterial vs. autoimmune-fibrotic pathology), and the drug is not currently marketed in Canada. This candidate should not advance without new supporting data.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for imipenem
- Any preclinical or in vitro data suggesting a biological pathway between carbapenem antibiotics and fibrotic/autoimmune disease
- TFDA/Health Canada label data (warnings, contraindications, drug interactions) — currently a Data Gap
- Independent replication of the TxGNN signal, given it currently reads as embedding-similarity noise rather than a grounded hypothesis

**Note on the broader evidence pack:** This report covers only the rank-1 candidate (diffuse scleroderma) as specified by the template. The same evidence pack contains other predicted indications for imipenem with materially stronger support that may warrant separate evaluation — notably **salmonellosis** (L3, decision stage S2, Proceed with Guardrails; 20 literature hits including a Phase 4 clinical evaluation) and **staphylococcus aureus infection** (L2, decision stage S3, Proceed with Guardrails; multiple completed Phase 3/4 trials and clinical case series on imipenem/fosfomycin combination therapy for MRSA). Both are grounded in imipenem's actual antibacterial mechanism, unlike the scleroderma pairing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

