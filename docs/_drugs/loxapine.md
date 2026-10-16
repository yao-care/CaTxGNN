---
layout: default
title: Loxapine
parent: Model Prediction Only (L5)
nav_order: 564
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Loxapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Bipolar disorder, major affective disorder, schizophrenia"
monitor_inn: "LOXAPINE"
predicted_indications: ["manic bipolar affective disorder", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "congenital disorder of glycosylation with defective fucosylation", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "atypical glycine encephalopathy"]
---

# Loxapine
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

# Loxapine: From Schizophrenia and Bipolar Disorder to Manic Bipolar Affective Disorder

## One-Sentence Summary

Loxapine is a first-generation antipsychotic originally used for schizophrenia, bipolar disorder and major affective disorder.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **no registered clinical trials** but **20 publications** (mostly reviews) currently supporting this direction, largely around inhaled loxapine for agitation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder, major affective disorder, schizophrenia (from the knowledge-graph indication list; the Canadian licence records contain no indication text) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (strictly by the rules: no clinical trials and no completed RCTs in the data compiled; the supplied literature consists of reviews, which would suggest L3 at most) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, loxapine is a dibenzoxazepine antipsychotic that blocks dopamine D2 and serotonin 5-HT2A receptors. This mechanism is consistent with controlling mania and agitation. This mechanistic reasoning is inferred from class knowledge, not from the supplied data.

Bipolar disorder is already among loxapine's original indications, so the predicted indication (the manic phase of bipolar disorder) is closely related to what the drug is already used for. The literature also describes inhaled loxapine (Adasuve) as approved in the USA and EU for acute agitation associated with bipolar I disorder or schizophrenia. Two Phase III randomised controlled trials of this formulation are discussed in the literature, but they are not registered in the data compiled here.

The other nine predictions for this drug (for example retinal dystrophy, hydranencephaly, X-linked myopia, and several congenital or metabolic disorders) have high model scores but no trials, no literature and no plausible mechanistic link. They are rated L5 / Hold and are not pursued in this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic review / meta-analysis | Human Psychopharmacology | Evaluates short-term drug treatments for agitation in schizophrenia or bipolar disorder |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | Review of 2 Phase III RCTs | Int J Clin Pract | Effect sizes of inhaled loxapine for agitation in schizophrenia or bipolar disorder |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | Inhaled loxapine approved in the USA and EU for acute agitation in bipolar disorder or schizophrenia; two randomised, double-blind, placebo-controlled trials |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based options for managing a manic episode, including choice of mood stabiliser and antipsychotic |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatr Dis Treat | Safety, efficacy and patient acceptability of inhaled loxapine for acute agitation |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Review | Drugs in R&D | Expert review of inhaled loxapine for acute agitation in bipolar disorder and schizophrenia |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Review | Expert Opin Pharmacother | Improving drug treatment of agitation in bipolar disorder; few approved agents exist |
| [38301034](https://pubmed.ncbi.nlm.nih.gov/38301034/) | 2024 | Review | Prim Care Companion CNS Disord | Alternative approaches to acute agitation in schizophrenia and bipolar disorder |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Review | Expert Rev Neurother | Fifty years of experience with loxapine for rapid non-coercive tranquilisation in acute behavioural disturbances |
| [15568205](https://pubmed.ncbi.nlm.nih.gov/15568205/) | 2005 | Review | Human Psychopharmacology | Treatment of acute mania from clinical trials to practice recommendations |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02169991 | LOXAPAC IM | Not listed | Not listed |
| 02230838 | XYLAC | Not listed | Not listed |
| 02230839 | XYLAC | Not listed | Not listed |
| 02242868 | XYLAC | Not listed | Not listed |

## Cytotoxicity

Not applicable. Loxapine is an antipsychotic, not an antineoplastic drug.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** epilepsy, benign prostatic hyperplasia, substance abuse/dependence, female breast carcinoma, cardiovascular disease, heart disease, glaucoma, neuroleptic malignant syndrome, Alzheimer disease, tardive dyskinesia, lingual-facial-buccal dyskinesia, and hyperprolactinemia (including familial and acquired forms and prolactin-producing pituitary tumour).
- **Drug interactions:** 100 interactions were recorded; 20 are listed in the data compiled for this report. Major-level interactions include **bupropion, morphine and potassium citrate**. Moderate-level interactions include epinephrine, several anticholinergics (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate), loperamide, lorcaserin, dronabinol, nabilone, eluxadoline, and some bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Label warnings and contraindications from the Health Canada product monograph were not available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Loxapine is already used in bipolar disorder and is mechanistically consistent with treating mania and agitation. Literature on inhaled loxapine supports the direction, and the drug is marketed in Canada. However, there are no registered trials in the data compiled, the supplied literature is mostly review articles, and the label safety data are missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Dosage form, route and approved indication details for the four Canadian DINs, and confirmation of whether an inhaled formulation is authorised in Canada
- Primary RCT data for mania specifically, as distinct from agitation
- A safety monitoring plan covering the knowledge-graph contraindications and the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

