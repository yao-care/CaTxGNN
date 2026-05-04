---
layout: default
title: Evinacumab
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Evinacumab
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

# Evinacumab: From Homozygous Familial Hypercholesterolemia to Diabetic Cataract

## One-Sentence Summary

Evinacumab (Evkeeza) is a fully human monoclonal antibody targeting Angiopoietin-like protein 3 (ANGPTL3), approved in the United States for the treatment of **homozygous familial hypercholesterolemia (HoFH)** in adults and adolescents. The TxGNN model predicts it may have potential in **Diabetic Cataract** — the highest-ranked prediction among a cluster of 10 ophthalmologic indications — with the closely related indication of **Diabetic Retinopathy** (rank 10) providing the only available mechanistic anchor, supported by **1 translational publication** from 2026. No clinical trials or direct literature exist for evinacumab in diabetic cataract itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data pipeline. Based on publicly known information, Evinacumab is a fully human IgG4 monoclonal antibody that inhibits **ANGPTL3 (Angiopoietin-like protein 3)**. ANGPTL3 normally suppresses the activity of lipoprotein lipase (LPL) and endothelial lipase; by blocking ANGPTL3, evinacumab broadly lowers plasma triglycerides, LDL-C, and HDL-C, offering a lipid-independent pathway that works even in patients with non-functional LDL receptors — the key rationale for its use in HoFH.

The predicted link to diabetic cataract is biologically indirect but not implausible. Chronic dyslipidaemia and hyperglycaemia both accelerate lens protein glycation, polyol pathway activation, and oxidative stress — the primary biochemical drivers of diabetic cataract. By correcting systemic metabolic dysregulation, ANGPTL3 inhibition might theoretically reduce the metabolic burden on the lens. The TxGNN model likely derives this prediction through shared disease-graph features: diabetic cataract and diabetic retinopathy share the same diabetic complication cluster, and the model's top 10 predictions are overwhelmingly cataract subtypes, suggesting a disease-node co-clustering effect rather than a drug-specific signal.

Importantly, a 2026 translational study (PMID 41555340) directly demonstrates that the **ANGPTL3–integrin α5 axis** drives blood-retinal barrier breakdown and retinal vascular leakage in diabetic retinopathy — establishing ANGPTL3 as more than just a lipid regulator in the diabetic eye. While retinal vasculature and the lens are distinct structures, this finding raises the possibility that ANGPTL3 may participate in broader diabetic ocular pathology. This indirect biological signal supports prioritising **diabetic retinopathy** (rank 10, L4 evidence) over diabetic cataract (rank 1, L5) as the more scientifically tractable repurposing target at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Evinacumab in diabetic cataract.

---

## Literature Evidence

Currently no related literature available for Evinacumab in diabetic cataract specifically.

> **Contextual note — Diabetic Retinopathy (Rank 10, L4):** Although outside the top prediction, the following publication provides the only available mechanistic evidence linking evinacumab's target (ANGPTL3) to any diabetic ocular indication and is included for reference:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41555340](https://pubmed.ncbi.nlm.nih.gov/41555340/) | 2026 | Mechanistic / Basic Science | Journal of Translational Medicine | Demonstrates that the ANGPTL3–integrin α5 axis drives blood-retinal barrier (BRB) breakdown and retinal vascular leakage in diabetic retinopathy; ANGPTL3 is identified as a clinical predictor of DR with a direct causal role in retinal vascular pathology, providing a rationale for ANGPTL3 inhibition as a potential therapeutic strategy |

---

## Canada Market Information

Evinacumab is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN prediction score (98.52%) for diabetic cataract appears to be driven by disease-cluster co-localisation within the diabetic complication graph rather than a verified drug-specific mechanism; there are no clinical trials, no preclinical studies, and no direct publications linking evinacumab to cataract of any type. The one available piece of evidence (PMID 41555340) supports a mechanistic hypothesis for **diabetic retinopathy** — a different, though related, ocular indication — and does not extend to the lens.

**To proceed, the following is needed:**

- Retrieve confirmed mechanism of action data from DrugBank or the prescribing information (ANGPTL3 pathway, downstream metabolic and vascular effects on ocular tissues)
- Obtain Health Canada and TFDA package insert data for safety warnings, contraindications, and drug interaction profile
- Conduct a targeted literature review on ANGPTL3 expression in human lens epithelial cells and its potential role in lens glycation or oxidative stress
- Evaluate whether the retinal vascular evidence (PMID 41555340) can support a hypothesis-generating preclinical study specifically in lens tissue
- Consider formally pivoting the repurposing evaluation to **diabetic retinopathy (rank 10, L4)** as the primary candidate, given the available mechanistic anchor and stronger scientific rationale compared to diabetic cataract
- If pursuing the cataract cluster further, clarify whether the model's clustering reflects genuine pharmacological plausibility or is an artefact of dense disease-node connectivity in the diabetic complication subgraph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

