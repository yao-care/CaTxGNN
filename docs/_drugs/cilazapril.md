---
layout: default
title: Cilazapril
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cilazapril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Cilazapril is an ACE inhibitor marketed in Canada, used as an antihypertensive-class drug (the licence records do not state the approved indication).
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, with a very high score (99.2%).
However, there are **0 clinical trials** and **20 publications**, and none of the publications study cilazapril or ACE inhibitors in pulmonary hypertension, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; cilazapril is an ACE inhibitor of the antihypertensive class |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.2% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Cilazapril is known to be an ACE inhibitor, so it blocks the renin-angiotensin-aldosterone system (RAAS). RAAS inhibition could plausibly affect pulmonary vascular remodelling, which is the only mechanistic argument the data supports.

There are also reasons for caution. In pulmonary hypertension driven by hypoxia, systemic vasodilators can worsen ventilation-perfusion matching and cause hypotension. The high TxGNN score comes from a graph-based prediction and is not backed by any cilazapril-specific study.

The same drug has two other predictions that are mechanistically more coherent, though also unsupported by trials or literature:
- **Malignant renovascular hypertension** (score 99.1%): strongly RAAS-dependent, so ACE inhibition fits. Renal function decline in bilateral renal artery stenosis or a solitary functioning kidney is a major concern.
- **Malignant hypertensive renal disease** (score 99.1%): RAAS activation is involved. Hyperkalaemia and abrupt changes in blood pressure or renal function are risks in compromised kidneys.

A fourth prediction, pulmonary hypertension with unclear multifactorial mechanism (99.2%), has no trials or literature and no basis for a mechanistic argument.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 retrieved publications are general hypoxia papers (brain ageing, cancer, keloid, multiple sclerosis, altitude). **None studies cilazapril or ACE inhibitors in pulmonary hypertension**, so they offer no direct support. Ten are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | Describes the basic mechanisms of hypoxaemia (low ambient oxygen, hypoventilation, V/Q mismatch, shunt); background only |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia and brain ageing: role in neurodegeneration and possible neuroprotection |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Clinical evidence and molecular mechanisms of cognitive impairment caused by hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | Cellular responses to hypoxia and their role in vascular disease, inflammation and cancer |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends Cancer | Deubiquitinases, HIF regulation and cancer |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clin Oncol | Modifying tumour hypoxia to improve radiotherapy and other cancer treatments |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biol | Interplay between hypoxia and multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review/Commentary | Rev Med Inst Mex Seguro Soc | Hypobaric hypoxia and adaptation at high altitude |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Preclinical | Adv Sci (Weinh) | NAT10/SEPT9/HIF-1α loop drives glycolysis addiction in gastric cancer cells |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Preclinical | Redox Biol | Altered glucose metabolism in keloid fibroblasts under hypoxia |

---

## Canada Market Information

Eight licences are registered; five are shown. Dosage form and approved indication text are not available in the records.

| DIN | Product Name |
|---------|------|
| 02283794 | MYLAN-CILAZAPRIL |
| 01911481 | INHIBACE |
| 02291142 | APO-CILAZAPRIL |
| 02283786 | MYLAN-CILAZAPRIL |
| 02283778 | MYLAN-CILAZAPRIL |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.

Please refer to the package insert for warnings and contraindications.

Class-level concerns relevant to the predicted uses, from general ACE-inhibitor pharmacology and not from cilazapril-specific data:
- Hypotension and worsened ventilation-perfusion matching in hypoxic lung disease
- Acute renal function decline in bilateral renal artery stenosis or a solitary functioning kidney
- Hyperkalaemia and abrupt blood pressure or renal changes in compromised kidneys

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction rests on a graph-based score alone. There are no clinical trials, and none of the 20 publications concerns cilazapril or ACE inhibitors in this condition. The hypoxia-related physiology also raises a plausible safety concern.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for cilazapril (for example, from DrugBank)
- A targeted literature search on ACE inhibitors in pulmonary hypertension, using drug-specific terms rather than generic hypoxia terms
- Consideration of prioritising the renovascular and malignant hypertensive renal disease predictions, which are more mechanistically coherent. These would need a review of ACE-inhibitor class data and a strict renal monitoring plan.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

