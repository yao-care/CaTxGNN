---
layout: default
title: Mitomycin
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Cytotoxic Chemotherapy to Osteoclastic Giant Cell Tumor of Pancreas

## One-Sentence Summary

Mitomycin is a DNA-crosslinking cytotoxic agent marketed in Canada as an injectable. The provided licence records do not list an approved indication.
The TxGNN model predicts it may be effective for **osteoclastic giant cell tumor of pancreas**, but there are currently **0 clinical trials** and **0 publications** for this specific disease, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Osteoclastic giant cell tumor of pancreas |
| TxGNN Prediction Score | 99.86% (model rank 3448) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Mitomycin is a cytotoxic agent that crosslinks DNA, which is a generic antitumour mechanism. That makes a link to pancreatic malignancy plausible, but only in a broad sense.

The model gives several pancreatic tumour subtypes almost identical scores (about 99.8% to 99.9%). This suggests the model is picking up a general "cytotoxic drug and pancreatic cancer" pattern rather than anything specific to this rare subtype. Osteoclastic giant cell tumor of pancreas is a very rare entity. No drug-specific or disease-specific evidence was provided to show that mitomycin works against it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for osteoclastic giant cell tumor of pancreas.

Literature was found for other pancreatic predictions from the same drug. It is old and indirect:

| PMID | Year | Type | Journal | Related Prediction | Key Findings |
|------|-----|------|------|------|---------|
| [2140281](https://pubmed.ncbi.nlm.nih.gov/2140281/) | 1990 | Review | Bull Cancer | Malignant exocrine pancreas neoplasm | Chemotherapy of exocrine pancreatic cancer has a poor response. 5-FU alone is the most active drug (20–30% response). Whether mitomycin was evaluated is not shown in the excerpt. |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Clinical study | Nihon Geka Gakkai Zasshi | Malignant exocrine pancreas neoplasm | Tamoxifen was added to immuno-chemotherapy (including mitomycin) after pancreatic cancer resection. The study focus is hormone therapy, not mitomycin. |
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | Pancreatic IPMN | Adjuvant and neoadjuvant radiochemotherapy in ductal pancreatic carcinoma, which is a different disease entity. |
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | Pancreatic IPMN and IPMN carcinoma | Pseudomyxoma peritonei with pancreatic IPMN managed with intraperitoneal hyperthermic chemoperfusion. It does not show mitomycin efficacy against pancreatic IPMN. |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bull Cancer | Undifferentiated pancreatic carcinoma | Diagnosis and treatment of unknown primary tumours. It is indirect and not specific to mitomycin. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2230451 | MITOMYCIN FOR INJECTION |
| 2464691 | MITOMYCIN FOR INJECTION USP |
| 2531941 | MITOMYCIN FOR INJECTION, USP |

Dosage form and approved indication text were not available in the provided records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-crosslinking antitumour antibiotic) |
| Myelosuppression Risk | High (delayed and cumulative myelosuppression is expected with this class) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelets, renal function, liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are class-level information. Please refer to the package insert warnings and precautions for product-specific details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for osteoclastic giant cell tumor of pancreas has no supporting trials or literature and only a generic mechanistic link (Evidence Level L5, model prediction only). It should not advance on the model score alone.

Among the ten predictions, malignant exocrine pancreas neoplasm is the broadest and most clinically plausible category. It has been marked "Research Question" and should be prioritised for a modern literature and trial review before any pancreatic indication moves forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- A current search of ClinicalTrials.gov and PubMed for mitomycin in pancreatic cancer, including rare subtypes
- Approved indication text for the three Canadian DINs, to establish the original indication and route compatibility
- Expert review of whether evidence for broader pancreatic cancer can be extended to this rare subtype

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

