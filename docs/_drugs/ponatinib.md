---
layout: default
title: Ponatinib
parent: Model Prediction Only (L5)
nav_order: 746
evidence_level: L5
indication_count: 2
---

# Ponatinib
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

# Ponatinib: Repurposing Prediction for Gingival Fibromatosis

## One-Sentence Summary

Ponatinib is a multi-kinase inhibitor marketed in Canada as ICLUSIG, and the license data supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal (Evidence Level L5) and should be treated as a hypothesis, not a candidate ready for development.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, ponatinib is a multi-kinase inhibitor, and a kinase-pathway effect could in principle be relevant to a proliferative tissue disorder.

Hereditary gingival fibromatosis is rare and largely genetic (for example, SOS1-related). The supplied data documents no kinase-pathway rationale linking ponatinib to this condition, so no mechanistic link can be established. The very high TxGNN score (0.990) is a statistical output of the knowledge-graph model. It is not biological or clinical confirmation.

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
| 2437333 | ICLUSIG |

Dosage form, manufacturer and approved indication text were not provided in the license record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no linked trials or publications, no mechanism of action data, and no plausible kinase-based rationale for a largely genetic, rare condition. The package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data, for example from DrugBank
- A targeted literature and trial search on ponatinib in gingival fibromatosis
- Confirmation of the approved indication and dosage form for DIN 2437333

**Alternative lead:** The second-ranked prediction, **liposarcoma** (TxGNN score 99.00%, Evidence Level L4), has one linked preclinical kinase-profiling study (PMID 29132397, 2017). The supplied metadata does not show whether ponatinib was tested in that study, so the full text must be checked. It is currently classed as a research question, not a development candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

