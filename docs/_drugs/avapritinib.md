---
layout: default
title: Avapritinib
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: From KIT/PDGFRA-Driven Tumours to Axial Spondylometaphyseal Dysplasia

## One-Sentence Summary

Avapritinib is a KIT/PDGFRA kinase inhibitor. Based on general knowledge, it is used in gastrointestinal stromal tumour and systemic mastocytosis, because the Evidence Pack lists no original indication.
The TxGNN model predicts it may be effective for **axial spondylometaphyseal dysplasia**, but there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data provided |
| Predicted New Indication | Axial spondylometaphyseal dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general knowledge, avapritinib inhibits the KIT and PDGFRA tyrosine kinases, which drive certain tumours and mast cell disorders.

Axial spondylometaphyseal dysplasia is a rare skeletal dysplasia with no known KIT/PDGFRA involvement. No mechanistic link to the original indications was identified, so the prediction rests only on the TxGNN score. The model score is very high, but it should be read as a hypothesis-generating signal, not as biological support.

Other top predictions carry the same weakness:
- Most are rare developmental or motor neuron conditions with no evident KIT/PDGFRA rationale.
- The exception is amyotrophic lateral sclerosis (ALS), which has a speculative link. Other KIT/CSF1R-active kinase inhibitors, such as masitinib, have been studied in ALS through mast cell and microglia modulation. For avapritinib there are no supporting data, and CNS penetration and safety in this population are unknown.
- ALS is therefore best treated as a preclinical research question, not a clinical candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2551764 | AYVAKYT |
| 2551780 | AYVAKYT |
| 2551799 | AYVAKYT |
| 2551772 | AYVAKYT |

Dosage form and approved indication text are not included in the provided licence records.

## Cytotoxicity

Avapritinib is an antineoplastic agent based on its known oncology use.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials, no publications and no plausible KIT/PDGFRA mechanism for this rare skeletal dysplasia. Safety data from the Canadian package insert has also not been reviewed, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank, to test whether any KIT/PDGFRA link exists
- Original indication and approved indication text for the four DINs
- Any disease-specific biological rationale, such as expression or pathway data, for axial spondylometaphyseal dysplasia
- If a neurological direction is pursued, a separate preclinical review for ALS, including CNS penetration and safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

