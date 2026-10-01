---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 519
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

# Lansoprazole: From Acid-Related Gastrointestinal Disorders to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI) marketed in Canada. Its original indication is not recorded in the source data, but the PPI class is used for acid-related conditions such as peptic ulcer and gastro-oesophageal reflux disease.
The TxGNN model predicts it may be effective for **duodenogastric reflux** with a score of 99.69%.
Support is weak: **0 clinical trials** and **2 publications**, and the only direct study is a rat model that raises a safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data. The PPI class is used for peptic ulcer, *H. pylori* infection, GERD, NSAID-induced GI lesions and Zollinger-Ellison syndrome (PMID 18679668) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 (preclinical study only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology, lansoprazole is a proton pump inhibitor that suppresses gastric acid secretion. Its efficacy in acid-related upper GI disease is well established, so it could plausibly ease symptoms of reflux-related mucosal injury.

The mechanistic fit is only partial. Duodenogastric (bile) reflux is driven mainly by bile and pancreatic secretions rather than by acid. Suppressing acid may therefore offer limited benefit for the underlying problem.

The only direct study is a rat model (PMID 15052437) in which lansoprazole promoted gastric carcinogenesis under duodenogastric reflux. Possible explanations include hypergastrinaemia or an altered gastric environment. Because the original indication and mechanism are both missing from the source data, the high TxGNN score cannot be checked against known pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study (rat) | Gastric Cancer | Examined combined duodenogastric reflux and acid inhibition. Per the title, lansoprazole **promoted gastric carcinogenesis** in rats with reflux, which is a safety signal |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Update on PPI clinical use and pharmacokinetics. PPIs are first-choice drugs for peptic ulcer, *H. pylori* infection, GERD, NSAID-related GI injury and Zollinger-Ellison syndrome. Duodenogastric reflux is not listed among these uses |

---

## Canada Market Information

Lansoprazole has 20 licenses (DINs) in Canada. Five main authorizations are shown below. Dosage form and approved indication text are not available in the source data.

| DIN | Product Name |
|---------|------|
| 2165503 | PREVACID |
| 2353849 | MYLAN-LANSOPRAZOLE |
| 2422816 | RIVA-LANSOPRAZOLE |
| 2249472 | PREVACID FASTAB |
| 2402629 | TARO-LANSOPRAZOLE |

---

## Safety Considerations

- **Preclinical safety signal**: In a rat model of duodenogastric reflux, lansoprazole promoted gastric carcinogenesis (PMID 15052437). Human relevance is unknown, but it needs attention before any use in this setting.

No warnings, contraindications or drug interaction data are available in the source record. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a rat study that points toward harm rather than benefit. There are no clinical trials, and the mechanistic link is uncertain because bile reflux is not acid-driven. A second prediction, duodenal obstruction, also has no credible mechanistic link. That is a mechanical condition, and none of the retrieved trials or papers tests lansoprazole for it, so its high score likely reflects a graph-association artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- The original approved indication, to assess similarity to the predicted indication
- Human clinical data on lansoprazole in duodenogastric reflux, and an assessment of whether the rat carcinogenesis signal applies to humans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

