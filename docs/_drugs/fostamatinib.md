---
layout: default
title: Fostamatinib
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Fostamatinib
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

# Fostamatinib: From Immune Thrombocytopenia (ITP) to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib (Tavalisse) is a selective SYK (spleen tyrosine kinase) inhibitor, approved by the U.S. FDA for chronic immune thrombocytopenia (ITP) in adults, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Autosomal Thrombocytopenia with Normal Platelets**, a rare inherited platelet disorder with partial mechanistic overlap with ITP through the SYK–FcγR signalling axis.
There are currently **no clinical trials** and **no publications** specifically supporting this repurposing direction, placing this prediction at a hypothesis-generating stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Immune Thrombocytopenia (ITP) — FDA-approved; no Canadian DIN on file |
| Predicted New Indication | Autosomal Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 (Mechanistic / Biological Rationale) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Fostamatinib is a prodrug rapidly converted in vivo to its active metabolite R406, a potent and selective inhibitor of SYK. In immune thrombocytopenia, SYK drives antibody-dependent platelet destruction via FcγRIIA signalling on macrophages and monocytes; blocking SYK reduces immune-mediated platelet clearance and has demonstrated clinical efficacy in Phase 3 trials. This is fostamatinib's established mechanism and the pharmacological basis for its FDA approval.

Autosomal thrombocytopenia with normal platelets — exemplified by ANKRD26-related thrombocytopenia — is a mechanistically distinct entity caused by genetic defects in megakaryopoiesis and platelet production rather than peripheral immune destruction. However, SYK plays a recognised role in normal megakaryocyte development and in platelet receptor signalling (GPVI, FcγRIIA), providing an indirect biological rationale. Moreover, some cases of inherited thrombocytopenia may harbour a superimposed immune clearance component, in which SYK inhibition could offer marginal benefit even if the primary genetic defect is unaddressed.

The high TxGNN score (99.45%) most likely reflects strong topological proximity between fostamatinib and ITP-related nodes in the knowledge graph rather than disease-specific experimental evidence. The prediction should be interpreted as a hypothesis-generating signal: mechanistic plausibility is present but indirect, and no clinical or preclinical data currently validate this specific application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fostamatinib in autosomal thrombocytopenia with normal platelets.

---

## Literature Evidence

Currently no related literature available for Fostamatinib in autosomal thrombocytopenia with normal platelets.

---

## Canada Market Information

Fostamatinib is not currently marketed in Canada and holds no issued Drug Identification Numbers (DINs). It is approved in the United States (FDA, 2018) under the brand name Tavalisse® for the treatment of thrombocytopenia in adult patients with chronic ITP who have had an insufficient response to a previous treatment.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Fostamatinib has a coherent mechanistic basis for thrombocytopenic conditions via SYK inhibition, and the TxGNN prediction score is high (99.45%); however, autosomal thrombocytopenia with normal platelets is a genetically heterogeneous disorder driven primarily by impaired platelet production rather than immune destruction, and no clinical or preclinical data currently support this specific repurposing direction.

**To proceed, the following is needed:**
- Retrieve formal MOA data (SYK inhibition selectivity, IC50, off-target profile) from DrugBank API to address DG002
- Characterise which ANKRD26 or other genetic subtypes carry an immune-clearance component that SYK inhibition could address
- Commission or identify preclinical models (patient-derived iPSC megakaryocytes, ANKRD26-knockin mice) to test R406/fostamatinib effects on megakaryocyte differentiation and platelet output
- Obtain full safety package (key warnings, contraindications, DDI profile) — TFDA/Health Canada package insert data currently unavailable (DG001)
- Assess Health Canada regulatory pathway requirements for a drug with no existing Canadian approval prior to any IND-enabling work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

