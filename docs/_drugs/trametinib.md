---
layout: default
title: Trametinib
parent: Model Prediction Only (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From BRAF V600 Melanoma to Choroideremia

## One-Sentence Summary

Trametinib is a MEK inhibitor marketed in Canada as MEKINIST. The evidence pack indicates it is used for BRAF V600-mutant melanoma, though the licence records supplied contain no indication text.
The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration, with a score of 99.31%.
**No clinical trials and no publications** support this prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence data (the pack's rationale notes marketing for BRAF V600 melanoma) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Trametinib is known to be a reversible, allosteric inhibitor of MEK1 and MEK2 (as described in the trial records). It acts downstream of BRAF and RAS in the MAPK pathway, and its efficacy in BRAF-mutant melanoma is established.

The link to choroideremia is weak. Choroideremia is an X-linked retinal degeneration caused by loss of function of the CHM gene (REP1 protein). The supplied data show no established connection between this disease and MAPK/MEK signaling. The high score (0.993) is most likely a knowledge-graph artifact, driven by ocular and melanoma-related neighbouring nodes rather than a real biological link.

Safety also argues against this use. MEK inhibitors are known to cause ocular toxicity, including serous retinopathy and retinal vein occlusion. That is a concern in a retina that is already degenerating.

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
| 2409658 | MEKINIST | Not listed | Not listed |
| 2409623 | MEKINIST | Not listed | Not listed |
| 2539993 | MEKINIST | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Ophthalmic examination is relevant given the ocular toxicity noted below |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Ocular toxicity (class effect):** MEK inhibitors can cause serous retinopathy and retinal vein occlusion. This is a particular concern in choroideremia, where the retina is already degenerating.

Please refer to the package insert for the full warnings, contraindications and drug interactions. No interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or publications behind it, and there is no known biological link between MEK inhibition and CHM/REP1 loss. The ocular toxicity profile of MEK inhibitors is a further safety obstacle in a degenerating retina.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence that MAPK/MEK modulation is relevant to choroideremia
- The Health Canada package insert, to complete the safety screening
- Detailed mechanism of action data
- An ocular safety assessment specific to retinal degeneration

Other predicted indications in this pack have more support. Superficial spreading melanoma is graded L2 with "Proceed with Guardrails", but it is largely an on-label use rather than true repurposing. Non-cutaneous melanoma is graded L2 and acral lentiginous melanoma L3, both with a "Research Question" recommendation. These could be evaluated as separate candidates.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

