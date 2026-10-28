---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 907
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a methylxanthine bronchodilator whose relations recorded in the knowledge graph centre on asthma and other chronic airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **no clinical trials** and **no publications that directly study theophylline in thrombosis** are available, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (relation recorded in the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Number of approvals | 6 (single-ingredient licences) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, theophylline is a nonselective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. PDE inhibition raises cAMP in platelets, which could plausibly reduce platelet aggregation. This is the likely basis for the high model score.

The link to the original airway indications is weak. Asthma and thrombosis are different disease areas, and the data compiled for this report show no established similarity between them. The mechanism also works in two directions: adenosine receptor antagonism could counteract the antiplatelet effect of adenosine. No retrieved literature shows a clinical antithrombotic benefit from theophylline.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications tests theophylline as a treatment for thrombotic disease. The table lists the items closest to the topic, and most are not direct evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostaglandins, platelets and atherosclerosis; background on cAMP-mediated antiplatelet mechanisms |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | Gen Pharmacol | Milrinone and adenosine inhibit human platelet response through cAMP; a different drug |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory/methodological | Br J Haematol | Platelet factor 4 radioimmunoassay; theophylline appears only as a sample-preparation additive |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Laboratory/methodological | Anal Chim Acta | Aptasensor for detecting theophylline; no therapeutic data |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Not classified | Minerva Cardioangiol | Theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy; a different compound, no abstract available |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00692700 | AA-THEO LA | Not stated | Not stated |
| 00627410 | ELIXIR DE THEOPHYLLINE | Not stated | Not stated |
| 02360101 | THEO ER | Not stated | Not stated |
| 02360128 | THEO ER | Not stated | Not stated |
| 00692697 | AA-THEO LA | Not stated | Not stated |
| 00692689 | AA-THEO LA | Not stated | Not stated |

All six licences are valid single-ingredient products. The licence records compiled for this report contain no indication text.

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (not label text): hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, peptic ulcer disease, hypothyroidism, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis, and others. Thrombocytopenia is of particular note for any antithrombotic use.
- **Drug Interactions** (100 interactions in total; examples):
  - **Major**: bupropion
  - **Moderate**: cimetidine, famotidine, ranitidine, omeprazole, rabeprazole, clarithromycin, doxycycline, tetracycline, minocycline, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - **Minor**: ephedrine

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by any trial or study that directly examines theophylline in thrombotic disease. The retrieved papers mostly use theophylline as an assay reagent or concern other drugs. The evidence level is therefore L5. The adenosine antagonism could also work against an antiplatelet effect.

**To proceed, the following is needed:**
- Mechanism of action data and the Health Canada package insert warnings and contraindications
- Preclinical or clinical evidence that theophylline reduces thrombus formation or platelet aggregation at tolerated doses
- A safety assessment covering the narrow therapeutic window and the drug interaction burden in patients likely to take anticoagulants or antiplatelet agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

