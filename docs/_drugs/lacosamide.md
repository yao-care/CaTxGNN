---
layout: default
title: Lacosamide
parent: Model Prediction Only (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Lacosamide: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Epilepsy (focal-onset seizures)…"
monitor_inn: "Lacosamide"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
---

# Lacosamide
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

## Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Lacosamide is an antiseizure medication, used mainly for focal-onset seizures in epilepsy.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**.
Support is limited: **0 registered clinical trials** and a small set of observational studies, case reports and reviews among **14 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (focal-onset seizures), as described in the literature. The Canadian licence records compiled for this report do not list indication text. |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 (observational studies only; no registered trials) |
| Canada Market Status | Marketed (valid licenses on record: at least 18) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lacosamide was not available in the data compiled for this report. Lacosamide is known to enhance slow inactivation of voltage-gated sodium channels, and it may also modulate CRMP2 (collapsin response mediator protein 2). Both actions could reduce neuronal hyperexcitability.

Several antiseizure drugs that act on sodium channels, such as lamotrigine and carbamazepine, are already used as mood stabilisers. This is the main reason the prediction is plausible. Epilepsy and bipolar disorder also frequently co-occur, and one report describes mood stabilisation with lacosamide in a patient with a mood disorder, PTSD and fronto-temporal epilepsy.

The direct clinical evidence is thin. It consists of a small retrospective comparison in bipolar disorder, an open-label pilot in **bipolar depression** (not mania), and observational data on mood in epilepsy. One case report also describes lacosamide-precipitated neutropenia in a patient with bipolar disorder.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide with other antiepileptics in bipolar disorder patients without epilepsy. This is the first assessment of lacosamide in bipolar disorder. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week pilot of efficacy and safety in bipolar depression. No abstract text was available, so results are not summarised here. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicentre cohort | Epilepsy Behav | Effect of lacosamide on depression and anxiety symptoms in patients with refractory focal epilepsy. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical stabilisation with lacosamide of a mood disorder comorbid with PTSD and fronto-temporal epilepsy. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report (safety) | Indian J Psychol Med | Lacosamide precipitated neutropenia in a patient with bipolar disorder and epilepsy. This is a safety signal. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | Druggability of CRMP2, a possible lacosamide target, in neurodegenerative disease. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | Therapeutic drug monitoring of antiepileptic drugs. Notes that some are also used for bipolar disorder. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Adv Drug Deliv Rev | Chemical properties of antiepileptic drugs, including lacosamide. |

## Canada Market Information

Lacosamide has 20 valid single-ingredient licences in Canada. Dosage form and approved-indication text were not available for these records. Five are shown below.

| DIN | Product Name |
|---------|------|
| 02357615 | VIMPAT |
| 02357666 | VIMPAT |
| 02357631 | VIMPAT |
| 02357623 | VIMPAT |
| 02490544 | MINT-LACOSAMIDE |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not taken from label text): the knowledge graph links lacosamide to cardiac conduction and rhythm conditions, including atrioventricular block, sick sinus syndrome, atrial fibrillation and flutter, coronary artery disease and myocardial ischaemia. It also links it to orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, liver disease and gallbladder disease.
- **Drug interactions:** 25 interactions are recorded, and 20 are detailed in the compiled data.
  - **Major:** dolasetron, ceritinib and siponimod.
  - **Moderate:** clarithromycin, ethanol, cobicistat, chloroquine, hydroxychloroquine, mefloquine, lidocaine, ketoconazole, pasireotide, alectinib, brigatinib, crizotinib, fingolimod, idelalisib, imatinib, ozanimod, sunitinib.
- **Bipolar-specific signal:** one case report describes neutropenia in a bipolar patient taking lacosamide (PMID 30275630).

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is backed only by one small retrospective study, one open-label pilot in bipolar depression, and case reports. There are no registered trials, and the one reported safety signal (neutropenia) is unresolved.

**To proceed, the following is needed:**
- A controlled trial in acute mania, with a placebo or active comparator.
- Results of the open-label bipolar depression pilot, and any replication.
- Detailed mechanism-of-action data for lacosamide.
- Health Canada package insert warnings and contraindications.
- A haematological and cardiac (ECG/conduction) monitoring plan, given the neutropenia case report and the cardiac signals from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence.
- For prioritisation: in the same prediction list, **migraine disorder** has stronger support than this indication. It has four registered trials (three Phase 3 and one Phase 2) and a published double-blind RCT against propranolol (PMID 41863672). It may be a more evidence-ready candidate for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

