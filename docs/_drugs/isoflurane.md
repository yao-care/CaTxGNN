---
layout: default
title: Isoflurane
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 7
---

# Isoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Isoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is an inhaled anesthetic, marketed in Canada under two licences. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (not stated in the supplied licence records) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isoflurane is a volatile anesthetic, and its efficacy as an anesthetic is established. Nothing in the Evidence Pack, however, links it mechanistically to Prinzmetal angina, a coronary vasospasm disorder.

The prediction therefore rests on the model score alone (0.997, rank 6,786 in the model's output). No trial, publication, or mechanistic rationale supports it. The prediction should be treated as a hypothesis to test, not a finding.

The same list contains one better-supported prediction, **migraine disorder** (rank 7, score 99.06%, evidence level L4). Preclinical work (PMID 8665587, 1996) reports that inhaled anesthetics inhibit cortical spreading depression, the phenomenon underlying migraine aura. One case report describes status migrainosus treated with general anesthesia (PMID 26323741). The supplied data does not confirm that isoflurane was the agent used. This is a plausible link, but not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2231929 | ISOFLURANE USP |
| 2188856 | FORANE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Prinzmetal angina is supported only by a model score, with no trials, literature, or mechanistic link (evidence level L5). Isoflurane is an inhaled agent, and route compatibility with the new indication has not been assessed.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank)
- Package insert warnings and contraindications from Health Canada
- A systematic literature and trial search specific to isoflurane and Prinzmetal angina
- Assessment of route and setting compatibility
- Consideration of migraine (rank 7) as a research question, with the full set of 13 publications reviewed (only 10 were supplied)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

