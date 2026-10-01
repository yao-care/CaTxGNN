---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 846
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Immunosuppression to Liposarcoma

## One-Sentence Summary

Sirolimus (marketed in Canada as RAPAMUNE) is an mTOR inhibitor used as an immunosuppressant in kidney transplantation. The TxGNN model predicts it may be effective for **liposarcoma**. Currently **5 clinical trials** and **11 publications** relate to this direction, but none tests sirolimus alone in liposarcoma, and the evidence is mostly class-level or preclinical.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 as graded in the Evidence Pack. Strictly, the evidence is single-arm Phase 2 trials of sirolimus or related drugs plus preclinical work, with no randomized trial. |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Sirolimus is known to inhibit mTOR (mammalian target of rapamycin), a kinase that drives cell growth and survival. Its efficacy as an immunosuppressant is established, and mechanistically it may be applicable to liposarcoma.

The link to liposarcoma is plausible but indirect. A pathology study of 99 dedifferentiated liposarcoma specimens (PMID 26518767) found that the Akt-mTOR and MAPK pathways are activated, so blocking mTOR is a reasonable idea. In mouse models, sirolimus combined with chloroquine, which blocks autophagy, stopped tumour growth in dedifferentiated and well-differentiated liposarcoma.

Human evidence is thin. It consists of Phase 2 single-arm studies, mostly of related drugs (ridaforolimus, temsirolimus, everolimus), and no randomized sirolimus data exist in this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. It directly tests the drug, but is not liposarcoma-specific. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib plus everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma. The population fits, but the agent is everolimus. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (an mTOR inhibitor) in advanced sarcoma. Class-level evidence in a mixed population. |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus plus liposomal doxorubicin in recurrent soft tissue and bone sarcoma. Small, class-level evidence. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab plus temsirolimus in paediatric recurrent or refractory solid tumours. Liposarcoma is at most a minor subset. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | In kidney transplant recipients (n=430 randomized), switching to sirolimus after early cyclosporine withdrawal reduced cancer risk. It is not liposarcoma-specific. |
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial | Clin Cancer Res | Ribociclib plus everolimus in dedifferentiated liposarcoma and leiomyosarcoma (SAR-096). |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents in advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening in renal transplant patients on long-term immunosuppression. Tangential relevance. |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine plus rapamycin synergistically blocked autophagy in well-differentiated liposarcoma. |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical | In Vivo | Chloroquine plus rapamycin arrested tumour growth in a dedifferentiated liposarcoma patient-derived xenograft mouse model. |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | The ATP-competitive mTOR kinase inhibitor MLN0128 showed antitumour activity in bone and soft-tissue sarcoma. First-generation rapalogs had limited clinical utility. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational | Tumour Biol | The Akt-mTOR and MAPK pathways are activated in dedifferentiated liposarcoma specimens. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02247111 | RAPAMUNE |
| 02243237 | RAPAMUNE |

Dosage form and approved indication text are not available for these licences.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is reasonable, and a Phase 2 sirolimus-plus-cyclophosphamide trial exists. However, there are no randomized sirolimus data in liposarcoma. Most human evidence comes from related mTOR inhibitors, and the sirolimus-specific support is preclinical. Randomized trials of mTOR inhibitors in other tumours, such as everolimus versus sunitinib in non-clear-cell renal cell carcinoma, have also been unfavourable.

Other predictions for sirolimus have much stronger support. Lymphangioleiomyomatosis (L1, Phase 3 MILES trial NCT00414648) and benign PEComa/angiomyolipoma (L2) are better candidates for further evaluation.

**To proceed, the following is needed:**
- Results and efficacy data from NCT02821507 (sirolimus plus cyclophosphamide), with liposarcoma-specific subgroup outcomes
- Mechanism of action data (DrugBank)
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Dosage form and approved indication text for the two Canadian DINs
- Drug interaction data, particularly for combination regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

