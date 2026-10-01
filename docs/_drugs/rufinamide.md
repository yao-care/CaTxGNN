---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 821
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Rufinamide: From Seizure Disorders to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide is marketed in Canada, and the supplied record does not list its approved indication. It is generally known as an anti-seizure drug.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it so far.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record (generally known as an anti-seizure drug) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Rufinamide is generally known as a sodium-channel modulator used as an anti-seizure drug. This is background knowledge, not from the supplied data. Its efficacy in its marketed seizure indication would make refractory seizures a plausible target. The prediction likely comes from rufinamide's position among other epilepsy drugs in the knowledge graph.

FIRES is a severe epilepsy syndrome with refractory seizures. It is thought to be driven by neuroinflammation, so a sodium-channel mechanism alone may not address the core disease process. The mechanistic link is therefore uncertain and unverified.

Four other epilepsy-related predictions also scored above 99.4%: perioral myoclonia with absences, atypical childhood epilepsy with centrotemporal spikes, cryptogenic late-onset epileptic spasms, and photosensitive occipital lobe epilepsy. All are L5 with no clinical evidence. Sodium-channel blockers can aggravate some absence-type syndromes, so the plausibility of at least one of these predictions is also uncertain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2369613 | BANZEL |
| 2369621 | BANZEL |
| 2369648 | BANZEL |
| 2545985 | AURO-RUFINAMIDE |
| 2545993 | AURO-RUFINAMIDE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. There are no registered trials, no literature, and no mechanism data. FIRES is likely driven by neuroinflammation, which a sodium-channel mechanism may not address. The Canadian safety documentation has not been reviewed, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert (approved indication, warnings, contraindications), the blocking gap for safety screening
- Mechanism of action data, for example from the DrugBank API
- A search for case reports, case series, or registry data on rufinamide in FIRES or other refractory epilepsy syndromes
- Assessment of formulation and route suitability for the target patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

