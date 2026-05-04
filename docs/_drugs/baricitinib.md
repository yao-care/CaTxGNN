---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baricitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Baricitinib is a selective JAK1 and JAK2 inhibitor approved in multiple jurisdictions for rheumatoid arthritis, atopic dermatitis, and COVID-19, though it currently holds no Canadian regulatory authorization.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital developmental disorder affecting both ocular structure and skeletal morphology.
This prediction is currently supported by **no clinical trials** and **no published literature**, resting entirely on computational model output.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Canadian regulatory data (Baricitinib is a JAK1/2 inhibitor broadly approved for rheumatoid arthritis in other jurisdictions) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on information embedded within the repurposing rationale, Baricitinib exerts its effect through selective inhibition of JAK1 and JAK2, blocking the downstream JAK-STAT signaling cascade. This mechanism reduces the production and signaling of pro-inflammatory cytokines and is the basis for its established efficacy in immune-mediated inflammatory diseases such as rheumatoid arthritis, atopic dermatitis, and severe COVID-19.

The predicted indication — colobomatous microphthalmia-rhizomelic dysplasia syndrome — is an ultra-rare congenital disorder characterized by structural eye anomalies (coloboma and microphthalmia) combined with shortening of the proximal limb bones (rhizomelic dysplasia). The JAK-STAT pathway does have a marginal role in ocular morphogenesis, including retinal cup formation and retinal pigment epithelium differentiation, and animal studies have reported JAK2 involvement in RPE cell fate decisions. However, this syndrome is primarily caused by mutations in embryonic transcription and developmental receptor genes (*PAX2*, *SOX2*, *OTX2*, *STRA6*), representing a fixed structural defect arising during embryogenesis — not an inflammation-driven or kinase-dysregulated process.

The mechanistic plausibility of this repurposing is therefore rated **low hypothetical**. Baricitinib's JAK1/JAK2 inhibition has no known pathway to correct pre-existing congenital structural malformations. The rhizomelic dysplasia component is an independent concern, typically linked to peroxisome biogenesis gene (*PEX*) or *DHAPAT* mutations — entirely outside the pharmacological reach of JAK inhibitors. The model's high confidence score most likely reflects indirect topological proximity within the knowledge graph rather than a direct or even plausible therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Canadian drug licenses (DINs) are currently registered for Baricitinib in this dataset. Baricitinib is not marketed in Canada according to the available regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model assigning a computationally high score of 99.94%, the mechanistic link between JAK1/JAK2 inhibition and this congenital developmental syndrome is extremely tenuous — the condition arises from embryonic structural defects unrelated to inflammatory or kinase-driven pathology — and no clinical or preclinical evidence (Evidence Level L5) exists to support further investigation at this time.

**To proceed, the following is needed:**

- Retrieve the complete drug monograph from Health Canada or the originating regulatory authority (e.g., EMA, FDA) for full warnings, contraindications, and drug interaction data
- Obtain complete MOA and pharmacological profile from DrugBank (DB11817) to fill the current mechanism data gap
- Commission a formal mechanistic feasibility review assessing whether JAK-STAT inhibition has any post-natal therapeutic role in colobomatous microphthalmia-rhizomelic dysplasia syndrome
- Conduct a targeted literature search on JAK-STAT signaling in congenital ocular malformations and skeletal dysplasias
- Confirm current Canadian regulatory status via a direct Health Canada Drug Product Database query, as marketed status may differ from this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

