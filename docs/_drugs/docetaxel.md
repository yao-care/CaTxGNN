---
layout: default
title: Docetaxel
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Antineoplastic Use (Label Text Not Supplied) to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane chemotherapy drug marketed in Canada, but the Evidence Pack does not include its approved indication text.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **50 clinical trials** (7 completed Phase 3) and **20 publications** currently supporting this direction.
This is probably an established use rather than true repurposing, so the label status should be confirmed against an external source.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 (7 completed Phase 3 trials are listed; the pack's own scoring says L2, pending relevance review of those trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Docetaxel is a taxane that stabilizes microtubules and blocks mitotic progression. This is a direct cytotoxic effect on rapidly dividing tumor cells, and breast cancer cells fit that profile.

The very high TxGNN score is consistent with this mechanism. Because the supplied original-indication field is empty, the prediction likely reflects an established labeled use rather than a genuinely new one. That should be verified against the Health Canada product monograph.

---

## Clinical Trial Evidence

The 10 most relevant of 50 listed trials are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2411 | Preoperative doxorubicin/cyclophosphamide (AC) with or without docetaxel, given before or after surgery, in stage II–III operable breast cancer |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | Completed | 3010 | Docetaxel + epirubicin vs FEC 100 in node-positive breast cancer, with sequential trastuzumab in HER2-positive patients |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1384 | EC followed by docetaxel vs ET followed by capecitabine as adjuvant treatment in HER2-negative, node-positive breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C followed by docetaxel vs paclitaxel as adjuvant chemotherapy in node-positive breast cancer |
| [NCT00615602](https://clinicaltrials.gov/study/NCT00615602) | Phase 3 | Completed | 489 | 6 vs 12 months of trastuzumab combined with dose-dense docetaxel after FE75C in HER2-overexpressing breast cancer |
| [NCT01547741](https://clinicaltrials.gov/study/NCT01547741) | Phase 3 | Unknown | 1871 | Docetaxel + cyclophosphamide vs anthracycline-based regimens in node-positive or high-risk node-negative, HER2-negative breast cancer |
| [NCT00003679](https://clinicaltrials.gov/study/NCT00003679) | Phase 3 | Unknown | 350 | Doxorubicin + docetaxel vs doxorubicin + cyclophosphamide as primary therapy in operable or locally advanced breast cancer |
| [NCT00015938](https://clinicaltrials.gov/study/NCT00015938) | Phase 2 | Completed | 95 | Docetaxel + vinorelbine + filgrastim in HER2-negative stage IV breast cancer |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Neoadjuvant bevacizumab, docetaxel and carboplatin in triple-negative breast cancer |
| [NCT02897050](https://clinicaltrials.gov/study/NCT02897050) | Phase 2 | Suspended | 170 | Neoadjuvant docetaxel with or without metronomic capecitabine/cyclophosphamide, followed by FEC, in triple-negative breast cancer |

---

## Literature Evidence

The 10 most relevant of 20 retrieved publications are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC trials: docetaxel + cyclophosphamide (TC) vs standard taxane-plus-anthracycline regimens in early breast cancer |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Randomized phase IIb | J Clin Oncol | Adding tamoxifen to preoperative dose-dense doxorubicin + docetaxel, assessed by pathologic response |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 | Breast Cancer | Docetaxel, cyclophosphamide and trastuzumab as neoadjuvant therapy in HER2-positive breast cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Weekly docetaxel + gemcitabine as first-line treatment of metastatic breast cancer |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clin Breast Cancer | Docetaxel/cisplatin as primary chemotherapy in locally advanced breast cancer, assessed by pathologic complete response |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase 2 (interim) | Breast Cancer | CEF followed by docetaxel as preoperative chemotherapy in early-stage breast cancer (79 patients analyzed) |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine + docetaxel + epirubicin as first-line therapy in advanced breast cancer |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Dose-finding | Tumori | Docetaxel + gemcitabine dose finding in metastatic breast cancer previously treated with anthracyclines |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Retrospective study of adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Early review of docetaxel's preclinical and clinical profile |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02458020 | DOCETAXEL INJECTION |
| 02361957 | DOCETAXEL INJECTION USP |
| 02439336 | DOCETAXEL INJECTION |

Dosage form, manufacturer and approved indication text were not supplied for these authorizations.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, antimitotic) |
| Myelosuppression Risk | High (neutropenia is typical for the taxane class; class-based, not from supplied toxicity data) |
| Emetogenicity Classification | Low (class-based) |
| Monitoring Items | CBC with differential, liver function, signs of fluid retention and edema |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Literature signal**: a retrospective cohort study examined adjuvant docetaxel-based chemotherapy in relation to breast cancer-related lymphedema. Docetaxel is known to cause fluid retention and peripheral edema.

Please refer to the package insert for full safety information. No drug interaction records were found in the query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large, completed Phase 3 trials and a plausible antimitotic mechanism support docetaxel in breast cancer. The supplied data show no original indication, so this is probably an established use rather than true repurposing. Health Canada label information is also missing.

**To proceed, the following is needed:**
- Confirm the approved indications in the Health Canada product monograph (indication text is empty for all 3 DINs).
- Retrieve package insert warnings and contraindications.
- Obtain mechanism-of-action data from DrugBank.
- Complete relevance grading for the trials still marked "pending", including the Phase 3 trials.
- Set up a hematologic and fluid-retention monitoring plan, and apply cytotoxic handling procedures.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

