---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Domperidone: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Dyspepsia, heartburn, epigastric pain, nausea and vomiting"
monitor_inn: "DOMPERIDONE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Domperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Domperidone: From Upper Gastrointestinal Symptoms to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist used to manage dyspepsia, heartburn, epigastric pain, nausea and vomiting. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyspepsia, heartburn, epigastric pain, nausea and vomiting (from pharmacology data; the Canadian licence records contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for domperidone is not available in the compiled data. From pharmacology data, domperidone acts as an antagonist at the dopamine D2 and D3 receptors (DRD2, DRD3). It is used mainly for gastrointestinal symptoms, and in some countries off-label to enhance lactation.

The link to the predicted indication is weak. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2, e.g. R137C/R137L) or, in some cases, GNAS. These variants cause constitutive receptor activation, leading to water retention and hyponatraemia. Domperidone has no known direct action on the V2 receptor or its cAMP signalling. A possible indirect route is dopaminergic modulation of renal water handling or vasopressin release, but this is not established. Because the disease is driven by receptor-level constitutive activity, blocking upstream vasopressin release would not be expected to help.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

All 10 authorisations below are valid single-ingredient products. Dosage form and approved indication text are not available in the compiled data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02350440 | DOMPERIDONE | Not available | Not available |
| 02236857 | PRO-DOMPERIDONE | Not available | Not available |
| 02369206 | JAMP-DOMPERIDONE | Not available | Not available |
| 02445034 | BIO-DOMPERIDONE | Not available | Not available |
| 02238341 | DOMPERIDONE | Not available | Not available |

(Five of the 10 licences are shown; the others are TEVA-, APO-, TARO-, MAR- and PRZ-DOMPERIDONE products.)

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease and gallbladder disease. These point to cardiac rhythm (QT prolongation) and hepatobiliary concerns that need verification against the product monograph.
- **Drug Interactions:** The interaction query completed, but it returned only pharmacological target entries (dopamine D2 and D3 receptors), not drug-drug interactions.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there is no clinical or literature support, and the proposed mechanism is implausible: NSIAD arises from constitutively active V2 receptors, which domperidone does not target. The knowledge-graph QT-prolongation signal adds a safety concern in a population (patients with hyponatraemia) where electrolyte disturbance can further raise arrhythmia risk.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Preclinical evidence (e.g. in vitro V2 receptor/cAMP assays) showing any plausible effect on NSIAD
- A systematic literature search for any link between dopamine antagonism and vasopressin or renal water handling
- A cardiac safety assessment (QT, electrolytes) for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

