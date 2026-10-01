---
layout: default
title: Phenazopyridine
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 1
---

# Phenazopyridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Phenazopyridine: From Urinary Tract Pain Relief to Bronchitis

## One-Sentence Summary

Phenazopyridine is generally known as a urinary tract analgesic that acts locally on the urothelial mucosa.
The TxGNN model predicts it may be effective for **bronchitis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone, so this is a hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract pain relief (general pharmacological knowledge; no indication text is recorded in the licence data) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indications are recorded in the supplied data. Phenazopyridine is generally known as a urinary tract analgesic with a local effect on the urothelial mucosa. It has no known antimicrobial, anti-inflammatory or mucolytic activity relevant to bronchial airway disease.

On the supplied data, no credible mechanistic link between its original use and bronchitis can be established. The TxGNN score of 0.992 comes from a knowledge-graph model. It may reflect network proximity or graph artifacts rather than biology, and it is not clinical evidence.

Any hypothesis would need independent mechanistic support, such as a plausible target or pathway in airway epithelium. Route compatibility has also not been assessed. A drug taken for urinary tract effects may not reach airway tissue in a relevant way.

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
| 476714 | PYRIDIUM |

Dosage form and approved indication text are not recorded for this authorization.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (L5, model prediction only). No plausible mechanism links this urinary analgesic to bronchitis, and the high score may be a graph artifact. There is no basis to advance it.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, such as a target or pathway in airway epithelium, supported by independent preclinical or literature evidence
- Mechanism of action data from DrugBank
- The Health Canada package insert, including warnings and contraindications, to start safety screening
- Confirmation of the Canadian licence record, including dosage form and approved indication. The Evidence Pack lists TFDA as an input source, and licence number 476714 should be checked against Health Canada's DIN database.
- An assessment of route and exposure compatibility for bronchitis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

