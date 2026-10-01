---
layout: default
title: Alectinib
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Alectinib is an ALK/RET tyrosine kinase inhibitor used for ALK-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but **0 clinical trials** and **0 publications** support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (the Canadian licence record has no indication text; this is taken from the retrieved literature) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Alectinib is known to inhibit ALK and RET kinases, and its efficacy in ALK-positive lung cancer is well established. However, nothing in the supplied data links ALK or RET signalling to gingival fibromatosis.

Gingival fibromatosis is a benign overgrowth of gum tissue, biologically distant from the ALK-driven malignancy for which alectinib is used. The high score most likely reflects proximity in the knowledge graph rather than a shared disease mechanism. The score is very high, but it is not backed by any trial, publication or mechanistic finding, so it should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2458136 | ALECENSARO | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/RET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the supplied pack.

Adverse events reported in the retrieved literature, from ALK-positive lung cancer settings, include:
- Hypertriglyceridemia-induced pancreatitis (case report)
- Drug reaction with eosinophilia and systemic symptoms (DRESS) (case report)
- Erythema multiforme (case report)
- Serious weight gain (retrospective analysis)

The literature also includes an ECG monitoring analysis of cardiac electrophysiology from the pivotal Phase II studies. These reports are not specific to gingival fibromatosis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature and no supporting mechanism, so it stays at evidence level L5. Gingival fibromatosis is a benign condition, and the known safety profile of a cancer-directed kinase inhibitor makes an unsupported repurposing here hard to justify.

**To proceed, the following is needed:**
- Mechanism of action data, and any evidence that ALK or RET signalling contributes to gingival fibromatosis
- Health Canada package insert warnings and contraindications
- Preclinical or case-level evidence of activity in gingival fibromatosis
- A benefit-risk assessment for a benign indication

Among the other predictions in this pack, **lung germ cell tumor** has the most indirect support (L4, Research Question). It rests on ALK-fusion case reports in rare thoracic tumors and a Phase 2/3 basket trial (NCT05770037, recruiting). It is worth reviewing separately, restricted to tumors with a confirmed ALK rearrangement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

