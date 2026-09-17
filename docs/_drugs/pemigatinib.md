---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: Original Indication Not on File — Predicted Association with Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is an FGFR1-3 selective small-molecule inhibitor (identified from the model's own rationale text; not present in the formal MOA field), but this evidence pack contains no record of its original approved indication, and it is not currently marketed in Canada. The TxGNN model's top prediction links it to **Multiple Endocrine Neoplasia**, but this is a low-confidence, model-only association — supported by **0 clinical trials** and **0 publications** — and the model's own rationale states there is no known direct mechanistic link between FGFR signaling and MEN.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication data on file for this drug in the current evidence pack |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pemigatinib is formally recorded as unavailable in this evidence pack. However, the model's own rationale text (used to justify other candidate indications in this same pack) identifies pemigatinib as an **FGFR1-3 (fibroblast growth factor receptor 1-3) selective inhibitor**, consistent with its known class as an antineoplastic targeted therapy.

For the top-ranked prediction, Multiple Endocrine Neoplasia, the model's own rationale is explicitly skeptical: MEN is driven primarily by germline mutations in *RET* and *MEN1*, which have no known direct relationship to the FGFR1-3 pathway that pemigatinib targets. The rationale states the high TxGNN score likely reflects indirect co-occurrence of endocrine-tumor nodes within the knowledge graph, rather than a genuine mechanistic inference — i.e., this should be read as a graph-topology artifact rather than a biologically grounded hypothesis.

Notably, this pattern is not isolated to rank 1. Of the ten predicted indications in this pack, several others also carry rationale text describing weak, reversed-direction, or species-mismatched mechanisms (e.g., an FGFR loss-of-function link to amenorrhea, veterinary diseases in cattle, and ALS pathophysiology pointing toward FGFR *activation* rather than inhibition). This lowers confidence in the overall ranking, not just the top entry.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Pemigatinib is **not currently marketed in Canada** — 0 licenses/DINs are on file in this evidence pack, so no product/dosage-form table can be produced.

---

## Cytotoxicity

Pemigatinib's rationale text explicitly describes it as an antineoplastic targeted agent (FGFR inhibitor class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1-3 selective small-molecule inhibitor) |
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
- This candidate has no clinical trial or literature support (L5, model prediction only), and the model's own mechanistic rationale explicitly questions the biological plausibility of the FGFR–MEN link, describing it as likely graph-topology noise rather than a genuine signal.

**To proceed, the following is needed:**
- TFDA/Health Canada product label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism-of-action data for pemigatinib (currently a High-severity data gap affecting mechanistic-relevance analysis)
- Original approved indication and regulatory history (currently absent from this evidence pack)
- Any preclinical or case-level evidence specifically connecting FGFR1-3 inhibition to MEN pathophysiology, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

