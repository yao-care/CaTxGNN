---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 742
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
description: "Pirfenidone: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pirfenidone: Extracutaneous mastocytoma
{: .text-alpha }

## One-Sentence Summary

Pirfenidone is an anti-fibrotic drug originally used to treat idiopathic pulmonary fibrosis and related interstitial pneumonias.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 14 of 14) |
| Number of DINs | 14 (valid: 14) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pirfenidone is a small-molecule anti-fibrotic agent whose efficacy in idiopathic pulmonary fibrosis has been established, and it may mechanistically be applicable to mast cell-related disease.

The proposed link is pirfenidone's anti-fibrotic and anti-inflammatory activity, namely modulation of TGF-beta and TNF-alpha, which might act on the stromal response around mast cell lesions. This link is plausible but unverified. No direct evidence supports it, and the relationship to the original lung-fibrosis indication has not yet been assessed.

The score should be read with caution. The ten top-ranked predictions are dominated by fibroblast-lineage tumours (fibrosarcomas, dermatofibrosarcoma protuberans), mastocytosis-type diseases and a few unrelated conditions. Many of these are driven by specific oncogenic mechanisms (for example KIT mutations or the COL1A1-PDGFB fusion) that pirfenidone is not known to target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for extracutaneous mastocytoma.

For context, the closest related prediction, **fibroblastic neoplasm** (rank 9, evidence level L4), has indirect literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project testing pirfenidone for desmoid tumours in familial adenomatous polyposis; details not available |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Pirfenidone affected TGF-β1-stimulated non-SMAD signalling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical/Review | Pharm Dev Technol | Pirfenidone proposed as a local injectable anti-fibrotic for Dupuytren's disease |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Permanente J | Undifferentiated pleomorphic sarcoma after pirfenidone use (safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in systemic sclerosis (safety signal) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02464500 | ESBRIET | Not specified | Not specified |
| 02464489 | ESBRIET | Not specified | Not specified |
| 02488515 | SANDOZ PIRFENIDONE TABLETS | Not specified | Not specified |
| 02531526 | PMS-PIRFENIDONE | Not specified | Not specified |
| 02514710 | JAMP PIRFENIDONE | Not specified | Not specified |

These are 5 of the 14 valid single-ingredient authorizations, and none are cancelled. Other holders include Sandoz (tablets and capsules), M-Pirfenidone, Auro-Pirfenidone and further JAMP and PMS products.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs, and the 20 shown are all rated Moderate. They include bupropion, omeprazole, esomeprazole, lansoprazole, cimetidine, eliglustat, obeticholic acid, naltrexone, miconazole, nitisinone, deferasirox, ticlopidine, lumefantrine, disulfiram, primaquine, thiabendazole and ivacaftor.
- **Case reports in related tumour types**: A report of undifferentiated pleomorphic sarcoma after pirfenidone use, and one of dermatofibromas aggravated by pirfenidone, are a caution for fibroblast-lineage tumours.
- **Liver**: Hepatotoxicity is a recognised risk of pirfenidone, which is relevant for any use in a compromised liver.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for extracutaneous mastocytoma is supported only by the model score (0.9971). There are no clinical trials or publications, and the proposed mechanism is speculative. Related case reports raise a safety signal in fibroblast-lineage tumours.

**To proceed, the following is needed:**
- Mechanism of action data for pirfenidone
- Package insert warnings and contraindications from Health Canada, which is a blocking gap for safety screening
- A targeted literature search for pirfenidone in mast cell disease, plus preclinical data in mast cell models
- An assessment of how the predicted disease relates to the original lung-fibrosis indication
- Dosage form and route information, to check whether the available oral products suit the disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

