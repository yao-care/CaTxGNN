---
layout: default
title: Nelarabine
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 1
---

# Nelarabine
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

# Nelarabine: From T-Cell Acute Lymphoblastic Leukemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine is a purine nucleoside analog chemotherapy. The supplied data lists no original indication; it is generally used for T-cell leukemia/lymphoma.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, with a score of 99.4%.
Currently there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (generally T-cell acute lymphoblastic leukemia / T-cell lymphoblastic lymphoma, from general knowledge) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. The following comes from general pharmacology and should be treated as a hypothesis. Nelarabine is a prodrug of ara-G, a purine nucleoside analog. Inside cells, ara-G accumulates as ara-GTP, particularly in T-lymphoblasts, where it is selectively cytotoxic to T cells.

Multiple sclerosis is partly driven by autoreactive T cells. Depleting these cells is conceptually similar to cladribine, another purine analog already used in relapsing MS. This is the only plausible link to the predicted indication. No trial or publication supports it so far.

There is also a major mechanistic conflict. Nelarabine carries a boxed warning for severe neurotoxicity, including demyelination, peripheral neuropathy, and Guillain-Barré-like ascending paralysis. This risk runs directly against a demyelinating disease and is the main barrier to this repurposing direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2299925 | ATRIANCE | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog, antimetabolite) |
| Myelosuppression Risk | Medium (neutropenia, thrombocytopenia and anemia are generally reported) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, serial neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

The entries above come from general drug-class knowledge, not the supplied data. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Key Warnings**: Boxed warning for severe neurotoxicity, including demyelination, peripheral neuropathy, and Guillain-Barré-like ascending paralysis. This is noted in the repurposing rationale. The Health Canada package insert has not been reviewed.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score. There are no clinical trials or literature, so the evidence level is L5. The boxed neurotoxicity warning, which includes demyelination, conflicts directly with treating multiple sclerosis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Original indication and approved indication text for the Canadian license
- Preclinical or clinical evidence that T-cell depletion with nelarabine can be achieved in MS without unacceptable neurotoxicity
- Assessment of dosing, route, and treatment duration compatibility with a chronic disease like MS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

