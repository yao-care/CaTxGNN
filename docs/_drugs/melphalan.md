---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Its Approved Use (Not Listed in the Supplied Records) to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug marketed in Canada, but the supplied records do not list its approved indications.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**, with **7 clinical trials** and **4 publications** linked to this prediction. The evidence is mostly indirect: small early-phase transplant studies in mixed solid tumors and very old literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence records |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 (the pack assigned L2, but no completed randomized trial is present; see Conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied records. Based on general knowledge of the drug class, melphalan is a bifunctional alkylating agent. It forms DNA interstrand cross-links that block cell division and trigger cell death. Its role is well established in high-dose chemotherapy regimens followed by autologous stem cell rescue.

Germ cell tumors are generally chemosensitive, and high-dose alkylator-based regimens with stem cell rescue have been tested in relapsed disease. This is the main reason the prediction is plausible. One Phase 2 trial in relapsed germ cell tumors (NCT00936936) lists melphalan in its first high-dose cycle, alongside gemcitabine, docetaxel and carboplatin.

The other predicted indications (ovarian germ cell tumor, ovarian choriocarcinoma, female breast carcinoma, and several mucinous adenocarcinomas) are outside this report's scope. Most of them have no linked trials or literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy in poor-prognosis relapsed germ cell tumors. Cycle 1 includes gemcitabine, docetaxel, melphalan and carboplatin; cycle 2 includes ifosfamide, carboplatin and etoposide. This is the most disease-specific trial. No results were supplied. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine in cancer patients. It tests melphalan directly, but the germ cell subset is small. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced and recurrent tumors. It is a mixed solid tumor cohort. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant for hematologic malignancy and selected solid tumors. Melphalan use and the germ cell subset are not confirmed. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | Not applicable | Completed | 174 | Autologous transplant program with high-dose regimens, with or without total-body irradiation, for hematologic cancers and selected solid tumors. Regimen details are not visible. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as a chemoprotectant with autologous transplant in pediatric solid and brain tumors. It is supportive care, so it is only indirect evidence. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis. The route and setting differ from germ cell therapy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Review of chemotherapy for testicular germinal tumors. No abstract was supplied. |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | Urologic Clinics of North America | Review of seminoma. No abstract was supplied. |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Case series | Voprosy Onkologii | Early experience treating testicular seminoma and its metastases with sarcolysin, an older name for melphalan. No abstract was supplied. |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Preclinical | Acta Unio Int Contra Cancrum | Effects of hormonal and alkylating drugs on pituitary follicle-stimulating function. Little bearing on efficacy in this disease. |

All four publications are 45 to 70 years old, and none has an abstract in the records. The findings above are inferred from titles only.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 4715 | ALKERAN |
| 2087286 | ALKERAN |
| 2480026 | TARO-MELPHALAN |
| 2473348 | MELPHALAN FOR INJECTION |

Dosage form, manufacturer and approved indication text are not available for these licences.

---

## Cytotoxicity

The supplied records contain no toxicity data. The entries below reflect general knowledge of alkylating agents, and the package insert should be checked.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High (dose-limiting, especially at high doses with stem cell rescue) |
| Emetogenicity Classification | Low to moderate (higher with high-dose intravenous use) |
| Monitoring Items | CBC with differential, renal and liver function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.77%), and NCT00936936 is a disease-specific Phase 2 trial that includes melphalan. However, no results were supplied. The other trials are small, early-phase studies in mixed solid tumors, and the literature is decades old and abstract-free. There is no completed randomized trial, so the L2 grade in the pack looks generous. This is a research question, not a candidate ready to advance.

**To proceed, the following is needed:**
- Published results or outcome data for NCT00936936, including response and survival in the germ cell subset
- Confirmation of melphalan's exact role in the other transplant regimens
- Mechanism-of-action data from DrugBank
- Canadian package insert warnings, contraindications and approved indications (the safety screening step is currently blocked without these)
- Route compatibility between the Canadian formulations and the regimens studied in germ cell tumors

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

