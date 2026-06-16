---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Eplerenone: From Heart Failure / Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor (MR) antagonist, with established use internationally for heart failure post-myocardial infarction and hypertension, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (WHO Group 3 PH)**, based on the known role of aldosterone/MR signalling in pulmonary vascular remodelling.
Supporting evidence is limited to mechanistic rationale and **20 retrieved publications** — none of which directly study eplerenone in this indication — and **no registered clinical trials** were identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure post-MI; hypertension (internationally established; not approved in Canada) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH) |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Eplerenone is a highly selective mineralocorticoid receptor (MR) antagonist. Unlike spironolactone, it has minimal affinity for androgen or progesterone receptors, which reduces off-target side effects. Internationally, it is approved for reducing cardiovascular mortality in stable patients with left ventricular dysfunction and clinical heart failure following acute myocardial infarction, and for essential hypertension. Detailed mechanism of action data was not available in this Evidence Pack; however, its pharmacological class is well established in the literature.

The mechanistic rationale for this prediction centres on the aldosterone/MR axis in pulmonary hypertension (PH). Aldosterone levels are elevated in patients with pulmonary arterial hypertension (PAH), and MR activation is believed to drive pulmonary vascular fibrosis, smooth muscle remodelling, and right ventricular (RV) hypertrophy. Animal model studies have demonstrated that MR antagonism can attenuate RV pressure overload — providing a plausible biological basis for this prediction.

However, the predicted indication is **WHO Group 3 PH** (PH secondary to lung disease or hypoxia), which differs pathophysiologically from Group 1 PAH. In Group 3 PH, hypoxic pulmonary vasoconstriction and the underlying lung disease are the primary drivers, and the degree to which aldosterone-mediated pathways contribute is not well characterised. No direct human clinical trial data exists for eplerenone in this setting, and in patients with concomitant chronic lung disease and renal impairment, the risk of hyperkalaemia — eplerenone's principal safety concern — would require careful evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> **Important caveat**: The 20 publications retrieved via the automated PubMed search query for eplerenone + pulmonary hypertension/hypoxia are **general hypoxia biology reviews** and do not directly study eplerenone in pulmonary hypertension. They are listed below for completeness but provide only indirect contextual support.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Describes the four core mechanisms of hypoxaemia (hypoventilation, V/Q mismatch, shunt, diffusion), foundational to understanding Group 3 PH pathophysiology |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Broad review of cellular hypoxia responses including angiogenesis and pH homeostasis; relevant background on HIF-driven vascular adaptation |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | Hypoxia and HIF-1 signalling in tissue fibrosis; contextually relevant to pulmonary vascular remodelling |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Hypoxia in innate immunity and inflammation — highlights physiologic vs. inflammatory hypoxia as distinct compartments |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia and neurodegeneration; limited relevance to PH but contextualises systemic hypoxia consequences |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology (RCR) | Therapeutic strategies targeting tumour hypoxia; limited relevance to PH but discusses HIF pathway intervention |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Basic Science | Redox Biology | Metabolic reprogramming of keloid fibroblasts under hypoxia via HIF-1α/PI3K/AKT; indirect mechanistic context |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Acute and chronic hypoxia causing cognitive impairment; not relevant to PH indication |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Science | Advanced Science | NAT10/HIF-1α glycolysis loop in gastric cancer; not relevant to eplerenone or PH |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hypoxia in multiple sclerosis pathology and vascular dysfunction; not directly relevant to PH |

---

## Canada Market Information

Eplerenone is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on file.

> For reference: eplerenone is approved in the United States (Inspra®, Pfizer) and the European Union for post-MI heart failure and hypertension. A Health Canada new drug submission would be required before any Canadian use.

---

## Safety Considerations

Please refer to the package insert for safety information.

> *Note*: Although formal package insert data was not available for this Evidence Pack, eplerenone's well-known class safety profile includes risk of **hyperkalaemia** (particularly with eGFR < 30 mL/min, use of ACE inhibitors/ARBs, or diabetes), which is especially relevant in the Group 3 PH patient population who commonly have concurrent CKD or advanced lung disease.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN prediction score is high (99.50%), and there is a plausible mechanistic rationale linking aldosterone/MR pathways to pulmonary vascular remodelling in PH. However, the 20 retrieved publications do not directly address eplerenone in pulmonary hypertension — they are general hypoxia biology reviews with no clinical or preclinical data on the drug-disease pair. With zero registered clinical trials and no direct human evidence, this candidate remains at hypothesis stage only (Evidence Level L4). Additionally, the WHO Group 3 PH population carries elevated hyperkalaemia risk that would need independent safety characterisation.

**To proceed, the following is needed:**

- **Targeted literature search**: Conduct a dedicated search for eplerenone (or class: MR antagonists / spironolactone) specifically in pulmonary hypertension models or patients — the current 20 papers are non-specific
- **Preclinical evidence review**: Identify animal model studies (monocrotaline or hypoxia-induced PH models) that tested MR antagonists to establish whether L4 evidence truly exists
- **MOA documentation**: Obtain formal DrugBank/TFDA mechanism of action data to enable mechanistic-link scoring
- **Safety assessment for Group 3 PH population**: Model hyperkalaemia risk given typical comorbidity profile (CKD, diuretics, ACEi co-use) in this patient population
- **Health Canada regulatory pathway**: eGFR thresholds and contraindications would need alignment with Canadian labelling standards before any clinical investigation
- **Expert consultation**: Pulmonology/respirology opinion on whether MR antagonism has a biologically distinct role in Group 3 vs. Group 1 PH to determine if a research protocol is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

