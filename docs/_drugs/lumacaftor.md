---
layout: default
title: Lumacaftor
parent: Model Prediction Only (L5)
nav_order: 560
evidence_level: L5
indication_count: 10
---

# Lumacaftor
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

# Lumacaftor: From Cystic Fibrosis to Leprosy

## One-Sentence Summary

Lumacaftor is a CFTR corrector marketed in Canada as ORKAMBI, used for cystic fibrosis.
The TxGNN model predicts it may be effective for **leprosy** (score 99.44%), but **0 clinical trials** and **0 publications** support this prediction.
It is a knowledge-graph prediction only, with no drug-specific evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from the product ORKAMBI and its F508del-CFTR mechanism; the licence records contain no indication text) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lumacaftor corrects the folding and trafficking of F508del-CFTR, the defective protein in cystic fibrosis. It works on human epithelial protein handling. It has no known antimycobacterial or immunomodulatory activity against *Mycobacterium leprae*.

The evidence review found **no mechanistic link** between the original indication and leprosy. Cystic fibrosis is a genetic epithelial disease, while leprosy is a chronic bacterial infection with a strong immune component. The high TxGNN score reflects patterns in the knowledge graph, not pharmacological or clinical support.

The prediction is therefore not currently plausible on mechanistic grounds. Detailed mechanism of action data is not available beyond the CFTR corrector class.

The other top-10 predictions (migraine subtypes, rheumatoid arthritis, pulmonary hypertension and others) also have no supporting evidence for lumacaftor. All are graded L5 and Hold. Literature retrieved for the migraine prediction was epilepsy and migraine genetics matched by disease-name keywords, not lumacaftor data.

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
| 2451379 | ORKAMBI |
| 2483831 | ORKAMBI |
| 2463040 | ORKAMBI |
| 2483858 | ORKAMBI |
| 2537087 | ORKAMBI |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no clinical trials, no literature and no plausible mechanism. The score alone does not justify moving forward.

**To proceed, the following is needed:**
- A testable mechanistic hypothesis linking CFTR correction to *M. leprae* infection or the host response, supported by preclinical data
- Any in vitro or animal study of lumacaftor in leprosy
- Health Canada package insert warnings and contraindications, and the full mechanism of action from DrugBank
- Approved indication text and dosage forms for the five DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

