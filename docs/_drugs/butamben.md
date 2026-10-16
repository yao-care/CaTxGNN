---
layout: default
title: Butamben
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Butamben: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
monitor_inn: "BUTAMBEN"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "acne keloid", "cauda equina syndrome", "hydroa vacciniforme, familial", "diabetic retinopathy"]
---

# Butamben
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

# Butamben: From Dermatitis to Bronchitis

## One-Sentence Summary

Butamben is a local anesthetic that was originally used for dermatitis-related symptoms.
The TxGNN model predicts it may be effective for **bronchitis**,
but **no clinical trials and no publications** currently support this direction. The prediction is computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text in the Canadian license record) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, butamben is an ester-type local anesthetic. Drugs of this class generally block voltage-gated sodium channels and reduce nerve signal conduction.

A theoretical link to bronchitis could be the suppression of airway sensory nerve activity, which might dampen the cough reflex. However, this is a hypothesis only. Nothing in the data compiled for this report supports it. Bronchitis is mainly an inflammatory or infectious airway disease, and symptom relief from a topical anesthetic would not treat its cause.

The high TxGNN score reflects network proximity in a knowledge graph. It is not proof of efficacy, and the similarity to the original indication has not yet been assessed. Route compatibility has also not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02028867 | CETACAINE LIQUID | Not specified | Not specified |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text)**: epilepsy, sudden cardiac arrest, heart conduction disease, respiratory failure. These are model-derived signals and need confirmation against the product label.
- **Drug Interactions**: No interaction records were found in the query.

Please refer to the package insert for complete warnings and contraindications.

---

## Other Predicted Indications (All Evidence Level L5, Hold)

None of the following has any registered clinical trial or publication:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Severe nonproliferative diabetic retinopathy | 99.74% | No clear mechanistic link |
| 3 | Acrodermatitis chronica atrophicans | 99.59% | Requires antibiotic therapy; weak link |
| 4 | Neonatal dermatomyositis | 99.57% | Neonatal systemic absorption and methemoglobinemia concerns |
| 5 | Secondary childhood interstitial lung disease (connective tissue disease) | 99.51% | Likely a network artifact |
| 6 | Amyopathic dermatomyositis | 99.48% | At most symptomatic relief |
| 7 | Acne keloid | 99.47% | At most pain or itch relief |
| 8 | Cauda equina syndrome | 99.46% | Neuraxial anesthetic exposure is itself a recognized cause of injury; safety concern |
| 9 | Familial hydroa vacciniforme | 99.45% | No plausible mechanism |
| 10 | Diabetic retinopathy | 99.14% | Likely a model artifact |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or publications, and the mechanism of action is unavailable. The safety review is also blocked because the package insert data has not been obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication, dosage form and route of administration for CETACAINE LIQUID
- A literature and trial search for butamben in airway or cough indications
- An assessment of route compatibility between the marketed product and the proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

