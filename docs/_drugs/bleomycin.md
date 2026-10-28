---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 6
monitor_inn: "BLEOMYCIN"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-10-28
description: "Bleomycin: predicted new indication cauda equina neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Bleomycin
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

## Bleomycin: cytotoxic glycopeptide antibiotic (DNA strand-breaking antineoplastic) → cauda equina neoplasm
{: .text-alpha }

## One-Sentence Summary

Bleomycin is a cytotoxic anticancer agent that breaks DNA strands, and it is marketed in Canada as an injectable product.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, with a score of 0.9930.
However, **no clinical trials** and only **1 publication** (a study of radiation therapy for relapsed CNS germinoma, not bleomycin in cauda equina tumours) are linked to this prediction, so the evidence is limited to the model output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bleomycin is known as a DNA-strand-breaking cytotoxic agent, so in principle it could act on rapidly dividing tumour cells in many tissues.

The single linked paper (PMID 9440744) describes radiation therapy for relapsed CNS germinoma after a primary chemotherapy regimen that included carboplatin, etoposide and bleomycin. It does not show that bleomycin is active in tumours of the cauda equina. The high score is therefore a computational prediction without clinical support.

Delivery to the central nervous system is also a concern, because bleomycin may penetrate the blood-CNS barrier poorly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort | Journal of Clinical Oncology | Retrospective evaluation of radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy including carboplatin, etoposide and bleomycin (PEB). It does not address cauda equina neoplasm directly. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02131692 | BLEOMYCIN FOR INJECTION USP | Not recorded | Not recorded |
| 02265982 | BLEOMYCIN FOR INJECTION | Not recorded | Not recorded |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-damaging glycopeptide antibiotic) |
| Myelosuppression Risk | Low (bleomycin is generally described as marrow-sparing; see package insert) |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function and chest imaging, skin and mucosal changes, liver and renal function, CBC |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified in the interaction query. Most entries are of unknown severity. One is classed as minor (levofloxacin). Others listed include pantoprazole, palonosetron, lactulose, aprepitant, morphine, omeprazole, vancomycin, prednisone and ondansetron.
- Pulmonary toxicity (interstitial pneumonitis and fibrosis) is a recognized risk of bleomycin, as described in the literature linked to other predictions, and is relevant to any new use.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trial studies bleomycin in cauda equina neoplasm, and the one linked paper concerns a different tumour type. CNS penetration and pulmonary toxicity add further concerns.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of bleomycin activity in cauda equina or spinal tumours
- Mechanism of action data and an assessment of blood-CNS barrier penetration, including whether intrathecal or local delivery is feasible
- Package insert warnings and contraindications from Health Canada
- A pulmonary safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

