---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: From Iron Overload to Hepatic Porphyria

## One-Sentence Summary

Deferiprone (DB08826) is an oral iron chelator used globally for transfusion-dependent iron overload — most notably in thalassemia — though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently supporting this direction.
The evidence base remains at the preclinical and mechanistic level (L4), positioning this as a research hypothesis that requires prospective clinical investigation before any repurposing decision can be made.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Transfusion-dependent iron overload (global use; no Taiwan registration) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Deferiprone is a bidentate oral iron chelator (3-hydroxy-4-methylpyrid-2(1H)-one) that works by binding free ferric iron (Fe³⁺) in the labile iron pool and facilitating its urinary excretion. Detailed mechanism of action data is not available in the current evidence pack; however, deferiprone's core pharmacological action — systemic and organ-level iron depletion — is well-established across its approved and investigational indications in hematological diseases.

Iron plays a pivotal and well-characterized role in the pathogenesis of hepatic porphyrias, particularly Porphyria Cutanea Tarda (PCT). Excess hepatic iron activates ALAS1 (aminolevulinic acid synthase 1), amplifying porphyrin precursor production; concurrently, free iron drives Fenton-reaction-mediated oxidative damage that underlies the hallmark features of skin photosensitivity and hepatocellular injury. This is precisely why phlebotomy — which depletes hepatic iron stores — is established first-line therapy for PCT, providing a direct mechanistic rationale for exploring an oral iron chelation strategy in patients who cannot tolerate phlebotomy.

The TxGNN prediction is mechanistically coherent. Literature PMID 32678895 provides translational clinical evidence that iron chelation rescues hemolytic anemia and photosensitivity in Congenital Erythropoietic Porphyria (CEP), while PMID 17854053 demonstrates in a Hfe⁻/⁻ murine PCT model that oral deferiprone reduces hepatic uroporphyrin accumulation to a degree comparable to an iron-deficient diet. Taken together, these findings suggest a plausible biological pathway — but no human clinical trials of deferiprone specifically in hepatic porphyria have been conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Clinical Case Series / Translational | *Blood* | Iron chelation rescued hemolytic anemia and skin photosensitivity in Congenital Erythropoietic Porphyria (CEP) patients; provides clinical translational rationale for iron chelation across porphyria subtypes |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal Study (murine model) | *Hepatology* | Oral deferiprone (L1) reduced hepatic uroporphyrin accumulation in Hfe⁻/⁻ mice with PCT-like disease, performing comparably to an iron-deficient diet; directly supports the mechanistic feasibility of deferiprone in hepatic porphyria |

---

## Taiwan Market Information

Deferiprone currently has no registered products in Taiwan (TFDA). No license or approved indication data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Key warnings, contraindications, and drug interaction data are not available in the current evidence pack (Data Gaps DG001–DG002). Of particular clinical concern in this target population: deferiprone carries a known risk of **agranulocytosis** requiring mandatory weekly neutrophil monitoring, and its safety profile in patients with pre-existing **hepatic disease** (relevant to porphyric liver involvement) has not been formally characterized. These gaps must be resolved before any clinical decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between deferiprone and hepatic porphyria is scientifically plausible — iron depletion is the established therapeutic principle for PCT — but the current evidence is limited to a porphyria subtype case series (CEP, not classic hepatic PCT) and a single murine model study. With zero registered clinical trials and no Taiwan regulatory presence, the evidence base does not yet support advancement beyond a research hypothesis.

**To proceed, the following is needed:**

- **MOA data**: Retrieve complete mechanism of action from DrugBank API (DG002) to confirm and document the iron-chelation rationale formally
- **Safety package**: Obtain TFDA package insert and/or EMA/FDA label for full warnings, contraindications, and drug interactions — particularly agranulocytosis monitoring requirements and hepatic safety data (DG001)
- **Indication refinement**: Clarify target porphyria subtype — PCT is the strongest candidate given its iron-phlebotomy paradigm; CEP and other subtypes warrant separate evaluation
- **Clinical pilot study**: Design a prospective n-of-1 or small cohort study in PCT patients with confirmed hepatic iron overload who are contraindicated or intolerant to phlebotomy
- **Comparator context**: Review evidence for existing alternatives (low-dose hydroxychloroquine, deferoxamine) in porphyria to position deferiprone's potential differentiated value
- **Regulatory pathway**: Assess feasibility of Taiwan NDA or compassionate use pathway given zero local licensing history
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

