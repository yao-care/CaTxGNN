---
layout: default
title: Cobimetinib
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Cobimetinib
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

# Cobimetinib: From Melanoma to Amyotrophic Lateral Sclerosis

## One-Sentence Summary

Cobimetinib is a selective MEK1/2 inhibitor approved globally (US, EU) in combination with vemurafenib for the treatment of BRAF V600E/K mutation-positive unresectable or metastatic melanoma; it currently holds no approved indication in Taiwan.
The TxGNN model predicts it may be effective for **Amyotrophic Lateral Sclerosis (ALS)**,
with **0 clinical trials** and **0 publications** currently supporting this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600E/K mutation-positive unresectable or metastatic melanoma (global; not approved in Taiwan) |
| Predicted New Indication | Amyotrophic Lateral Sclerosis (ALS) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cobimetinib is a potent, selective oral inhibitor of MEK1/2 (mitogen-activated extracellular signal-regulated kinase 1 and 2), key effector kinases within the RAS/RAF/MEK/ERK signalling cascade. It is approved in the United States and European Union in combination with vemurafenib (a BRAF inhibitor) for BRAF-mutated advanced melanoma. Detailed mechanism of action data from DrugBank was not successfully retrieved in this Evidence Pack (Data Gap DG002); however, cobimetinib's class identity as a MEK inhibitor is well established in oncology literature and forms the basis of the mechanistic inference below.

The predicted connection to ALS draws on emerging preclinical evidence that dysregulated MEK/ERK signalling contributes to motor neuron degeneration. Three specific lines of reasoning support this link: (1) ERK hyperactivation has been documented in degenerating motor neurons of ALS patients and animal models; (2) MEK inhibition has demonstrated anti-neuroinflammatory effects in microglia within TDP-43 and FUS model systems; and (3) abnormal ERK phosphorylation is consistently observed in SOD1-mutant ALS models. TxGNN likely established this candidate-disease connection by traversing knowledge graph nodes shared between MEK/ERK pathway biology and motor neuron degeneration pathology.

It must be emphasised, however, that all mechanistic reasoning above remains at the level of inference. No direct clinical evidence exists for cobimetinib in ALS. Furthermore, cobimetinib is an oncology agent with a toxicity profile optimised for cancer patients — including risks of retinopathy, left ventricular dysfunction, hepatotoxicity, and rhabdomyolysis — which would require careful re-evaluation in an ALS patient population who typically have no cancer-related comorbidities. CNS penetration, a critical pharmacokinetic requirement for a neurodegenerative target, has not been characterised for cobimetinib in available public literature.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for cobimetinib in amyotrophic lateral sclerosis.

---

## Literature Evidence

Currently no related literature is available linking cobimetinib to amyotrophic lateral sclerosis.

---

## Taiwan Market Information

Cobimetinib is not currently approved or marketed in Taiwan. No product licenses or Drug Identification Numbers are on record with the Taiwan FDA (TFDA). Consequently, no locally approved indication text is available for reference.

---

## Cytotoxicity

Cobimetinib meets the antineoplastic criteria: it is indicated for melanoma (a malignant disease) and belongs to the targeted kinase inhibitor class used in oncology practice.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — MEK1/2 kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to Moderate (anaemia and thrombocytopenia reported; less myelosuppressive than conventional chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), creatine phosphokinase (CPK/CK), left ventricular ejection fraction (LVEF by echocardiography), ophthalmological evaluation (central serous retinopathy/retinal vein occlusion), renal function, serum electrolytes |
| Handling Protection | Institutional cytotoxic drug handling precautions recommended; standard targeted oral agent procedures apply |

---

## Safety Considerations

Please refer to the approved product monograph (e.g., Cotellic® prescribing information, FDA/EMA) for complete safety information. No Taiwan-specific warnings, contraindications, or drug interaction data were available in this Evidence Pack (Data Gap DG001). The DDI database query returned no results for this candidate-disease pair.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.73%), the supporting evidence for cobimetinib in ALS is entirely at the mechanistic-inference level (Evidence Level L5), with zero clinical trials and zero published studies identified. Additionally, the drug's oncology-derived toxicity profile and unknown CNS penetration represent substantial translational barriers that must be addressed before any further development decision.

**To proceed, the following is needed:**

- **Class-effect literature review**: Search for other MEK inhibitors (e.g., trametinib, selumetinib) in ALS preclinical or clinical contexts to establish whether there is class-level biological support
- **MOA data remediation** (Data Gap DG002): Retrieve full cobimetinib mechanism-of-action and pharmacology data from DrugBank to confirm the MEK/ERK–ALS connection
- **Safety data remediation** (Data Gap DG001): Obtain the full prescribing information / product monograph to formally assess warnings and contraindications relevant to an ALS population
- **CNS penetration assessment**: Evaluate published pharmacokinetic data on cobimetinib's blood–brain barrier permeability, which is essential for any neurodegenerative indication
- **Toxicity-population fit analysis**: Assess whether cobimetinib's known risks (serous retinopathy, cardiomyopathy, hepatotoxicity, rhabdomyolysis) are acceptable in ALS patients, who typically have normal organ function but progressive motor disability
- **Regulatory pathway exploration**: Investigate orphan drug designation eligibility for ALS in Taiwan and other jurisdictions to understand incentive structures if development is considered
- **Preclinical feasibility study design**: If the class-effect review is positive, design a targeted cobimetinib experiment in a validated ALS model (SOD1-G93A or TDP-43 transgenic mice) as the minimal evidence threshold before any clinical planning

---

> **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

