---
layout: default
title: Desipramine
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 8
monitor_inn: "Desipramine"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "attention deficit-hyperactivity disorder", "specific developmental disorder", "chondromyxoid fibroma", "faciodigitogenital syndrome", "benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder"]
last_modified_at: 2026-11-24
description: "Desipramine: predicted new indication attention deficit hyperactivity disorder, inattentive type (evidence level L5). In Canada: 5 DINs (5 marketed)"
---

# Desipramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Desipramine: Tricyclic antidepressant (norepinephrine reuptake inhibitor) → attention deficit hyperactivity disorder, inattentive type
{: .text-alpha }

## One-Sentence Summary

Desipramine is a tricyclic antidepressant with strong norepinephrine reuptake inhibition, and it is currently marketed in Canada.
The TxGNN model predicts it may be useful for **attention deficit hyperactivity disorder, inattentive type**.
**No clinical trials and no publications** directly studying this disease were found, so the prediction rests on the model score and a plausible mechanism only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for desipramine: "Available evidence suggests that many depressions have a biochemical basis in the form of a relative deficiency of neurotransmitters such as norepinephrine and serotonin. Norepinephrine deficiency may be associated with relatively low urinary 3-methoxy-4-hydroxyphenyl glycol (MHPG) levels, while serotonin deficiencies may be associated with low spinal fluid levels of 5-hydroxyindoleacetic acid." ([DailyMed: Norpramin (desipramine hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=70b562ea-9f21-4e4a-b3ed-0590b2892f6a), label version 2025-07-03; accessed 2026-11-19.) Desipramine is, however, a tricyclic antidepressant known for strong norepinephrine reuptake inhibition. Boosting noradrenergic signalling in prefrontal circuits plausibly supports attention. This is the same general mechanism as atomoxetine, a non-stimulant norepinephrine reuptake inhibitor used for ADHD. It fits the high model score.

This is a mechanistic argument only. No trial or publication specific to the inattentive subtype was retrieved. The plausibility therefore remains unverified, and the evidence level is L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02216248 | DESIPRAMINE | DESIPRAMINE HYDROCHLORIDE | Marketed |
| 02216256 | DESIPRAMINE | DESIPRAMINE HYDROCHLORIDE | Marketed |
| 02216264 | DESIPRAMINE | DESIPRAMINE HYDROCHLORIDE | Marketed |
| 02216272 | DESIPRAMINE | DESIPRAMINE HYDROCHLORIDE | Marketed |
| 02216280 | DESIPRAMINE | DESIPRAMINE HYDROCHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Desipramine is currently marketed in Canada. All of its Health Canada licences in the data compiled for this report are valid single-ingredient licences. The licence records carry no indication or dosage-form text.

---

## Safety Considerations

- **Drug Interactions**: Screening found 100 recorded interactions. Major-level interactions include:
  - epinephrine
  - bupropion
  - lorcaserin
  - potassium citrate
  - cisapride
  - dexfenfluramine

  Many other interactions are rated moderate, including anticholinergic agents such as atropine, hyoscyamine and glycopyrronium, as well as famotidine, cimetidine, clarithromycin and morphine.
- **Cardiovascular concern**: Tricyclic antidepressants carry cardiac risks, and reports of sudden death in children treated with desipramine have been noted. Cardiac safety would need careful assessment in any ADHD use, especially in young patients.
- **Metabolism**: The interaction burden is notably related to CYP2D6 metabolism.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high. However, there are no trials or publications for this specific subtype (evidence level L5), and the cardiovascular and interaction risks are significant.

**To proceed, the following is needed:**
- Subtype-specific clinical or observational evidence for desipramine in inattentive-type ADHD
- Mechanism-of-action data
- Package insert warnings and contraindications from Health Canada
- A cardiac safety assessment, including paediatric risk, and a CYP2D6 interaction management plan

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Norpramin (desipramine hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=70b562ea-9f21-4e4a-b3ed-0590b2892f6a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

