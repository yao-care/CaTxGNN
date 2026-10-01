---
layout: default
title: Trastuzumab Deruxtecan
parent: Model Prediction Only (L5)
nav_order: 926
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab deruxtecan: From HER2-Positive Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan (marketed in Canada as ENHERTU) is a HER2-directed antibody-drug conjugate with a topoisomerase I inhibitor payload, used in HER2-expressing cancers.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a graph-based signal only and has no biological or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence record (the drug is a HER2-directed ADC used in HER2-expressing cancers) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, trastuzumab deruxtecan combines a HER2-targeting antibody with a cytotoxic topoisomerase I inhibitor payload. Its efficacy is established in HER2-expressing cancers.

The data does not support a mechanistic link to drug-induced osteoporosis. No bone-metabolism pathway is evident for a HER2-directed cytotoxic ADC. Osteoporosis is a bone-remodelling disorder, and nothing connects HER2 targeting or topoisomerase I inhibition to it. The high TxGNN score (0.993, rank 11,995) most likely reflects knowledge-graph neighbourhood effects rather than real biology.

The other nine predicted indications are also unsupported. These include diabetic retinopathy, bronchitis, diabetic cataract and several rare tumours. The respiratory prediction (bronchitis) is especially concerning because interstitial lung disease and pneumonitis are known class toxicities of this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2514400 | ENHERTU |

The dosage form and approved indication text are not listed in the record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor payload) |
| Myelosuppression Risk | Medium (neutropenia and other cytopenias are expected with this payload class; confirm against the product monograph) |
| Emetogenicity Classification | Medium (confirm against the product monograph) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, respiratory symptoms and imaging for lung toxicity, cardiac function (LVEF) |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for authoritative details.

---

## Safety Considerations

- **Key Warnings**: Interstitial lung disease and pneumonitis are known class toxicities of this drug. This is relevant to the bronchitis prediction and to any use outside the approved oncology setting.
- **Renal toxicity**: A case report describes deruxtecan-induced reversible Fanconi syndrome ([PMID 37492824](https://pubmed.ncbi.nlm.nih.gov/37492824/), 2023).
- **Systemic cytotoxic exposure**: This is a safety concern for any non-oncology indication.

No drug interaction data were found in the query.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN score alone, with no clinical trials, no literature, and no plausible mechanism linking a cytotoxic HER2-directed ADC to osteoporosis. Using a toxic systemic agent for a non-malignant bone disorder is not justified without evidence. All ten predicted indications for this drug are currently rated Hold at evidence level L5.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal linking the drug to bone metabolism
- For the oncology-type predictions (for example, tumour of testis and paratestis), a HER2 expression feasibility check as a prerequisite
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

