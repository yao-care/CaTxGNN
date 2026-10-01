---
layout: default
title: Treosulfan
parent: Model Prediction Only (L5)
nav_order: 931
evidence_level: L5
indication_count: 10
---

# Treosulfan
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

# Treosulfan: From Conditioning Before Stem Cell Transplantation to Diabetic Cataract

## One-Sentence Summary

Treosulfan is an alkylating cytotoxic drug used as conditioning treatment before hematopoietic stem cell transplantation.
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on knowledge-graph proximity alone, and related alkylating agents are associated with cataract formation, so the direction may even be harmful.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Conditioning before hematopoietic stem cell transplantation (the Canadian licence text is not available) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Treosulfan is a bifunctional alkylating prodrug. It is converted to epoxybutane derivatives that damage DNA, and it is used as a myeloablative conditioning agent.

A plausible mechanistic link between this action and diabetic cataract has not been established. Diabetic cataract is driven by high blood sugar, activation of the polyol pathway, and oxidative stress in the lens. A systemic DNA-alkylating drug does not target any of these. The high TxGNN score (0.990, rank 16,236) most likely reflects closeness in the knowledge graph rather than a real treatment effect.

The other nine top predictions follow the same pattern: eight further cataract subtypes (nuclear senile, cortical, mature, tetanic, craniostenosis, immature, type 2 diabetes-associated and senile) and diabetic retinopathy. All are at L5 with no supporting trials or publications, so they look like graph-similarity artifacts shared across cataract-related diseases. Related alkylating agents such as busulfan are associated with cataract formation, which argues against benefit.

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
| 2517388 | TRECONDYV |
| 2560585 | TREOSULFAN FOR INJECTION |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (myeloablative conditioning agent) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (at minimum, complete blood count with differential, plus liver and renal function) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Class-level ocular concern**: Related alkylating conditioning agents are associated with cataract formation. This is a particular concern for a drug proposed to treat cataract.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, preclinical or literature support and no plausible mechanism. A myeloablative cytotoxic drug has a very poor risk-benefit profile for a non-life-threatening eye condition, and the class-level cataract risk points the other way.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action (MOA) data from DrugBank
- Any preclinical or clinical evidence linking treosulfan to lens or retinal disease
- Approved indication text and dosage forms for the two Canadian licences
- Route compatibility assessment (a systemic cytotoxic injection versus the usual local or oral approaches for eye disease)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

