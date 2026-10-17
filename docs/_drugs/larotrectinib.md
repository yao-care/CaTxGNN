---
layout: default
title: Larotrectinib
parent: Model Prediction Only (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Larotrectinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not stated in the Canadian licence data compiled for this report (lit…"
monitor_inn: "Larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "progesterone-receptor negative breast cancer", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "thrombocytopenia"]
---

# Larotrectinib
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

# Larotrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib (marketed in Canada as VITRAKVI) is a selective TRK kinase inhibitor. The Canadian licence text compiled for this report does not state an approved indication, but the literature identifies it as a tumour-agnostic therapy for NTRK fusion-positive cancers.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but only **1 clinical trial** (a broad, indirect basket trial) and **2 publications** are linked to this prediction, so the evidence is indirect and weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data compiled for this report (literature describes NTRK fusion-positive solid tumours) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 (indirect; no MEN-specific trial) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the literature, larotrectinib is a selective inhibitor of the TRK receptors (NTRK1/2/3). It is used as a tumour-agnostic therapy for cancers driven by NTRK gene fusions.

The link to multiple endocrine neoplasia is indirect. MEN-associated tumours, such as medullary thyroid carcinoma, are driven mainly by **RET** alterations rather than NTRK. The supporting literature discusses kinase-inhibitor therapy in advanced thyroid cancer and resistance mechanisms in RET-driven cancers. The NCI-MATCH trial assigns patients by molecular alteration, including NTRK fusions, and not by MEN diagnosis. Benefit would therefore be expected only in the rare patients whose tumours carry an NTRK fusion.

The very high TxGNN score is a computational prediction. No MEN-specific clinical data support it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6452 | NCI-MATCH: single-arm basket trial of genetically directed therapy in advanced, refractory solid tumours, lymphomas and myeloma, including a larotrectinib arm for NTRK fusion-positive tumours. It is not MEN-specific, so support is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Kinase-inhibitor therapy for advanced thyroid cancer. Approved drugs are mostly antiangiogenic multikinase inhibitors, plus some mutation-specific options. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/Mechanistic | NPJ Precision Oncology | Resistance to selective RET inhibitors (selpercatinib) in a patient with medullary thyroid carcinoma, mediated by alternative oncogenes. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02490331 | VITRAKVI | Not specified | Not specified |
| 02490315 | VITRAKVI | Not specified | Not specified |
| 02490323 | VITRAKVI | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective TRK kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically blood counts, liver and renal function) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Most are rated Moderate, with a few rated Minor. One is rated **Major**: **clarithromycin**. Moderate interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Acid suppressants: omeprazole, cimetidine
  - Antiemetics: aprepitant, dolasetron
  - Other examples: pioglitazone, saxagliptin, cisapride, clotrimazole

Package insert warnings and contraindications for Canada were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MEN prediction rests on a high model score and indirect evidence only. The one linked trial is a tumour-agnostic basket study. The literature concerns RET-driven thyroid cancer, not NTRK-driven disease. Larotrectinib would be plausible only in NTRK fusion-positive patients, who are already covered by its tumour-agnostic use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Detailed mechanism-of-action data
- Evidence on how often NTRK fusions occur in MEN-associated tumours, and MEN-specific case or cohort data
- A drug-interaction management plan, particularly for strong CYP3A4 inhibitors such as clarithromycin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

