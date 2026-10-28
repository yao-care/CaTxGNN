---
layout: default
title: Lorlatinib
parent: Model Prediction Only (L5)
nav_order: 560
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "LORLATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
description: "Lorlatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Not recorded in the local data"
---

# Lorlatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lorlatinib: Fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.
Other predictions with some literature (for example lung hilum carcinoma and lung germ cell tumor) are discussed below, but none provides direct evidence for a true new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lorlatinib is a brain-penetrant, third-generation inhibitor of the ALK and ROS1 kinases. Its efficacy in ALK-positive NSCLC is well established, notably in the Phase 3 CROWN trial against crizotinib.

For the top-ranked prediction, the connection is weak. No plausible link between ALK/ROS1 inhibition and fibromatosis, gingival has been identified, and no trials or literature were found. The score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The same applies to the next several predictions: fibroma of lung (score 0.9975) and hamartoma of lung (0.9975) are not ALK-driven, and their high scores probably reflect similarities the model learned between these diseases and the lung cancer indication, not biological evidence.

Some lower-ranked predictions have a more reasonable biological basis, although none is a true repurposing signal:
- **Lung hilum carcinoma (0.9974)**: This is essentially the approved NSCLC indication in a particular anatomical presentation. The only evidence is a 2023 case report of pathological complete response after neoadjuvant lorlatinib in advanced ALK-positive lung cancer.
- **Lung germ cell tumor (0.9974)**: The retrieved literature concerns ALK-driven neuroblastoma (including a Phase 1 trial of lorlatinib with or without chemotherapy) and ALK-fusion glioma case reports, not germ cell tumors. The ALK-driven biology is real, but the evidence does not transfer to this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked predicted indication (gingival fibromatosis). No trials were found for any of the other predicted indications either.

---

## Literature Evidence

Currently no related literature is available for gingival fibromatosis.

For context, the table below lists the most relevant publications retrieved for other predicted indications. They support the existing NSCLC indication or adjacent ALK-driven diseases, not the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33207094](https://pubmed.ncbi.nlm.nih.gov/33207094/) | 2020 | RCT (Phase 3 CROWN) | N Engl J Med | First-line lorlatinib vs crizotinib in advanced ALK-positive NSCLC |
| [38819031](https://pubmed.ncbi.nlm.nih.gov/38819031/) | 2024 | RCT (5-year follow-up) | J Clin Oncol | Long-term progression-free survival and intracranial benefit of lorlatinib over crizotinib |
| [42217582](https://pubmed.ncbi.nlm.nih.gov/42217582/) | 2026 | RCT (7-year update) | Ann Oncol | Long-term CROWN outcomes after 7 years of follow-up |
| [36535300](https://pubmed.ncbi.nlm.nih.gov/36535300/) | 2023 | RCT (post hoc analysis) | Lancet Respir Med | 3-year updated efficacy, including intracranial activity |
| [39368244](https://pubmed.ncbi.nlm.nih.gov/39368244/) | 2024 | Network meta-analysis | Lung Cancer | Lorlatinib compared with other ALK inhibitors as first-line therapy |
| [37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/) | 2023 | Phase 1 trial | Nat Med | Lorlatinib with or without chemotherapy in relapsed/refractory ALK-driven neuroblastoma |
| [37934724](https://pubmed.ncbi.nlm.nih.gov/37934724/) | 2023 | Case report | Am J Case Rep | Pathological complete response after neoadjuvant lorlatinib in advanced ALK-positive lung cancer |
| [38554546](https://pubmed.ncbi.nlm.nih.gov/38554546/) | 2024 | Review | Lung Cancer | Practical guide to managing lorlatinib adverse events |
| [39537504](https://pubmed.ncbi.nlm.nih.gov/39537504/) | 2025 | Case report | J Clin Lipidol | Complex dyslipidemia induced by lorlatinib |
| [40551396](https://pubmed.ncbi.nlm.nih.gov/40551396/) | 2025 | Case report | Pediatr Blood Cancer | Pulmonary toxicity when lorlatinib was given with anti-GD2 antibody in neuroblastoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02485974 | LORBRENA | Not specified | Not specified |
| 02485966 | LORBRENA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Lipid profile and metabolic parameters (hyperlipidemia and metabolic effects are reported); pulmonary symptoms; liver function. Please also refer to the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 interacting drugs. Examples include:
- **Major**: dexamethasone, clarithromycin
- **Moderate**: hydrocortisone, triamcinolone, betamethasone, cimetidine, aprepitant, bupropion, morphine, and several antidiabetic drugs (for example dapagliflozin, empagliflozin, saxagliptin, linagliptin, glimepiride, chlorpropamide)

**Safety signals from the literature** (case reports and pharmacovigilance, not label text):
- Hyperlipidemia, dyslipidemia and wider metabolic effects, including weight gain
- Acute respiratory distress syndrome (case report)
- Pulmonary toxicity when combined with anti-GD2 antibody therapy
- Sweet syndrome (case report)

Health Canada package insert warnings and contraindications were not available for this report, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gingival fibromatosis prediction has a very high model score (0.9981) but no trials, no literature and no plausible mechanism linking ALK/ROS1 inhibition to the disease. The evidence is at L5, model prediction only. The other top predictions are either benign or non-ALK-driven conditions without evidence, or restatements of the approved NSCLC indication. Lorlatinib's metabolic and pulmonary toxicity also argue against pursuing a benign indication without a clear biological rationale.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a testable biological hypothesis linking lorlatinib's targets to gingival fibromatosis
- The Health Canada package insert warnings and contraindications, which are required for safety screening
- Approved indication text, dosage forms and manufacturer details for the two Canadian DINs
- Preclinical or early clinical evidence in the target disease, if the hypothesis is pursued
- A separate review of neuroblastoma and other ALK-driven tumours, where the literature shows a real mechanistic link, if a genuine repurposing direction is wanted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

