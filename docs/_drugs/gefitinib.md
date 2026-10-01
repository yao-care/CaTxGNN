---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor, used in Canada for non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score, but **0 clinical trials** and **0 publications** currently support this direction. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (from the published literature; the Health Canada indication text is blank in the input) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on known information, gefitinib is an EGFR tyrosine kinase inhibitor. Its efficacy in EGFR-mutant NSCLC is established, and EGFR signalling might plausibly relate to fibroblast proliferation.

Gingival fibromatosis is a benign overgrowth of gingival connective tissue and is biologically far from lung cancer. No trial, publication or preclinical study in the Evidence Pack links gefitinib to this condition. The high TxGNN score reflects a pattern in the knowledge graph, not confirmed biology. Any mechanistic link is a hypothesis to test, not a finding.

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
| 02248676 | IRESSA |
| 02468050 | APO-GEFITINIB |
| 02487748 | SANDOZ GEFITINIB |
| 02491796 | NAT-GEFITINIB |
| 02500663 | JAMP GEFITINIB |

The input does not include dosage forms or approved indication text for these products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the retrieved literature also discusses interstitial lung disease, QT prolongation and cutaneous toxicity |
| Handling Protection | Please refer to the package insert for handling requirements |

---

## Safety Considerations

The Health Canada package insert warnings, contraindications and drug interaction data are not available in the input. Please refer to the package insert for safety information.

The literature retrieved for other predicted indications reports these gefitinib-related signals:
- **Interstitial lung disease** (NEJM correspondence, 2010; targeted-therapy pulmonary toxicity review, 2011)
- **QT prolongation** (mechanistic study, 2021; a cohort of 122 NSCLC patients, 2023)
- **Cutaneous toxicity** (acneiform eruption, paronychia and xerosis with EGFR inhibitors)

These signals are context only. They are not a substitute for the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no established mechanistic link (Evidence Level L5). The benign, fibrotic nature of the disease also gives little rationale for a drug with notable skin and lung toxicity.

Among the other top-10 predictions, lung hilum carcinoma (rank 5) has the most support, a single case report of a gefitinib super-responder. It largely overlaps with the existing NSCLC use rather than being true repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or case-level evidence linking EGFR signalling to gingival fibroblast overgrowth
- Approved indication text and dosage forms for the five Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

