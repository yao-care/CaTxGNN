---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From Hemostatic/Antidiuretic Therapy to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin is a synthetic analog of vasopressin (ADH), clinically established for central diabetes insipidus, nocturnal enuresis, and bleeding disorders such as mild hemophilia A and von Willebrand disease Type 1.
The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency**,
however, with **0 clinical trials** and **0 publications** currently supporting this direction, and the mechanistic rationale assessed as a poor fit.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed in Canada regulatory data (known established uses: central diabetes insipidus, nocturnal enuresis, bleeding disorder prophylaxis) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Desmopressin (DDAVP) is a synthetic structural analog of arginine vasopressin. Its hemostatic effect is mediated primarily through V2 receptor stimulation on vascular endothelium, triggering rapid release of stored von Willebrand factor (vWF) and Factor VIII — thereby enhancing platelet adhesion and amplifying the intrinsic coagulation pathway. It is this mechanism that underpins its established use in mild hemophilia A and Type 1 von Willebrand disease.

Congenital prothrombin deficiency is a rare autosomal recessive bleeding disorder caused by mutations in the *F2* gene, resulting in reduced synthesis or impaired function of prothrombin (Factor II). Standard treatment is replacement therapy with fresh frozen plasma (FFP) or prothrombin complex concentrates (PCC). The mechanistic fit for Desmopressin is poor: its hemostatic action operates entirely through vWF and FVIII release, with no known direct or indirect regulatory effect on prothrombin synthesis or activity.

The high TxGNN score (99.70%) most likely reflects broad node-level similarity within the "hemorrhagic disorder" cluster of the knowledge graph, rather than a disease-specific mechanistic link. This is a recognized limitation of graph-based prediction: diseases sharing phenotypic similarity (bleeding tendency) can receive elevated scores even when their molecular pathologies — and therefore their therapeutic targets — are fundamentally different.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No DIN records were found for Desmopressin in the current evidence pack.

> **⚠️ Data Gap Notice**: Desmopressin is a long-established drug marketed internationally under brand names such as DDAVP, Stimate, Noctiva, and Nocdurna. The absence of Canadian DIN records likely reflects a gap in the data collection pipeline rather than the true regulatory status. It is strongly recommended to verify directly via Health Canada's Drug Product Database (DPD) before drawing conclusions about Canadian market availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Critical Safety Flags Identified During Multi-Indication TxGNN Analysis**
>
> The following contraindication-level concerns were surfaced during mechanistic review of co-predicted indications and should be incorporated into any subsequent safety assessment:
>
> - **Pseudo-von Willebrand Disease (Platelet-type vWD)**: Desmopressin is **absolutely contraindicated**. The GPIb gain-of-function mutation in this condition causes spontaneous vWF–platelet binding; administering Desmopressin to release additional vWF can precipitate massive platelet aggregation, thrombocytopenia, and thrombotic events.
> - **Inherited Thrombophilia**: Desmopressin's pro-hemostatic, pro-thrombotic mechanism is directionally harmful in patients with hereditary hypercoagulable states and should not be considered.
> - **Hereditary Thrombocytosis**: Elevated platelet counts combined with Desmopressin's hemostatic amplification may increase thrombotic risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction of Desmopressin for congenital prothrombin deficiency represents a mechanistic mismatch — Desmopressin acts exclusively through the vWF/Factor VIII axis with no capacity to compensate for Factor II (prothrombin) deficiency, which requires direct replacement therapy. There is zero clinical trial or literature evidence to support this indication, and the high TxGNN score is attributable to non-specific graph topology rather than a clinically actionable connection.

**To proceed, the following is needed:**

- **Resolve the data gap on MOA**: Retrieve the full mechanism of action from DrugBank API (DB00035) to support proper mechanistic reasoning.
- **Resolve the data gap on safety profile**: Download and parse the package insert from Health Canada / TFDA to obtain formal warnings and contraindications.
- **Verify Canada market status**: Cross-check against Health Canada's Drug Product Database directly to confirm whether Desmopressin holds active DINs.
- **Consider re-ranking by mechanistic validity**: Among the 10 predicted indications, Glanzmann thrombasthenia (Rank 3) and primary release disorder of platelets (Rank 4) carry stronger mechanistic rationale and are more suitable for moving to a Research Question stage (S1), pending literature confirmation.
- **Flag knowledge graph anomaly**: The "flood factor deficiency" node (Rank 7) appears to be a KG mapping artifact for von Willebrand disease — if confirmed, Desmopressin would represent an **L1-level established therapy** for that entity, warranting immediate re-classification to "Go."
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

