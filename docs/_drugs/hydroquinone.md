---
layout: default
title: Hydroquinone
parent: Moderate Evidence (L3-L4)
nav_order: 458
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-13
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L4). Approved use: Not stated in the Canadian license data"
monitor_inn: "HYDROQUINONE"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Hydroquinone: From Pigmentation Disorders (Topical Depigmenting Agent) to Seborrheic Keratosis

## One-Sentence Summary

Hydroquinone is a tyrosinase inhibitor best known as a topical skin-lightening agent. The Canadian license data compiled for this report does not state an approved indication.
The TxGNN model predicts it may be effective for **seborrheic keratosis**, but the support is thin: **0 clinical trials** and **1 publication** (a prospective observational study) for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, hydroquinone inhibits tyrosinase and reduces melanin synthesis, so it may lighten pigmented skin lesions.

Seborrheic keratosis is a benign proliferation of epidermal cells that is often pigmented. Depigmentation might reduce the pigment component of the lesions, but it would not address the underlying growth. The link is therefore indirect and mostly cosmetic.

The only supporting publication is a prospective observational study of combination treatment for facial pigmentary disorders. It does not test hydroquinone for seborrheic keratosis directly.

Other predictions in the list are weaker still:
- **Vulvar inverted follicular keratosis** (score 99.64%): no trials or literature; likely reflects similarity to other keratosis entities in the knowledge graph.
- **Exanthem** (score 99.42%): one Phase 4 trial of an herbal depigmenting system (hydroquinone used as a comparator) and a pregnancy skin-conditions review, both only tangential.
- **Lichen disease** (score 99.07%): a pigmentary disorders review and a case report that responded to topical tacrolimus, not hydroquinone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for seborrheic keratosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Prospective observational study | J Plast Reconstr Aesthet Surg | Combination treatment algorithm for multiple facial pigmentary disorders in Asian patients; no definitive algorithm existed before this work. Indirect relevance to seborrheic keratosis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02491702 | ERFA HYDROQUINONE | Not stated | Not stated |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (these come from a computational drug-disease contraindication network, not from label text): sunburn, adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease, atopic eczema, and dermatitis.

Please refer to the package insert for warnings, contraindications and drug interaction information. No drug interactions were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a model prediction only. No clinical trials exist for seborrheic keratosis, and the single publication is an indirect observational study on facial pigmentation. Hydroquinone's depigmenting action would not treat the underlying benign growth.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication, dosage form), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Direct clinical or preclinical evidence of hydroquinone in seborrheic keratosis
- Assessment of whether a cosmetic pigment-lightening benefit is clinically meaningful for this indication
- Review of the knowledge-graph-flagged conditions (e.g., skin atrophy, dermatitis) against the topical use case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

