---
layout: default
title: Fluphenazine
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluphenazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Psychotic disorder, schizophrenia, schizophreniform disorder…"
monitor_inn: "Fluphenazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "myopia X-linked", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Fluphenazine
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

## Fluphenazine: From Psychotic Disorders to Retinal Dystrophy with or without Extraocular Anomalies
{: .text-alpha }

## One-Sentence Summary

Fluphenazine is a first-generation antipsychotic originally used for psychotic disorders, including schizophrenia and schizoaffective disorder.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorder, schizophrenia, schizophreniform disorder, schizoaffective disorder, mental disorder (licence text not provided; taken from the knowledge-graph indication list) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% (rank 236) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluphenazine is a phenothiazine-class antipsychotic that acts mainly by blocking dopamine D2 receptors. Its efficacy in psychotic disorders is well established.

Inherited retinal dystrophy is a genetically driven degenerative eye condition, and it is pharmacologically distant from psychosis. The data compiled for this report show no plausible mechanistic link between D2 antagonism and retinal degeneration. The very high score (99.99%) reflects a graph-based prediction and is not evidence of efficacy. It may partly reflect artefacts of the network structure. This prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 00410632 | FLUPHENAZINE |
| 00405345 | FLUPHENAZINE |
| 00405361 | FLUPHENAZINE |

All three are valid single-ingredient authorizations. Dosage form and approved indication text were not available in the compiled data.

---

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not label text):**
The knowledge graph links fluphenazine to the following conditions as contraindications. These should be confirmed against the official package insert.
- **Cardiovascular:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, coronary thrombosis, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- **Blood disorders:** neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anaemia (including macrocytic), hemoglobinopathy
- **Neurological:** epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
- **Hepatic and biliary:** liver disease, gallbladder disease
- **Metabolic and other:** hyperglycaemia, obesity disorder, monogenic obesity, benign prostatic hyperplasia, female breast carcinoma, substance abuse/dependence

**Drug Interactions:** 100 interactions were identified. The 20 reviewed include:
- **Major:** bupropion, morphine
- **Moderate:** acarbose, famotidine, epinephrine, hydrocortisone, albiglutide, alogliptin, metformin, pioglitazone, amphotericin B, hyoscyamine, loperamide, triamcinolone, atropine, dexamethasone, lorcaserin, betamethasone
- **Minor:** ascorbic acid

Several interacting agents are glucose-lowering drugs or corticosteroids, which is consistent with fluphenazine's hyperglycaemia concern.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no clinical trials, no literature, and no plausible mechanistic link between D2 antagonism and inherited retinal degeneration. The long list of knowledge-graph contraindications, particularly cardiac and neurological ones, adds caution.

**To proceed, the following is needed:**
- Mechanistic evidence linking fluphenazine to retinal dystrophy pathways, including mechanism of action data
- Preclinical studies (for example, retinal models) to support any biological rationale
- Official package insert warnings and contraindications from Health Canada
- Route and dosage-form compatibility assessment for an ocular or retinal indication

**Note:** Among the model's other predictions for fluphenazine, **manic bipolar affective disorder** (score 99.98%) is the most biologically coherent. It has indirect literature support, mainly reviews of long-acting injectable antipsychotics, and is classed as L4 and a research question. It would be a more reasonable candidate for further evaluation than the retinal prediction, though no fluphenazine-specific bipolar RCT or registered trial is available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

