---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Primidone: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
---

# Primidone
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

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is an anticonvulsant originally used to treat epilepsy, including generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are currently **0 clinical trials** and **0 publications** supporting this top-ranked prediction. The score is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the Canadian licence records contain no indication text; this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primidone is an established anticonvulsant (it is partly metabolized to phenobarbital), its efficacy in epilepsy is well recognized, and its action is aimed at reducing neuronal hyperexcitability.

For the top-ranked prediction, trigeminal nerve neoplasm, no mechanistic link to an anticonvulsant is evident. No antineoplastic mechanism is known for primidone, so the high score should be treated as a hypothesis from the knowledge graph, not as evidence of efficacy.

The lower-ranked predictions are more plausible mechanistically. Several are reflex seizure disorders within the epilepsy spectrum (audiogenic seizures, micturition-induced seizures, eating seizures, startle epilepsy, orgasm-induced seizures, thinking seizures and reading seizures). These are close to the approved indications, and so are largely redundant with them. Trigeminal neuralgia, the only other prediction with a plausible link, is already treated mainly with carbamazepine, an established standard of care. Beta-ketothiolase deficiency, a metabolic disorder, has no evident link to primidone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm, nor for any of the other top-10 predicted indications.

---

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For context, the literature found for lower-ranked predictions is indirect only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs for indications other than epilepsy; evidence mostly from case series and small trials (trigeminal neuralgia) |
| [14249886](https://pubmed.ncbi.nlm.nih.gov/14249886/) | 1964 | Preclinical (animal) | Biull Eksp Biol Med | Audiogenic convulsions in animals after prior primidone administration |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Preclinical (mouse) | Neurol Psychiatr | Effect of phenobarbital, diphenylhydantoin and primidone on brain enzyme activity in audiogenic epilepsy in mice |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clin Neurosci | Primidone (500–1,000 mg/day) is among the most useful drugs for cortical myoclonus (cited for reading seizures) |
| [4525036](https://pubmed.ncbi.nlm.nih.gov/4525036/) | 1974 | Case report (veterinary) | J Am Vet Med Assoc | Long-term primidone therapy in a dog (eating seizures) |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case report | Chin Med J (Taipei) | Startle epilepsy presenting as drop attacks; primidone use not shown in the title |

None of these is a controlled study of primidone in the predicted indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00399310 | PRIMIDONE | Not specified | Not specified |
| 00396761 | PRIMIDONE | Not specified | Not specified |

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease edges, not from package insert text):
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, leukopenia, pancytopenia, anaemia (including macrocytic anaemia) and several congenital neutropenia syndromes
- Porphyria (including inherited porphyria)
- Kidney disease and liver disease
- Sleep-related breathing disorders: obstructive sleep apnoea and congenital central hypoventilation syndrome
- Psychiatric and substance-related conditions: anxiety disorder, neurotic disorder, dysthymic disorder and substance abuse/dependence
- Gallbladder disease and pyoureter

**Drug interactions:** 100 interactions were found in the DDI query. Examples:
- **Major:** morphine, eliglustat
- **Moderate:** doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcitriol, pioglitazone, bupropion, aprepitant, metronidazole, canagliflozin, saxagliptin, dronabinol
- **Minor:** cimetidine

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, rests on a model score alone, with no trials, no literature and no known antineoplastic mechanism for primidone. Among the lower-ranked predictions, the reflex seizure indications overlap with the existing epilepsy use and are supported only by old, indirect or animal evidence. Trigeminal neuralgia is a research question, since carbamazepine is already the standard treatment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Mechanism of action data for primidone
- Any primary evidence, preclinical or clinical, linking primidone to trigeminal nerve neoplasm, or a decision to evaluate the more plausible indications (such as trigeminal neuralgia) instead
- Approved indication text and dosage forms for the two Canadian DINs
- A drug-interaction review, particularly for the major interactions with morphine and eliglustat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

