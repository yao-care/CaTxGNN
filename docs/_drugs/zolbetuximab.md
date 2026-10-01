---
layout: default
title: Zolbetuximab
parent: Model Prediction Only (L5)
nav_order: 988
evidence_level: L5
indication_count: 10
---

# Zolbetuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Zolbetuximab: From Gastric Cancer to Diabetic Cataract

## One-Sentence Summary

Zolbetuximab is a CLDN18.2-targeted antibody, marketed in Canada as VYLOY and developed for CLDN18.2-positive gastric cancer. The TxGNN model predicts it may be effective for **diabetic cataract**, with a score of 98.5%. However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (zolbetuximab is a CLDN18.2-targeted antibody developed for gastric cancer) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the structured input. Zolbetuximab is a chimeric IgG1 antibody against Claudin-18.2 (CLDN18.2). This target is found mainly in gastric mucosa and CLDN18.2-positive tumours. The antibody acts by killing target-expressing cells through ADCC/CDC (antibody-dependent and complement-dependent cytotoxicity).

**The mechanistic case for this prediction is weak.** Lens clouding in diabetes is driven by polyol pathway flux, oxidative stress and protein glycation. CLDN18.2 has no established role in these processes. A cytotoxic, immune-effector antibody is also a poor fit for a benign, chronic lens condition. The high score most likely reflects graph proximity among cataract-related nodes in the knowledge graph, not biology.

The same pattern appears across all ten predictions in the pack: cataract subtypes (diabetic, type 2 diabetes-associated, craniostenosis, immature, mature, tetanic, cortical, nuclear senile and senile cataract) and diabetic retinopathy. All have scores of 98.2–98.5%, evidence level L5, and no supporting trials or literature. For diabetic retinopathy, the effective biologics target VEGF rather than CLDN18.2. A cytotoxic ADCC/CDC antibody could also pose ocular safety concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2553996 | VYLOY |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (monoclonal antibody acting through ADCC/CDC against CLDN18.2-expressing cells) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Nausea and vomiting are noted as safety concerns; please refer to the package insert for the formal classification |
| Monitoring Items | Please refer to the package insert warnings and precautions (infusion reactions and hypersensitivity should be considered) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The Evidence Pack contains no Health Canada warnings, contraindications or drug interaction data (the interaction query returned no results). The only safety information available is a general profile of nausea, vomiting, hypersensitivity and infusion reactions. This profile is unfavourable for a benign chronic condition such as cataract. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature and no credible mechanistic link between CLDN18.2 targeting and lens or retinal disease. The drug's cytotoxic mechanism and safety profile also argue against use in a benign chronic eye condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence that CLDN18.2 is expressed in lens or retinal tissue and is relevant to disease, from preclinical or mechanistic studies
- Any clinical or preclinical study linking zolbetuximab to cataract or diabetic eye disease
- A route-of-administration compatibility assessment (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

