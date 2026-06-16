---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# Catridecacog: From Congenital Factor XIII A-Subunit Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog is a recombinant Factor XIII A-subunit (rFXIII) originally indicated for prophylaxis of bleeding episodes in patients with congenital Factor XIII A-subunit deficiency.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
with **no clinical trials** and **no publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Factor XIII A-subunit deficiency (no Canadian DIN on record) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, catridecacog is a recombinant Factor XIII A-subunit that catalyzes the final step of the coagulation cascade — cross-linking fibrin monomers into a mechanically stable clot network. In congenital FXIII A-subunit deficiency, patients suffer from severe, delayed-onset bleeding because unstable fibrin clots dissolve prematurely; catridecacog restores cross-linking activity and clot durability.

The theoretical bridge to **primary release disorder of platelets** (dense and/or alpha granule deficiencies) rests on a specific biological observation: Factor XIII is stored within platelet alpha granules as platelet FXIII (pFXIII). When granule release is impaired, endogenous pFXIII is not secreted at the site of injury, potentially weakening the fibrin network that must compensate for defective primary hemostasis. Supplementing with circulating rFXIII could theoretically reinforce fibrin cross-linking to partially offset the hemostatic gap — however, this is an indirect inference. Catridecacog replenishes plasma-phase FXIII; it does not repair granule release machinery or platelet activation pathways. The mechanistic link is weak.

Two additional high-scoring TxGNN predictions — **pseudo-von Willebrand disease** (platelet-type vWD, rank #2, 99.29%) and **Glanzmann thrombasthenia** (rank #3, 99.15%) — share a structurally similar rationale: all three are platelet function disorders where primary hemostasis is impaired, and enhanced fibrin cross-linking may provide partial secondary hemostatic compensation. Among the three, Glanzmann thrombasthenia carries the relatively strongest mechanistic logic, as rFXIII's fibrin-stabilizing role parallels the bypass coagulation rationale behind rFVIIa (NovoSeven) use in that condition — though rFXIII acts downstream of thrombin generation rather than amplifying it. Pseudo-vWD, by contrast, centers on a GPIbα gain-of-function mutation consuming large-multimer vWF, a pathway entirely orthogonal to FXIII. All three remain at the level of theoretical inference only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Catridecacog currently has no Drug Identification Numbers (DINs) in Canada and is not marketed. No licensed product information is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications are supported exclusively by TxGNN model output (Evidence Level L5), with zero registered clinical trials and no published literature across all queried sources. The mechanistic connections are theoretically plausible but indirect, and catridecacog has no Canadian regulatory presence, making near-term clinical repurposing impractical without foundational groundwork.

**To proceed, the following is needed:**
- MOA data from DrugBank API (DG002: flagged as High severity) to confirm cross-linking pharmacodynamics relevant to platelet disorders
- Safety profile: package insert warnings, contraindications, and DDI data are entirely absent (DG001: flagged as Blocking) — must be resolved before any safety evaluation
- Preclinical evidence: animal models or in vitro studies demonstrating rFXIII benefit in platelet release disorders or Glanzmann thrombasthenia
- Literature re-query: expand to case reports, compassionate use, or off-label documentation for rFXIII in any platelet function disorder
- Regulatory pathway scoping: orphan drug designation assessment in Canada for the three rare platelet disease indications
- Prioritization decision: if further development is warranted, **Glanzmann thrombasthenia** should be evaluated first given its comparatively stronger mechanistic rationale and existing rFVIIa precedent as a bypass therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

