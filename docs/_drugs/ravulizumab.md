---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 792
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Disorders (PNH, aHUS) to Severe Congenital Neutropenia due to G6PC3 Deficiency

## One-Sentence Summary

Ravulizumab is a long-acting C5 complement inhibitor, used for complement-mediated blood and kidney disorders such as paroxysmal nocturnal haemoglobinuria (PNH) and atypical haemolytic uraemic syndrome (aHUS).
The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**.
However, this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complement-mediated disorders (PNH, aHUS); the licence records provide no indication text |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input record. Based on known information, ravulizumab is a long-acting inhibitor of complement component C5. It blocks terminal complement activation, which is why it is used in PNH and aHUS, where intravascular haemolysis is driven by complement.

The link between the original and predicted indications is weak. G6PC3 deficiency is a disorder of neutrophil metabolism and survival, and there is no known complement-driven pathology. The high score (0.9996) most likely reflects proximity among related blood-disorder nodes in the knowledge graph rather than a shared biological mechanism.

The same pattern appears across the other top-ranked predictions. Nine of the top ten are other neutropenias or haematological/platelet conditions (cyclic haematopoiesis, CXCR2-deficiency neutropenia, X-linked neutropenia, pseudo-von Willebrand disease and similar), plus primary hyperoxaluria. None has trials or literature supporting a role for terminal complement inhibition. The prediction should be treated as a hypothesis-generating signal, not as evidence of efficacy.

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
| 2533456 | ULTOMIRIS |
| 2533448 | ULTOMIRIS |

---

## Safety Considerations

Please refer to the package insert for safety information.

As a general class concern, C5 inhibition raises the risk of serious infection with encapsulated bacteria (e.g., meningococcus). This matters especially in patients with neutropenia or other immunodeficiency, who are already vulnerable to infection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a knowledge-graph score. There are no clinical trials or publications, no plausible mechanistic link to G6PC3-related neutropenia, and the added infection risk of C5 inhibition is a safety concern in a neutropenic population.

**To proceed, the following is needed:**
- Health Canada package insert data (warnings, contraindications), which is required before any safety screening
- Confirmed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that complement activation contributes to G6PC3-deficiency neutropenia
- Approved indication text for the two DINs, to confirm the original indications
- Any supporting clinical or case-level evidence, none of which has been identified so far
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

