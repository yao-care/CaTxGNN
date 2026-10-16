---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Amylmetacresol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the licence data (marketed as an antibacterial throat l…"
monitor_inn: "AMYLMETACRESOL"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
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

# Amylmetacresol: From Throat Antiseptic Lozenges to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is a locally acting antiseptic marketed in Canada in throat lozenges (the Health Canada licence data compiled for this report does not list a formal approved-indication text).
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (marketed as an antibacterial throat lozenge) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amylmetacresol is known as a topical antiseptic used in throat lozenges. Its pharmacological action in cauda equina syndrome has not been established.

The link between the original use (local oropharyngeal infection and soreness) and the predicted indication is weak. Cauda equina syndrome is a compressive neurological condition of the lower spinal nerve roots. A mild local anaesthetic-like effect (possibly sodium channel blockade) is speculative and would not plausibly address nerve compression. The high score most likely reflects proximity in the knowledge graph rather than a verified pharmacological rationale.

Other top-ranked predictions are also unsupported by evidence:

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|---|---|---|---|
| 2 | Neurogenic bladder (obsolete ontology term) | 99.96% | L5 |
| 3 | Irritable bowel syndrome | 99.89% | L5 |
| 4 | Ciliary body disease | 99.70% | L5 |
| 5 | Panuveitis | 99.68% | L5 |
| 6 | Iris disease | 99.63% | L5 |
| 7 | Infectious anterior uveitis | 99.57% | L5 |
| 8 | Uveitis | 99.53% | L5 |
| 9 | Ciliary body cancer | 99.46% | L5 |
| 10 | Benign neoplasm of ciliary body | 99.45% | L5 |

The only weakly plausible rationale among these is infectious anterior uveitis, based on in vitro antibacterial and antiviral activity. There is no evidence of intraocular penetration, efficacy or ocular safety, and established pathogen-directed therapy is far better supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02375567 | Antibacterial Throat Lozenges | Not stated | Not stated |
| 02382938 | Cepacol Sensations | Not stated | Not stated |
| 02404982 | Cepacol Children's Fruity Strawberry | Not stated | Not stated |
| 02388642 | Cepacol Sensations Sore Throat & Cough | Not stated | Not stated |
| 02382881 | Cepacol Sensations Sore Throat & Blocked Nose | Not stated | Not stated |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report, and no disease-level contraindications were identified from the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score, with no clinical trials, no publications and no plausible mechanism linking a throat antiseptic to cauda equina syndrome. Safety and mechanism data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data for amylmetacresol (for example from DrugBank)
- Package insert warnings and contraindications from Health Canada
- Preclinical or mechanistic evidence for any candidate indication
- Remapping of the obsolete neurogenic bladder term to a current disease concept, if that candidate is pursued
- Assessment of route compatibility, since the current products are oral lozenges and the predicted indications would need different routes of delivery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

