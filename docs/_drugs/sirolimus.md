---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 853
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-05
monitor_inn: "SIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor marketed in Canada under the brand name RAPAMUNE.
The TxGNN model predicts it may be effective for **liposarcoma**, but the evidence level is **L5**: there is **1 registered clinical trial** (a single-arm Phase 2 study in myxoid liposarcoma and chondrosarcoma without posted results), and no published study directly tests sirolimus in liposarcoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on what is known, sirolimus inhibits mTOR, a kinase that drives cell growth and survival through the PI3K/AKT/mTOR pathway.

This pathway is frequently activated in soft tissue sarcomas, including liposarcoma, for example in settings with MDM2/CDK4 amplification and PTEN loss. Preclinical mouse models also suggest that mTOR inhibition can slow tumour growth in sarcomas. This gives a plausible biological reason for the model's prediction.

However, this is a mechanistic argument only. The registered trial combines sirolimus with cyclophosphamide in a mixed sarcoma population, and no published results are available to show a liposarcoma-specific benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma; no results are posted or published, and no liposarcoma-specific outcome can be drawn |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | In renal transplant patients, switching to sirolimus after early cyclosporine withdrawal reduced cancer risk; not a study in liposarcoma |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapies in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of molecular-targeted agents in advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas |

None of these publications tests sirolimus as a treatment for liposarcoma. They provide background on sarcoma biology and on cancer risk in transplant patients.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247111 | RAPAMUNE | Not listed | Not listed |
| 02243237 | RAPAMUNE | Not listed | Not listed |

Both authorizations are valid single-ingredient licences.

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified. Major-level interactions include amphotericin B (including the lipid complex), mesalazine, balsalazide and clarithromycin. Moderate-level interactions include several diabetes medicines (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant and cimetidine.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mTOR-pathway rationale is plausible, but the only trial in this setting is a single-arm study of a sirolimus–cyclophosphamide combination without posted results. No published study tests sirolimus in liposarcoma, so the evidence level is L5.

**To proceed, the following is needed:**
- Results of NCT02821507, ideally with a liposarcoma-specific subgroup analysis
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from Health Canada
- A review of the many drug interactions, particularly the major-level ones, before any oncology use

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

