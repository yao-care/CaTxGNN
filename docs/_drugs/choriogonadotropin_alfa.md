---
layout: default
title: Choriogonadotropin Alfa
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Choriogonadotropin alfa: From Fertility Treatment to Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa is a recombinant human chorionic gonadotropin (hCG) marketed in Canada as OVIDREL. The provided data does not state its approved indication.
The TxGNN model predicts it may be effective for **peptic esophagitis** (score 98.4%), but there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided license data (OVIDREL is generally used in assisted reproduction) |
| Predicted New Indication | Peptic esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Choriogonadotropin alfa is a recombinant hCG, which acts as an agonist of the luteinizing hormone/chorionic gonadotropin receptor (LHCGR) in the gonads. Its efficacy in its original reproductive setting is established, but nothing in the data connects that mechanism to esophageal disease.

The relationship between the original and new indication is weak. No role for LHCGR signaling in esophageal mucosal injury or acid reflux is documented. The high score (0.984) most likely reflects proximity in the knowledge graph rather than a biological rationale.

The other top predictions show the same pattern. They cluster into esophageal conditions (esophagitis, ulcer, malformation), cardiac conduction disorders (sinoatrial block, His bundle tachycardia, familial heart block) and vasomotor disorders (Raynaud disease, POTS). None has trial or literature support, and some, such as congenital esophageal malformation, are biologically implausible for a gonadotropin agonist.

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
| 2371588 | OVIDREL |
| 2262088 | OVIDREL |

---

## Safety Considerations

Please refer to the package insert for safety information.

Several top predictions are arrhythmia or conduction disorders (His bundle tachycardia, sinoatrial block, sinoatrial node disease, progressive familial heart block). Any consideration of those indications would need a cardiac safety assessment first.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials, no publications and no plausible mechanism linking LHCGR agonism to esophageal disease. Safety and mechanism data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) and the approved indication text for both DINs
- A systematic literature and trial search for hCG or LHCGR agonism in esophageal disease, to check whether any biological rationale exists
- A review of whether the other top-ranked candidates, or a candidate outside this esophageal/cardiac/vascular cluster, have stronger support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

