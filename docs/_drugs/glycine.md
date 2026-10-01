---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Glycine: From Unlisted Original Indication to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid used in Canada mainly as an ingredient in irrigation solutions, a parenteral nutrition product (Clinimix) and a sterile diluent. Its approved indication text is not available in the data reviewed.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the prediction rests on the model alone: **1 clinical trial** and **2 publications** were retrieved, and none of them tests glycine for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Glycine is a simple amino acid that appears in Canada as a component of irrigation solutions, nutrition products and a diluent. Its original indication is not recorded in the data supplied, so the prediction cannot be checked against known clinical use.

Glycine is known to act on glycine-gated chloride channels on immune and epithelial cells. This gives it plausible general anti-inflammatory and cytoprotective properties, which could in theory relate to inflamed nasal mucosa. However, the supplied data show no specific mechanism linking glycine to nasal cavity disease.

The very high score (99.85%, model rank 3,614) reflects a pattern in the knowledge graph, not confirmed biology or clinical results. It should be treated as a hypothesis to test.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET imaging study of a radiotracer (18F-FPPRGD2) in glioblastoma, gynaecological cancer and renal cell carcinoma. It does not test glycine, and the link to this prediction is probably a keyword artifact (relevance grade C). |

No registered trial tests glycine for nasal cavity disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic science (animal tissue) | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. It describes tissue glycoconjugates, not glycine treatment. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical formulation study | Chemical & Pharmaceutical Bulletin | Oligoarginine-polymer conjugates as a mucosal adjuvant for nasal vaccination in mice. It is unrelated to glycine as a therapy. |

Neither publication provides clinical evidence for glycine in nasal cavity disease.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 498793 | GLYCINE IRRIGATION USP |
| 799955 | GLYCINE 1.5% IRRIGATION USP SOL |
| 2443651 | PH 12 STERILE DILUENT FOR FLOLAN |
| 2046709 | CLINIMIX |
| 2013932 | CLINIMIX |

Showing 5 of 20 authorizations. Dosage form and approved indication text are not available for these products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). The one retrieved trial and both publications are unrelated to glycine treatment, and there is no mechanistic or clinical support for nasal cavity disease. Safety data are also missing, so the candidate cannot move past the initial screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indications and dosage forms for the Canadian glycine products
- Mechanism of action data, for example from DrugBank
- Preclinical or clinical studies of glycine in nasal or upper airway inflammation
- Assessment of whether a route suitable for nasal use exists, since the current products are irrigation, nutrition and diluent formulations

**Note:** The second predicted indication, acute laryngopharyngitis (score 99.84%), is in the same position. It has no supporting trials, and its one retrieved publication concerns a different drug, so it is also on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

