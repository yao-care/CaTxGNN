---
layout: default
title: Tafamidis
parent: Model Prediction Only (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloidosis to Primary Release Disorder of Platelets

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) tetramer stabilizer, used to treat transthyretin amyloidosis.
The TxGNN model ranks **primary release disorder of platelets** as its top prediction, but **0 clinical trials** and **0 publications** support it.
No plausible biological link to this disease was found, so the high score is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input record. From the evidence analysis, tafamidis binds the thyroxine-binding sites of the TTR tetramer. This prevents the tetramer from dissociating into amyloidogenic monomers, which is the rate-limiting step of TTR amyloid formation. The Canadian license record does not list an approved indication, so the original indication above comes from the supporting literature.

Primary release disorder of platelets is a defect in platelet granule secretion. No known pathway connects TTR stabilization to platelet release or granule secretion. The model's high score (rank 130,486 among all scored pairs) most likely reflects network proximity in the knowledge graph rather than a real pharmacological relationship. This prediction should not be treated as a repurposing lead without new mechanistic evidence.

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
| 2517841 | VYNDAMAX |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no publications and no mechanistic rationale. Nothing supports moving it forward.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking TTR stabilization to platelet granule release
- Preclinical or in vitro data in platelet function models
- Health Canada package insert warnings and contraindications, for the safety screen
- Mechanism of action data confirmed from DrugBank

**Note on other predictions for this drug:** Two lower-ranked predictions have much stronger support and may be more useful to review first.
- **Primary amyloidosis (rank 5):** Evidence Level L1, Proceed with Guardrails. It rests on the ATTR-ACT randomized trial (PMID 30145929), but that trial covers transthyretin amyloid cardiomyopathy, not light-chain (AL) amyloidosis. It is also an on-label use rather than true repurposing.
- **Acquired amyloid peripheral neuropathy (rank 6):** Evidence Level L2, Proceed with Guardrails. The supporting evidence is for hereditary ATTR polyneuropathy, mainly in early-stage disease, and regulatory status for this use differs by region.

This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

