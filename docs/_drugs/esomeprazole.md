---
layout: default
title: Esomeprazole
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 3
---

# Esomeprazole
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

# Esomeprazole: From Acid-Related Gastric Disorders to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) used for acid-related upper gastrointestinal disorders.
The TxGNN model predicts it may be effective for **duodenogastric reflux** with a very high score, but currently only **1 general review article** and **0 clinical trials** support this specific indication. That evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (Canadian licence indication text is empty); esomeprazole is a PPI for acid-related disorders |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 (indirect literature only, no trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Esomeprazole is a proton pump (H+/K+-ATPase) inhibitor that suppresses gastric acid secretion. Its efficacy in acid-related disease is well established.

Duodenogastric reflux is different. It is driven by bile and pancreatic secretions flowing back into the stomach, not by acid. Acid suppression may ease associated symptoms or mucosal irritation, but it does not correct the reflux itself. The high TxGNN score most likely reflects graph proximity to GERD and peptic disease rather than a true mechanistic link.

The only supporting article is a general PPI review, which is indirect evidence for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General update on PPI clinical use and pharmacokinetics. PPIs are first-choice drugs for peptic ulcer, H. pylori infection, GERD, NSAID-induced lesions and Zollinger-Ellison syndrome. Duodenogastric reflux is not addressed. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2442493 | ESOMEPRAZOLE |
| 2339099 | APO-ESOMEPRAZOLE |
| 2479419 | MYL-ESOMEPRAZOLE |
| 2394847 | ESOMEPRAZOLE |
| 2244521 | NEXIUM - 20MG |

Dosage form and approved indication text are not available for these licences.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials and only one indirect review. The mechanism does not fit, because duodenogastric reflux is not acid-driven. The score is likely a graph-neighbourhood artifact.

**Note on a related prediction:**
The same Evidence Pack lists **duodenal ulcer** (rank 3, score 99.40%) with L1 evidence. It has multiple completed Phase 3 trials, RCT literature and a network meta-analysis. Esomeprazole is very likely already labelled for this use, so it may be on-label use rather than true repurposing. Confirm against current labels before treating it as a repurposing candidate.

**To proceed, the following is needed:**
- Direct clinical evidence, such as controlled studies of esomeprazole in duodenogastric (bile) reflux
- Mechanism of action data (DrugBank)
- Health Canada package insert warnings and contraindications
- Original indication text from the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

