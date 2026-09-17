---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ivabradine: From Cardiac Rate Modulation (Original Indication Not on File) to Hypertrichosis (Disease)

## One-Sentence Summary

Ivabradine's original approved indication could not be confirmed from available data — the evidence pack notes it as a selective HCN4/If-channel blocker that reduces heart rate at the sinoatrial node, but no formal indication or MOA record was retrieved. The TxGNN model's top prediction is **Hypertrichosis (disease)**, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known biological link between If-channel blockade and hair follicle growth regulation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on file; drug is not currently marketed in Canada |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this evidence pack). Based on the limited information available, ivabradine is described as a selective HCN channel (If current) blocker acting on sinoatrial node pacemaker cells to reduce heart rate — a cardiac rate-control mechanism.

This mechanism has no known intersection with hair follicle growth regulation. The model's own rationale for the top-ranked prediction explicitly states the link is a pure knowledge-graph embedding similarity, with **no biological basis**: *"Ivabradine acts on the cardiac sinoatrial node HCN4 channel, with no known overlap with hair follicle growth regulatory pathways; this is purely a TxGNN graph embedding similarity prediction, lacking biological grounding."*

The same pattern holds for the remaining five candidates in this evidence pack (Ambras-type hypertrichosis, periodontal malformation syndrome, Dandy-Walker malformation syndrome, hair shaft abnormality, and nephrogenic syndrome of inappropriate antidiuresis) — each rationale independently concludes there is no plausible pharmacological or pathophysiological connection to ivabradine's known cardiac mechanism. Notably, the periodontal candidate returned 20 PubMed co-occurrence hits, but the rationale confirms none of these actually study ivabradine in relation to periodontal disease; this is assessed as a knowledge-graph co-occurrence false positive (likely mediated indirectly through shared diabetes/cardiovascular comorbidity nodes).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ivabradine is not currently marketed in Canada under this evidence pack (market status: Not Marketed; 0 licenses/DINs on file). No product listing table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications for ivabradine in this evidence pack carry L5 evidence (model prediction only) with no supporting clinical trials and no literature directly studying the drug-disease relationship. The model's own mechanistic rationale explicitly rejects biological plausibility for the top-ranked candidate (hypertrichosis) and all others, indicating these are knowledge-graph embedding artifacts rather than credible repurposing signals.

**To proceed, the following is needed:**
- Confirmed original indication and regulatory history for ivabradine (currently missing from this evidence pack)
- Mechanism of action data from DrugBank (flagged as High-severity data gap)
- Health Canada / TFDA label warnings and contraindications (flagged as Blocking data gap — required before any S1 safety review)
- A biologically plausible hypothesis linking HCN/If-channel blockade to any of the six predicted indications before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

