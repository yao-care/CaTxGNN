---
layout: default
title: Vandetanib
parent: Moderate Evidence (L3-L4)
nav_order: 959
evidence_level: L3
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Vandetanib: From Advanced Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor. According to the published literature in the Evidence Pack, it is used for advanced medullary thyroid cancer.
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma (RCC)**.
Support so far is thin: **4 clinical trials** (none with reported results; two terminated with 7 or fewer patients) and **6 publications**, none of which is a vandetanib efficacy trial in RCC.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced medullary thyroid cancer (from published literature; Health Canada indication text is not in the input) |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed (CAPRELSA) |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From its known pharmacology, vandetanib inhibits VEGFR2, EGFR and RET. VEGFR2 inhibition blocks tumour blood-vessel formation, and RET is the key driver in medullary thyroid cancer.

Clear cell RCC is a strongly angiogenesis-dependent tumour. Loss of the VHL gene stabilises HIF and drives VEGF overproduction, and VEGFR-targeted kinase inhibitors are already an established RCC drug class. This is why a VEGFR2-blocking drug is mechanistically plausible here. A preclinical study (PMID 15886878) showed that ZD6474 (vandetanib) inhibited angiogenesis and altered tumour microvasculature in a mouse RCC model.

For rare subtypes (FH/SDH-deficient or HLRCC-associated RCC), the rationale is a hypothesised VEGF/EGFR dependence. A very high TxGNN score is a model output, not clinical proof. The other predicted entities are weaker. Ultra-rare, unclassified, TFE3-fusion and childhood RCC have no trials or literature. Angiolipoma and familial spontaneous pneumothorax have no clear mechanistic link and may reflect knowledge-graph proximity only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in Von Hippel-Lindau disease with renal tumours. Directly tests the VHL/HIF/VEGF rationale; no results in the input |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell RCC. Terminated after 3 patients, so uninformative |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC or SDH-associated kidney cancer or sporadic papillary RCC. Rare subset, terminated early |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Carboplatin and gemcitabine with or without vandetanib in advanced urothelial cancer. Indirect for RCC (likely matched via renal pelvis); no results in the input |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15886878](https://pubmed.ncbi.nlm.nih.gov/15886878/) | 2004 | Preclinical | Angiogenesis | ZD6474 inhibited angiogenesis and altered microvascular architecture in an orthotopic mouse RCC model |
| [15519796](https://pubmed.ncbi.nlm.nih.gov/15519796/) | 2004 | Preclinical | Int J Radiat Oncol Biol Phys | ZD6474 combined with a vascular-disrupting agent in human RCC (Caki-1) and Kaposi's sarcoma models |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Other (design not verifiable) | Clin Exp Metastasis | Therapy for metastatic FH-deficient RCC; no standard regimen, several phase 2 combination trials ongoing |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Phase 2 trial (different drug) | Clin Cancer Res | Guadecitabine in SDH-deficient tumours including HLRCC-associated RCC. Context for the rare subtype; not about vandetanib |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical | Mol Cancer Res | Mouse model of TFE3 translocation RCC with new therapeutic targets; no vandetanib data |
| [32691271](https://pubmed.ncbi.nlm.nih.gov/32691271/) | 2021 | Long-term follow-up | Endocrine | Long-term safety of vandetanib in advanced medullary thyroid cancer; background for safety assessment |
| [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/) | 2014 | Meta-analysis | Br J Clin Pharmacol | Incidence and risk of hepatic toxicity with anti-angiogenic TKIs |
| [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/) | 2020 | Meta-analysis | Expert Rev Clin Pharmacol | Proteinuria risk with VEGFR-TKIs, including vandetanib |
| [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) | 2012 | Meta-analysis | Cancer Treat Rev | Treatment-related mortality with VEGFR TKI therapy in advanced solid tumours |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Review of nintedanib that mentions vandetanib among anti-angiogenic agents |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2378590 | CAPRELSA |
| 2378582 | CAPRELSA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2, EGFR, RET) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function and urine protein are suggested by the class-level literature above; otherwise refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No drug-specific warnings, contraindications or interaction data were retrieved. Please refer to the package insert for safety information.

Class-level signals in the retrieved literature are hepatic toxicity, proteinuria and treatment-related mortality with VEGFR TKIs (PMIDs 23981115, 32105149, 22651902). A 2012 Prescrire commentary (PMID 23185843) judged vandetanib "too dangerous" in medullary thyroid cancer, which argues for a careful risk-benefit review before any new use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for RCC is plausible and the TxGNN score is high. However, the on-indication trials are either terminated with tiny enrolment (n=3 and n=7) or completed without reported results (n=37), and the literature contains no clinical efficacy evidence for vandetanib in RCC. Safety signals for this drug class also need to be weighed.

**To proceed, the following is needed:**
- Results of the completed VHL/renal tumour trial (NCT00566995), and confirmation of what the urothelial trial (NCT01191892) found
- The Health Canada product monograph (indication, warnings, contraindications), which is required for safety screening
- Mechanism of action data from DrugBank
- A decision on which RCC subtype to prioritise (clear cell/VHL versus rare FH/SDH-deficient types) and a risk-benefit assessment against established VEGFR-TKI options

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

