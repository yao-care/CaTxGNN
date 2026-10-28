---
layout: default
title: Eptifibatide
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eptifibatide: predicted new indication Rheumatoid arthritis. The top-ranked prediction… (evidence level L5). Approved use: Acute coronary syndrome"
monitor_inn: "Eptifibatide"
predicted_indications: ["rheumatoid arthritis", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "hemoglobinopathy", "female breast carcinoma", "beta-thalassemia with other manifestations", "partial deletion of the short arm of chromosome 16"]
---

# Eptifibatide
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

## Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Eptifibatide is a platelet glycoprotein (GP) IIb/IIIa inhibitor originally used to treat acute coronary syndrome.
The TxGNN model's top-ranked prediction is rheumatoid arthritis, which has no supporting studies. The best-supported prediction is **hemoglobinopathy (mainly sickle cell disease)**, with **1 clinical trial** and **4 publications** behind it.
This report therefore focuses on hemoglobinopathy, the only prediction with human evidence, while noting the top-ranked prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (the Canadian licence records provide no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9998 (hemoglobinopathy); 0.9999 (rheumatoid arthritis, rank 1) |
| Evidence Level | L5 (hemoglobinopathy); L5 (rheumatoid arthritis) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold (hemoglobinopathy is a research question: it merits further study but is not ready for escalation) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, eptifibatide is a synthetic peptide that blocks the GP IIb/IIIa (αIIbβ3) receptor on platelets and so prevents platelet aggregation. This is why it works in acute coronary syndrome, where platelet-rich clots block coronary arteries.

In sickle cell disease, platelet activation, adhesion, thrombosis and inflammation are thought to contribute to microvascular occlusion and painful crises. Researchers have therefore proposed that blocking platelet aggregation could reduce these episodes. Early human studies examined safety, pain episodes and inflammatory markers, and an in vitro microvascular model supports the mechanism.

Several other sickle cell genotypes (HbSC, HbSD, HbSE, sickle-beta-thalassemia, and sickle cell with hereditary persistence of fetal hemoglobin) share the same score of 0.9998. Their rationale is extrapolated from sickle cell anemia, with no genotype-specific evidence. For rheumatoid arthritis, platelet activation and integrin signalling might contribute to synovial inflammation, but nothing supports this link yet.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Randomized, double-blind, placebo-controlled study of eptifibatide safety and efficacy during acute pain episodes in sickle cell disease. It was stopped early with only 13 participants, so it cannot support efficacy conclusions. |

No clinical trials are registered for the other nine predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase I study | Br J Haematol | Safety and pharmacodynamics of eptifibatide in four patients with sickle cell anaemia in a steady, non-crisis state; examined inhibition of platelet aggregation and CD40L release. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot clinical study | Thromb Res | Evaluated the safety and efficacy of eptifibatide in patients with sickle cell disease during acute painful episodes. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Clinical study | Am J Hematol | Looked at the effect of eptifibatide on inflammation markers during acute pain episodes in sickle cell disease. |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro model | J Clin Invest | A microfluidic model of microvascular occlusion and thrombosis in sickle cell disease and hemolytic uremic syndrome, supporting the biological rationale. |

Other predictions have little literature. Female breast carcinoma has two preclinical studies (PMIDs 25090985 and 33522559: cell-line and organ-on-chip work showing proapoptotic and anti-metastatic effects of αIIbβ3 inhibition). HbSC disease has one tolerability study in acute coronary syndrome (PMID 24678072), whose relevance to HbSC cannot be confirmed.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02540827 | EPTIFIBATIDE INJECTION | Not specified | Not specified |
| 02540819 | EPTIFIBATIDE INJECTION | Not specified | Not specified |

---

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not taken from label text): thrombocytopenia, blood coagulation disease, and impaired renal function disease.
- **Drug Interactions**: 100 interactions were found in total. The main ones are:
  - **Major**: deferasirox, ibritumomab tiuxetan, tositumomab (I-131).
  - **Moderate**: acetylsalicylic acid, dexfenfluramine, fenfluramine, sibutramine.
  - Other listed interactions have no assigned severity level (for example pantoprazole, omeprazole, morphine, simvastatin, prednisone).
- **Population-specific concern**: bleeding risk is the main issue, especially in sickle cell patients who are often hospitalized, and in oncology patients.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hemoglobinopathy (sickle cell disease) is the most credible prediction, with a plausible mechanism and early human studies. However, the only registered trial was terminated with 13 participants, so efficacy remains unproven. All other predictions, including the top-ranked rheumatoid arthritis, have either no evidence or only preclinical evidence. Hemoglobinopathy is best treated as a research question rather than a candidate ready to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- Detailed mechanism of action data
- A larger, adequately powered randomized trial in sickle cell disease, with a bleeding-risk assessment
- Review of the existing pilot study results to judge efficacy signals
- For the other predictions (rheumatoid arthritis, other sickle cell genotypes, breast carcinoma), any clinical or genotype-specific evidence before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

