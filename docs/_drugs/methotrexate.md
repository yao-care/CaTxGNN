---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Established Antifolate Uses to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is a long-established antifolate drug, and it is currently marketed in Canada under 20 DINs.
The TxGNN model predicts it may be effective for **pulmonary blastoma**, a rare lung tumour, with a score of 99.45%.
However, **0 clinical trials** and **0 publications** were retrieved for this specific indication, so the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records provided |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general pharmacology, methotrexate is an antifolate that inhibits dihydrofolate reductase (DHFR). This blocks nucleotide synthesis and suppresses rapidly dividing cells. Its cytotoxic activity is established in several cancers.

Pulmonary blastoma is a rare malignant lung tumour. A generic antiproliferative mechanism could in principle apply to it. Nothing in the retrieved data links methotrexate to this tumour specifically, and no disease-specific mechanism has been checked. The high TxGNN score is therefore a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorizations are listed below. Dosage form, manufacturer and approved-indication text were empty in the source records.

| DIN | Product Name |
|---------|------|
| 2099705 | Methotrexate Sodium Injection |
| 2454874 | Metoject Subcutaneous |
| 2491338 | Methotrexate Subcutaneous |
| 2454831 | Metoject Subcutaneous |
| 2454769 | Metoject Subcutaneous |

---

## Cytotoxicity

The general profile below comes from the drug class, not from the Evidence Pack. Please confirm against the package insert warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite / antifolate) |
| Myelosuppression Risk | Medium to high, dose-dependent |
| Emetogenicity Classification | Low to moderate, depending on dose |
| Monitoring Items | CBC with differential, liver and renal function, pulmonary symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature for related lymphoma searches also describes two methotrexate-associated signals. These are methotrexate-associated lymphoproliferative disorders, some of them EBV-related, and methotrexate-induced lung injury. The lung injury signal matters most for any pulmonary indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). No trials or publications support methotrexate in pulmonary blastoma, and no mechanism has been checked against the record.

Other ranked candidates in this pack have more supporting material, though still indirect:
- **Primary pulmonary lymphoma (rank 2):** rated L4, with case reports and primary CNS lymphoma data.
- **Small cell lung carcinoma (rank 3):** rated L3, with historical combination-regimen studies from 1978 to 1985.
- **Hodgkin lymphoma (rank 5):** rated L3, with historical VBM regimen studies.

These would be more sensible starting points for a deeper review.

**To proceed, the following is needed:**
- A targeted literature review of methotrexate in pulmonary blastoma, including case reports and registries
- Mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications
- Approved-indication text for the Canadian authorizations
- A review of pulmonary toxicity risk, given the methotrexate lung injury reports

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

