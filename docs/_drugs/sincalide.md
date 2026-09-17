---
layout: default
title: Sincalide
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
---

# Sincalide
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

# Sincalide: From Gallbladder Function Diagnostics to Malignant Catarrh (Low-Confidence Prediction)

## One-Sentence Summary

Sincalide is a synthetic cholecystokinin (CCK) analog used as a diagnostic agent to stimulate gallbladder contraction and pancreatic secretion. TxGNN's top prediction assigns a very high score to **malignant catarrh** — a herpesvirus disease of cattle — but this is supported by **zero clinical trials and zero publications**, and the mechanistic rationale itself flags the prediction as a likely species/ontology mismatch rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in evidence pack (no approved licenses on file); clinically known as a diagnostic aid for gallbladder/pancreatic function |
| Predicted New Indication | Malignant catarrh (bovine herpesvirus disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as `[Data Gap]`, DG002). Based on contextual information embedded in the evidence pack's own rationale text, Sincalide is a CCK analog used clinically for gallbladder function diagnostics — it is not a treatment for any disease, human or veterinary.

The top-ranked prediction, malignant catarrh, is a herpesvirus-driven disease of cattle and other ruminants. There is no known physiological link between CCK signalling and this pathogen-driven condition, and the rationale field explicitly states there is "no verifiable mechanistic hypothesis" and "no supporting literature." Rank 2 (infectious bovine rhinotracheitis) is the same pattern — another cattle virus disease — strongly suggesting the model is confusing veterinary and human disease ontologies rather than surfacing a real signal.

Across all 10 ranked predictions in this pack, none reach above L4 evidence, none have any clinical trials, and the handful of literature hits (e.g., CCK and pancreatic acinar cell physiology, thyroid-status effects on insulin secretagogues) are basic-science papers studying CCK/CCK-8 as a laboratory tool, not therapeutic evidence for the predicted disease. This evidence pack is best read as a demonstration of TxGNN false positives rather than a viable repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (malignant catarrh).

*Note: Lower-ranked candidates in this pack (cytomegalovirus infection, hyperthyroidism) do have 1–3 literature hits each, but all are basic-science/animal studies studying CCK as a physiological probe, not evidence of therapeutic benefit — see overview table below.*

---

## Canada Market Information

Sincalide is not currently marketed in Canada. No DIN registrations or product licenses are on file.

---

## All Predicted Indications — Overview (for transparency)

| Rank | Disease | TxGNN Score | Evidence Level | Literature (n) | Notes |
|------|---------|------------|-----------------|-----------------|-------|
| 1 | Malignant catarrh | 99.96% | L5 | 0 | Cattle disease; likely ontology mismatch |
| 2 | Infectious bovine rhinotracheitis | 99.96% | L5 | 0 | Cattle disease; likely ontology mismatch |
| 3 | Cytomegalovirus infection | 99.96% | L5 | 1 | Sole paper studies CCK's role in acinar cell exocytosis, unrelated to antiviral activity |
| 4 | Thrombotic disease | 99.94% | L5 | 0 | No known CCK–coagulation link |
| 5 | Hyperthyroidism | 99.93% | **L4** | 3 | Papers show thyroid status affects response to CCK-8 as a secretagogue — direction reversed (thyroid affects drug response, not drug treats thyroid disease) |
| 6 | TR-β resistance to thyroid hormone | 99.92% | L5 | 0 | No mechanistic link |
| 7 | Hyperthyroxinemia | 99.88% | L5 | 0 | No mechanistic link |
| 8 | Homozygous familial hypercholesterolemia | 99.85% | L5 | 0 | No mechanistic link |
| 9 | Prinzmetal angina | 99.84% | L5 | 0 | No mechanistic link |
| 10 | Amenorrhea (disease) | 99.83% | L5 | 0 | No mechanistic link |

All 10 candidates carry a scoring-stage recommendation of **Hold**, and none progress past decision stage S0.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — flagged as `[Data Gap]`, DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are L4–L5 evidence with no clinical trials and, at best, tangential basic-science literature. The top two predictions (malignant catarrh, infectious bovine rhinotracheitis) are veterinary diseases with no plausible mechanistic link to a human diagnostic agent, indicating a likely model artifact rather than a genuine repurposing opportunity. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label/warning data from the relevant regulatory authority before any safety review can begin.
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to properly assess biological plausibility.
- Re-run KG/TxGNN prediction with veterinary-disease ontology terms filtered out, to prevent species-mismatched false positives from surfacing in future evidence packs.
- If a genuine human-relevant signal is desired, review lower-confidence predictions with actual literature support (e.g., hyperthyroidism, L4) rather than the top-ranked score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

