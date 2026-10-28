---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "QUETIAPINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "distal 17p13.3 microdeletion syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "trichotillomania", "syndromic myopia", "myopia 26, X-linked, female-limited"]
description: "Quetiapine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Not recorded in the local data"
---

# Quetiapine
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

## Quetiapine: Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Quetiapine is an atypical antipsychotic originally used for schizophrenia and bipolar disorder (including manic episodes).
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but it has **no clinical trials and no publications** behind it.
The best-supported prediction among the top 10 is **trichotillomania**, with **0 clinical trials** and **6 publications**, all case reports or reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 for the rank 1 prediction; L4 for trichotillomania |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold (retinal dystrophy); Hold, with trichotillomania as a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Quetiapine is known as an atypical antipsychotic that blocks dopamine D2 and serotonin 5-HT2A receptors, with additional histamine H1 and alpha-1 adrenergic blockade. This is general pharmacology and was not part of the data compiled here.

**Retinal dystrophy (rank 1):** No plausible link was identified between quetiapine's receptor pharmacology and the genetic basis of inherited retinal dystrophy. The high score is a computational output only. The other top-10 predictions are also unsupported by any trials or literature. They include rare genetic or developmental conditions such as congenital glycosylation disorders, hydranencephaly, a chromosomal microdeletion syndrome, a polymicrogyria syndrome, several forms of myopia, and a demyelinating neuropathy. An antipsychotic is not expected to modify the underlying pathology of any of these.

**Trichotillomania (rank 8):** This is the only prediction with a credible rationale. Trichotillomania is a hair-pulling disorder on the obsessive-compulsive spectrum, with dopaminergic and serotonergic involvement. Quetiapine's D2 and 5-HT2A antagonism is consistent with how antipsychotics are used as augmentation in obsessive-compulsive disorder. It also shares a psychiatric treatment setting with the original indications. The supporting evidence is thin, and one report describes quetiapine exacerbating obsessive-compulsive symptoms, so the direction of effect is not settled.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the rank 1 prediction or trichotillomania.

---

## Literature Evidence

No literature is available for retinal dystrophy. The following publications relate to trichotillomania. Study types are inferred from titles and the abstracts available, so they should be verified against the full texts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review with case report | Psychiatry | Overview of trichotillomania treatment; a 33-year-old female veteran showed a favourable response to quetiapine |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report/series | Revista Brasileira de Psiquiatria | Quetiapine for the treatment of trichotillomania (no abstract available) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report and review | J Psychiatry Neurosci | Quetiapine exacerbated obsessive-compulsive symptoms in a patient with OCD and trichotillomania; reviews antipsychotic-induced OCS |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Reviews pharmacological treatment of trichotillomania; notes there are no treatment guidelines and the cause is unknown |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case report and review | Psychosomatics | Treatment of recurrent Rapunzel syndrome and trichotillomania |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; not specific to quetiapine |

---

## Canada Market Information

Quetiapine has 20 valid single-ingredient licences in Canada. Dosage form and approved indication text were not available in the compiled records.

| DIN | Product Name |
|---------|------|
| 02296594 | PMS-QUETIAPINE |
| 02244107 | SEROQUEL |
| 02317893 | QUETIAPINE |
| 02321513 | SEROQUEL XR |
| 02317370 | PRO-QUETIAPINE |

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for these.

**Contraindication-related conditions (from knowledge-graph data, not label text):** The data flag conditions in which quetiapine may be a concern, including:
- Cardiovascular: long QT syndrome, torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypertension, myocardial infarction
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity, hypothyroidism, potassium deficiency
- Haematological: neutropenia, agranulocytosis
- Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal dystonia, blepharospasm
- Other: liver disease, gallbladder disease, female breast carcinoma

**Drug interactions:** The interaction screen returned 100 interactions, most of them moderate. The two major interactions in the displayed sample are:
- **Bupropion** (Major)
- **Morphine** (Major)

Moderate interactions in the sample include:
- Antidiabetic drugs: metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide
- Anticholinergic drugs: atropine, hyoscyamine, glycopyrronium, clidinium
- Other: epinephrine, dexamethasone, famotidine, loperamide, aprepitant, lorcaserin, bisacodyl

The metabolic and sedation risks are relevant for any trichotillomania use, since patients would likely be treated long term.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (retinal dystrophy) and the other eight predictions without evidence rest on model scores alone, with no trials, no literature, and no plausible mechanism (evidence level L5).
- Trichotillomania has a plausible mechanism and a handful of case reports and reviews (L4), but nothing controlled. It should be treated as a research question, not a recommendation.

**To proceed, the following is needed:**
- Mechanism of action data for quetiapine
- Package insert warnings and contraindications from Health Canada
- For trichotillomania: a controlled trial, or at least a systematic review of quetiapine use, weighing benefit against metabolic and sedation risks, and clarifying the report of worsened obsessive-compulsive symptoms
- For retinal dystrophy and the other L5 predictions: a mechanistic rationale before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

