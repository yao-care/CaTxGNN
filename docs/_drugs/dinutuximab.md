---
layout: default
title: Dinutuximab
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Dinutuximab: predicted new indication Vertebral anomalies and variable endocrine and T-cell dysfunction (evidence level L5). Approved use: Neuroblastoma"
monitor_inn: "DINUTUXIMAB"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Dinutuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Dinutuximab: From Neuroblastoma to Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction
{: .text-alpha }

## One-Sentence Summary

Dinutuximab is an anti-GD2 monoclonal antibody, originally used to treat **neuroblastoma**.
The TxGNN model predicts it may be effective for **vertebral anomalies and variable endocrine and T-cell dysfunction**, a rare developmental and immunodeficiency syndrome.
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model's graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuroblastoma |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled drug record. Dinutuximab is known to be a monoclonal antibody against GD2, a ganglioside found on the surface of neuroblastoma cells. Its efficacy in neuroblastoma rests on targeting GD2-expressing tumour cells.

**No mechanistic link is apparent for this prediction.** The predicted condition is a rare developmental and immunodeficiency syndrome with no known GD2-driven disease process. The high TxGNN score (0.994) is a graph-based inference only, and no trials or publications support it. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

**Other predictions for this drug.** Among the other candidates, **ganglioneuroblastoma** (rank 2, score 99.39%) is biologically plausible because it belongs to the same neuroblastic tumour family as neuroblastoma, and these tumours commonly express GD2. This is largely an extension within the same tumour family rather than true repurposing. The related literature is limited to a pediatric neuroblastoma study of irinotecan-temozolomide with dinutuximab (COG ANBL1221) and case reports, none specific to ganglioneuroblastoma.

The other two candidates, retroperitoneal neoplasm and BCR-ABL1-positive chronic myelogenous leukaemia, have no supporting trials or publications. The leukaemia prediction has no credible mechanistic rationale, because the disease is driven by the BCR-ABL1 fusion kinase rather than GD2.

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
| 02483076 | UNITUXIN | Not specified | Not specified in the compiled data (neuroblastoma is the original indication) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-GD2 monoclonal antibody), not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert and local institutional policy for handling of antineoplastic agents |

---

## Safety Considerations

**Drug Interactions** (100 interactions recorded; the main ones from the available list are shown below)

- **Major interactions:**
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisolone, prednisone
  - Deferiprone
  - Samarium (153Sm) lexidronam
- **Moderate interactions:**
  - Metronidazole, tinidazole, secnidazole, benznidazole
  - Rosuvastatin, simvastatin
  - Chloroquine, hydroxychloroquine
  - Disulfiram
  - Strontium chloride Sr-89

The many major corticosteroid interactions deserve particular attention if dinutuximab were ever combined with these agents in a new patient population.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no literature, and no plausible GD2-related mechanism for this rare syndrome. Evidence is at the lowest level (L5), so there is no basis for further investment in this indication.

**To proceed, the following is needed:**
- A credible biological rationale linking GD2 targeting to the predicted condition
- Any preclinical or clinical data specific to this condition
- The Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Detailed mechanism-of-action data from DrugBank
- Consideration of ganglioneuroblastoma as a more plausible lead, which would first require confirming the design and subgroup data of the neuroblastoma-family study (COG ANBL1221)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

