---
layout: default
title: Neostigmine
parent: Model Prediction Only (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Neostigmine
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

# Neostigmine: From a Cholinesterase Inhibitor to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Neostigmine is an acetylcholinesterase inhibitor that raises acetylcholine levels at the neuromuscular junction, and it is currently marketed in Canada.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Neostigmine is known to inhibit acetylcholinesterase, which raises synaptic acetylcholine at the neuromuscular junction. This is the rationale for symptomatic treatment of acetylcholine receptor antibody-mediated myasthenia gravis.

Myasthenia gravis is an autoimmune disease in which the acetylcholine receptors on muscle are lost or blocked. A drug that keeps more acetylcholine available can partly compensate. The predicted indication is a thymic hyperplasia subtype of this disease, so the mechanistic link is plausible.

Nothing in the supplied data addresses this subtype specifically. The high score of 0.9997 should be read as a hypothesis from the model, not as confirmed efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Six licenses are on record. Five are listed below. Dosage form and approved indication text were not supplied for these products.

| DIN | Product Name |
|---------|------|
| 2230592 | NEOSTIGMINE OMEGA |
| 2475480 | NEOSTIGMINE METHYLSULFATE INJECTION USP |
| 2475499 | NEOSTIGMINE METHYLSULFATE INJECTION USP |
| 2387166 | NEOSTIGMINE OMEGA |
| 2230593 | NEOSTIGMINE OMEGA |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials and no publications, so the evidence is limited to the model score (L5). The mechanistic link is plausible, but nothing shows that neostigmine works in the thymic hyperplasia subtype specifically.

Lower-ranked predictions have more supporting material:
- **Autoimmune limb-girdle myasthenia, neonatal myasthenia gravis and autoimmune disease of the peripheral nervous system:** Each has some literature and is rated L4 as a research question. The literature is mostly case reports, reviews and preclinical work, with no controlled data on neostigmine.
- **Congenital myasthenia refractory to acetylcholinesterase inhibitors:** This prediction contradicts the drug's mechanism.
- **Hypersplenism and atypical hemolytic-uremic syndrome:** These have no evident mechanistic link.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action data from DrugBank
- Approved indication and dosage form details for the Canadian licenses, to confirm the original use and route compatibility
- Clinical or observational evidence of neostigmine use in myasthenia gravis with thymic hyperplasia, for example from thymectomy cohorts
- A review of safety in special populations, such as neonates and patients with airway disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

