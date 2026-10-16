---
layout: default
title: Reslizumab
parent: Model Prediction Only (L5)
nav_order: 802
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Reslizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). Approved use: Eosinophilic pneumonia"
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
---

# Reslizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Reslizumab: From Eosinophilic Pneumonia to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Reslizumab is an anti-IL-5 antibody originally associated with eosinophilic lung conditions (eosinophilic pneumonia and pulmonary eosinophilia).
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic pneumonia; pulmonary eosinophilia (taken from the knowledge-graph indication data, because no approved indication text is available for the Canadian license) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

A second prediction, **primary release disorder of platelets** (score 99.25%), was also generated. It is also evidence level L5 with a Hold recommendation, and is covered in the sections below.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, reslizumab is an anti-IL-5 monoclonal antibody that reduces eosinophils by blocking IL-5 signalling. This is consistent with its use in eosinophil-driven lung disease.

For the predicted new indication, the mechanistic link is weak. Immune-mediated thrombocytopenia (such as ITP) is driven mainly by autoantibody-mediated platelet destruction and impaired platelet production. No established connection to IL-5 or eosinophils has been identified. A speculative link might exist through Th2/eosinophil-associated immune dysregulation, but no data in this report supports it.

The second prediction, primary release disorder of platelets, is a qualitative platelet function defect (impaired granule secretion). It has no known IL-5 or eosinophil-dependent pathway. The one linked publication is a review of hypereosinophilic syndrome, which concerns eosinophilic disease rather than platelet disorders, so it is likely a spurious association. The high TxGNN scores (0.995 and 0.993) are computational predictions only and are not corroborated by clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either predicted indication.

---

## Literature Evidence

For thrombocytopenia due to immune destruction (the top prediction), currently no related literature available.

For the second prediction (primary release disorder of platelets), one publication is linked, though its relevance is low:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Review | Current Medical Research and Opinion | Review of hypereosinophilic syndrome management, including the anti-IL-5 agent mepolizumab. It addresses eosinophilic disease, not platelet disorders. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02456419 | CINQAIR | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions rest only on model scores, with no clinical trials and no supporting literature. The mechanistic link between IL-5 blockade and immune-mediated platelet destruction or platelet release defects is weak. The one linked publication is not relevant to the predicted indications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example, from DrugBank)
- Literature or preclinical evidence linking IL-5/eosinophil biology to immune thrombocytopenia
- Approved indication text and dosage form for the Canadian license (DIN 02456419)
- Route-of-administration compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

