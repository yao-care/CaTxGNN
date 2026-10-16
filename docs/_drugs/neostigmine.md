---
layout: default
title: Neostigmine
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Neostigmine: predicted new indication Myasthenia gravis with thymus hyperplasia (evidence level L5). Approved use: Myasthenia gravis"
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

# Neostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Neostigmine is a cholinesterase inhibitor originally used to treat myasthenia gravis and related neuromuscular junction disease.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**, but **no clinical trials and no publications** specific to this subtype were found, so the prediction rests on the model score and its closeness to the already-established indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myasthenia gravis (also adult-onset myasthenia gravis and neuromuscular junction disease, per the knowledge graph) |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Neostigmine is a reversible acetylcholinesterase inhibitor. By slowing the breakdown of acetylcholine, it raises acetylcholine levels at the neuromuscular junction. This is the established symptomatic mechanism in myasthenia gravis. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from general pharmacology.

Myasthenia gravis with thymus hyperplasia is a subtype of the disease for which neostigmine is already used. The high prediction score therefore mostly reflects how close this subtype is to the original indication, not new evidence. The mechanism is plausible, but a repurposing claim cannot be built on it alone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The other predicted indications do have some literature, but it is mostly indirect:

- **Myasthenia, limb-girdle, autoimmune (L4):** one 2016 review on unusual MG presentations, with no neostigmine efficacy data.
- **Autoimmune disease of the peripheral nervous system (L4):** mainly MG mechanism studies, animal models and drug-interaction reports, with no controlled trials.
- **Neonatal myasthenia gravis (L4):** several case reports and a 2025 treatment review, with no controlled trials. This is the only prediction advanced to the next screening stage, as a research question.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230592 | NEOSTIGMINE OMEGA | Not specified | Not specified |
| 02475480 | NEOSTIGMINE METHYLSULFATE INJECTION USP | Not specified | Not specified |
| 02475499 | NEOSTIGMINE METHYLSULFATE INJECTION USP | Not specified | Not specified |
| 02387166 | NEOSTIGMINE OMEGA | Not specified | Not specified |
| 02230593 | NEOSTIGMINE OMEGA | Not specified | Not specified |

Six valid single-ingredient licences are held in total. Only five are shown here. The sixth is NEOSTIGMINE METHYLSULFATE INJECTION, USP (DIN 02537516).

## Safety Considerations

**Contraindication signals from the knowledge graph** (not taken from label text): epilepsy, peptic ulcer disease, asthma (intrinsic and allergic), sudden cardiac arrest, heart conduction disease, peritonitis, hyperthyroidism (including Graves disease and thyrotoxicosis), urinary tract obstruction, and Hirschsprung disease and related syndromes (including Mowat-Wilson syndrome).

**Drug Interactions:** 47 interactions were found in total. The one rated **Major** is **bupropion**. Many are rated **Moderate**, including:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- Anticholinergics and antispasmodics: atropine, hyoscyamine, methscopolamine, glycopyrronium, dicyclomine, clidinium, trospium, mepenzolate
- Aminoglycosides: kanamycin, neomycin, paromomycin
- Bowel preparations: picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes

Other points from the predicted-indication review:
- Bronchitis: cholinesterase inhibition may increase bronchial secretions and bronchoconstriction, so this is a potential harm.
- Congenital myasthenia refractory to cholinesterase inhibitors: some subtypes may worsen with this class of drug.
- Fetal akinesia deformation sequence: fetal or prenatal use would raise substantial safety concerns.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no trial or literature support. It is a subtype of a disease for which neostigmine is already established, so the high score adds little new information. The other predictions are either indirect (L4) or unsupported and potentially harmful (bronchitis, refractory congenital myasthenia).

**To proceed, the following is needed:**
- Subtype-specific clinical evidence for myasthenia gravis with thymus hyperplasia, for example registry or observational data on neostigmine use
- Approved indication text, dosage forms and package insert warnings and contraindications for the Canadian products
- Mechanism-of-action data from DrugBank
- For neonatal myasthenia gravis, the only prediction advanced as a research question: a dosing and safety evaluation in neonates
- A review of the major bupropion interaction and the knowledge-graph contraindication signals before any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

