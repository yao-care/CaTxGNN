---
layout: default
title: Procainamide
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Procainamide
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

# Procainamide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Procainamide is a Class IA sodium-channel blocker antiarrhythmic, marketed in Canada as an injection.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record (the drug's known use is cardiac arrhythmia) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Procainamide is a Class IA antiarrhythmic that blocks sodium channels, and its efficacy in arrhythmia is well established. However, no plausible mechanism links this action to tic disorders.

The prediction therefore looks like a statistical artefact of the knowledge graph rather than a biologically grounded hypothesis. The score is very high (99.46%), but the model rank is 9,829. Many other predictions for this drug score nearly the same, so the score does little to separate promising candidates from weak ones.

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
| 2184486 | PROCAINAMIDE HYDROCHLORIDE INJECTION USP | Injection (from product name) | Not provided in the licence record |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug.

One safety signal appears in the evidence for another predicted indication, rheumatoid arthritis. Procainamide is associated with drug-induced lupus, antihistone and antinuclear antibodies, glomerulopathy and pulmonary fibrosis. Any repurposing plan should account for this autoimmune risk, and NAT2 acetylator status is a relevant pharmacogenetic modifier.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction has no trials, no literature and no identifiable mechanism, so it is Level L5 (model prediction only). Procainamide's known pharmacology does not point toward tic disorders.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indication), since safety screening cannot start without it
- Mechanism of action data from DrugBank, followed by an analysis of any link to tic disorders
- Preclinical or mechanistic evidence supporting a role in Tourette syndrome
- A review of the other predicted indications:
  - **Hyperthyroidism** and **Prinzmetal angina** have only case reports and small cohorts. These describe arrhythmia management in those patients, not treatment of the underlying disease.
  - **Rheumatoid arthritis** shows a safety signal rather than benefit.
  - The remaining predictions have no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

