---
layout: default
title: Pentosan Polysulfate
parent: Model Prediction Only (L5)
nav_order: 714
evidence_level: L5
indication_count: 3
---

# Pentosan Polysulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Pentosan Polysulfate: From an Unrecorded Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Pentosan polysulfate is marketed in Canada as ELMIRON, but the supplied data does not record its approved indication.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **0 clinical trials** and **0 publications** support this direction.
The prediction rests on a model score alone, and the available rationale points to a possible safety concern rather than a benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The supplied data records neither an original indication nor a mechanism of action, so no mechanistic link between the drug and the predicted disease can be drawn from it.

Using general pharmacology (not from the supplied data), pentosan polysulfate is a heparin-like sulfated polysaccharide with weak anticoagulant and fibrinolytic activity, and bleeding is a recognised risk. Primary release disorder of platelets is a platelet secretion defect. A drug that impairs hemostasis would be expected to worsen it, so the direction of effect looks **unfavourable**.

The two next-ranked predictions show the same pattern:

- **Glanzmann thrombasthenia** (score 99.65%): a bleeding disorder caused by deficiency or dysfunction of platelet integrin alpha-IIb/beta-3. An anticoagulant would be expected to increase bleeding risk.
- **Pseudo-von Willebrand disease** (score 99.62%): a gain-of-function defect in platelet GPIb-alpha that causes bleeding. Any beneficial effect of a sulfated polysaccharide here is speculative, and the anticoagulant activity is a bleeding-risk concern.

The high TxGNN scores likely reflect associations in the knowledge graph rather than a therapeutic rationale. Reviewers should check this before any further work.

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
| 2029448 | ELMIRON |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the queried data.

Bleeding risk is the main concern for the predicted indications, which are all bleeding or platelet function disorders. This comes from general pharmacological knowledge, not from the supplied data, and should be confirmed against the Health Canada label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no trials or publications. The available pharmacological reasoning suggests the drug's anticoagulant properties could worsen the predicted conditions, so this is a safety concern rather than a repurposing opportunity.

**To proceed, the following is needed:**
- The Health Canada package insert, with warnings, contraindications and the approved indication
- Mechanism of action data (for example, via DrugBank)
- A review of why the knowledge graph links this drug to platelet disorders, to rule out a spurious association
- Preclinical or clinical evidence that the drug does not worsen bleeding in these populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

