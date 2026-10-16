---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Durvalumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
monitor_inn: "Durvalumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Durvalumab
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

# Durvalumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 antibody, originally used for transitional cell (urothelial) carcinoma.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma** (the top-ranked prediction), but **no clinical trials or publications** were found for this specific disease.
Related urothelial and cervical diseases ranked lower in the prediction list have some early-phase trial support, summarized below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (the Canadian licence record has no indication text) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, durvalumab is a monoclonal antibody that blocks PD-L1, which releases the brake that tumours place on T cells. Its efficacy in urothelial carcinoma is the basis of its original indication.

Prostatic urethra urothelial carcinoma is a urothelial carcinoma arising in the same epithelial lineage as transitional cell carcinoma of the bladder. PD-L1 blockade is therefore biologically plausible. This rationale rests on general knowledge, not on trial or literature data specific to this disease.

### Other Predictions with Some Supporting Evidence

The prediction list also includes diseases with registered trials, although these are not the top-ranked prediction:

- **Infiltrating bladder urothelial carcinoma, sarcomatoid variant** (score 99.98%): two trials, summarized below.
- **Kidney pelvis sarcomatoid transitional cell carcinoma** (score 99.98%): one early-phase pilot trial.
- **Endocervical carcinoma** (score 99.91%): one completed Phase 1 trial and two publications that are not specific to this disease.

The remaining predictions (renal pelvis papillary urothelial carcinoma, uterine ligament adenocarcinoma, and several rare cervical or uterine ligament carcinomas) have no trials or literature.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, prostatic urethra urothelial carcinoma. The most closely related trials from the other predictions are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab with neoadjuvant chemotherapy in variant-histology bladder cancer. Terminated with very few participants, so it is unlikely to give conclusive efficacy data. No results provided. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, not recruiting | 54 | Pre-surgical pilot of durvalumab plus tremelimumab in muscle-invasive, high-risk urothelial carcinoma ineligible for cisplatin. Assesses safety and immune effects. No outcomes reported. |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy with durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer. Informs feasibility and safety, not efficacy of durvalumab alone. |

## Literature Evidence

No literature is available for the top-ranked prediction. Two publications were found for endocervical carcinoma, and neither is specific evidence of durvalumab efficacy in that disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Nonrandomized clinical trial | Oncology and Therapy | Phase 1 study of ceralasertib (an ATR kinase inhibitor) plus durvalumab in Chinese patients with advanced solid tumours refractory to prior anti-PD-(L)1 therapy or without standard options. Assesses safety, pharmacokinetics and antitumour activity. |
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Review of small cell neuroendocrine carcinoma of the cervix, covering molecular basis and therapeutic advances. Notes that evidence is limited to case series and case reports. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02468816 | IMFINZI | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query found **81 interacting drugs**. The 20 entries returned include:
  - **Major**: adalimumab.
  - **Moderate**: systemic corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, tetanus toxoid and anthrax vaccine.
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a very high model score but no trials or publications, so it is supported only by the model and by general PD-L1 biology. Related urothelial and cervical diseases have only small, early-phase or terminated trials without reported results.

**To proceed, the following is needed:**
- Trial and literature searches specific to prostatic urethra urothelial carcinoma, including upper-tract and variant-histology urothelial disease.
- Results from NCT02812420 and any usable data from the terminated NCT03912818.
- Package insert warnings and contraindications from Health Canada, and the approved indication text for the IMFINZI licence.
- Mechanism of action data from DrugBank.
- A review of the interaction with systemic corticosteroids and other immunosuppressants.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

