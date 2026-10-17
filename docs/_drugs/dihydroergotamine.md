---
layout: default
title: Dihydroergotamine
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Dihydroergotamine: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder (also migraine with or without aura…"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Dihydroergotamine: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Dihydroergotamine (DHE) is an ergot-derived drug originally used to treat migraine and cluster headache.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
but the data compiled for this report show **no registered clinical trials** for this specific subtype and **20 publications** that mostly address migraine in general rather than this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (also migraine with or without aura, cluster headache, paroxysmal hemicrania, hemicrania continua) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L4 (no completed trials for this subtype; only general migraine literature and mechanistic reasoning) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, DHE is an ergot derivative that acts as an agonist at 5-HT1B/1D receptors, with additional activity at 5-HT1F, dopamine D2 and adrenergic receptors. Through cranial vasoconstriction and inhibition of trigeminal neuropeptide release (for example CGRP), it is thought to abort migraine attacks.

Migraine with brainstem aura shares the trigeminovascular pathophysiology of other migraine types. The prediction is therefore a subtype extension of an indication DHE already has. The high TxGNN score (0.994) is a computational result and probably reflects mostly the closeness of this subtype to the approved migraine indications.

There is an important caveat. DHE is a potent vasoconstrictor, and brainstem aura (formerly basilar-type migraine) has traditionally raised concern about vasoconstrictors because of possible posterior circulation ischemia. One publication in the data (PMID 20533960) notes that DHE is currently contraindicated in patients with hemiplegic migraine and basilar-type migraine, while discussing its use in migraine with posterior fossa symptoms. This tension is the main reason for caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications compiled are mostly reviews, guidelines and studies of general migraine populations. None specifically tests DHE in migraine with brainstem aura. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20533960](https://pubmed.ncbi.nlm.nih.gov/20533960/) | 2010 | Review / case series | Headache | DHE use in migraine with posterior fossa symptoms; notes DHE is labelled as contraindicated in hemiplegic and basilar-type migraine |
| [11903525](https://pubmed.ncbi.nlm.nih.gov/11903525/) | 2001 | RCT | Headache | IV valproate compared with IM metoclopramide plus DHE for acute migraine (general migraine population, not subtype-specific) |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine treatments |
| [19708964](https://pubmed.ncbi.nlm.nih.gov/19708964/) | 2009 | Guideline | European Journal of Neurology | EFNS guideline on drug treatment of migraine |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | Headache | Rescue therapy for acute migraine with triptans, DHE and magnesium |
| [8262792](https://pubmed.ncbi.nlm.nih.gov/8262792/) | 1993 | Open-label field trial | Headache | Office-based treatment of acute migraine with DHE mesylate in 311 patients |
| [39373843](https://pubmed.ncbi.nlm.nih.gov/39373843/) | 2024 | Phase 3 open-label | CNS Drugs | 12-month safety and tolerability of STS101 (DHE nasal powder) for acute migraine |
| [41186275](https://pubmed.ncbi.nlm.nih.gov/41186275/) | 2026 | Open-label study | Headache | Participant satisfaction with STS101 (DHE nasal powder) in the ASCEND study |
| [31213753](https://pubmed.ncbi.nlm.nih.gov/31213753/) | 2018 | Double-blind trial | Hippokratia | Ergotamine-based combination compared with sumatriptan in migraine without aura |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus as a complication of migraine with or without aura |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02228947 | MIGRANAL NASAL SPRAY 4MG/ML | Not specified | Not specified |
| 00027243 | DIHYDROERGOTAMINE (DHE), 1MG/ML | Not specified | Not specified |

---

## Safety Considerations

- **Disease-level contraindication signals (from the TxGNN knowledge graph, not label text)**: hypertension and hypertensive disorders, liver failure, porphyria (inherited porphyria and porphyrin metabolism disease), coronary artery disease, Prinzmetal angina, and peripheral vascular disease (including peripheral arterial disease and intermittent claudication).
- **Drug Interactions**: 100 interactions were identified. Major interactions include isometheptene, epinephrine (including ophthalmic and topical forms), ephedrine (including nasal), clarithromycin, lorcaserin, fenfluramine and dexfenfluramine. Moderate interactions include doxycycline, tetracycline, aprepitant, dexamethasone, cimetidine, clotrimazole, miconazole, eluxadoline, glycerol phenylbutyrate and metreleptin. Only the first 20 are shown in the compiled data.
- **Subtype-specific concern**: as noted above, vasoconstriction may raise concern for posterior circulation ischemia in brainstem aura.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, but there are no clinical trials and no subtype-specific studies. The literature also points to a potential safety conflict, because DHE has traditionally been contraindicated in basilar-type migraine, which is now classified as migraine with brainstem aura. The high TxGNN score mainly reflects its closeness to existing migraine indications and does not outweigh this concern. The evidence level is L4, and the data stage is a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap), including whether basilar-type or brainstem aura migraine is explicitly contraindicated
- Mechanism of action data from DrugBank
- Subtype-specific safety and efficacy evidence, with particular attention to posterior circulation ischemia risk
- Indication text, dosage form and route information for the two Canadian licences
- Review of the cardiovascular and hepatic contraindication signals and the major drug interactions in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

