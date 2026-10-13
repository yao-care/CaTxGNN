---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 289
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diphenhydramine: From Allergic Rhinitis and Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine, originally used for allergic rhinitis, several forms of allergic conjunctivitis (atopic, vernal, papillary), vasomotor rhinitis and insomnia.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic/vernal/papillary conjunctivitis, insomnia (the Canadian licence records contain no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, diphenhydramine is a first-generation H1 receptor antagonist. It blocks histamine-mediated itching, redness and vasodilation, and its use in allergic, atopic, vernal and papillary conjunctivitis is established.

Ocular rosacea shares some features with these conditions, namely surface inflammation and vascular dilation. Symptom relief through H1 blockade is therefore plausible. The model's high score (0.992) probably reflects similarity to the existing conjunctivitis indications.

The link is indirect, though. Ocular rosacea is driven mainly by meibomian gland dysfunction, tear film instability, microbial and Demodex factors, and innate immune and neurovascular dysregulation. Histamine plays at most a minor role. Any benefit would probably be limited to symptom relief rather than treatment of the underlying disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Diphenhydramine has 20 valid single-ingredient authorizations in Canada and no cancelled ones. The data compiled for this report do not include dosage form or approved indication text for these products. Five representative products are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02141728 | ALLERGY FORMULA CAPLETS | Not available | Not available |
| 02304252 | BENADRYL ALLERGY LIQUIGELS | Not available | Not available |
| 02478757 | SLEEP-EZE EXTRA STRENGTH MINIS | Not available | Not available |
| 00596612 | DIPHENHYDRAMINE HYDROCHLORIDE INJECTION USP | Not available (injection by name) | Not available |
| 02019698 | CHILDREN'S BENADRYL ALLERGY LIQUID | Not available (liquid by name) | Not available |

The product names suggest both allergy and sleep-aid products, which is consistent with the original indications.

## Safety Considerations

**Drug Interactions:** The interaction screen is complete and returned 100 interacting drugs. Most are rated Moderate. Two examples rated **Major** are:
- Potassium citrate
- Eliglustat

Many Moderate interactions involve anticholinergic agents (e.g. atropine, hyoscyamine, glycopyrronium, dicyclomine) and CNS-depressant or opioid agents (e.g. morphine, nabilone, dronabinol). Other examples include loperamide, bupropion, metoclopramide and lorcaserin. These interactions are additive effects of diphenhydramine's anticholinergic and sedative properties.

Please refer to the package insert for warnings and contraindications, because that information is not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). No clinical trials or publications exist, and the mechanistic link is indirect, since histamine is not a primary driver of ocular rosacea. The package-insert safety information is also missing, which prevents safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this blocks safety screening)
- Mechanism of action data for diphenhydramine
- A literature and trial search for antihistamines in ocular rosacea
- Assessment of route compatibility (e.g. an ophthalmic formulation versus the oral and injectable products currently marketed)
- Preclinical or pilot clinical data showing a symptomatic benefit in ocular rosacea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

