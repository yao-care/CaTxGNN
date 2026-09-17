---
layout: default
title: Methocarbamol
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol: From Skeletal Muscle Relaxation to Cauda Equina Syndrome

## One-Sentence Summary

Methocarbamol's original indication record and mechanism of action are both missing from the current data pull, though the evidence pack's own rationale text identifies it as a centrally-acting skeletal muscle relaxant. TxGNN's top prediction is **Cauda Equina Syndrome**, but this is a pure knowledge-graph embedding similarity score (99.98%) with **zero supporting clinical trials or literature**. Across all 10 TxGNN candidates for this drug, evidence level is uniformly **L5** (model prediction only), and two literature hits that surfaced for other candidates (anaphylaxis, ventricular tachycardia) appear to be keyword mismatches rather than genuine mechanistic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no original indication records; MOA marked as data gap) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for methocarbamol is not available. Based on the information present elsewhere in this evidence pack (the rationale text for other candidate indications), methocarbamol is understood to be a **centrally-acting skeletal muscle relaxant**, but no original indication text was returned from DrugBank, and no dosage/route data exists.

For the top-ranked candidate, cauda equina syndrome, the evidence pack explicitly states there is **no known mechanistic link**: the prediction is driven solely by TxGNN's knowledge-graph embedding similarity (score 0.9998, model rank 894 of the full candidate set) and is not supported by any pharmacological or pathophysiological pathway. Cauda equina syndrome is a surgical neurological emergency (nerve root compression), and a centrally-acting muscle relaxant has no established disease-modifying role in that condition based on the data available here.

The nine other candidates surfaced by the model (irritable bowel syndrome, panuveitis, anaphylaxis, iris disease, uveitis, ventricular tachycardia, food-dependent exercise-induced anaphylaxis, conjunctivitis, obsolete bundle branch block) show the same pattern: high embedding similarity scores (99.93%–99.98%) with no mechanistic rationale. Where literature did surface (anaphylaxis: PMID 20086833; ventricular tachycardia: PMID 30050852), the source documents themselves note these are likely keyword mismatches — one is a general review of arthropod-bite management that mentions methocarbamol only as an adjunct treatment for widow spider envenomation, and the other is a case report of lamotrigine toxicosis in a dog with no connection to methocarbamol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Cauda Equina Syndrome.

*(Note: the only literature hits in this evidence pack are attached to lower-ranked candidates — anaphylaxis and ventricular tachycardia — and are assessed as likely mismatches rather than supporting evidence; see rationale above.)*

---

## Canada Market Information

Methocarbamol currently has **0 authorizations on file** and a market status of **Not Marketed** in this dataset. No DIN, product, or dosage-form records are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were all queried but returned no results in this evidence pack — a TFDA label review is flagged as a blocking data gap; see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by mechanism, clinical trials, or credible literature — evidence level L5 across all 10 candidates. Two of the few literature hits retrieved for this drug are flagged as likely mismatches, and basic safety/regulatory data (TFDA label, MOA) are outright missing, which blocks even a preliminary safety screen (S1).

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any safety pre-screen)
- Confirmed mechanism of action (DrugBank API query)
- Original indication record (currently empty — needed to assess biological plausibility of repurposing)
- Targeted literature/clinical-trial search specifically for methocarbamol + cauda equina syndrome (current searches returned 0 hits)
- If pursuing lower-ranked candidates instead, independent verification that the anaphylaxis/ventricular tachycardia literature hits are true mismatches before discarding those signals entirely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

