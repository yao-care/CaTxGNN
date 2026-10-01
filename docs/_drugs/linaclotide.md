---
layout: default
title: Linaclotide
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 3
---

# Linaclotide
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

# Linaclotide: From Gastrointestinal Disorders to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide is a locally acting gut drug that is marketed in Canada as CONSTELLA.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Linaclotide is a minimally absorbed guanylate cyclase-C (GC-C) agonist. It acts locally on the intestinal lining, raising cGMP, increasing fluid secretion and gut transit, and dampening visceral pain signalling. Detailed mechanism data and the original approved indications are not recorded in the Evidence Pack.

The link to cauda equina syndrome is weak. Linaclotide has no known action on the cauda equina or on nerve-root compression or injury. The only plausible connection is indirect: it might ease the constipation and bowel dysfunction that can accompany the syndrome. That would be symptom management, not treatment of the underlying condition.

The very high TxGNN score (99.96%) is a knowledge-graph prediction. It has no clinical data behind it and should be read as a hypothesis, not as evidence of efficacy.

**Other predictions in the pack (both L5, Hold):**
- **Obsolete neurogenic bladder (disease):** score 99.89%. There is no direct mechanism, because linaclotide stays in the gut and is unlikely to affect bladder function. The disease term is also flagged as obsolete in the ontology.
- **Insomnia (disease):** score 99.51%. There is no plausible pharmacological link, because linaclotide is not CNS-active. Any benefit would be indirect, through better GI symptoms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2469510 | CONSTELLA |
| 2417162 | CONSTELLA |
| 2417170 | CONSTELLA |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanism does not plausibly reach the target condition. The high score alone does not justify moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data from DrugBank
- Any preclinical or clinical evidence linking GC-C agonism to cauda equina syndrome, or to neurogenic bowel dysfunction in that setting
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

