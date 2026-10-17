---
layout: default
title: Perampanel
parent: Model Prediction Only (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Perampanel: predicted new indication Visual epilepsy (evidence level L5). Approved use: Partial epilepsy / partial motor epilepsy"
monitor_inn: "PERAMPANEL"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Perampanel
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

# Perampanel: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel is an oral antiseizure medication, marketed in Canada for focal-onset (partial) seizures.
The TxGNN model predicts it may be effective for **visual epilepsy**.
Currently **0 clinical trials** and **20 publications** are linked to this prediction. The publications are general epilepsy and perampanel papers, and none studies visual epilepsy specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy / partial motor epilepsy (Health Canada indication text was not available in the compiled data) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (indirect evidence only, via the parent epilepsy indication) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured drug record. The published literature describes perampanel as a selective, noncompetitive AMPA-receptor antagonist. It reduces glutamate-driven excitation at postsynaptic membranes, and it is the first approved antiepileptic drug to work this way. It is approved in Canada as adjunctive therapy for partial-onset seizures in adults.

Visual (photosensitive or occipital) epilepsy is a seizure syndrome in which the visual cortex is hyperexcitable. This kind of glutamate-mediated excitability is the same one perampanel dampens in its approved indication. The prediction is therefore biologically plausible.

The link is still indirect. The retrieved publications are reviews, guidelines, network meta-analyses and pharmacology papers on epilepsy in general. None tests perampanel in visual epilepsy, so the prediction rests on the parent indication rather than direct proof.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visual epilepsy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Perampanel as add-on therapy for drug-resistant focal epilepsy |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Systematic review / network meta-analysis | Drugs | Compared third-generation antiseizure drugs, including perampanel, as add-on for focal-onset seizures in adults |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic review / network meta-analysis | J Neurol | Efficacy and safety of antiseizure drugs in idiopathic generalized epilepsies |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline / review | Neurology | AAN/AES guideline update on newer antiepileptic drugs for new-onset epilepsy |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy Behav | Clinical trial and real-world evidence for perampanel monotherapy |
| [29953584](https://pubmed.ncbi.nlm.nih.gov/29953584/) | 2019 | Narrative review | Epilepsia | Perampanel's potential as a broad-spectrum antiseizure drug |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development of perampanel for partial-onset seizures |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Cohort | Front Neurol | Real-life use of perampanel in childhood absence epilepsy |
| [36734057](https://pubmed.ncbi.nlm.nih.gov/36734057/) | 2023 | Multicentre case collection | Epilepsia | Perampanel as targeted therapy in rare genetic epilepsies |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Cohort | Ann Clin Transl Neurol | Efficacy of perampanel in paediatric epilepsy with known or presumed genetic cause |

---

## Canada Market Information

Health Canada holds 12 valid single-ingredient authorizations for perampanel, with no cancelled licenses. Dosage form and approved-indication text were not available for these entries. The first five are shown below.

| DIN | Product Name |
|---------|------|
| 02404532 | FYCOMPA |
| 02404524 | FYCOMPA |
| 02404559 | FYCOMPA |
| 02522632 | TARO-PERAMPANEL |
| 02522667 | TARO-PERAMPANEL |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening found 56 interacting drugs, mostly rated Moderate. Examples include:
  - Opioids and related agents: morphine, codeine, hydrocodone, diphenoxylate, difenoxin and opium. The concern is additive central nervous system effects.
  - Cannabinoids: dronabinol and nabilone.
  - Sedating antihistamines: promethazine and chlorpheniramine.
  - Other: dexamethasone, metoclopramide, chloroquine, hydroxychloroquine, dextromethorphan, sibutramine and ethanol.
  - Clarithromycin is the one example listed here as a Minor interaction.
- **Psychiatric effects (from the literature)**: Published reports note a boxed warning for serious psychiatric and behavioural reactions such as aggression and irritability, and case reports of psychosis. Confirm this against the current Canadian product monograph.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.92%), but no clinical trial or study addresses visual epilepsy, and the supporting literature is indirect. Evidence stays at L4, which is not enough to move forward.

Among the other predictions compiled for this drug, **status epilepticus** has the strongest support. It has a Phase 2 trial in progress (NCT06401707, perampanel for post-cardiac-arrest status epilepticus prophylaxis, 52 participants). Two further trials (NCT04309721, Phase 3; NCT05684978, Phase 4) were terminated after enrolling one patient each, so they give no efficacy data. Systematic reviews and case series also report seizure cessation with perampanel in refractory status epilepticus. It could be assessed as a separate candidate.

**To proceed, the following is needed:**
- Case series, registry data or a pilot trial of perampanel in visual or photosensitive epilepsy
- Mechanism-of-action data in the drug record, and a defined mechanistic link to visual-cortex hyperexcitability
- Health Canada product monograph warnings and contraindications, to support a safety screen
- Approved indication text and dosage-form details for the Canadian licenses
- A plan for monitoring psychiatric and behavioural adverse effects, and for managing the CNS-depressant interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

