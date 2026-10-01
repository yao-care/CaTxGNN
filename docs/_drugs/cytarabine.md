---
layout: default
title: Cytarabine
parent: Moderate Evidence (L3-L4)
nav_order: 236
evidence_level: L4
indication_count: 9
---

# Cytarabine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine is a nucleoside-analog chemotherapy drug. The retrieved literature describes it as one of the most effective drugs against adult acute leukemia; the Canadian license records supplied no indication text.
The TxGNN model predicts it may be effective for **small cell lung carcinoma (SCLC)**, but the supporting evidence is weak: **3 clinical trials** were retrieved and **none tests cytarabine in SCLC**, and the **20 publications** are mostly old or indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license records (the literature describes use in acute leukemia) |
| Predicted New Indication | Small cell lung carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source data. Cytarabine belongs to the nucleoside-analog (antimetabolite) class, which inhibits DNA synthesis in rapidly dividing cells. This gives a generic cytotoxic rationale for any fast-growing tumor such as SCLC.

The retrieved data do not show that cytarabine benefits SCLC patients. The cytarabine clinical studies found are older phase II trials in non-small cell lung cancer (NSCLC), a different histology. The SCLC items are mainly case-level reports of meningeal spread, plus one older SCLC study in which cytarabine alone produced no responses.

The TxGNN score (0.998) is uniformly high across all of this drug's predicted indications, so it does not discriminate between them. It should be read as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy vs. observation in early-stage NSCLC. Wrong histology, and cytarabine is not shown as the studied agent. |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for NSCLC leptomeningeal metastasis. Cytarabine is only mentioned as a commonly used intrathecal option. |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed plus radiotherapy for leptomeningeal metastasis from solid tumors. The studied drug is pemetrexed, not cytarabine. |

All three trials were graded low relevance (C). None tests cytarabine in SCLC.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical study | Am J Clin Oncol | Continuous-infusion Ara-C alone gave no responses in 10 heavily pretreated SCLC patients, with severe toxicity. It was also added to CAV in 25 extensive-stage patients. |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical study | Am J Clin Oncol | VP-16 plus infusional Ara-C in 17 patients with relapsed SCLC. Three early deaths were due to progressive tumor. |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Clinical study | Med Pediatr Oncol | 20 untreated SCLC patients received cyclophosphamide, Adriamycin and subcutaneous cytarabine with radiotherapy. Cytarabine's individual contribution was not verified. |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case series | Am J Med | Meningeal carcinomatosis in SCLC. The overall remission rate with intensive chemotherapy was 78% in 60 patients. |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | High-dose cytarabine plus cisplatin in 37 untreated NSCLC patients. The response rate was 14%, with grade IV myelosuppression in 32%. |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Cytarabine, cisplatin and vindesine in 32 patients with advanced NSCLC. |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot study | Eur J Cancer Clin Oncol | Cisplatin plus cytarabine pilot in advanced NSCLC. No abstract is available. |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Preclinical | Biochem Pharmacol | Daunorubicin- and VM-26-resistant SCLC cell lines showed collateral sensitivity to gemcitabine and cytarabine. |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiot Chemother | Ara-C is rapidly deactivated by cytidine deaminase, and analogs were developed to prolong its activity. |

No randomized controlled trials were found.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2406772 | PMS-CYTARABINE |
| 2126656 | CYTARABINE INJECTION |
| 2515296 | CYTARABINE INJECTION |
| 2515490 | VYXEOS |

Dosage form, manufacturer and approved indication text were not provided for these licenses.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside-analog antimetabolite) |
| Myelosuppression Risk | High. The retrieved high-dose cytarabine plus cisplatin study reported grade IV myelosuppression in 32% of patients. |
| Emetogenicity Classification | Low to moderate. Nausea and vomiting were reported in the retrieved studies. |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

The classification, emetogenicity and monitoring items reflect the drug class and general practice, not DrugBank toxicity data. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction plus older, indirect studies: cytarabine alone showed no responses in pretreated SCLC, and the other clinical data are in NSCLC or leptomeningeal disease. No registered trial tests cytarabine in SCLC, and the very high TxGNN score does not distinguish this indication from the drug's other predictions.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Direct, modern clinical evidence of cytarabine efficacy in SCLC, such as registered trials or prospective studies

**Other predicted indications:**
- Primary pulmonary lymphoma is mechanistically plausible, since cytarabine is part of established lymphoma regimens, but no study addresses it directly.
- Neuroblastoma has the most coherent preclinical signal, with in vitro cytarabine-induced differentiation, but no clinical data.
- Four other predicted indications (well-differentiated fetal adenocarcinoma of the lung, pulmonary blastoma, ganglioneuroblastoma, and the vertebral anomalies and T-cell dysfunction syndrome) are prediction-only, with no retrieved trials or literature.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

