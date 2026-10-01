---
layout: default
title: Anifrolumab
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab is an anti-type I interferon receptor antibody, known for treating systemic lupus erythematosus (SLE).
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-only signal (L5) and should be treated as a hypothesis, not a treatment claim.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus (the Canadian licence record has no indication text; this is based on the drug's known approval) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Anifrolumab is an antibody against the type I interferon receptor subunit 1 (IFNAR1). It blocks type I interferon signalling, which is the basis of its use in SLE. Detailed mechanism data is not available in the DrugBank input, so this description relies on the analysis notes in the Evidence Pack.

The mechanistic link to diabetic cataract is weak. Diabetic cataract is driven mainly by polyol pathway flux and oxidative stress in the lens, and no established role for type I interferon has been identified. The high score of 0.985 most likely reflects ontology-neighbour propagation in the knowledge graph rather than a biological connection. The other top predictions for this drug are also cataract subtypes (tetanic, mature, immature, senile, nuclear, cortical, craniostenotic and type 2 diabetes-associated cataract). This clustering supports the artefact interpretation, since many of these are morphological stages or unrelated causes of lens opacity.

Diabetic retinopathy (rank 10) is the one biologically conceivable prediction. Chronic inflammation and interferon-related signalling have been implicated in retinal microvascular damage. However, there are no trials or literature for anifrolumab in this setting, and anti-VEGF therapy and laser are far better supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for diabetic cataract.

For reference, the only literature found across the top 10 predictions is linked to cortical cataract (rank 8):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/) | 2025 | Review | Int J Mol Sci | Ophthalmological safety of emerging and conventional SLE therapies. It addresses ocular safety, not efficacy of anifrolumab for cataract (based on title and abstract excerpt). |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2522845 | SAPHNELO |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials or publications, and no plausible mechanism links type I interferon blockade to diabetic cataract. Systemic immunosuppression also carries infection risk that has no offsetting ocular benefit here.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or observational evidence linking type I interferon signalling to lens or retinal disease
- Ophthalmic safety data on cataract risk in SLE patients on anifrolumab, for example a steroid-sparing effect. This is a more relevant research question than a treatment claim.
- Assessment of route compatibility (a systemic antibody versus an ocular target)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

