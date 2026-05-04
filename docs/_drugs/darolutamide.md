---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide (brand name: NUBEQA) is an androgen receptor (AR) antagonist approved internationally for non-metastatic castration-resistant prostate cancer (nmCRPC).
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-metastatic castration-resistant prostate cancer (nmCRPC) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from the DrugBank data extract for this analysis. Based on known information, Darolutamide is a selective androgen receptor (AR) antagonist that competitively inhibits androgen binding to the AR, thereby blocking downstream AR-driven transcriptional signaling. Its established efficacy in prostate cancer — a tumour highly dependent on AR pathway activation — forms the pharmacological basis of any cross-indication prediction via this mechanism.

The theoretical case for HoFH rests on the AR's known role in hepatic lipid metabolism: AR signaling can modulate PCSK9 expression and regulate LDL receptor (LDLR) degradation in hepatocytes. In theory, AR antagonism could upregulate LDLR surface expression and reduce circulating LDL cholesterol. This indirect link is the likely reason TxGNN assigned a high score — the lipid metabolism node in the knowledge graph is densely connected to androgen signaling.

However, HoFH is fundamentally caused by homozygous loss-of-function mutations in the *LDLR* gene itself. Even if AR antagonism increased LDLR transcription, the structurally defective or absent receptor cannot be rescued by this mechanism. This incompatibility, combined with the availability of highly effective approved therapies (PCSK9 inhibitors, Lomitapide, Evinacumab), means the TxGNN high score most likely reflects non-specific connectivity at a shared metabolic network node rather than a true actionable mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen receptor antagonist (second-generation anti-androgen; hormone therapy) |
| Myelosuppression Risk | Low (AR antagonists do not cause direct bone marrow suppression; myelotoxicity not a class effect) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST/bilirubin), CBC, blood pressure, QTc interval |
| Handling Protection | Classified as a hazardous drug (antineoplastic category); follow institutional hazardous drug handling and disposal protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported by L5 evidence only — a TxGNN model score with no clinical trials, no published literature, and a mechanistic hypothesis that is structurally incompatible with the primary pathophysiology of HoFH (homozygous LDLR loss-of-function). Well-established and internationally approved therapies already exist for this condition.

**To proceed, the following is needed:**
- Preclinical validation: in vitro and animal model studies to determine whether AR antagonism meaningfully affects LDL metabolism in LDLR-deficient contexts
- MOA data: formal retrieval from DrugBank API to characterize the AR–cholesterol pathway linkage
- Safety data: full package insert review (e.g., Health Canada, FDA, or EMA prescribing information) for complete warnings, contraindications, and drug interaction profile
- Patient stratification hypothesis: identification of any HoFH subgroup (e.g., partial LDLR function, compound heterozygotes) where AR-mediated LDLR upregulation might be physiologically meaningful
- Regulatory gap: Darolutamide is currently not marketed in Canada; market entry pathway would need evaluation if evidence were to strengthen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

