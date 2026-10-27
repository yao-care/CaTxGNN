---
layout: default
title: Naratriptan
parent: Moderate Evidence (L3-L4)
nav_order: 643
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-13
description: "Naratriptan: predicted new indication Migraine with brainstem aura (evidence level L3). Approved use: Migraine disorder (migraine with or without aura)"
monitor_inn: "NARATRIPTAN"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Naratriptan
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
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

## Naratriptan: From Migraine to Migraine with Brainstem Aura
{: .text-alpha }

## One-Sentence Summary

Naratriptan is a triptan originally used to treat migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
but there are currently **no registered clinical trials** and only **20 publications** of general migraine literature (mostly indirect for this subtype) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (migraine with or without aura) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known information, naratriptan is a selective 5-HT1B/1D receptor agonist from the triptan class. Its efficacy in acute migraine is established, and mechanistically it may be applicable to migraine with brainstem aura.

Migraine with brainstem aura is a subtype of migraine with aura, so it shares the trigeminovascular pathophysiology that triptans target: cranial vasoconstriction and inhibition of CGRP and other neuropeptide release. The very high TxGNN score fits this close biological overlap with the approved indication.

There is an important caution. Triptans have historically been treated with care in migraine with brainstem aura (formerly basilar-type migraine) because of theoretical vascular risk. The retrieved literature does not address this subtype specifically, so the supporting evidence is indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below are general migraine and naratriptan studies. None of them targets migraine with brainstem aura directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized, double-blind crossover comparison of headache recurrence with naratriptan vs sumatriptan in recurrence-prone patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Naratriptan given during the prodrome to prevent migraine headache |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT (randomized, double-blind, placebo-controlled) | Headache | Naratriptan 1 mg and 2.5 mg twice daily as short-term prophylaxis of menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies in adults |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Sumatriptan was less effective in migraine with aura than without aura |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review | Headache | Managing intractable migraine with naratriptan |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Treatment during the premonitory phase of migraine as a possible management strategy |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open-label pilot study | Neurological Sciences | Naratriptan as short-term prophylaxis of pure menstrual migraine |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatric Drugs | Use of triptans for pediatric migraine |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of hormonal causes, prophylaxis and treatment of menstrual migraine |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02314290 | TEVA-NARATRIPTAN | Not specified | Not specified |
| 02314304 | TEVA-NARATRIPTAN | Not specified | Not specified |
| 02322323 | SANDOZ NARATRIPTAN | Not specified | Not specified |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph links naratriptan to contraindications in the following conditions:
  - Cardiovascular: hypertension, coronary artery disease, myocardial infarction, myocardial ischemia, Prinzmetal angina, peripheral vascular disease, peripheral arterial disease, intermittent vascular claudication
  - Cerebrovascular: stroke, cerebral infarction, transient ischemic attack, vertebrobasilar insufficiency, familial or sporadic hemiplegic migraine
  - Metabolic and other: liver failure, diabetes mellitus, diabetic ketoacidosis, obesity, hemoglobinopathy
- **Drug Interactions**: 39 interactions were identified in total. Among those listed, the **Major** interactions are:
  - Serotonergic or weight-loss agents: lorcaserin, dexfenfluramine, fenfluramine, sibutramine
  - 5-HT3 antagonists: dolasetron, palonosetron, granisetron, ondansetron
  - Methylene blue

  Moderate interactions include morphine (including liposomal morphine). Interactions with unknown severity include lansoprazole, pantoprazole, omeprazole, prednisone, ranitidine, clarithromycin, bupropion, budesonide and promethazine.

The vertebrobasilar insufficiency, stroke and hemiplegic migraine contraindications are especially relevant to brainstem aura. Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high and the pathophysiology overlaps closely with approved migraine use. However, there are no registered trials, the literature does not address this subtype, and the knowledge graph flags vascular and cerebrovascular contraindications that bear directly on brainstem aura. The finding is best treated as a research question rather than an actionable indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Subtype-specific evidence on triptan safety and efficacy in migraine with brainstem aura
- A cardiovascular and cerebrovascular risk assessment and exclusion criteria for any proposed study

*Note: The lower-ranked predictions, atrophoderma vermiculata and ulerythema ophryogenesis, have no clinical trials, no literature and no plausible mechanistic link. They are likely knowledge-graph artifacts and were not evaluated further.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

