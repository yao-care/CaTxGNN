---
layout: default
title: Cisatracurium
parent: Model Prediction Only (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Anesthesia Adjunct (Neuromuscular Blockade) to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a nondepolarizing neuromuscular blocker used in anesthesia.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but there are **0 clinical trials** and **0 publications** supporting this direction, and the pharmacology gives no plausible link. This is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records (the drug is a neuromuscular blocker used in anesthesia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cisatracurium is a nondepolarizing neuromuscular blocker that antagonizes nicotinic acetylcholine receptors at the neuromuscular junction. It is given by injection in operating rooms and intensive care units to produce skeletal muscle relaxation. Detailed mechanism-of-action data was not available in the source record, so this description comes from the pharmacological assessment attached to the prediction.

Cauda equina syndrome is caused by compression of the lumbosacral nerve roots. Blocking neuromuscular transmission would not relieve that compression and would cause flaccid paralysis. We found no plausible mechanistic link between the original use and the predicted indication. The high TxGNN score reflects patterns in the knowledge graph, not biological or clinical evidence.

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
| 2563266 | Cisatracurium Besylate Injection USP Multi-Dose | Not listed | Not listed |
| 2408813 | Cisatracurium Besylate Injection USP Multidose | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for this drug in the source data. Separately, magnesium sulfate, which is standard therapy in preeclampsia (another predicted indication), is known to potentiate neuromuscular blockers, so any obstetric anesthesia use needs monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and the pharmacology argues against benefit: neuromuscular blockade does not treat nerve-root compression. The other top-ranked predictions (for example preeclampsia, migraine, irritable bowel syndrome) are also L5 or weakly linked. The trials retrieved for preeclampsia and thrombotic disease study magnesium sulfate dosing and anesthesia techniques, not cisatracurium as a treatment.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, supported by preclinical data
- Mechanism-of-action data from DrugBank
- The approved indication text and Health Canada package insert warnings and contraindications
- Evidence that a parenteral, hospital-only neuromuscular blocker could have any therapeutic role in the predicted condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

