---
layout: default
title: Darolutamide
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Darolutamide: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Not listed in the Canadian license data compiled for this report"
monitor_inn: "Darolutamide"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "cytomegalovirus infection", "thrombotic disease", "infectious bovine rhinotracheitis", "malignant catarrh"]
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is a non-steroidal androgen receptor antagonist marketed in Canada as NUBEQA. The TxGNN model's top-ranked prediction is **homozygous familial hypercholesterolemia**, but **no clinical trials and no publications** support it. This is a model-only prediction with very weak evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data compiled for this report (darolutamide is an androgen receptor antagonist; its use in prostate cancer is general knowledge, not taken from the data) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, darolutamide is a non-steroidal androgen receptor antagonist.

Homozygous familial hypercholesterolemia is caused by defects in the LDL receptor pathway. There is no clear mechanistic link between androgen receptor blockade and this pathway. The high TxGNN score (99.11%) reflects a network-based prediction only, with no supporting trials or literature, so it should not be read as evidence of efficacy.

Other top-ranked predictions show the same pattern. Most are low-plausibility or likely knowledge-graph artifacts: HIV infection, feline and simian immunodeficiency, cytomegalovirus infection, bovine rhinotracheitis, and malignant catarrh. Two have slightly more context:

- **Multiple endocrine neoplasia (rank 2, score 99.06%):** Two trials were found, both in androgen-driven (likely prostate) cancer settings, where darolutamide's mechanism is relevant. The match to MEN syndromes is probably a disease-classification artifact.
- **Thrombotic disease (rank 8, score 98.29%):** One case report was found. It concerns paraneoplastic syndromes in prostate cancer and is not evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for homozygous familial hypercholesterolemia.

For reference, the trials linked to the second-ranked prediction (multiple endocrine neoplasia) are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07795177](https://clinicaltrials.gov/study/NCT07795177) | Phase 2 | Not yet recruiting | 40 | Spatial multi-omics study predicting response to androgen deprivation plus second-generation endocrine agents in metastatic hormone-sensitive prostate cancer. Not relevant to MEN. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision-oncology platform study. Terminated after only 2 participants, so no usable efficacy or safety signal. |

---

## Literature Evidence

Currently no related literature available for homozygous familial hypercholesterolemia.

For reference, the only publication found among the top predictions (thrombotic disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41669591](https://pubmed.ncbi.nlm.nih.gov/41669591/) | 2026 | Case report | Cureus | A 72-year-old man with BRCA2-mutated metastatic prostate cancer developed SIADH and thrombotic microangiopathy as paraneoplastic syndromes. Does not show that darolutamide treats thrombosis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02496348 | NUBEQA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (androgen receptor antagonist), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** The interaction screening completed with **100 interactions** recorded. The 20 listed in the data include several Major-level interactions:
  - **Major:** Dexamethasone, Eluxadoline, Rosuvastatin
  - **Moderate:** Clarithromycin, Empagliflozin, Glyburide, Glycerol phenylbutyrate, Metreleptin, Repaglinide, Rifaximin, Simvastatin, Sulfasalazine, Troglitazone, Cobicistat, Deferasirox, Eltrombopag, Lusutrombopag
  - **Minor:** Aprepitant, Cimetidine, Miconazole

  The Major interaction with rosuvastatin and the Moderate interaction with simvastatin are particularly relevant for a lipid-disorder indication, since patients would likely be on statins.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials or literature behind it and no plausible mechanistic link between androgen receptor antagonism and LDL receptor pathway defects. Evidence is L5 (model prediction only). The statin interactions add a further concern for this indication.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to allow a mechanistic-link analysis
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Approved indication text, dosage form, and manufacturer for the Canadian license
- Preclinical or mechanistic evidence linking androgen receptor signaling to LDL receptor or cholesterol metabolism, before any clinical study is considered
- An assessment of whether the lower-ranked predictions (such as multiple endocrine neoplasia) reflect true biology or classification artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

