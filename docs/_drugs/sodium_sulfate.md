---
layout: default
title: Sodium Sulfate
parent: Model Prediction Only (L5)
nav_order: 857
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Sodium Sulfate: predicted new indication Dyspepsia (evidence level L5). Approved use: Not stated in the Canadian licence data compiled for this report (pro…"
monitor_inn: "SODIUM SULFATE"
predicted_indications: ["dyspepsia"]
---

# Sodium Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sodium Sulfate: From Osmotic Bowel Preparation to Dyspepsia

## One-Sentence Summary

Sodium sulfate is an osmotic saline laxative, marketed in Canada as a component of bowel-cleansing products. The TxGNN model predicts it may be effective for **dyspepsia**, but this is a model prediction only: there are **no registered clinical trials** and **no directly relevant publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data compiled for this report (products are known bowel-preparation formulations) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, sodium sulfate is an osmotic saline laxative: it retains water in the gut lumen and increases luminal volume, which stimulates bowel evacuation.

A link to dyspepsia (functional upper gastrointestinal symptoms) is plausible only indirectly, through effects on gastrointestinal motility and luminal content. The relationship between the original use (bowel cleansing) and the predicted use is weak, and no mechanistic study supports it.

The three publications retrieved all concern **dextran sodium sulfate (DSS)**, a chemical used to induce colitis in animal models, or herbal treatments tested in DSS colitis models. DSS is a different polymer from sodium sulfate, so these papers say nothing about the drug's effect on dyspepsia. The very high TxGNN score should be read as a model output, not as clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The papers below mention dyspepsia only in passing and all use DSS-induced animal models. They are listed for transparency, not as supporting evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Preclinical (animal) | Int J Mol Sci | Atractylodin, a herbal compound, reduced DSS-induced colitis via PPARα agonism; not about sodium sulfate |
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Preclinical (pig) | Molecules | DSS-induced gut injury altered donepezil pharmacokinetics and gastric myoelectric activity; not about sodium sulfate |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Preclinical (animal) | J Inflamm Res | Si-Ni Decoction (herbal) modulated gut microbiota in DSS ulcerative colitis; not about sodium sulfate |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00777838 | PEGLYTE POWDER | Not specified | Not specified |
| 02378329 | JAMPLYTE | Not specified | Not specified |
| 00677442 | COLYTE | Not specified | Not specified |
| 02552612 | JAMPLYTE + BISACODYL | Not specified | Not specified |
| 02326302 | BI-PEGLYTE | Not specified | Not specified |

A sixth licence (MOVIPREP, DIN 02359499) is also valid. All six licences are single-ingredient, currently valid, and none are cancelled.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug–disease links in the TxGNN knowledge graph, not taken from product label text):

- **Gastrointestinal obstruction or dysmotility:** ileus, paralytic ileus, intestinal obstruction, pyloric stenosis, toxic megacolon, appendicitis, gastroparesis, familial visceral myopathy, chronic diarrhoeal disease, *Clostridium difficile* colitis
- **Kidney and electrolyte disorders:** kidney disease, anuria, pyoureter, nephrocalcinosis, potassium deficiency, hypercalcaemia, phosphorus metabolism disease, hypoaldosteronism, hyperkalaemic periodic paralysis, periodic paralysis
- **Cardiac and neuromuscular:** atrioventricular block, epilepsy, myotonia congenita
- **Haematological and metabolic:** sickle cell anaemia, hereditary persistence of fetal haemoglobin, primary hyperoxaluria, hereditary haemochromatosis, haemosiderosis, iron metabolism disease, Wilson disease

**Drug interactions:** The interaction screen returned 100 interacting drugs. The first 20 returned include one Major and 19 Moderate interactions.
- **Major:** amiodarone
- **Moderate (examples):** abarelix, abiraterone, acetazolamide, salbutamol, amantadine, amiloride, aminophylline, amitriptyline, amphetamine, aripiprazole

Many of these are likely linked to electrolyte disturbance or QT-related risk. This is an inference, as the interaction details were not provided.

Please also refer to the package insert for warnings and contraindications, which could not be obtained for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, and the retrieved literature concerns dextran sodium sulfate, a different substance used in animal colitis models. The drug's established osmotic laxative action has no clear connection to dyspepsia, and the knowledge-graph safety signals (gastrointestinal obstruction, kidney and electrolyte disorders) raise additional concern for use in this setting.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to assess a plausible link to dyspepsia
- Approved indication text and dosage forms for the Canadian licences
- A targeted literature search for sodium sulfate itself (not dextran sodium sulfate) in functional upper gastrointestinal disorders
- Clinical evidence, or a justified rationale, supporting use in dyspepsia before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

