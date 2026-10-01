---
layout: default
title: Temozolomide
parent: High Evidence (L1-L2)
nav_order: 881
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **2** 
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

# Temozolomide: From an Unrecorded Original Indication to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug marketed in Canada, but the record does not list its original approved indication.
The TxGNN model predicts it may be effective for **adult astrocytic tumour** (glioblastoma and anaplastic astrocytoma), with **2 registered clinical trials** and **20 publications** supporting this direction.
Astrocytic tumours are an established temozolomide use, so this is probably confirmation of an existing indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Health Canada licence data |
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral alkylating agent. It methylates DNA (at O6-guanine), creating cytotoxic lesions in glioma cells. Benefit depends on the tumour's MGMT promoter methylation status, because methylation limits the cell's ability to repair this damage.

Detailed mechanism of action data is not available in the record, and no original indication is listed. The standard-of-care role of temozolomide in glioblastoma and anaplastic astrocytoma is nonetheless well documented in the retrieved literature. The high TxGNN score (0.994) agrees with this clinical record.

Because the record's original indication field is empty, check the labelled indications in the Health Canada record before treating this as a new candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised comparison of temozolomide vs PCV (procarbazine, lomustine, vincristine) in recurrent WHO grade III–IV astrocytic tumours. Directly tests temozolomide in the target population. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding and safety study of XL184 (cabozantinib) with temozolomide and radiotherapy in first-line glioblastoma. Supportive safety data only, not temozolomide efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Radiotherapy alone vs radiotherapy plus concomitant and adjuvant temozolomide in glioblastoma (efficacy and safety). |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | Five-year final analysis of the EORTC-NCIC phase III trial of radiotherapy with temozolomide vs radiotherapy alone. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 phase 3: lomustine-temozolomide vs standard temozolomide in MGMT-methylated newly diagnosed glioblastoma. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 phase 3: dose-dense temozolomide alone vs radiotherapy alone in elderly patients with anaplastic astrocytoma or glioblastoma. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Maintenance tumour-treating fields plus temozolomide vs temozolomide alone in glioblastoma. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Bevacizumab added to temozolomide and radiotherapy (the standard of care) in newly diagnosed glioblastoma. |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT | J Neurooncol | Exploratory cohort of newly diagnosed anaplastic astrocytoma or oligo-astrocytoma treated with radiotherapy and temozolomide. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG BN007 phase II/III: dual immune checkpoint blockade in MGMT-unmethylated newly diagnosed glioblastoma. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Review of glioblastoma and other primary adult brain malignancies. |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early review of temozolomide in malignant glioma (glioblastoma and anaplastic astrocytoma). |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02241093 | TEMODAL |
| 02389835 | ACH-TEMOZOLOMIDE |
| 02443554 | TARO-TEMOZOLOMIDE |
| 02516810 | JAMP TEMOZOLOMIDE |
| 02395282 | TEVA-TEMOZOLOMIDE |

The record lists 20 licences in total; the 5 above are shown. Dosage form and approved indication text are not available for these entries.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Medium to high (neutropenia and thrombocytopenia are expected, especially in combination with radiotherapy or lomustine) |
| Emetogenicity Classification | Low to moderate, depending on dose |
| Monitoring Items | CBC with differential, liver function, renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomised phase 3 trials support temozolomide in adult astrocytic tumours, including the registered NCT00052455 and the published EORTC-NCIC, NOA-08 and CeTeG/NOA-09 trials. The indication appears to be established practice rather than a new use, so the main task is confirmation, not discovery.

**To proceed, the following is needed:**
- Confirm the labelled indications in the Health Canada records, which are currently blank, to decide whether this is truly new
- Obtain the package insert warnings and contraindications (a blocking gap for safety screening)
- Add detailed mechanism of action data from DrugBank
- Consider MGMT promoter methylation status for patient selection

**Secondary candidate:** Cauda equina neoplasm (score 99.30%) has only one case report (a relapsed spinal myxopapillary ependymoma) and no registered trials. It is a research question (Level L4) and not ready for development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

