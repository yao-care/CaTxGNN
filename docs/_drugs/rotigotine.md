---
layout: default
title: Rotigotine
parent: Model Prediction Only (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "ROTIGOTINE"
predicted_indications: ["attention deficit-hyperactivity disorder", "schizophrenia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "faciodigitogenital syndrome", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "atypical glycine encephalopathy", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited"]
description: "Rotigotine: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Rotigotine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Rotigotine: Attention deficit-hyperactivity disorder
{: .text-alpha }

## One-Sentence Summary

Rotigotine is a dopamine agonist originally used to treat Parkinson disease and restless legs syndrome.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**,
but there are currently **no registered clinical trials** and only **3 publications** (none of which tested rotigotine in ADHD), so this is a research question rather than an evidence-backed indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 (preclinical/mechanistic literature only) |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, rotigotine is a dopamine receptor agonist with highest affinity at D3, D2 and D1 receptors, and it also has some activity at 5-HT1A and alpha2B adrenergic receptors.

ADHD is associated with dopaminergic and noradrenergic dysregulation, so a link exists, but it is indirect. Restless legs syndrome, one of rotigotine's original indications, is often seen together with ADHD in children and shares a dopaminergic basis. A 2021 study of how the dopamine D4 receptor and the alpha2A adrenoceptor interact also relates to ADHD receptor biology.

There is an important caveat. Established ADHD treatments work by increasing dopamine and norepinephrine signalling, and direct D2/D3 agonism is not an established ADHD strategy. No study has evaluated rotigotine in ADHD.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Review of pharmacological options for restless legs syndrome in children, a condition often seen with ADHD |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General review of restless legs syndrome (symptoms, prevalence of 2–3% in Western countries, diagnostic criteria) |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical/Mechanistic | Pharmacological Research | Dopamine D4 receptor variants and α2A adrenoceptor form heteromers with different pharmacology; relevant to ADHD and impulse-control disorders |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02403927 | NEUPRO | Not listed | Not listed |
| 02403897 | NEUPRO | Not listed | Not listed |
| 02403919 | NEUPRO | Not listed | Not listed |
| 02403900 | NEUPRO | Not listed | Not listed |
| 02403943 | NEUPRO | Not listed | Not listed |

(5 of 6 valid single-ingredient authorizations shown; the sixth is DIN 02403935, also NEUPRO.)

---

## Safety Considerations

**Contraindication-related conditions from the knowledge graph** (these come from drug-disease relationship data, not from label text):
- Hypertensive disorder / hypertension
- Multiple system atrophy
- Postural orthostatic tachycardia syndrome
- Orthostatic hypotension
- Drug-induced dyskinesia

**Drug Interactions:** 51 interactions were found in total. The 20 listed in the compiled data are all of Moderate level. Main ones include:
- Opioids and related agents: morphine (including liposomal), codeine, opium, diphenoxylate, difenoxin
- Sedating antihistamines: promethazine, chlorpheniramine, cetirizine, brompheniramine, carbinoxamine, clemastine, nasal azelastine
- Cannabinoids: dronabinol, nabilone
- Others: metoclopramide, ethanol, sibutramine, dextromethorphan, ioflupane I-123

Please refer to the package insert for the full warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction rests on a high model score and an indirect dopaminergic link. There are no clinical trials, and no study has tested rotigotine in ADHD. Direct D2/D3 agonism is also not an established ADHD approach. The package insert safety data are missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking data gap)
- Detailed mechanism of action data from DrugBank
- Preclinical or early-phase clinical evidence of rotigotine in ADHD or ADHD-related models
- A review of cardiovascular and orthostatic risks, given the hypertension- and hypotension-related contraindications, in a younger ADHD population
- Approved indication text and dosage form for the Canadian NEUPRO authorizations

**Note on other predictions:** The other nine predicted indications are weaker. Schizophrenia (rank 2, Hold) is largely opposed to rotigotine's mechanism, since dopamine agonists can worsen psychosis. The remaining eight (ranks 3–10) have no supporting trials or literature and are model predictions only (L5).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

