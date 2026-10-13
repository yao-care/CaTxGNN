---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

## One-Sentence Summary

Amifampridine was originally used to treat Lambert-Eaton myasthenic syndrome (LEMS), a rare neuromuscular disorder.
The TxGNN model predicts it may be effective for **glaucoma**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a computational prediction only, with no direct evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, amifampridine is a voltage-gated potassium channel blocker. It prolongs presynaptic depolarization and increases neurotransmitter release at the neuromuscular junction, which is why it works in LEMS.

For glaucoma, no clear link has been established. Glaucoma involves raised intraocular pressure and loss of retinal ganglion cells, and neither is known to be influenced by presynaptic potassium channel blockade. The high TxGNN score (99.71%) should be read as a computational signal from a knowledge graph, not as evidence of biological plausibility.

Other predictions in the list show a similar pattern. Several (acute intermittent porphyria, porphyria, esophageal varices, varicose disease, and p14-deficiency immunodeficiency) have no apparent mechanistic connection and are likely graph-based artifacts. The paraneoplastic neurological conditions (limbic encephalitis, polyneuropathy, cerebellar degeneration) are more biologically plausible. They share paraneoplastic autoimmunity with LEMS and are flagged as research questions. Even for these, benefit is speculative and no clinical data were provided.

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
| 02502984 | FIRDAPSE | Not specified | Not specified |
| 02503034 | RUZURGI | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions**: 68 potential interactions were identified in the interaction database. The list below shows the first 20 of the 68 entries, with the one Major interaction highlighted.

- **Major**: Bupropion
- **Moderate**: hydrocortisone, betamethasone, dexamethasone, prednisolone, prednisone, dexfenfluramine, diethylpropion, dronabinol, ephedrine, fenfluramine, levofloxacin, mazindol, metoclopramide, morphine (including liposomal), opium, phentermine, polyethylene glycol (3350 with electrolytes), sibutramine

**Other concerns noted in the analysis**: Amifampridine may lower the seizure threshold. This matters most in conditions where seizures already occur, such as porphyria and limbic encephalitis.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanistic link to amifampridine's action on neuromuscular transmission. Evidence is at level L5.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to glaucoma
- Preclinical or mechanistic studies showing an effect on intraocular pressure or retinal ganglion cell survival
- Package insert warnings and contraindications from Health Canada, including seizure risk
- Consideration of the paraneoplastic neurological predictions (limbic encephalitis, polyneuropathy, cerebellar degeneration) as better-grounded research questions, given their shared autoimmune basis with LEMS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

