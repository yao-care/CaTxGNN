---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Sore Throat Relief to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is a topical antiseptic used in throat lozenges. The licence records do not state an approved indication, but the product names point to sore throat relief.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (product names indicate throat lozenges for sore throat) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amylmetacresol is a locally acting antiseptic in throat lozenges. It shows in vitro antibacterial and antiviral activity in the oropharynx and is not used systemically.

No plausible pathway links this activity to cauda equina syndrome, a compressive neurological condition. The prediction score is high (99.99%), but it comes from the model alone, and no mechanistic or similarity analysis supports it. The remaining nine predictions have the same problem. They include obsolete neurogenic bladder, irritable bowel syndrome and a cluster of uveal-tract diseases (ciliary body disease, panuveitis, iris disease, uveitis and others). The uveal cluster likely reflects a shared graph-neighbourhood artifact rather than independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2375567 | ANTIBACTERIAL THROAT LOZENGES |
| 2382938 | CEPACOL SENSATIONS |
| 2404982 | CEPACOL CHILDREN'S FRUITY STRAWBERRY |
| 2388642 | CEPACOL SENSATIONS SORE THROAT & COUGH |
| 2382881 | CEPACOL SENSATIONS SORE THROAT & BLOCKED NOSE |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score (L5). There are no trials or publications, no mechanistic link, and no plausible route from a topical throat antiseptic to a compressive neurological condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to test whether any biological link exists
- Approved indication text for the licensed products
- Route compatibility assessment (lozenge vs. the systemic or local route the new indication would require)
- Any preclinical or clinical evidence for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

