---
layout: default
title: Estrone
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 2
---

# Estrone
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

# Estrone: From Endogenous Estrogen to Zinc, Elevated Plasma

## One-Sentence Summary

Estrone (雌酮) is an endogenous estrogen hormone with known roles in hormonal homeostasis, traditionally associated with hormone replacement therapy in menopausal conditions.
The TxGNN model predicts it may be effective for managing **Zinc, Elevated Plasma** (hyperzincemia),
with **0 clinical trials** and **2 publications** currently offering only indirect, mechanistic support for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication data available (not marketed in Taiwan) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Estrone is an endogenous estrogen — one of the three primary estrogens naturally produced in the human body — and has been used clinically in hormone replacement contexts for menopausal conditions.

The mechanistic link proposed by the TxGNN model centres on estrogen's known ability to upregulate metallothionein (MT) gene expression. Metallothioneins are cysteine-rich proteins that chelate zinc and other heavy metals in tissues; by increasing MT expression — particularly in the liver — estrone could theoretically enhance zinc sequestration and reduce circulating plasma zinc concentrations. Estrogen response elements (EREs) have been identified in MT gene promoter regions, making this pathway biologically plausible.

However, this mechanistic chain is indirect and inferential. No direct clinical evidence exists that estrone has been used to treat hyperzincemia. The two identified literature items touch on estrogen-zinc interactions in the contexts of protein-calorie malnutrition and perimenopausal metabolism, but neither directly validates estrone as a treatment for elevated plasma zinc. This prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [807594](https://pubmed.ncbi.nlm.nih.gov/807594/) | 1975 | Observational/Cross-sectional | J Clin Endocrinol Metab | Studied the pituitary-gonadal axis in 28 men with severe protein-calorie malnutrition; testosterone and gonadal hormone changes observed during refeeding, providing indirect context on estrogen–mineral homeostasis relationships |
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Interventional Study (dietary) | Am J Clin Nutr | Examined soy protein intake effects on iron indexes and total antioxidant status in perimenopausal women; notes that estrogen deficiency may increase metabolic and oxidative risk, tangentially relevant to estrogen–metal homeostasis |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.81%), there are no clinical trials and zero direct studies supporting estrone as a treatment for elevated plasma zinc. Evidence consists solely of indirect mechanistic inference, warranting a Hold until foundational safety and mechanistic data gaps are resolved.

**To proceed, the following is needed:**
- Retrieve MOA data from DrugBank (DB00655) to confirm or refute the estrogen → metallothionein → zinc sequestration pathway
- Conduct a targeted literature search specifically on estrone/estrogen effects on plasma zinc levels or metallothionein regulation in human subjects
- Download and parse the TFDA 仿單 (package insert) to address the **Blocking** data gap (DG001) on warnings and contraindications before any safety evaluation can proceed
- Identify whether any preclinical (animal or in vitro) studies have directly tested estrone's effect on zinc homeostasis
- Assess route compatibility and clinically feasible dosing for this proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

