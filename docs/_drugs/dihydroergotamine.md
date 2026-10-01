---
layout: default
title: Dihydroergotamine
parent: Model Prediction Only (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
---

# Dihydroergotamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Dihydroergotamine: From Migraine (General) to Migraine with Brainstem Aura

## One-Sentence Summary

Dihydroergotamine (DHE) is an ergot derivative used for decades in the acute treatment of migraine, so migraine is taken here as its original indication (Canadian licence data does not state one).
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are currently **0 registered clinical trials** and no publications specific to this subtype. The **20 publications** found are mostly general migraine reviews, and one directly relevant paper notes that DHE is contraindicated in this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, inferred from the literature; not stated in the Canadian licence data |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L4 (no trials, no subtype-specific studies; mechanistic plausibility only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed drug-specific mechanism of action data is not available in the provided data. General pharmacology describes DHE as an agonist at 5-HT1B/1D receptors, with additional activity at adrenergic and dopaminergic receptors. Its acute antimigraine effect is thought to come from cranial vasoconstriction and inhibition of neuropeptide release from the trigeminovascular system.

Migraine with brainstem aura is a subtype of migraine, so a link to a drug with established acute migraine efficacy is biologically plausible. The very high TxGNN score most likely reflects DHE's strong general association with migraine, not evidence specific to this subtype.

The same vasoconstrictive activity is also the main concern. A 2010 paper on DHE in migraine with posterior fossa symptoms (PMID 20533960) states that DHE has long been contraindicated in hemiplegic and basilar-type migraine. This prediction therefore carries a safety conflict as well as a potential benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below tests DHE specifically in migraine with brainstem aura. Study types are taken from the pack's classification or inferred from titles and abstracts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20533960](https://pubmed.ncbi.nlm.nih.gov/20533960/) | 2010 | Review / case-based report | Headache | Most directly relevant paper. Discusses DHE in migraine with posterior fossa symptoms and notes it is contraindicated in hemiplegic and basilar-type migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence assessment / guideline | Headache | American Headache Society update on the evidence for acute migraine drugs in adults |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | Headache | Rescue therapy for acute migraine (triptans, DHE, magnesium) in emergency, urgent care and headache clinic settings |
| [39373843](https://pubmed.ncbi.nlm.nih.gov/39373843/) | 2024 | Phase 3 open-label study | CNS Drugs | 12-month safety and tolerability of STS101 (DHE nasal powder) for acute migraine |
| [11903525](https://pubmed.ncbi.nlm.nih.gov/11903525/) | 2001 | Comparative trial | Headache | IV valproate compared with IM metoclopramide followed by IM DHE 1 mg in acute migraine with or without aura |
| [8262792](https://pubmed.ncbi.nlm.nih.gov/8262792/) | 1993 | Open-design field trial | Headache | Office-based DHE mesylate (D.H.E. 45) in 311 patients with migraine with or without aura |
| [27837002](https://pubmed.ncbi.nlm.nih.gov/27837002/) | 2016 | Safety study | Neurology | Safety of domperidone for nausea associated with DHE infusion and headache |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus as a complication of migraine with or without aura |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Observational / post hoc analysis | Neurology | Sumatriptan is less effective in migraine with aura than without aura (not DHE-specific) |
| [31213753](https://pubmed.ncbi.nlm.nih.gov/31213753/) | 2018 | Double-blind comparative trial | Hippokratia | Ergotamine-based combination vs sumatriptan in migraine without aura (not DHE-specific) |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2228947 | MIGRANAL NASAL SPRAY 4MG/ML |
| 27243 | DIHYDROERGOTAMINE (DHE), 1MG/ML |

Dosage form and approved indication text are not available in the provided licence data.

---

## Safety Considerations

- **Key Warnings and Contraindications**: The literature (PMID 20533960) reports that DHE has long been contraindicated in hemiplegic migraine and basilar-type migraine. This directly overlaps with the predicted indication and should be checked against the current Canadian label.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on general pharmacology and a high model score, with no clinical trials and no subtype-specific studies. The historical contraindication in basilar-type and hemiplegic migraine conflicts directly with the predicted use.

**To proceed, the following is needed:**
- The current Health Canada product monograph (warnings and contraindications) for both DINs, to confirm whether brainstem-aura or basilar-type migraine is contraindicated
- Drug-specific mechanism of action data (MOA)
- Approved indication text and dosage forms for the two DINs
- Subtype-specific clinical evidence and a cardiovascular and cerebrovascular safety assessment for patients with brainstem aura
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

