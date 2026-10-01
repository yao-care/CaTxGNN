---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 377
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is a calcium channel blocker sold in Canada and generally used to lower blood pressure. The licence records supplied do not state the approved indication. The TxGNN model predicts it may help with **pulmonary hypertension owing to lung disease and/or hypoxia**, but there are **0 clinical trials** and no retrieved publication that studies felodipine for this condition. The evidence is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence records (hypertension is the drug's general use, from background knowledge rather than the Evidence Pack) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Felodipine is a vasoselective L-type calcium channel blocker that relaxes vascular smooth muscle. Its effect in systemic hypertension is well established, and it could plausibly also dilate the pulmonary vascular bed.

The prediction is weak for this specific indication. The 0.999 score reflects network proximity to hypertension and vasodilator nodes in the knowledge graph, not clinical support. In lung disease, pulmonary vasodilation can blunt hypoxic pulmonary vasoconstriction, worsen ventilation-perfusion matching and aggravate hypoxemia, so the same mechanism that makes the prediction plausible is also a risk.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 18 retrieved papers cover hypoxia biology in general (brain, cancer, fibrosis, immunity). None evaluates felodipine or pulmonary hypertension treatment. The most relevant ones are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | Describes the four basic mechanisms of hypoxemia (low ambient oxygen, hypoventilation, V/Q mismatch, right-to-left shunt). Background only, no drug data |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia and brain aging, including hypoxia from pulmonary disease. Not about felodipine |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Clinical evidence and mechanisms of cognitive impairment under acute and chronic hypoxia. Not about felodipine |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | Cellular responses to hypoxia and their role in vascular disease, inflammation and cancer. Not about felodipine |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell Tissue Res | Hypoxia signalling through HIF-1 in tissue repair and fibrosis. Not about felodipine |

---

## Canada Market Information

Eight licences are recorded; the five below are the ones supplied in detail. Dosage form and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 2280272 | SANDOZ FELODIPINE |
| 2057778 | PLENDIL |
| 2452367 | APO-FELODIPINE |
| 851787 | PLENDIL |
| 851779 | PLENDIL |

---

## Safety Considerations

- **Predicted-indication risk**: Pulmonary vasodilation in patients with lung disease may worsen gas exchange and hypoxemia by impairing hypoxic pulmonary vasoconstriction.

Please refer to the package insert for warnings, contraindications and drug interaction information. No such data was available in the Evidence Pack, and the drug interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on graph proximity. There are no trials and no literature on felodipine for this condition, and the mechanism could plausibly worsen hypoxemia in lung disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data from DrugBank
- Felodipine-specific hemodynamic or outcome data in pulmonary hypertension due to lung disease, with attention to oxygenation

**Other predicted indications are better supported and worth a separate review:**
- **Prinzmetal angina** (rank 7): L2, with several small felodipine-specific clinical studies from 1989 to 1995. Its recommendation is Proceed with Guardrails, limited to confirmed vasospastic angina, with monitoring for hypotension, reflex tachycardia and peripheral edema.
- **Chronic pulmonary heart disease** (rank 6): L3, with small, old hemodynamic studies only. It remains a research question.

The remaining predictions (ranks 2, 3, 4 and 5) are L5 with a Hold recommendation.

This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires clinical validation before use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

