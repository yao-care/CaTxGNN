---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 901
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "TETRABENAZINE"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
description: "Tetrabenazine: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Tetrabenazine
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

## Tetrabenazine: Polycystic kidney disease 3 with or without polycystic liver disease
{: .text-alpha }

## One-Sentence Summary

Tetrabenazine is a drug originally used to treat movement disorders such as Huntington disease.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**,
but this is a model prediction only: **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tetrabenazine is generally known as a reversible VMAT2 inhibitor that depletes monoamines in the central nervous system. This is general pharmacology and not drawn from the compiled data. Its use has been established in hyperkinetic movement disorders, including Huntington disease and related syndromes.

No mechanistic link to the predicted indication has been established. Polycystic kidney and liver disease is a disorder of cyst formation linked to ciliary dysfunction. Nothing in the available data connects monoamine depletion through VMAT2 inhibition to this pathology. The high TxGNN score (0.9990) reflects a prediction from the TxGNN model (deep learning) and has not been corroborated by any trial or publication.

Other top-ranked predictions show the same pattern. They include renal-hepatic-pancreatic dysplasia, Joubert syndrome with renal defect, karyomegalic interstitial nephritis, and acute intermittent porphyria. All are L5 (model prediction only) with no plausible mechanistic link identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For reference, the fifth-ranked prediction (thoracic malformation) retrieved one case report, PMID [11293103](https://pubmed.ncbi.nlm.nih.gov/11293103/) (2001, *Revista de neurologia*), on spasmodic torticollis with vertebral hemangioma. It is tangential and does not show that tetrabenazine treats the predicted condition.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02402424 | PMS-TETRABENAZINE | Not specified | Not specified |
| 02407590 | APO-TETRABENAZINE | Not specified | Not specified |
| 02199270 | NITOMAN | Not specified | Not specified |

All three products are valid single-ingredient authorizations; none is cancelled.

---

## Safety Considerations

- **Contraindications (TxGNN model output, not label text)**: The TxGNN model (deep learning) links tetrabenazine with contraindications in the following conditions. These links may reflect similarities the model learned between related diseases, not biological evidence:
  - Cardiovascular and rhythm: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, multiple system atrophy
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
  - Movement: Parkinson disease, parkinsonian disorder, tardive dyskinesia, lingual-facial-buccal dyskinesia, drug-induced akathisia
  - Hepatic and biliary: liver disease, gallbladder disease
  - Endocrine: hyperprolactinemia (including familial and acquired forms) and prolactin-producing pituitary tumour
- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total (20 shown in the compiled data). Major-level interactions include:
  - Bupropion
  - Dolasetron
  - Metoclopramide

  Moderate-level interactions include famotidine, loperamide, morphine, lorcaserin, clarithromycin, levofloxacin, palonosetron, dronabinol, nabilone, eliglustat and several laxatives or bowel preparations. Metronidazole is minor. The QT-related and CNS-active entries deserve particular attention given the long QT contraindication.

Package insert warnings and contraindications from Health Canada were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or relevant publications, and no mechanistic link between VMAT2 inhibition and cyst-forming ciliopathies. The knowledge-graph contraindications, including liver disease, also raise caution in a population with hepatic involvement.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and an analysis of any plausible link to polycystic kidney/liver disease pathways
- Health Canada package insert warnings and contraindications for safety screening
- Preclinical evidence (cell or animal models of polycystic kidney disease) before any clinical consideration
- A review of the other ranked predictions, none of which currently has supporting evidence either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

