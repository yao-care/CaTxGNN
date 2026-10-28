---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Metoclopramide: predicted new indication Gastroduodenitis (evidence level L4). Approved use: Gastroesophageal reflux disease"
monitor_inn: "Metoclopramide"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Metoclopramide: From Gastroesophageal Reflux Disease to Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug, originally used for gastroesophageal reflux disease and reflux esophagitis.
The TxGNN model predicts it may be effective for **gastric ulcer**,
but only **1 clinical trial** (indirect, on endoscopic visualization) and a body of mostly general review literature currently support this direction. Direct evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease; esophagitis; peptic esophagitis |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, metoclopramide acts as a dopamine D2 antagonist and a 5-HT4 agonist. It enhances gastric emptying and upper gastrointestinal motility. This is the basis of its use in reflux disease.

A prokinetic could plausibly reduce gastric stasis and bile or alkaline reflux, which can aggravate mucosal injury. However, metoclopramide does not suppress acid and has no established ulcer-healing effect, so any benefit in gastric ulcer would be indirect. The very high TxGNN score most likely reflects the drug's close network association with other upper gastrointestinal conditions (reflux disease, esophagitis) rather than ulcer-specific efficacy.

Other predicted indications follow the same pattern. Gastroduodenitis has the most plausible link through antroduodenal motility. Peptic ulcer disease and gastrojejunal ulcer rest on indirect reasoning only. Peptic ulcer perforation has no sound mechanistic rationale; it is an acute surgical emergency, and the high score appears to be a network artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind trial of metoclopramide premedication in upper GI bleeding. It tests whether endoscopic visualization improves and whether repeat endoscopy, interventional radiology or surgery is needed. It does not test ulcer healing, so it is indirect evidence only. |

---

## Literature Evidence

The most relevant publications retrieved for gastric ulcer are listed below. Most are general reviews, not studies of metoclopramide in gastric ulcer.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use of metoclopramide; mentions easing emergency endoscopy in upper GI haemorrhage |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Review | Drugs | Diabetic gastroparesis and its limited treatment options |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Systematic review | Paediatric Drugs | Pharmacological management of gastro-oesophageal reflux in children |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgraduate Medicine | Strategies for ulcers and reflux esophagitis that resist standard regimens |
| [7510617](https://pubmed.ncbi.nlm.nih.gov/7510617/) | 1994 | Review | Drugs | Cisapride (related prokinetic) improved healing in reflux oesophagitis |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomized crossover study | MMW | In 12 healthy men, metoclopramide did not significantly change serum gastrin or gastric acid secretion |
| [579607](https://pubmed.ncbi.nlm.nih.gov/579607/) | 1978 | Review | Canadian Journal of Surgery | Symposium on medical treatment of peptic ulcer; notes metoclopramide hastens gastric emptying |
| [7017896](https://pubmed.ncbi.nlm.nih.gov/7017896/) | 1981 | Review | Scand J Gastroenterol Suppl | Therapeutic implications of duodeno-gastric reflux |
| [15259526](https://pubmed.ncbi.nlm.nih.gov/15259526/) | 2004 | Review | American Family Physician | Evaluation and management of nonulcer dyspepsia |
| [8686797](https://pubmed.ncbi.nlm.nih.gov/8686797/) | 1996 | Review | American Journal of Surgery | Delayed gastric emptying after gastric surgery, often after operations for peptic ulcer disease |

Two points are worth noting from the wider set of retrieved studies:
- A 2024 double-blind RCT ([38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/)) and a 2026 triple-blind RCT ([42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/)) examined metoclopramide for gastric visualization in acute upper GI bleeding. Both address endoscopic visualization, not ulcer treatment.
- A rat study ([2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/), 1989) reported an ulcer-protective effect in aspirin-induced and pylorus-ligated models. This is preclinical only.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02185431 | Metoclopramide Hydrochloride Injection | Injection | Not specified in the data |
| 02548755 | PRZ-Metoclopramide | Not specified | Not specified in the data |
| 02230431 | PMS-Metoclopramide Tablets | Tablet | Not specified in the data |
| 02510790 | PMS-Metoclopramide Hydrochloride Injection | Injection | Not specified in the data |
| 02230433 | PMS-Metoclopramide Oral Solution | Oral solution | Not specified in the data |

Nine valid single-ingredient DINs are registered in total; the five main ones are shown above. The dosage form column is inferred from product names, as the compiled data lists no dosage form.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Contraindications and cautions from the knowledge graph** (these are drug-disease links, not label text):
- Neurological: epilepsy, Parkinson disease and parkinsonian disorders, tardive dyskinesia, torsion dystonia, neuroleptic malignant syndrome
- Cardiovascular and endocrine: hypertension, pheochromocytoma and related adrenal or paraganglioma tumours
- Gastrointestinal and organ function: active peptic ulcer disease, cirrhosis of liver, impaired renal function
- Psychiatric: anxiety disorder, dysthymic disorder
- Metabolic: porphyria, methemoglobinemia due to methemoglobin reductase deficiency

"Active peptic ulcer disease" appearing on this list deserves attention, since it is closely related to the predicted indication, gastroduodenitis.

**Drug interactions:** The query returned 100 interactions; the first 20 returned are summarized here.
- **Major:** tramadol, amisulpride
- **Moderate:** fentanyl, codeine, dihydrocodeine, alfentanil, alprazolam, amitriptyline, amantadine, cetirizine, chlorpheniramine, ethanol, and others
- **Minor:** acetaminophen

Many of the moderate interactions involve central nervous system depressants.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9990), but the only clinical trial concerns endoscopic visualization in GI bleeding, not ulcer healing. Metoclopramide has no acid-suppressive or cytoprotective action, and the knowledge graph lists active peptic ulcer disease as a contraindication. Evidence is limited to the L4 level.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing
- Detailed mechanism of action data (MOA) from DrugBank
- Clinical studies that directly assess ulcer healing or ulcer outcomes, not only endoscopic visualization
- Clarification of the knowledge-graph contraindication for active peptic ulcer disease
- A closer look at gastroduodenitis as an alternative candidate, since it has the strongest mechanistic link (antroduodenal motility) among the predictions, though efficacy for the inflammatory condition itself remains unproven
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

