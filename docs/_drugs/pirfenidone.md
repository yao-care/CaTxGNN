---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an oral antifibrotic drug, originally used to treat idiopathic pulmonary fibrosis (IPF). The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, but **no clinical trials and no publications** support this prediction. Among the top 10 predictions, only **fibroblastic neoplasm** has any literature (6 publications, mostly preclinical or case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (from literature; the Health Canada licence records contain no indication text) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. According to the published literature, pirfenidone inhibits several growth factors, including TGF-β, PDGF, EGF and FGF. This reduces fibroblast proliferation and collagen synthesis. Its efficacy in pulmonary fibrosis is the basis for its approval.

For the top-ranked prediction, extracutaneous mastocytoma, there is no clear mechanistic link. Mast cell neoplasia is driven mainly by KIT mutations, and no pirfenidone-relevant mechanism is documented. The high score is therefore not supported by clinical or mechanistic evidence. It may reflect only the knowledge graph's internal associations.

Most other top-10 predictions are fibroblastic tumours (fibrosarcoma, dermatofibrosarcoma protuberans, low grade fibromyxoid sarcoma). For these, TGF-β/fibroblast modulation gives a weak theoretical rationale. Whether pirfenidone would promote or suppress tumour growth in sarcoma is unknown. Other predictions include familial Mediterranean fever (anti-inflammatory effects only in preclinical models; colchicine is the established therapy) and hepatic infarction (pirfenidone is itself associated with liver enzyme elevation).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for extracutaneous mastocytoma. None of the other nine top-10 predicted indications has a registered trial either.

---

## Literature Evidence

No related literature is available for extracutaneous mastocytoma.

The only candidate with any literature is **fibroblastic neoplasm** (rank 9, TxGNN score 99.23%, evidence level L4). It is shown here for reference. Several records were truncated in the input, so study details could not be fully verified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project testing pirfenidone for desmoid tumours in familial adenomatous polyposis. This is the closest clinical signal. The design and outcome could not be verified from the available text. |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma after pirfenidone use. This is a potential safety signal. |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis. |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone showed anti-fibrotic action in Dupuytren's disease-derived fibroblasts by inhibiting TGF-β1-mediated effects. |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Effects on TGF-β1-stimulated non-SMAD signalling pathways in Dupuytren's disease-derived fibroblasts. |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical | Pharm Dev Technol | Pirfenidone explored as a local injectable antifibrotic for Dupuytren's disease. |

Overall, the evidence is indirect and mixed on benefit versus harm. Dupuytren's disease is a benign fibroproliferative disorder, not a malignancy.

---

## Canada Market Information

Health Canada lists 14 licences for pirfenidone. Dosage form and approved indication text are not available in the records received.

| DIN | Product Name |
|---------|------|
| 02488515 | SANDOZ PIRFENIDONE TABLETS |
| 02531526 | PMS-PIRFENIDONE |
| 02464500 | ESBRIET |
| 02464489 | ESBRIET |
| 02531534 | PMS-PIRFENIDONE |

---

## Safety Considerations

- **Literature safety signals:** Two case reports raise concern in fibroblastic tumour settings. One describes an undifferentiated pleomorphic sarcoma arising after pirfenidone use. The other describes dermatofibromas aggravated by pirfenidone together with mycophenolate. Case reports cannot establish causality.
- **Hepatic effects:** Pirfenidone is associated with liver enzyme elevation, which argues for caution in any hepatic injury setting.
- **Drug interactions:** No interaction records were retrieved.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on the model score alone, with no trials, no literature and no mechanistic link to mast cell neoplasia. The only partly supported candidate, fibroblastic neoplasm, has indirect preclinical evidence and two case reports that suggest possible harm. Treat it as a research question, not a development candidate.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication), which is a blocking item for safety screening
- Mechanism of action data from DrugBank
- A targeted literature search on pirfenidone in mast cell neoplasms and fibroblastic tumours, including the full text and outcomes of the desmoid tumour pilot study
- A review of the sarcoma and dermatofibroma case reports to assess whether pirfenidone could promote tumours
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

