---
layout: default
title: Fluticasone Furoate
parent: Model Prediction Only (L5)
nav_order: 405
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Fluticasone Furoate: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma, intrinsic asthma, allergic asthma, allergic rhinitis…"
monitor_inn: "FLUTICASONE FUROATE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fluticasone Furoate: From Asthma and Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is an inhaled and intranasal corticosteroid originally used for asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but this is a computational prediction only, with **no registered clinical trials** and **2 publications** that do not directly test the drug in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, intrinsic asthma, allergic asthma, allergic rhinitis, vasomotor rhinitis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluticasone furoate is a potent glucocorticoid receptor agonist with anti-inflammatory activity. Its efficacy in asthma and allergic rhinitis is established, and mechanistically it may be applicable to atopic eczema.

Asthma, allergic rhinitis and atopic eczema are all allergic (atopic) conditions that often occur together. Topical corticosteroids are a standard class of treatment for eczema, so the prediction is biologically plausible.

However, the plausibility comes from the drug class, not from evidence on fluticasone furoate itself. The model score is high, but none of the supplied studies evaluate this drug for eczema. Note also that the Canadian products are inhaled or intranasal forms, so a skin formulation and route would need separate consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews adrenal suppression (HPA axis effects) with intranasal corticosteroids in allergic rhinitis, which often coexists with asthma and atopic dermatitis. It does not assess efficacy in eczema. |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Case study of allergen immunotherapy in a patient with autoimmune disease. It is not about fluticasone furoate for eczema. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02298589 | AVAMYS | Not listed | Not listed |
| 02446588 | ARNUITY ELLIPTA | Not listed | Not listed |
| 02446561 | ARNUITY ELLIPTA | Not listed | Not listed |
| 02444186 | BREO ELLIPTA | Not listed | Not listed |
| 02408872 | BREO ELLIPTA | Not listed | Not listed |

Two further DINs (02474522 and 02515776) are for TRELEGY ELLIPTA. All 7 licences are currently valid.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug–disease links, not label text): measles, herpes simplex keratitis, varicella zoster infection, fungal infections, dermatophytosis, pulmonary tuberculosis, parasitic and other infectious diseases, ocular hypertension, glaucoma, adrenocortical insufficiency, Addison disease, adrenal gland hyperfunction, Cushing syndrome, and diseases of the upper and lower respiratory tract, nasal cavity and paranasal sinuses.
- **Adrenal suppression**: the supplied review (PMID 19571596) discusses HPA-axis suppression with intranasal corticosteroids. This is relevant if the drug were used on large areas of skin or over long periods.
- **Drug interactions**: no interaction records were found.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and class-level plausibility only (Evidence Level L5). There are no registered trials and no literature testing fluticasone furoate in atopic eczema. Established topical corticosteroids already exist for this condition, and the licensed products are not skin formulations.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of fluticasone furoate in atopic eczema
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada (currently missing)
- Assessment of a suitable topical formulation and route, and of systemic exposure and adrenal suppression risk
- Comparison with existing topical corticosteroids to show added value

**Note on other predicted indications:** Of the other seven predictions, bronchitis has the most indirect support (a COPD triple-therapy RCT, a chronic cough cohort study with fluticasone furoate, and an asthma RCT). It is best treated as a research question rather than a candidate for development. The remaining predictions have no supporting trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

