---
layout: default
title: Prochlorperazine
parent: Model Prediction Only (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Prochlorperazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "PROCHLORPERAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Prochlorperazine
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

## Prochlorperazine: From Schizophrenia to Retinal Dystrophy With or Without Extraocular Anomalies (Computational Prediction Only)
{: .text-alpha }

## One-Sentence Summary

Prochlorperazine is a phenothiazine antipsychotic, originally used for schizophrenia.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but **no clinical trials and no publications** support it, so it rests on model output alone.
The best-supported direction among the predictions is **manic bipolar affective disorder**, which has **7 publications** (mostly old case reports, reviews and safety reports) and no clinical trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (the Canadian licence records contain no approved indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, prochlorperazine is a phenothiazine that blocks dopamine D2 receptors. This is consistent with its use in schizophrenia.

For the top prediction, retinal dystrophy, no mechanistic link is established. The score is very high, but it is a purely computational output. D2 antagonism has no known relevance to inherited retinal degeneration. Phenothiazines also carry ocular adverse effects, so the risk-benefit is unfavourable without supporting evidence.

The other top-ranked predictions are similarly unsupported. These include hydranencephaly, a congenital disorder of glycosylation, X-linked and syndromic myopia, Charcot-Marie-Tooth disease type 1G, polymicrogyria and atypical glycine encephalopathy. Most are congenital or monogenic conditions that a D2 antagonist is not expected to change.

The one biologically plausible prediction is **manic bipolar affective disorder** (score 0.9998). It is close to the original psychiatric use, and antipsychotics of this class are used for mania and acute agitation. Even so, its support is limited to old case reports, surveys and safety papers. Modern guideline-endorsed agents are available.

## Clinical Trial Evidence

Currently no related clinical trials registered, for the top prediction or for manic bipolar affective disorder.

## Literature Evidence

No literature is available for the top prediction (retinal dystrophy). The table below covers the best-supported prediction, manic bipolar affective disorder.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | Journal of Psychiatric Practice | Use and safety of antipsychotic drugs during pregnancy, in the context of schizophrenia and related illness |
| [26819726](https://pubmed.ncbi.nlm.nih.gov/26819726/) | 2015 | Cohort | Journal of Pharmaceutical Health Care and Sciences | Analysis of spontaneous adverse event reports on hyperglycaemia with antipsychotics |
| [13617778](https://pubmed.ncbi.nlm.nih.gov/13617778/) | 1959 | Case report | Annales Médico-Psychologiques | Confusional dream-like attack caused by prochlorperazine in a mildly manic-depressive patient |
| [14242542](https://pubmed.ncbi.nlm.nih.gov/14242542/) | 1965 | Review | Obstetrics and Gynecology | Approach to severe psychological disorders of the puerperium |
| [14233737](https://pubmed.ncbi.nlm.nih.gov/14233737/) | 1964 | Review | American Journal of Psychiatry | Survey of electroshock therapy combined with phenothiazines and reserpine |
| [14062306](https://pubmed.ncbi.nlm.nih.gov/14062306/) | 1963 | Review | La Tunisie Médicale | Emergency management of agitation in general practice |
| [14222730](https://pubmed.ncbi.nlm.nih.gov/14222730/) | 1964 | Review | L'Encéphale | Psychodysleptic manifestations during treatment with psycholeptics |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00886432 | PROCHLORAZINE | Not specified | Not specified |
| 00789720 | ODAN-PROCHLORPERAZINE | Not specified | Not specified |
| 00886440 | PROCHLORAZINE | Not specified | Not specified |

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from knowledge-graph drug-disease edges, not from package insert text):
- Cardiovascular: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, long QT syndrome (including familial), torsades de pointes, coronary artery disease, myocardial infarction, coronary thrombosis
- Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Hepatic, renal and gastrointestinal: liver disease, gallbladder disease, kidney disease, pyoureter, gastric ulcer
- Metabolic and other: hyperglycaemia, obesity disorders (including monogenic obesity), benign prostatic hyperplasia, substance abuse/dependence, female breast carcinoma

**Drug Interactions:** 100 interactions were recorded. The 20 listed in the compiled data are mostly Moderate.
- **Major:** bupropion, potassium citrate
- **Moderate (examples):** metformin, pioglitazone, alogliptin, acarbose, chlorpropamide and canagliflozin (antidiabetics, with glycaemic effects); atropine, hyoscyamine and glycopyrronium (anticholinergics); morphine; epinephrine; clarithromycin; famotidine

Please refer to the package insert for label warnings and contraindications, which are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, retinal dystrophy, is a purely computational result with no trials, no literature and no mechanistic basis. All ranked predictions are L5, except manic bipolar affective disorder at L4, and that one is supported only by old reports and safety papers. Prochlorperazine also carries a substantial safety burden, including cardiac, neurological and ocular risks.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- For manic bipolar affective disorder, a structured review of the evidence against current guideline-endorsed agents, and a decision on whether it is worth pursuing as a research question
- For the retinal and congenital predictions, preclinical support for a mechanism before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

