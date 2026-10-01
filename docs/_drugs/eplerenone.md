---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Eplerenone: From Mineralocorticoid Receptor Antagonism to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor (MR) antagonist marketed in Canada. The Evidence Pack does not list its approved indication text.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**.
There are **0 clinical trials** and **18 publications** on general hypoxia biology, none of which studies eplerenone, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada records provided |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Eplerenone is a selective MR antagonist. Aldosterone/MR signaling has been implicated in pulmonary vascular remodeling and fibrosis, so blocking it could plausibly help in pulmonary hypertension.

This link is biologically plausible but unverified. The provided data contain no eplerenone-specific support. The high TxGNN score (0.995) reflects a model prediction, not independent clinical evidence.

Four other indications were also predicted, and all have L5 evidence and a "Hold" recommendation:
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.50%). It has the same score as the top prediction, which suggests a shared graph neighborhood rather than independent evidence.
- **Malignant renovascular hypertension** (99.50%). There is an indirect rationale, since renin-angiotensin-aldosterone activation drives this condition. Hyperkalemia and renal-function risk would need a safety review.
- **Malignant hypertensive renal disease** (99.50%). It is mechanistically plausible, but its score is identical to the renovascular entry, so it is likely not independent evidence.
- **Braddock syndrome** (99.34%). No mechanistic link could be identified, so it is treated as a likely knowledge-graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 18 retrieved publications are general hypoxia-biology papers. None mentions eplerenone, and none reports treatment of pulmonary hypertension. All are marked "relevance: pending". The 10 shown below are the most relevant reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | Four basic mechanisms of hypoxemia: low ambient oxygen, hypoventilation, V/Q mismatch, right-to-left shunt |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia in brain aging and neurodegeneration, including settings of pulmonary disease |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Clinical evidence and molecular mechanisms of cognitive impairment from acute and chronic hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | Cellular oxygen sensing and hypoxia's role in vascular disease, inflammation and cancer |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Not classified | Cell Tissue Res | Role of hypoxia and HIF-1 signalling in tissue repair and fibrosis |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Not classified | Annu Rev Immunol | Hypoxia and HIF in innate immunity and inflammation |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Not classified | J Appl Physiol | Translational overview of hypoxia (no abstract available) |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biol | Interplay between hypoxia and multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | Hypobaric hypoxia and altitude adaptation |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clin Oncol | Modifying tumour hypoxia to improve radiotherapy outcomes |

---

## Canada Market Information

Five of the six authorizations are listed in the Evidence Pack. Dosage form and approved indication text were not provided.

| DIN | Product Name |
|---------|------|
| 02543397 | JAMP EPLERENONE |
| 02323060 | INSPRA |
| 02323052 | INSPRA |
| 02471442 | MINT-EPLERENONE |
| 02543389 | JAMP EPLERENONE |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug-interaction data were available in the Evidence Pack.

One caution comes from the mechanism-based review of the hypertension-related predictions. Hyperkalemia and renal-function risk would need a safety review in populations with renal artery stenosis, malignant hypertension or renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no registered trials and no eplerenone-specific literature. The 99.50% score is shared by several related entries, so it likely reflects graph structure rather than independent evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data (for example from DrugBank) to test the MR-signaling link in pulmonary vascular disease
- Approved indication text and dosage forms for each DIN, to define the original indication
- A targeted search for eplerenone or MR-antagonist studies in pulmonary hypertension (preclinical and clinical)
- A hyperkalemia and renal-function safety review for the target population

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

