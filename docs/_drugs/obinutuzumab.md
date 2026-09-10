---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 569
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Pregerminal Center CLL/SLL

## One-Sentence Summary

Obinutuzumab is a glycoengineered anti-CD20 monoclonal antibody already used in chronic lymphocytic leukemia (CLL) and follicular lymphoma (FL). The TxGNN model further predicts activity in **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)** — a molecular subtype defined by unmutated IGHV status — but this specific candidate currently has **no matching clinical trials or literature**, so it rests on the model's prediction score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (per trial-level literature in this evidence pack; a formal regulatory label record was not retrieved — data gap) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for obinutuzumab is flagged as a data gap in this evidence pack. Based on the information that is available, obinutuzumab is a third-generation, glycoengineered, type II anti-CD20 monoclonal antibody. Its cytotoxic effect against B-cell malignancies operates through enhanced antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis, and direct induction of apoptosis — a mechanism described in the supporting evidence for a related B-cell malignancy candidate in this same pack (follicular lymphoma).

"Pregerminal center" CLL/SLL refers to the subset of CLL/SLL arising from B cells that have not undergone germinal-center somatic hypermutation (i.e., unmutated IGHV). This is not a distinct disease from CLL/SLL but a molecular/prognostic subtype of it. Since CD20 expression on malignant lymphocytes is not dependent on IGHV mutation status, the mechanistic rationale for obinutuzumab activity in this subtype is biologically plausible — the antibody's target antigen is present regardless of subtype.

That said, this is a subtype-level extrapolation rather than a genuine cross-disease repurposing signal, and no trial or publication in this query set specifically studied this named subtype. Broader-term CLL/SLL trials likely exist in the literature (obinutuzumab is already used in CLL) but were not captured under this exact disease-name query, so the mechanistic plausibility currently outpaces the directly attributable evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Obinutuzumab is not currently marketed in Canada — 0 DINs on file, market status "Not Marketed." No product licenses are available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (type II anti-CD20 monoclonal antibody, not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; hepatitis B screening prior to initiation (class-level consideration for anti-CD20 antibodies); infusion-related reaction monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by the TxGNN model's prediction score — no clinical trials or literature were retrieved for this specific molecular subtype, and obinutuzumab is not currently marketed in Canada. Evidence is insufficient to move beyond model-prediction stage.

**To proceed, the following is needed:**
- Regulatory label data (TFDA/Health Canada) confirming the original approved indication(s) and formal MOA documentation
- A broader-term literature/trial search using general "CLL/SLL" and "unmutated IGHV CLL" keywords to check whether existing obinutuzumab CLL evidence is attributable to this subtype
- Canadian market authorization status confirmation before any commercial evaluation proceeds
- Formal safety data (warnings, contraindications, DDI) from the product monograph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

