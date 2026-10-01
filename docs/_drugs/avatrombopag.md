---
layout: default
title: Avatrombopag
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: From Thrombocytopenia Treatment to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag is a thrombopoietin (TPO) receptor agonist that raises platelet counts. The Evidence Pack does not list an approved indication for it.
The TxGNN model predicts it may be effective for **macrothrombocytopenia with mitral valve insufficiency**, a rare syndromic low-platelet disorder.
Currently **0 clinical trials** and **0 publications** support this prediction, so it rests on model output and mechanistic plausibility alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided record (drug class: TPO receptor agonist for low platelet counts) |
| Predicted New Indication | Macrothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, avatrombopag is a TPO receptor agonist. It stimulates megakaryocytes, the cells that produce platelets. Low platelet count is the shared feature between the drug's class use and the predicted condition, so the link is mechanistically plausible.

Whether it would work depends on the cause of the disorder. This syndromic macrothrombocytopenia may involve impaired megakaryocyte maturation or platelet production. If so, a drug that pushes megakaryocyte output could help, but only for some genetic defects. There is no evidence yet on this.

The other top-ranked predictions are of mixed plausibility:
- **Hereditary thrombocytopenia with normal platelets** (99.995%): the mechanism fits, but efficacy is genotype-dependent and unproven.
- **Transient neonatal thrombocytopenia** and **dense granule disease**: the fit is weak. The first is self-limiting and has no neonatal safety data. The second is a platelet function defect that raising platelet count would not correct.
- **Motor neuron and cortical malformation predictions** (ALS, Mills syndrome, monomelic amyotrophy, and others): no plausible link to TPO receptor agonism. They look like knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2542706 | DOPTELET | — | — |

Dosage form, manufacturer, and approved indication text are not included in the provided record.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (0 interactions found). This is not proof of no interactions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.995%), but no clinical trials or publications back it (L5). Package insert safety data have not been reviewed, and efficacy in inherited platelet disorders depends on the specific genetic defect. Several other top predictions (motor neuron diseases, cortical malformation) have no credible mechanism.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which must be obtained before safety screening
- Mechanism of action data (for example from DrugBank)
- Confirmation of the approved indication and dosage form for DIN 2542706
- A literature and trial search for avatrombopag or other TPO receptor agonists in inherited macrothrombocytopenia, to identify which genetic subtypes might respond
- Pediatric safety data before considering any neonatal use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

