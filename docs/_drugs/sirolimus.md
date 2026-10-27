---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 853
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Renal cell carcinoma (nonpapillary…"
monitor_inn: "SIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lung PEComa", "vulva sarcoma"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Sirolimus: From Renal Cell Carcinoma and Lymphangioleiomyomatosis to Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor whose recorded original uses are renal cell carcinoma and lymphangioleiomyomatosis (LAM).
The TxGNN model predicts it may be effective for **liposarcoma** (the top-ranked prediction), with **1 clinical trial** (a completed single-arm Phase 2) and **7 publications** compiled for this indication.
Among the other predicted indications, the strongest support is for **lymphangiomyoma/LAM**, with **9 clinical trials** including two Phase 3 trials, and 20 publications. Because LAM is already one of the drug's original indications, that entry supports the drug's known use rather than a truly new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (nonpapillary, clear cell) and lymphangioleiomyomatosis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (one completed Phase 2 single-arm trial; no randomized control) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold (research question; see Conclusion) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the compiled data. Based on known information, sirolimus inhibits mTOR, a kinase that drives cell growth and survival through the PI3K/AKT/mTOR pathway.

This pathway is frequently activated in soft tissue sarcomas, including liposarcoma, for example in settings with PTEN loss. Renal cell carcinoma, one of sirolimus's original indications, is also an mTOR-pathway-dependent tumour, so applying mTOR inhibition to another solid tumour is mechanistically plausible.

There are important limits. The only liposarcoma-related trial is a single-arm study in a mixed sarcoma population, and the sirolimus was combined with cyclophosphamide. A liposarcoma-specific effect cannot be separated from these data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma; single-arm, multicentre, and no liposarcoma-specific subgroup result in the data provided |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | In renal transplant patients, sirolimus after early cyclosporine withdrawal reduced cancer risk; not a liposarcoma treatment study |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents for advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening in renal transplant patients on long-term immunosuppression |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohort | Fam Cancer | Clinical spectrum of PTEN hamartoma tumour syndrome |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | Three FAVA cases emphasizing the mTOR pathway |

Most of this literature is indirect: reviews or transplant-setting reports, not liposarcoma treatment studies.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247111 | RAPAMUNE | Not listed | Not listed |
| 02243237 | RAPAMUNE | Not listed | Not listed |

---

## Cytotoxicity

Sirolimus is not a conventional cytotoxic chemotherapy but an mTOR inhibitor with immunosuppressive and antiproliferative activity. Its original indications include renal cell carcinoma, so the points below apply when it is used in oncology.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the contraindication-linked conditions below (kidney, liver, lipid and glucose abnormalities, infections) suggest monitoring renal and liver function, lipids, glucose and infection signs |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Disease associations from the knowledge graph (not label text):** The data compiled for this report link sirolimus with contraindication or caution signals in the following areas:
- Metabolic: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hyperlipidemia, hypertriglyceridemia, familial hyperlipidemia
- Cardiovascular and cerebrovascular: hypertension, stroke, cerebral infarction, pericardial effusion
- Kidney and liver: kidney disease, liver disease, gallbladder disease, hyperbilirubinemia, Gilbert syndrome
- Infections: infectious disease, pneumocystosis, cytomegalovirus infection, progressive multifocal leukoencephalopathy
- Lung: interstitial lung disease
- Malignancy: cancer, brain cancer, embryonal carcinoma

**Drug Interactions:** 100 interactions were found; 20 are shown in the data.
- **Major:** amphotericin B (including lipid complex), clarithromycin, mesalazine, balsalazide
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), aprepitant, cimetidine

Package insert warnings and contraindications for the Canadian products have not been retrieved. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Liposarcoma support rests on one single-arm Phase 2 trial (combination with cyclophosphamide, mixed sarcoma population) and mostly indirect literature, so efficacy specific to liposarcoma is unproven.
- Pharmacologically, mTOR inhibition is plausible, and the drug is marketed in Canada, so this is best treated as a research question.
- Safety review cannot proceed because the package insert data are missing.

**For context on other predicted indications:**
- **Lymphangiomyoma/LAM** (Proceed with Guardrails, L1): the Phase 3 MILES trial (NCT00414648) and the early-disease MLE trial (NCT03150914) support it. LAM is already an original indication, so this is not a new use.
- **Lung PEComa** (Proceed with Guardrails, L3): extrapolated from LAM evidence; confirm the diagnosis first.
- **Benign PEComa** (L4): case reports and retrospective series only.
- **Renal cell carcinoma subtypes, uterine PEComa, ovarian myxoid liposarcoma, vulva sarcoma** (Hold, L5): prediction only, with no direct trial or literature support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Liposarcoma-specific efficacy data from NCT02821507 and any randomized or subtype-specific studies
- A drug-interaction management plan and monitoring for immunosuppression-related adverse events
- Approved indication and dosage form details for the two Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

