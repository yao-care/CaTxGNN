---
layout: default
title: Imipenem
parent: Model Prediction Only (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Imipenem is a carbapenem antibiotic (marketed with cilastatin) that is used against serious bacterial infections.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records provided |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Imipenem is a bactericidal carbapenem that inhibits bacterial penicillin-binding proteins, and its efficacy in bacterial infections is well established.

Diffuse scleroderma is an autoimmune, fibrotic disease with no infectious driver. There is no plausible mechanistic link between an antibacterial cell-wall inhibitor and this condition, and no immunomodulatory or antifibrotic activity of imipenem is described. The very high TxGNN score (rank 282 among its predictions) is not supported by any trial or publication, so it most likely reflects an artifact of the knowledge graph rather than a real repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02351706 | TARO-IMIPENEM-CILASTATIN | Not stated | Not stated |
| 02358344 | IMIPENEM AND CILASTATIN FOR INJECTION USP | Not stated | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanism (L5), so it should not be pursued. Other predicted indications for imipenem are better supported and deserve attention instead:
- **Typhoid fever (L3):** recent retrospective observational reports describe carbapenems as a last-line option for extensively drug-resistant strains.
- **Staphylococcus aureus infection (L3):** small Phase 4 trials test imipenem combinations (with fosfomycin or linezolid) in MRSA.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication and dosage form details for both Canadian DINs
- For the S. aureus candidate, confirmation of imipenem's role in NCT03583333 (Phase 3) and NCT00707239 (Phase 2), whose titles are truncated. Confirmation could raise its evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

