---
layout: default
title: Eptifibatide
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is an injectable platelet inhibitor (a GP IIb/IIIa antagonist) used in acute coronary syndrome. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials and no publications** currently support this specific prediction. Among the other predicted indications, **hemoglobinopathy (sickle cell disease)** has the most human evidence, with **1 clinical trial** and **4 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; the linked literature describes use in acute coronary syndrome |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, eptifibatide is a GP IIb/IIIa antagonist that blocks platelet aggregation. Its efficacy in acute coronary syndrome is established.

Platelet activation has been proposed to contribute to synovial inflammation in rheumatoid arthritis, so a link is conceivable. This idea is speculative. No trials or literature were found, and the very high score (99.99%) reflects a knowledge-graph prediction, not a confirmed effect.

**A stronger lead exists elsewhere in the list.** Rank 7, hemoglobinopathy (sickle cell disease), has a clearer rationale. Platelet activation and GP IIb/IIIa-mediated adhesion contribute to vaso-occlusion and inflammation in sickle cell disease, and eptifibatide has been tested directly in patients (see below). The other sickle-syndrome variants (HbSD, HbSE, HbS-beta-thalassemia, HPFH-sickle) are indirect extrapolations with no disease-specific data.

Two lower-ranked predictions look unlikely:
- **Beta-thalassemia and partial deletion of chromosome 16p** are probably knowledge-graph artifacts driven by hemoglobinopathy proximity, with no plausible antiplatelet mechanism.
- **Female breast carcinoma** rests only on preclinical work: αIIbβ3 blockade induced apoptosis in MCF-7 cells in vitro, and integrin/platelet interactions may shape the metastatic niche.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

For the best-supported alternative, hemoglobinopathy (sickle cell disease):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Randomized, double-blind, placebo-controlled safety study of eptifibatide for acute pain episodes in sickle cell disease. It is direct evidence, but too small to assess efficacy. |

---

## Literature Evidence

Currently no related literature available for rheumatoid arthritis.

For hemoglobinopathy (sickle cell disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase 1 trial | Br J Haematol | Safety and pharmacodynamics of eptifibatide in four steady-state sickle cell anaemia patients. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot clinical study | Thromb Res | Evaluated safety and efficacy of eptifibatide during acute painful episodes in sickle cell disease. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Clinical study | Am J Hematol | Effect of eptifibatide on inflammation biomarkers during acute pain episodes (no abstract available). |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro model | J Clin Invest | Microfluidic model of microvascular occlusion and thrombosis in sickle cell disease and hemolytic uremic syndrome. |

**Citation to verify:** PMID 24678072 (linked to sickle cell-hemoglobin C disease) appears to describe eptifibatide in acute coronary syndrome, not a sickle-specific study. Its title is truncated and its year (2005) does not match the PMID, so it should not be counted as supporting evidence.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2540827 | EPTIFIBATIDE INJECTION | Not listed | Not listed |
| 2540819 | EPTIFIBATIDE INJECTION | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

Bleeding risk is the key consideration for any new use of a GP IIb/IIIa antagonist. It is noted in the sickle cell rationale and needs to be weighed against benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For rheumatoid arthritis, the prediction rests only on a model score, with no trials, no literature and a speculative mechanism. The sickle cell disease direction is more credible, but the only randomized trial was terminated early with 13 patients and efficacy is unproven.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For rheumatoid arthritis: any preclinical or clinical evidence that platelet GP IIb/IIIa blockade affects synovial inflammation
- For sickle cell disease: a full review of the terminated trial and the pilot studies, and a bleeding-risk assessment, before considering a research question
- Verification of the PMID 24678072 citation
- Route and dosage-form compatibility assessment, since the Canadian licence records list no dosage form or indication text

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

