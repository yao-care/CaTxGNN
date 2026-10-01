---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is an iodinated radiographic contrast agent used for diagnostic imaging, not as a treatment for any disease.
The TxGNN model predicts **osteoarthritis susceptibility** with a very high score, but there are **0 clinical trials** and **0 publications** for this prediction.
The score most likely reflects a knowledge-graph artifact rather than real therapeutic potential.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (iodinated radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ioversol is an inert iodinated contrast agent that makes tissues visible on X-ray and CT imaging. It has no known anti-osteoarthritic pharmacology.

No credible mechanistic link to osteoarthritis susceptibility was found. The high TxGNN score most likely reflects the drug's proximity to musculoskeletal disease nodes in the knowledge graph, not a biological effect. The prediction should be treated as a model artifact unless independent evidence emerges.

The other top predictions (rheumatoid arthritis, brachyolmia, hemoglobinopathy, alopecia and several ultra-rare skeletal dysplasias) also have no plausible mechanism and no supporting clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis susceptibility.

For the closely related prediction **osteoarthritis** (rank 2), four trials exist. All are genicular or digital artery embolization studies. In these, contrast agents such as ioversol serve at most for angiographic guidance, and the embolic agent (Lipiodol/ethiodized oil) is a different drug. They are not evidence for ioversol.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Sham-controlled genicular artery embolization in symptomatic knee osteoarthritis; ioversol is not the tested intervention |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | Pilot sham-controlled embolization trial for knee osteoarthritis pain; ioversol has at most an imaging role |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Lipiodol embolization in digital (hand) osteoarthritis; active agent is ethiodized oil |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Safety study of a Lipiodol emulsion for knee pain from inflammatory hypervascularization; does not evaluate ioversol |

---

## Literature Evidence

Currently no related literature available for osteoarthritis susceptibility.

The only related publication, for osteoarthritis, is listed below. It concerns Lipiodol, not ioversol.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Prospective single-arm pilot trial | Diagn Interv Imaging | LipioJoint-1: safety and efficacy of transient genicular artery embolization with an ethiodized oil emulsion in knee osteoarthritis |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 1900854 | OPTIRAY 320 |
| 2035626 | OPTIRAY 320 (ULTRAJECT) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials, no literature and no plausible mechanism. Ioversol is a contrast agent without disease-modifying activity, and the osteoarthritis trials found involve embolization procedures rather than ioversol as a therapy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data from DrugBank
- Any direct evidence that ioversol itself, not the embolization procedure or another agent, affects osteoarthritis
- Approved indication text, dosage form and manufacturer for the two Canadian licences

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

