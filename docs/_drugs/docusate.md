---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 2
---

# Docusate
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

# Docusate: From Constipation (Stool Softener) to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is an anionic surfactant stool softener, marketed in Canada under many brand names.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction that is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation / stool softening (general drug class use; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, docusate is an anionic surfactant stool softener that acts within the gut lumen. It has no known role in treating iron deficiency or its complications.

Plummer-Vinson syndrome is driven by iron deficiency and presents with anemia, dysphagia and esophageal webs. Nothing in the supplied data links docusate's stool-softening action to any of these features. The high TxGNN score (99.18%) most likely reflects proximity in the knowledge graph, not a biological rationale.

The only plausible indirect connection is that docusate is sometimes co-formulated with oral iron to reduce constipation. That is a tolerability adjunct, not a disease-modifying effect. Nothing in the supplied data supports it.

The second-ranked prediction, *vitamin B12- and folate-independent constitutional megaloblastic anemia* (score 99.15%), has the same problem. Docusate has no known effect on nucleotide synthesis or erythropoiesis, and no trials or literature support it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 20 licenses in total. The five main ones are below. Dosage form and approved-indication text were not available in the supplied records.

| DIN | Product Name |
|---------|------|
| 2530538 | NRA-DOCUSATE SODIUM |
| 1994344 | SOFLAX CAPSULES 100MG |
| 2484226 | COLACE CLEAR |
| 2526492 | ENEMEEZ |
| 870226 | RATIO-DOCUSATE SODIUM |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link to iron-deficiency disease. The evidence level is L5 and the case remains at the earliest screening stage (S0).

**To proceed, the following is needed:**
- Mechanism of action data for docusate (e.g., from DrugBank), to test whether any biological link to iron-deficiency or megaloblastic anemia exists
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Any clinical or preclinical evidence, from a systematic search of ClinicalTrials.gov and PubMed, that connects docusate to Plummer-Vinson syndrome
- Route and dosage-form compatibility assessment, if evidence emerges

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

