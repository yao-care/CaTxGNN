---
layout: default
title: Belimumab
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a BLyS (BAFF)-neutralizing monoclonal antibody, originally used to treat systemic lupus erythematosus, including the paediatric form.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus; paediatric systemic lupus erythematosus (the licence records contain no approved indication text, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, belimumab neutralises BLyS (BAFF), which suppresses B-cell survival and autoantibody production. This is the basis for its use in lupus, an autoantibody-driven disease.

For the predicted indication, no plausible mechanistic link was identified. Primary platelet release disorders are typically inherited, qualitative platelet function defects (granule secretion or signalling abnormalities) and are not primarily driven by B cells or autoantibodies. The very high TxGNN score is therefore a model output only, with no trial or publication behind it, and may be a knowledge-graph artefact.

**Other predictions from the model (all L5, all Hold):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Pseudo-von Willebrand disease | 99.96% | Caused by gain-of-function variants in GP1BA (a genetic platelet receptor defect). BAFF inhibition has no clear pathway to correct it. |
| Glanzmann thrombasthenia | 99.88% | Inherited deficiency or dysfunction of integrin αIIbβ3. Belimumab does not act on this receptor. A speculative role in anti-GPIIb/IIIa alloantibody refractoriness is unsupported by data. |
| Fetal and neonatal alloimmune thrombocytopenia (FNAIT) | 99.59% | The most biologically plausible, since maternal alloantibodies drive the disease. However, belimumab has limited effect on long-lived plasma cells, and its use in pregnancy is not well established (placental IgG transfer and fetal B-cell effects are concerns). |
| Severe nonproliferative diabetic retinopathy | 99.05% | A microvascular disease driven by hyperglycaemia, VEGF and inflammation. There is no direct evidence linking BLyS inhibition to retinal outcomes, and effective therapies already exist. |
| Autosomal dominant macrothrombocytopenia | 99.04% | Caused by inherited megakaryocyte and platelet cytoskeletal defects (e.g., MYH9, TUBB1), not by immune mechanisms. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02370050 | BENLYSTA | Not specified | Not specified |
| 02470489 | BENLYSTA | Not specified | Not specified |
| 02370069 | BENLYSTA | Not specified | Not specified |

All three authorisations are valid single-ingredient products.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug Interactions**: 69 interactions were identified in total. The main ones from the first 20 reviewed are:

- **Major**: adalimumab, baricitinib, certolizumab pegol, and BCG live vaccine (Tice strain)
- **Moderate**: roflumilast, alemtuzumab, anakinra, azathioprine, canakinumab, alefacept, and several vaccines or live biological products (tetanus toxoid, anthrax vaccine, adenovirus type 4 vaccine, cholera vaccine, *Candida albicans*, *Bifidobacterium longum infantis*)
- **Minor**: zinc salts (acetate, gluconate, sulfate, chloride)

The major and moderate interactions largely reflect additive immunosuppression and concerns around live vaccines.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only a model score behind it, with no trials or publications, and no plausible mechanistic link to belimumab's B-cell/BAFF action. The same applies to most of the other predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Any preclinical or clinical evidence for the predicted indication
- If a lead is pursued, FNAIT is the most biologically plausible candidate. It would first need preclinical work and a pregnancy-specific safety assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

