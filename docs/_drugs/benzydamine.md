---
layout: default
title: Benzydamine
parent: Model Prediction Only (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Benzydamine: predicted new indication benign prostatic hyperplasia (evidence level L5). Approved use: Not specified in the available licence data"
monitor_inn: "Benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
---

# Benzydamine
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

## Benzydamine: From Locally Marketed Single-Ingredient Products to Benign Prostatic Hyperplasia
{: .text-alpha }

## One-Sentence Summary

Benzydamine is a non-steroidal anti-inflammatory agent with local anesthetic activity, and it is currently marketed in Canada in four single-ingredient products. The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**. At present there are **no clinical trials and no publications** supporting this direction, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, benzydamine is a non-steroidal anti-inflammatory agent with local anesthetic activity. Its reported actions include inhibition of pro-inflammatory cytokines (TNF-alpha, IL-1beta) and membrane-stabilizing effects. This description could not be confirmed from the supplied data.

Chronic prostatic inflammation and lower urinary tract symptoms are thought to contribute to BPH. A plausible, but unverified, link therefore exists through anti-inflammatory and analgesic effects. No direct evidence shows that benzydamine affects prostate growth or urinary outflow obstruction. The score of 0.9926 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02494434 | PHARIXIA ALCOHOL FREE | Not listed | Not listed |
| 02463105 | ODAN-BENZYDAMINE | Not listed | Not listed |
| 02229777 | PHARIXIA | Not listed | Not listed |
| 02239537 | PMS-BENZYDAMINE | Not listed | Not listed |

All four licences are valid single-ingredient products.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report, and no disease-level contraindications were identified from the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this indication is a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, the mechanism of action data is missing, and the Canadian licence data lack indication text and dosage forms. Without these, the prediction cannot be meaningfully assessed. The Health Canada safety label data are also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications, dosage forms)
- Mechanism of action data from DrugBank
- Route-of-administration compatibility assessment. Benzydamine products are typically topical or oral-rinse, which may not reach prostate tissue, so this needs to be checked.
- A targeted literature and trial search for benzydamine in BPH or prostatic inflammation
- Preclinical or mechanistic studies, if no clinical evidence is found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

