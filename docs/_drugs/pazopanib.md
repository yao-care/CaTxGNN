---
layout: default
title: Pazopanib
parent: High Evidence (L1-L2)
nav_order: 705
evidence_level: L2
indication_count: 10
---

# Pazopanib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Pazopanib: From Its Approved Indication (Not Listed in the Input) to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Pazopanib is a multi-targeted tyrosine kinase inhibitor, and the input does not list its original approved indication. The TxGNN model predicts it may be effective for **unclassified renal cell carcinoma**. This direction is supported by **1 related clinical trial** (a completed Phase 3 that is not subtype-specific) and **6 publications**, including a Phase 2 single-arm study in non-clear cell RCC.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the input (the rationale expects an advanced renal cell carcinoma label, but this is unconfirmed) |
| Predicted New Indication | Unclassified renal cell carcinoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Pazopanib inhibits VEGFR, PDGFR and c-KIT. Anti-angiogenic therapy is established in renal cell carcinoma (RCC), so a drug with this mechanism is a plausible candidate for RCC subtypes.

Unclassified RCC falls under non-clear cell RCC. Non-clear cell disease is less VEGF-driven than clear cell disease, so efficacy is plausible but less certain. Non-clear cell RCC is also underrepresented in clinical trials, and treatment is often extrapolated from clear cell data. In clear cell RCC, pazopanib has shown non-inferiority to sunitinib.

Direct prospective evidence is limited to one single-arm Phase 2 study and several retrospective cohorts. The only Phase 3 trial in the package is not specific to non-clear cell or unclassified histology. The high TxGNN score reflects the model's prediction and is not histology-specific proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Completed | 544 | Randomized sequential study of sorafenib then pazopanib versus pazopanib then sorafenib in advanced or metastatic RCC. It is high quality but not restricted to non-clear cell or unclassified histology, so it is indirect for this subtype. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 single-arm | Cancer Res Treat | Open-label multicenter study of pazopanib's efficacy and safety in metastatic non-clear cell RCC. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | PANORAMA, an Italian multicenter study of first-line pazopanib efficacy and toxicity in non-clear cell RCC. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Cohort | Clin Genitourin Cancer | Outcomes of pazopanib in metastatic non-clear cell RCC, where data were previously limited. |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world cohort | Ecancermedicalscience | Compares first-line sunitinib and pazopanib in non-clear cell and sarcomatoid RCC. |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Cohort | Eur Urol Oncol | IMDC data comparing contemporary (immuno-oncology-based or cabozantinib) and traditional first-line therapies across non-clear cell subtypes, including unclassified RCC. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Cohort (indirect) | Clin Genitourin Cancer | Carcinoma of unknown primary with RCC-like features treated with targeted therapy; indirect relevance. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2352303 | VOTRIENT |
| 2552957 | AURO-PAZOPANIB |
| 2525666 | PMS-PAZOPANIB |

Dosage form, manufacturer and approved indication text were not provided for these authorizations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted VEGFR/PDGFR/c-KIT tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and there are prospective and real-world data in non-clear cell RCC, but direct evidence for the unclassified subtype is limited to a single-arm Phase 2 study and retrospective cohorts. The one Phase 3 trial is indirect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text for the Canadian authorizations, to confirm the original indication
- Results specific to the unclassified RCC subgroup from the Phase 2 study and the IMDC cohort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

