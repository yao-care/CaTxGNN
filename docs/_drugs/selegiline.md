---
layout: default
title: Selegiline
parent: Moderate Evidence (L3-L4)
nav_order: 838
evidence_level: L3
indication_count: 4
---

# Selegiline
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

# Selegiline: From Parkinson's Disease to Schizophrenia

## One-Sentence Summary

Selegiline is a monoamine oxidase B (MAO-B) inhibitor originally used to treat Parkinson's disease and depressive disorders.
The TxGNN model predicts it may be useful for **schizophrenia** (specifically as add-on treatment for negative symptoms),
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (the approved indication text for the Canadian licence is not available; this is taken from the drug's known indication list, which also includes major depressive disorder and anxiety disorder) |
| Predicted New Indication | Schizophrenia (the model's top-ranked prediction was a rare neurodevelopmental disorder with no supporting evidence, so the highest-ranked prediction with evidence is evaluated here) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails (research-question stage) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, selegiline irreversibly inhibits MAO-B (and MAO-A at higher oral doses), which slows the breakdown of dopamine and raises its availability in the brain.

Negative symptoms of schizophrenia (such as reduced motivation, blunted emotion and social withdrawal) are thought to relate to low dopamine activity in the prefrontal cortex. Standard antipsychotics treat positive symptoms (hallucinations, delusions) reasonably well but have limited effect on negative symptoms. Boosting dopamine with selegiline on top of an antipsychotic is therefore a plausible approach. Selegiline's proposed antioxidant and neuroprotective effects also fit the research on oxidative stress in schizophrenia.

The effect is most likely limited to add-on use for negative symptoms, not a core antipsychotic effect. The results of published studies have been mixed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomized, placebo-controlled test of selegiline added to antipsychotics for negative symptoms in inpatients with chronic schizophrenia (2007). No results are available in the compiled data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT (double-blind, multicenter) | Am J Psychiatry | Selegiline added to antipsychotics for negative symptoms in outpatients with schizophrenia |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT (double-blind) | Hum Psychopharmacol | 8-week trial of selegiline added to risperidone for negative symptoms; the authors note earlier results were contradictory |
| [10587287](https://pubmed.ncbi.nlm.nih.gov/10587287/) | 1999 | RCT (double-blind) | J Clin Psychopharmacol | Deprenyl (selegiline) augmentation in 16 patients with predominantly negative symptoms |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT (placebo-controlled) | Biol Psychiatry | Selegiline 10 mg/day vs placebo for 6 weeks in 33 patients with tardive dyskinesia |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic review / meta-analysis | Eur Neuropsychopharmacol | Efficacy and safety of oral and transdermal selegiline across psychiatric disorders |
| [26848926](https://pubmed.ncbi.nlm.nih.gov/26848926/) | 2016 | Systematic review | Cochrane Database Syst Rev | Antioxidant treatments for schizophrenia |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Role of selegiline in negative symptoms of schizophrenia |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic review | Schizophr Res | Drug treatments for primary negative symptoms in schizophrenia |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | Open-label pilot | J Nerv Ment Dis | Low-dose selegiline (5 mg twice daily) added to antipsychotics in 21 patients with schizophrenia or schizoaffective disorder |
| [7901857](https://pubmed.ncbi.nlm.nih.gov/7901857/) | 1993 | Clinical report | Pharmacopsychiatry | Selegiline for neuroleptic-induced parkinsonism |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230641 | SELEGILINE | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications flagged in the drug-disease knowledge graph (not label text)**: These include multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, kidney disease, liver disease, gallbladder disease, bipolar disorder and other major affective disorders, psychotic disorders (including schizophreniform and schizoaffective disorder), mental disorder, phaeochromocytoma and related adrenal or paraganglioma tumours, melanoma, sudden cardiac arrest, heart conduction disease, tardive dyskinesia, and some gastrointestinal and cardiac cancers. The listing of psychotic disorders is particularly relevant to the schizophrenia direction and needs careful clinical review.
- **Drug Interactions**: 100 interactions are recorded. Major interactions include bupropion, isometheptene, diethylpropion, phentermine and dexfenfluramine. Moderate interactions include epinephrine, metoclopramide, and a range of diabetes medicines (insulins, glimepiride, repaglinide, nateglinide, chlorpropamide, acetohexamide). Serotonergic and sympathomimetic combinations require particular attention when selegiline is combined with antipsychotics or antidepressants.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Schizophrenia is the best-supported prediction: several randomized trials and reviews have examined selegiline as add-on treatment for negative symptoms, and the drug is already marketed in Canada. However, the one registered trial is early phase with no available results, the published findings are mixed, and the knowledge graph lists psychotic disorders as a contraindication. This is best treated as a research question rather than a ready-to-use new indication.

The other predictions are weaker. The top-ranked disease (perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis) and congenital disorder of glycosylation with defective fucosylation have no trials or literature, and no supported mechanism. Retinal dystrophy has only one indirect, non-selegiline-specific article. All three are on hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism of action data
- Published results from the completed trial (NCT00456976) and a critical appraisal of the randomized trials, including the conflicting findings
- Clinical review of the psychotic-disorder contraindication signal and of interaction management with antipsychotics and antidepressants
- Dose and formulation clarification (low-dose oral use vs higher doses with non-selective MAO inhibition)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

