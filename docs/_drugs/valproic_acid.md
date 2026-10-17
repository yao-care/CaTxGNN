---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 963
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Valproic Acid: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
monitor_inn: "VALPROIC ACID"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "thinking seizures", "orgasm-induced seizures", "eating seizures", "audiogenic seizures", "micturation-induced seizures", "reading seizures"]
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Valproic acid is an established antiseizure medicine, used for epilepsy (including absence epilepsy) and for the manic phase of bipolar disorder.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 registered clinical trials** and only **1 publication**, a 1997 case series on a different condition (Sturge-Weber syndrome). Evidence for this prediction is effectively absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy; manic bipolar affective disorder; absence epilepsy (from the TxGNN knowledge graph, as no approved-indication text was available for the Canadian licences) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Based on general knowledge, valproic acid is a broad-spectrum antiseizure drug with proven efficacy in epilepsy. It is thought to act by enhancing GABA-mediated inhibition and modulating ion channels. It is also known to inhibit histone deacetylases (HDACs), which has prompted interest in possible antineoplastic effects. This has mainly been discussed in glioma.

The link to a trigeminal nerve neoplasm is speculative. The only retrieved paper concerns Sturge-Weber syndrome, a neurocutaneous vascular disorder, not a tumour of the trigeminal nerve. The HDAC-inhibition argument has not been demonstrated for trigeminal tumours. In practice, any benefit would most plausibly be limited to controlling seizures that accompany a brain or nerve tumour, not to treating the tumour itself. The very high model score is therefore not supported by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales españoles de pediatría | Review of 14 Sturge-Weber syndrome cases over 25 years, covering clinical characteristics, evolution and treatment response. It does not address trigeminal nerve neoplasm. |

---

## Canada Market Information

Sixteen valid single-ingredient licences are on record. The main ones are listed below. Dosage form and approved-indication text were not available.

| DIN | Product Name |
|---------|------|
| 02239699 | APO-DIVALPROEX |
| 02458926 | MYLAN-DIVALPROEX |
| 00596418 | EPIVAL |
| 02236807 | PMS-VALPROIC ACID |
| 00443832 | DEPAKENE |

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report. The following information comes from other sources.

- **Contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links valproic acid with the following conditions as contraindications: liver disease, pancreatitis, kidney disease, thrombocytopenia, hematologic disease, gallbladder disease, inherited porphyria and other porphyrin metabolism disorders, urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia), cognitive disorder, anxiety disorder, neurotic disorder, dysthymic disorder, and pyoureter.
- **Drug interactions**: The interaction screening returned 100 interacting drugs, and the first 20 were reviewed.
  - **Major**: glycerol phenylbutyrate.
  - **Moderate**: bupropion, morphine (including liposomal), acetylsalicylic acid, clarithromycin, difenoxin, diphenoxylate, activated charcoal, dronabinol, metoclopramide, nabilone.
  - **Minor**: cimetidine, esomeprazole, and several antacids (magnesium oxide, magnesium carbonate, magnesium hydroxide, aluminum hydroxide, calcium carbonate, magaldrate).

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. There are no registered trials, and the single retrieved paper is unrelated to trigeminal nerve tumours. Any antineoplastic rationale is speculative, so there is no basis to advance this indication.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a documented rationale for activity in trigeminal nerve tumours
- Preclinical or clinical studies specific to this tumour type
- Health Canada package insert warnings and contraindications, which are required for safety screening

**Note on other predictions for this drug:** The data compiled for this report also includes other predicted indications that are far better supported. The strongest is **visual epilepsy**, with evidence level L1 and a "Proceed with Guardrails" recommendation. It rests on the childhood absence epilepsy RCT and on guideline-level reviews, and is closer to an extension of the existing indication than to true repurposing. If a repurposing candidate is needed for this drug, that indication is a better starting point than trigeminal nerve neoplasm.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

