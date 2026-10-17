---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Benzocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection"
monitor_inn: "BENZOCAINE"
predicted_indications: ["papillary conjunctivitis"]
---

# Benzocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Benzocaine: From Tinea Pedis and Dermatitis to Papillary Conjunctivitis

## One-Sentence Summary

Benzocaine is a topical ester-type local anesthetic, listed in the knowledge base for symptomatic use in conditions such as tinea pedis, dermatitis and pharyngitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection (from the knowledge base; the Canadian licences list no approved indication text) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, benzocaine is a topical ester-type local anesthetic that blocks voltage-gated sodium channels. Its known uses are symptomatic relief of pain or itch.

Papillary conjunctivitis is typically allergic or related to contact lenses or foreign bodies. A plausible link would be symptomatic relief of ocular surface discomfort or itch. This link is speculative: benzocaine is not an established ophthalmic agent, and no mechanistic or clinical validation is available.

There are also reasons for caution. Topical anesthetics can damage the cornea with repeated use and delay epithelial healing. Benzocaine is also a known contact sensitizer, so it could worsen an allergic or papillary reaction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230958 | ONE TOUCH TOPICAL ANESTHETIC GEL | Not listed | Not listed |
| 01930699 | ZAP TOPICAL ANESTHETIC GEL | Not listed | Not listed |
| 02028867 | CETACAINE LIQUID | Not listed | Not listed |

All three are valid single-ingredient products.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** The knowledge graph links benzocaine to a broad set of conditions, including:
  - liver failure, liver disease and hepatic encephalopathy
  - kidney disease
  - epilepsy
  - porphyria
  - blood disorders (thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disease)
  - diabetes and diabetic ketoacidosis
  - herpes simplex infection
  - sarcoidosis
  - hyperparathyroidism and hypercalcemia
  - substance abuse/dependence

  These edges come from a model knowledge graph and need verification against the official product labelling.
- **Ocular concerns (from the repurposing assessment):** possible corneal toxicity with repeated use, delayed epithelial healing, and contact sensitization.

No drug interaction records were found.

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score (99.38%). There are no clinical trials or publications, the mechanism data is incomplete, and the ocular safety concerns (corneal toxicity, sensitization) argue against the use. The evidence level is L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (e.g., from DrugBank)
- Preclinical or literature evidence of benefit in papillary conjunctivitis
- An assessment of ocular safety and route compatibility, since the current Canadian products are topical gels and a liquid, and none is confirmed as an ophthalmic formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

