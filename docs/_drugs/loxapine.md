---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Loxapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Loxapine: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Loxapine is a first-generation (typical) antipsychotic originally used to treat schizophrenia, with an inhaled formulation (Adasuve®) already approved abroad for acute agitation.
> The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
> a prediction reinforced by **20 supporting publications**, including pooled Phase III RCT data — though it is **not currently marketed in Canada**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (oral loxapine, first-generation/typical antipsychotic); inhaled formulation already approved in the US/EU for acute agitation |
| Predicted New Indication | Manic Bipolar Affective Disorder (acute agitation associated with bipolar mania) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action record for loxapine is currently a data gap in this evidence pack (DG002). However, the literature captured here consistently describes loxapine as a dibenzoxazepine-class, first-generation antipsychotic that acts primarily as a **D2 dopamine / 5-HT2A serotonin receptor antagonist** — the same mechanism shared by other agents used to control acute psychiatric agitation and mania.

The proposed new indication is not a distant extrapolation: an inhaled formulation of loxapine (Adasuve®, using the Staccato® delivery system) has already been approved in the **United States and European Union** specifically for the acute treatment of agitation associated with **schizophrenia or bipolar I disorder**. This means the "predicted" indication substantially overlaps with an already-established, regulator-approved use elsewhere — the TxGNN signal here reflects a real, mechanistically coherent extension rather than a purely speculative association.

Two Phase III randomized, placebo-controlled trials (referenced across multiple publications, e.g. NCT00628589 and NCT00721955) enrolled patients with either schizophrenia or bipolar I disorder experiencing acute agitation, and a head-to-head PLACID trial compared inhaled loxapine against intramuscular aripiprazole in the same population. This gives the bipolar-mania prediction a materially stronger evidence base than the other candidates in this evidence pack.

For transparency, nine additional TxGNN-predicted candidates (ranks 2–10, all scoring >99.8%) were also reviewed — including retinal dystrophy, hydranencephaly, X-linked myopia variants, a congenital glycosylation disorder, Charcot-Marie-Tooth type 1G, polymicrogyria, and atypical glycine encephalopathy. None have clinical trial or literature support, and none share a plausible mechanistic link to D2/5-HT2A antagonism (they are predominantly monogenic structural/metabolic disorders). All nine were scored **L5 / Hold** and are excluded from further evaluation in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in ClinicalTrials.gov or ICTRP for this specific drug–disease pair (structured trial records were not retrieved). Note: the Literature Evidence below discusses two pivotal Phase III RCTs (NCT00628589, NCT00721955) and the PLACID trial by publication, but these were not captured as discrete clinical-trial registry records in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | RCT (pooled analysis, 2 Phase III trials) | Int J Clin Pract | Pooled effect-size analysis of two pivotal Phase III RCTs of inhaled loxapine for agitation in schizophrenia/bipolar disorder |
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT | Eur Neuropsychopharmacol | PLACID trial: assessor-blind RCT comparing inhaled loxapine vs. IM aripiprazole in acutely agitated schizophrenia/bipolar I patients across 23 centres |
| [28376877](https://pubmed.ncbi.nlm.nih.gov/28376877/) | 2017 | RCT (protocol/design) | BMC Psychiatry | Study design paper for the PLACID randomized trial |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | RCT (responder analysis) | BJPsych Open | PANSS-EC responder analysis from two Phase III RCTs (344 schizophrenia, 314 bipolar I patients) |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review & Meta-analysis | Hum Psychopharmacol | Systematic review of short-term pharmacological interventions for agitation in schizophrenia/bipolar disorder |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Review | Expert Rev Neurother | 50-year experience review of loxapine for rapid non-coercive tranquilization of acute behavioral disturbances |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based review of treatment options and clinical suggestions for bipolar mania |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Expert Review/Commentary | Drugs in R&D | Expert commentary on inhaled loxapine for acute agitation in bipolar disorder and schizophrenia |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatr Dis Treat | Safety, efficacy, and patient acceptability review of inhaled loxapine for acute agitation in bipolar I/schizophrenia |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Clinical Review | Int J Mol Sci | Narrative/clinical mini-review of efficacy and tolerability of inhaled loxapine for acute agitation |

---

## Canada Market Information

Loxapine is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) are on file (0 licenses recorded). Any Canadian development pathway for this indication would require a new submission rather than a label-extension of an existing authorization.

---

## Safety Considerations

- **Key Warnings**: Formal Health Canada/TFDA label warnings have not yet been extracted for this drug (data gap, see below). However, the evidence pack's mechanistic rationale notes that the inhaled loxapine formulation (Adasuve®) carries a **boxed warning for bronchospasm** and is subject to a Risk Evaluation and Mitigation Strategy (REMS) in jurisdictions where it is approved — this should be treated as a material safety signal pending formal label confirmation.
- **Drug Interactions**: No interaction data currently on file (query returned no results).

> Please refer to the official package insert for complete safety information once available — formal contraindication and warning data for this drug have not yet been retrieved (see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The bipolar-mania prediction is supported by a coherent mechanistic story (D2/5-HT2A antagonism), an existing approved use for the same drug in the same patient population abroad (inhaled loxapine for agitation in bipolar I disorder/schizophrenia in the US/EU), and 10+ relevant publications including pooled and head-to-head Phase III RCT data (L1 evidence). This is one of the stronger repurposing signals in this evidence pack — the other nine TxGNN candidates (ranks 2–10) lack any clinical, literature, or mechanistic support and were held.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain and parse the official Health Canada/TFDA-equivalent product label (warnings, contraindications) — this is currently blocking formal S1 safety screening.
- Resolve **DG002**: confirm loxapine's formal DrugBank-sourced mechanism-of-action record to replace the rationale-derived MOA used in this report.
- Since loxapine is not currently marketed in Canada, determine the regulatory pathway (new submission vs. leveraging existing US/EU Adasuve approval data) before advancing further.
- Formal drug-interaction (DDI) profile, as the current query returned no results.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

