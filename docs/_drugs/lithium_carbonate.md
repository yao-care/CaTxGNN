---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a long-established mood stabiliser (bipolar disorder is its general-knowledge use; the Canadian licence data provided do not list an indication). The TxGNN model predicts it may be effective for **pseudoachondroplasia**, a rare skeletal dysplasia, but **no clinical trials and no publications** currently support this prediction. It is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided licence data (general knowledge: bipolar disorder) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Lithium is known to inhibit GSK-3β and modulate Wnt/β-catenin signalling. This pathway influences chondrocyte and growth-plate biology, which is the only plausible bridge to a skeletal disorder.

Pseudoachondroplasia is caused by COMP gene mutations that lead to protein misfolding and endoplasmic reticulum stress in chondrocytes. No direct link between this disease mechanism and lithium's pharmacology is documented in the provided data. The link is speculative.

The score of 99.98% reflects the model's ranking (rank 825), not clinical evidence. The original psychiatric use and the new skeletal indication share no obvious pharmacological or clinical relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

---

## Other Predicted Candidates

All other candidates are also Hold. Only one has any literature, and it is a general review of genetic skeletal disorder therapies whose relevance to lithium is unconfirmed.

| Rank | Predicted Indication | Score | Evidence Level | Notes |
|------|------|------|------|------|
| 2 | Acromesomelic dysplasia, Hunter-Thompson type | 99.96% | L5 | BMP/Wnt crosstalk only; no data |
| 3 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.96% | L5 | No established link; teratogenicity concern |
| 4 | Brachyolmia | 99.96% | L5 | Speculative Wnt link |
| 5 | Myosclerosis | 99.96% | L5 | Hypothetical antifibrotic effect |
| 6 | Brachyolmia-amelogenesis imperfecta syndrome | 99.96% | L4 | One review ([PMID 31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/), 2019, *Orphanet J Rare Dis*); relevance needs full-text check |
| 7 | Brachydactyly-syndactyly syndrome | 99.95% | L5 | Speculative; teratogenic risk |
| 8 | Behr syndrome | 99.63% | L5 | Preclinical neuroprotection only |
| 9 | WHIM syndrome | 99.56% | L5 | Neutrophil-raising effect; does not target CXCR4 defect |
| 10 | Combined immunodeficiency due to moesin deficiency | 99.29% | L5 | Neutrophil effect only; safety concerns in immunodeficiency |

---

## Canada Market Information

Nine licences are recorded. The five main ones are listed below. Dosage form and approved indication text are not available in the provided data.

| DIN | Product Name |
|---------|------|
| 02011239 | CARBOLITH |
| 00236683 | CARBOLITH |
| 02216132 | PMS-LITHIUM CARBONATE - CAP 150MG |
| 02242837 | APO-LITHIUM CARBONATE |
| 00461733 | CARBOLITH |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Developmental caution**: Lithium is a known teratogen concern. This matters for the developmental and skeletal conditions predicted here.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no publications and no documented mechanistic link. Lithium's known teratogenic concern adds caution for developmental skeletal disorders.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (for example, from DrugBank)
- Targeted literature review on lithium and GSK-3β/Wnt modulation in COMP-related chondrocyte pathology
- Preclinical evidence (for example, a pseudoachondroplasia cell or animal model) before any clinical consideration
- Full-text check of the one retrieved review to confirm whether it mentions lithium

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

