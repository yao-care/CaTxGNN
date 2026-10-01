---
layout: default
title: Lorlatinib
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor, marketed for ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis** (score 99.81%), but **0 clinical trials** and **0 publications** support this prediction.
It is a model output only, with no mechanistic rationale, so it should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (taken from the literature; the license records list no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Lorlatinib is known from the literature to be a brain-penetrant inhibitor of ALK and ROS1 fusion kinases, and its efficacy in ALK-positive NSCLC is well established.

Gingival fibromatosis (here, the hereditary form) is a benign overgrowth of gum tissue. No ALK- or ROS1-driven mechanism is established for it, so there is no evident target link between the original and predicted indications. The high score most likely reflects proximity in the knowledge graph rather than disease-specific biology.

For these reasons the prediction is not currently plausible on mechanistic grounds. Any further work would need a new biological hypothesis, such as evidence of kinase pathway involvement in gingival fibroblast overgrowth.

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
| 2485974 | LORBRENA |
| 2485966 | LORBRENA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Literature on lorlatinib in ALK-positive cancers reports lipid abnormalities, CNS effects (cognitive and mood changes) and pulmonary toxicity. Lipid profile, neurocognitive status and respiratory symptoms are therefore reasonable to monitor. Confirm against the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No formal warning, contraindication or interaction data are available in the record. Please refer to the package insert for safety information.

Published reports on lorlatinib in other diseases point to these signals, which would matter for any new use:
- **Metabolic:** hypercholesterolemia, hypertriglyceridemia, weight gain, and a possible link to nephrotic syndrome.
- **CNS:** cognitive and mood effects.
- **Pulmonary:** acute respiratory distress syndrome (case report) and pulmonary toxicity when combined with anti-GD2 antibody.

Gingival fibromatosis is a benign condition, so this toxicity profile weighs heavily against the benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials or publications, and no plausible ALK/ROS1-related mechanism. Lorlatinib's metabolic and neurocognitive toxicity is hard to justify in a benign condition.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking kinase signalling to gingival fibroblast overgrowth, with preclinical support
- Detailed mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications
- A benefit-risk assessment for a benign indication

Other lower-ranked TxGNN predictions for lorlatinib (for example lung hilum carcinoma and lung germ cell tumor) have some literature. It concerns ALK-positive NSCLC and ALK-driven neuroblastoma, not the labelled disease terms. It is indirect evidence, and mapping it to those terms would be a data-curation decision.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

