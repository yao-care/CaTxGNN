---
layout: default
title: Neostigmine
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Neostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "bronchitis", "fetal akinesia deformation sequence", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors"]
description: "Neostigmine: predicted new indication Autoimmune disease of peripheral nervous system (evidence level L5). In Canada: 6 DINs (6 marketed)"
---

# Neostigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Neostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## One-Sentence Summary

Neostigmine is a cholinesterase inhibitor originally used to treat myasthenia gravis and related neuromuscular junction disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune disease of peripheral nervous system |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Neostigmine is a reversible acetylcholinesterase inhibitor. By slowing the breakdown of acetylcholine, it raises acetylcholine levels at the neuromuscular junction. This is the established symptomatic mechanism in myasthenia gravis. This description comes from general pharmacology. According to the Mechanism of Action section of the US FDA-approved prescribing information for neostigmine: "Neostigmine methylsulfate is a competitive cholinesterase inhibitor. By reducing the breakdown of acetylcholine, neostigmine methylsulfate induces an increase in acetylcholine in the synaptic cleft which competes for the same binding site as nondepolarizing neuromuscular blocking agents, and reverses the neuromuscular blockade." ([DailyMed: neostigmine prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=95fb1b3d-be9a-fdb4-e053-2a95a90a5e90), label version 2023-05-15; accessed 2026-11-19.)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The other predicted indications do have some literature, but it is mostly indirect:

- **Myasthenia, limb-girdle, autoimmune (L4):** one 2016 review on unusual MG presentations, with no neostigmine efficacy data.
- **Autoimmune disease of the peripheral nervous system (L4):** mainly MG mechanism studies, animal models and drug-interaction reports, with no controlled trials.
- **Neonatal myasthenia gravis (L4):** several case reports and a 2025 treatment review, with no controlled trials.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02230592 | NEOSTIGMINE OMEGA | NEOSTIGMINE METHYLSULFATE | Marketed |
| 02230593 | NEOSTIGMINE OMEGA | NEOSTIGMINE METHYLSULFATE | Marketed |
| 02387166 | NEOSTIGMINE OMEGA | NEOSTIGMINE METHYLSULFATE | Marketed |
| 02475480 | NEOSTIGMINE METHYLSULFATE INJECTION USP | NEOSTIGMINE METHYLSULFATE | Marketed |
| 02475499 | NEOSTIGMINE METHYLSULFATE INJECTION USP | NEOSTIGMINE METHYLSULFATE | Marketed |
| 02537516 | NEOSTIGMINE METHYLSULFATE INJECTION, USP | NEOSTIGMINE METHYLSULFATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Six valid single-ingredient licences are held in total. The sixth is NEOSTIGMINE METHYLSULFATE INJECTION, USP (DIN 02537516).

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
- For neonatal myasthenia gravis: a dosing and safety evaluation in neonates
- A review of the major bupropion interaction and the knowledge-graph contraindication signals before any new use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from general pharmacology" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: neostigmine prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=95fb1b3d-be9a-fdb4-e053-2a95a90a5e90) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

