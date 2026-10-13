---
layout: default
title: Cemiplimab
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab is an anti-PD-1 antibody originally used to treat squamous cell carcinoma (cutaneous squamous cell carcinoma in particular).
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Squamous cell carcinoma (cutaneous squamous cell carcinoma, per the knowledge graph) |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cemiplimab is an antibody that binds human PD-1 (gene *PDCD1*) and blocks its interaction with PD-L1 (IC50 below 1 nM in an ELISA). This releases the brake on T-cell activity against tumours. Its efficacy in cutaneous squamous cell carcinoma has been shown, and it is also approved for some other cancers such as non-small cell lung cancer.

The link to the predicted indication is shared squamous histology. A squamous component in gallbladder adenosquamous carcinoma could plausibly respond to PD-1 blockade. However, adenosquamous biliary tumours are rare and have distinct biology, and no supporting data were available. This is therefore a hypothesis, not demonstrated benefit.

Other high-scoring predictions follow the same pattern (all with evidence level L5 unless noted):
- Glottis and supraglottis squamous cell carcinoma, and non-keratinizing sinonasal squamous cell carcinoma (head and neck squamous types)
- Rectal cloacogenic carcinoma, lung occult squamous cell carcinoma, urethral verrucous carcinoma
- Adenosquamous carcinomas of the prostate and pancreas (tumour types generally poorly responsive to PD-1 monotherapy)
- External ear basal cell carcinoma (L4, one case report; see below)

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for gallbladder adenosquamous carcinoma.

For reference, among the other top-ranked predictions, one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case report | Clinical and Experimental Dermatology | Lasting response after cemiplimab was stopped in a patient with locally advanced basal cell carcinoma (predicted indication: external ear basal cell carcinoma). A single case, not specific to the ear. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02487144 | LIBTAYO | Not available | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 9 moderate-level interactions were identified (DDInter), all with corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort. Corticosteroids may blunt the immune activity that PD-1 blockade relies on, so their use alongside cemiplimab should be reviewed. Separately, the pharmacology record lists its target as PD-1 (CD279).

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.99%), but there are no clinical trials or publications for gallbladder adenosquamous carcinoma. The mechanistic argument rests only on shared squamous histology, and this rare tumour has distinct biology. Evidence is at the model-prediction level (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian licence
- Detailed mechanism of action data from DrugBank
- A literature and trial search specific to biliary adenosquamous carcinoma, and external data on PD-1 inhibitors in biliary tract cancers
- Review of corticosteroid co-medication and a safety monitoring plan
- Prioritisation of candidates with some supporting evidence (for example, head and neck squamous types or basal cell carcinoma) for follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

