---
layout: default
title: Sumatriptan
parent: Moderate Evidence (L3-L4)
nav_order: 874
evidence_level: L4
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a triptan originally used to treat migraine (with or without aura) and cluster headache.
The TxGNN model predicts it may be useful for **migraine with brainstem aura**,
but there are **no registered clinical trials** and only **18 publications** (mostly general migraine reviews, not specific to this subtype). This is a subtype of an already-labelled condition, not a truly new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder, migraine with or without aura, cluster headache, paroxysmal hemicrania, hemicrania continua (from the knowledge graph; no approved-indication text is available for the Canadian licences) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, sumatriptan is a 5-HT1B/1D receptor agonist. It is thought to relieve migraine by constricting cranial blood vessels and by inhibiting the release of CGRP and other neuropeptides from trigeminal nerve endings.

Migraine with brainstem aura is a clinical subtype of migraine with aura, so it shares the trigeminovascular pathophysiology that sumatriptan targets. The very high TxGNN score most likely reflects this close proximity to the approved migraine indications in the disease ontology, rather than a genuinely new mechanistic discovery.

There is an important caveat. Triptans have historically been used cautiously, or avoided, in brainstem aura (formerly basilar-type migraine) and hemiplegic migraine because of theoretical concerns about vasoconstriction. Evidence of actual harm is limited, but the concern means that the apparent "fit" of this prediction cannot be taken at face value.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below studies sumatriptan specifically in migraine with brainstem aura. They address migraine in general, migraine with aura, or other triptans.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review (evidence assessment / guideline) | Headache | American Headache Society evidence assessment of acute migraine drug therapies |
| [12917936](https://pubmed.ncbi.nlm.nih.gov/12917936/) | 2003 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Oral sumatriptan for acute migraine |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytother Res | Ginger vs sumatriptan in 100 patients with migraine without aura; not about brainstem aura |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200 mg in acute migraine with aura |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Study | Neurology | Reports reduced efficacy of sumatriptan in migraine with aura compared with migraine without aura |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Commentary | Neurology | Subcutaneous sumatriptan and the migraine aura |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of sumatriptan in migraine and cluster headache |
| [26628293](https://pubmed.ncbi.nlm.nih.gov/26628293/) | 2016 | Review | Drugs | Sumatriptan/naproxen sodium for acute migraine with or without aura |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus as a complication of migraine with or without aura |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | Zolmitriptan (a different triptan) in migraine |

---

## Canada Market Information

Twenty single-ingredient sumatriptan licences are valid in Canada, with no cancelled ones. Dosage form, manufacturer and approved-indication text are not available in the data compiled for this report. Five representative authorisations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02212188 | IMITREX | Not available | Not available |
| 02230418 | IMITREX | Not available | Not available |
| 02256428 | PMS-SUMATRIPTAN | Not available | Not available |
| 02268388 | APO-SUMATRIPTAN | Not available | Not available |
| 02268906 | MYLAN-SUMATRIPTAN | Not available | Not available |

---

## Safety Considerations

**Contraindication-related conditions from the knowledge graph** (these come from drug–disease contraindication links in the knowledge graph, not from package insert text):
- Cardiovascular: coronary artery disease, myocardial infarction, coronary thrombosis, heart disease, congestive heart failure, hypertension, peripheral vascular disease, intermittent claudication
- Cerebrovascular: stroke, cerebral infarction, cerebrovascular disorder
- Hepatic and renal: liver disease, liver failure, kidney disease
- Others: epilepsy, diabetes mellitus, diabetic ketoacidosis, obesity, blood coagulation disease, haemoglobinopathy, anaemia, gallbladder disease, substance abuse/dependence

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major**: dexfenfluramine, fenfluramine, lorcaserin, sibutramine (serotonergic agents); dolasetron, granisetron, ondansetron, palonosetron (5-HT3 antagonists)
- **Moderate**: morphine, liposomal morphine
- Several others have an unclassified severity level, including pantoprazole, omeprazole, lansoprazole, metformin, doxycycline and cimetidine.

Package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is a subtype of an indication sumatriptan already carries, so it is a research question rather than a new repurposing opportunity. The evidence is model-prediction level only (L4), with no trials or subtype-specific literature. The historical caution about triptans in brainstem aura, combined with the cardiovascular and cerebrovascular contraindication signals, argues against advancing without more data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Subtype-specific clinical evidence (trials or case series) on triptan use and safety in migraine with brainstem aura
- A clinical and regulatory review of whether the theoretical vasoconstriction concern applies to this subtype
- Approved-indication text and dosage forms for the Canadian licences, to confirm how the labels treat aura subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

