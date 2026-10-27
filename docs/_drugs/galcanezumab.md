---
layout: default
title: Galcanezumab
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Galcanezumab: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Migraine disorder"
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Galcanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Galcanezumab: From Migraine Disorder to Heparin Cofactor 2 Deficiency
{: .text-alpha }

## One-Sentence Summary

Galcanezumab was originally used to prevent migraine.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but this prediction is supported by **no clinical trials and no publications**. It is a knowledge-graph prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, galcanezumab is a humanized monoclonal antibody that neutralizes calcitonin gene-related peptide (CGRP), and its efficacy in migraine prevention is established.

No credible mechanistic link to the predicted indication was identified. Heparin cofactor II deficiency is a thrombophilic disorder caused by reduced inhibition of thrombin (SERPIND1). CGRP signaling is not known to regulate heparin cofactor II activity or the coagulation cascade in a way that could correct this deficiency. The high score most likely reflects proximity among nodes in the knowledge graph rather than a biological rationale.

Two other predictions show the same pattern:
- **Antithrombin deficiency type 2** (score 99.41%): this is a functional defect in the SERPINC1 protein, and galcanezumab does not replace or enhance antithrombin function.
- **Factor 5 excess with spontaneous thrombosis** (score 99.41%): galcanezumab has no known effect on factor V. CGRP also has vasodilatory roles, and CGRP-pathway inhibition has been associated with vascular safety considerations. Use in a population at high thrombotic risk would need careful safety evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02491087 | EMGALITY | Not specified | Not specified |
| 02505134 | EMGALITY | Not specified | Not specified |
| 02491060 | EMGALITY | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

For the predicted indications, a theoretical concern applies to thrombotic conditions: CGRP-pathway inhibition has been associated with cardiovascular and vascular safety considerations, so any use in patients at high thrombotic risk would need careful evaluation. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are supported only by the model score. There are no clinical trials, no publications, and no plausible mechanistic link between CGRP neutralization and the coagulation deficiencies predicted. Safety data from the package insert are also missing.

**To proceed, the following is needed:**
- Mechanism of action data for galcanezumab
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Any preclinical or clinical evidence linking CGRP inhibition to heparin cofactor II, antithrombin, or factor V biology
- Approved indication text and dosage forms for the three Canadian DINs
- A dedicated vascular and thrombotic safety assessment before any consideration in thrombophilic populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

