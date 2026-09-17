---
layout: default
title: Idarucizumab
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: From Dabigatran Anticoagulation Reversal to Hemoglobinopathy

## One-Sentence Summary

Idarucizumab is a humanized antibody Fab fragment whose only established clinical role, per the evidence pack, is neutralizing the anticoagulant effect of dabigatran in emergency situations. The TxGNN model's top prediction is **Hemoglobinopathy**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic notes flag the prediction as lacking any known biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Emergency reversal of dabigatran (Pradaxa) anticoagulant effect — inferred from mechanistic notes; not present in formal Taiwan/Canada regulatory records (no licenses on file) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 95.66% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available (flagged as a High-severity data gap). Based on what is known, idarucizumab is a dabigatran-specific antibody fragment whose sole documented pharmacology is high-affinity binding and neutralization of dabigatran's anticoagulant activity — it has no established role in hematopoiesis, globin synthesis, or red-cell membrane/enzyme biology.

Hemoglobinopathies (e.g., sickle cell disease, thalassemia) arise from globin gene mutations or structural hemoglobin defects — a disease category mechanistically unrelated to anticoagulant reversal. The evidence pack's own rationale for this candidate states there is "no known biological plausibility" and attributes the high TxGNN score to sparse knowledge-graph connectivity (the drug node has few edges since both its original indication and MOA are data gaps), producing embedding noise rather than a genuine pharmacological signal.

The same pattern holds across ranks 2–10 (rheumatoid arthritis, several rare genetic/hematologic disorders, bronchitis, gout, a congenital dysplasia syndrome): all are scored L5/Hold, and the one literature hit (PMID 31381100, rank 9 "gout") is a case report about dabigatran reversal therapy where gout appears to be an incidental comorbidity, not a treated indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Idarucizumab has no marketing authorizations on file (market status: Not Marketed, 0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications are recorded as a Blocking data gap (DG001) — this must be resolved before any S1 safety evaluation can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (hemoglobinopathy) has zero clinical trial or literature support, and the mechanistic rationale explicitly assesses no biological plausibility, attributing the high TxGNN score to sparse graph connectivity rather than genuine signal. Combined with missing MOA and safety data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — Blocking gap, required before any safety review
- Confirmed mechanism of action data from DrugBank
- Any preclinical or mechanistic studies linking dabigatran-antibody pharmacology to hematologic/globin pathways, if they exist
- Re-evaluation of all 10 ranked candidates once the above gaps are closed, as none currently exceed L4 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

