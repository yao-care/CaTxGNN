---
layout: default
title: Choriogonadotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Choriogonadotropin Alfa: predicted new indication Peptic esophagitis (evidence level L5). Approved use: Not stated in the compiled licence data (the drug is generally known…"
monitor_inn: "Choriogonadotropin alfa"
predicted_indications: ["peptic esophagitis", "postural orthostatic tachycardia syndrome", "esophageal disease", "Raynaud disease", "non-syndromic esophageal malformation", "esophageal ulcer", "His bundle tachycardia", "sinoatrial block", "progressive familial heart block", "sinoatrial node disease"]
---

# Choriogonadotropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Choriogonadotropin alfa: From Fertility Treatment to Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa is a recombinant human chorionic gonadotropin (hCG), marketed in Canada as OVIDREL. It is generally used in fertility treatment, although the data compiled for this report do not include approved indication text.
The TxGNN model predicts it may be effective for **peptic esophagitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled licence data (the drug is generally known as an ovulation-induction agent) |
| Predicted New Indication | Peptic esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, choriogonadotropin alfa is a recombinant hCG that acts as a luteinizing hormone (LH) receptor agonist. It is used for ovulation induction and in hypogonadotropic hypogonadism.

No established mechanistic link connects LH/hCG receptor signaling to esophageal mucosal injury or acid-reflux pathophysiology. The high TxGNN score (98.44%) is a graph-based prediction. It likely reflects shared neighbours in the knowledge graph rather than biology, and no trial or publication supports it.

Other top predictions show the same pattern, with similarly high scores and no supporting evidence. They include postural orthostatic tachycardia syndrome, esophageal disease, Raynaud disease, esophageal ulcer, and several cardiac conduction disorders (sinoatrial block, sinoatrial node disease, His bundle tachycardia, progressive familial heart block). None has a plausible mechanistic rationale. This suggests the predictions are artefacts of the graph.

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
| 02371588 | OVIDREL | Not available | Not available |
| 02262088 | OVIDREL | Not available | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found, and no disease contraindications were identified from the knowledge graph. Because the cardiac conduction disorders among the other predictions would need a dedicated safety review, any use outside the established indication would require one.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no publications, and no plausible mechanistic link between LH/hCG receptor agonism and peptic esophagitis. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indication text
- Mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic evidence showing a biologically plausible role of LH/hCG signaling in esophageal mucosa
- Any clinical or observational reports supporting the predicted indication
- Route and formulation compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

