---
layout: default
title: Alglucosidase Alfa
parent: Model Prediction Only (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alglucosidase Alfa: predicted new indication Adult polyglucosan body disease (evidence level L5). Approved use: Glycogen storage disease (Pompe disease)"
monitor_inn: "ALGLUCOSIDASE ALFA"
predicted_indications: ["adult polyglucosan body disease", "congenital entropion", "congenital ectropion", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "epiblepharon", "ptosis-strabismus-ectopic pupils syndrome"]
---

# Alglucosidase Alfa
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

## Alglucosidase Alfa: From Glycogen Storage Disease to Adult Polyglucosan Body Disease
{: .text-alpha }

## One-Sentence Summary

Alglucosidase alfa is a recombinant enzyme originally used to treat glycogen storage disease (Pompe disease).
The TxGNN model predicts it may be effective for **adult polyglucosan body disease**,
but **no clinical trials and no publications** currently support this direction, so it should be treated as a research question only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glycogen storage disease (Pompe disease) |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alglucosidase alfa is a recombinant form of acid alpha-glucosidase (GAA). It breaks down glycogen inside lysosomes, and its use in glycogen storage disease is established.

Adult polyglucosan body disease (APBD) is caused by deficiency of the glycogen branching enzyme (GBE1). This leads to buildup of poorly branched, insoluble polyglucosan in neural tissue. The only plausible link is that both conditions involve abnormal glycogen metabolism.

The link is weak for two reasons. First, the primary defect in APBD is in the cytosolic branching step, not in lysosomal glycogen breakdown. Second, the enzyme has limited ability to cross the blood-brain barrier, so reaching affected nerve tissue is doubtful. The high score most likely reflects closeness within the glycogen storage disease family in the knowledge graph, not clinical data.

The other top-ranked predictions are also weak:
- **Glycogen branching enzyme deficiency (neuromuscular and fatal perinatal forms):** these are GSD type IV, where the missing enzyme is not the one this drug supplies. The association is at disease-class level only.
- **Eyelid, ocular and other rare congenital syndromes** (congenital entropion, ectropion, Horner syndrome, ptosis-related syndromes, epiblepharon and others): there is no plausible mechanistic connection, and these are most likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02284863 | MYOZYME | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model scoring (L5). The mechanism does not address the primary enzyme defect in APBD, brain penetration is doubtful, and there are no trials or publications.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic analysis showing whether lysosomal GAA replacement could affect polyglucosan accumulation
- Preclinical evidence (for example, in a GBE1-deficient model) showing the enzyme reaches affected neural tissue and reduces polyglucosan
- Health Canada package insert warnings and contraindications
- Route and formulation compatibility assessment for the proposed indication
- A literature and trial search specific to APBD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

