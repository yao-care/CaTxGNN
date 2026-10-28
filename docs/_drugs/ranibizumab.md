---
layout: default
title: Ranibizumab
parent: Model Prediction Only (L5)
nav_order: 794
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["immature cataract", "mature cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "hemorrhagic disease of newborn"]
description: "Ranibizumab: predicted new indication Immature cataract (evidence level L5). Approved use: Not recorded in the local data"
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ranibizumab: Immature cataract
{: .text-alpha }

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment originally used for eye diseases such as diabetic retinopathy, diabetic macular edema and macular degeneration.
This is largely an extension within the drug's existing disease family rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (based on literature titles; full study designs not verified) |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, ranibizumab is an anti-VEGF antibody fragment. VEGF drives retinal vascular permeability and neovascularization in diabetic retinopathy, and elevated serum and vitreous VEGF levels have been documented in this disease.

Neutralizing VEGF is mechanistically coherent with the regression of retinopathy severity seen in the literature. The predicted indication is also closely aligned with the drug's existing indications (diabetic retinopathy and diabetic macular edema), so it is mainly an extension within an established disease family.

One caveat: no clinical trials were supplied for this indication. The L1 grade rests on literature titles (RIDE/RISE post-hoc analyses, and the Port Delivery System versus monitoring trial in NPDR). These are consistent with Phase 3 RCT-derived evidence, but their full text and design were not verified.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication in the compiled data. The RIDE and RISE trials (NCT00473382 / NCT00473330) are referenced within the literature below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring in NPDR without macular edema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Meta-analysis of Phase 3 trials (post-hoc) | Ophthalmology Retina | Time to DME resolution with ranibizumab in relation to baseline DR severity |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT (post-hoc) | Clinical Ophthalmology | Predictors of early DR regression with ranibizumab in RIDE/RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT extension analysis | BMJ Open Ophthalmology | Effect of less frequent ranibizumab on DR severity scale scores in RIDE/RISE open-label extension |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review / meta-analysis | European Journal of Pharmacology | Sustained ranibizumab port delivery for DR and DME: disease modification and durability |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review / meta-analysis | Health Technology Assessment | Anti-VEGF vs laser photocoagulation for diabetic retinopathy |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Ranibizumab has been shown effective in DR, including DME |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT secondary analysis | JAMA Ophthalmology | Change in DR over 2 years comparing aflibercept, bevacizumab and ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT 5-year report | Retina | DR severity changes when treating DME with ranibizumab (DRCR.net Protocol I) |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Simulation model | BMJ Open Ophthalmology | Long-term impact of proactive anti-VEGF treatment in severe NPDR vs delaying until PDR |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02425629 | LUCENTIS | Not specified | Not specified |
| 02542250 | RANOPTO | Not specified | Not specified |
| 02525852 | MELVIZO | Not specified | Not specified |
| 02296810 | LUCENTIS | Not specified | Not specified |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: eye infectious disease; conjunctivitis.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is coherent and the literature includes RCT-derived analyses (RIDE/RISE, Pavilion) in diabetic retinopathy. The indication sits close to ranibizumab's existing use in the diabetic eye disease family, and the drug is marketed in Canada under 4 DINs. However, no trials were registered for this specific indication in the data, and the Canadian label text has not been reviewed.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert (warnings, contraindications, approved indications). This is a blocking gap for safety screening.
- Obtain detailed mechanism of action data (e.g., from DrugBank).
- Verify the full text and design of the key RCT-derived publications to confirm the evidence level.
- Confirm whether severe NPDR is already covered by the Canadian labelled indications.

## Other Predicted Indications (Not Recommended at This Time)

The other nine predictions all have a **Hold** recommendation. They are mainly cataract subtypes (immature, mature, tetanic, type 2 diabetes-associated, craniostenosis, cortical, nuclear senile and senile cataract), plus hemorrhagic disease of the newborn. Cataract is a lens opacification process and is not primarily VEGF-driven, and the retrieved literature covers ranibizumab in other retinal conditions rather than cataract treatment. The high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. For hemorrhagic disease of the newborn, the matched trials concern a different disease (hereditary hemorrhagic telangiectasia and chorioretinal neovascular diseases), and anti-VEGF therapy could theoretically worsen bleeding risk in neonates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

