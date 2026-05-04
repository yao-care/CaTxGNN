---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to X-Linked Ichthyosis (Non-STS-Deficient)

## One-Sentence Summary

Alirocumab is a PCSK9 inhibitor monoclonal antibody approved globally for LDL-cholesterol lowering in patients with familial hypercholesterolemia and established cardiovascular disease, though it currently holds no Canadian market authorization.
The TxGNN model's top prediction identifies **X-Linked Ichthyosis (without steroid sulfatase deficiency)** as a potential new indication; however, **zero clinical trials** and **zero publications** support this direction, placing it at the lowest possible evidence tier.
This report also flags a more mechanistically credible candidate — xanthomatosis and cholesterol catabolic process disease — identified at ranks 3 and 5 in the full prediction list.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Familial Hypercholesterolemia (global approvals; no Canadian DINs on record) |
| Predicted New Indication (Rank 1) | Ichthyosis, X-linked, without steroid sulfatase deficiency |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacology, Alirocumab is a fully human IgG1 monoclonal antibody that binds and inhibits PCSK9 — a serine protease secreted primarily by hepatocytes that would otherwise tag LDL receptors for lysosomal degradation. By blocking this interaction, Alirocumab increases LDL receptor recycling on hepatocyte surfaces, boosting hepatic clearance of circulating LDL-C by approximately 50–60%. It is approved in the United States and European Union for heterozygous familial hypercholesterolemia (HeFH) and atherosclerotic cardiovascular disease.

X-linked ichthyosis without steroid sulfatase (STS) deficiency is a rare skin barrier disorder. The "non-STS-deficient" subtype is distinct from classical XLI: it does not involve the STS enzyme, and its pathophysiology centres on keratinocyte differentiation abnormalities and cholesterol sulfate retention in the stratum corneum — a metabolic axis that operates completely independently of the hepatic PCSK9/LDL receptor signalling pathway targeted by Alirocumab.

The high TxGNN score (99.43%) most plausibly reflects cholesterol-node topological proximity in the knowledge graph rather than a genuine mechanistic bridge. The repurposing rationale embedded in the evidence pack itself concludes that PCSK9 inhibition has no direct influence on cutaneous cholesterol sulfate metabolism, and that the two metabolic axes do not overlap. This is a critical barrier that cannot be resolved without a novel and currently uncharacterised indirect pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ichthyosis, X-linked, without steroid sulfatase deficiency.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Canada Market Information

Alirocumab currently holds no Drug Identification Numbers (DINs) in Canada and is recorded as not marketed in this evidence pack. No approved indication text is available from Canadian regulatory records.

> **Note:** Alirocumab (Praluent®, Sanofi/Regeneron) has received approvals in the United States (FDA, 2015) and European Union (EMA, 2015) for hypercholesterolemia and cardiovascular risk reduction. Canadian Health Canada regulatory status should be independently verified against the Health Canada Drug Product Database, as the absence of DINs in this evidence pack may reflect a data collection gap.

---

## Safety Considerations

Please refer to the package insert for safety information.

> TFDA package insert warnings and contraindications were not retrieved for this report (Data Gap DG001, severity: Blocking). This gap must be resolved before any clinical safety screening can proceed.

---

## Supplementary: Higher-Priority Candidates in the Top-10 List

While the rank 1 prediction is assessed as Hold, two candidates in the full prediction list carry meaningfully stronger repurposing rationale and are highlighted here for completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 3 | Xanthomatosis | 99.37% | L5 | Research Question |
| 5 | Cholesterol catabolic process disease | 99.36% | L3 | Research Question |

**Xanthomatosis (Rank 3):** Xanthomas arise from LDL-C and cholesterol ester deposition in skin, tendons, and cornea — a direct consequence of the hypercholesterolaemia that Alirocumab is designed to treat. LDL-C reduction of >50% is mechanistically expected to reduce lipid deposition and may promote xanthoma regression. Case reports of PCSK9 inhibitor use in familial hypercholesterolaemia-associated xanthomas support biological plausibility, though no dedicated RCT exists.

**Cholesterol Catabolic Process Disease (Rank 5):** One completed Phase 3 trial (NCT03207945) studied PCSK9 inhibition in HIV-infected patients with cholesterol metabolism dysregulation (n=118). While this is an indirect evidence bridge (HIV-specific population, not the target disease category), it is the only clinical trial in the entire top-10 list, and it provides L3-level mechanistic support for the PCSK9/cholesterol catabolic axis.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rank 1 — X-Linked Ichthyosis, Non-STS-Deficient)*

**Rationale:**
The TxGNN prediction score is high but the mechanistic analysis identifies no credible biological link between hepatic PCSK9 inhibition and cutaneous cholesterol sulfate pathophysiology; the high score is an artefact of knowledge graph topology rather than a genuine therapeutic signal, and there is no supporting clinical or preclinical evidence of any kind.

**To proceed on Rank 1, the following would be needed:**
- Preclinical evidence (cell or animal model) demonstrating that PCSK9 inhibition alters keratinocyte cholesterol sulfate metabolism in STS-independent XLI
- A pharmacological mechanistic bridge between circulating LDL-C modulation and stratum corneum lipid composition
- Resolution of Data Gap DG001 (TFDA/Health Canada package insert warnings) before any safety screening

**For the more promising candidates (Ranks 3 & 5), recommended next steps:**
- Retrieve complete NCT03207945 results publication to determine primary endpoint outcome for cholesterol catabolic process disease (Rank 5)
- Conduct a targeted PubMed search for PCSK9 inhibitor + xanthoma case series or observational studies (Rank 3)
- Resolve Data Gap DG002 (MOA documentation) and DG001 (safety data) to enable S1 safety screening for both candidates
- Assess route compatibility: Alirocumab is a subcutaneous injection; confirm this is appropriate for the target patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

