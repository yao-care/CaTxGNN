---
layout: default
title: Entrectinib
parent: Moderate Evidence (L3-L4)
nav_order: 333
evidence_level: L3
indication_count: 10
---

# Entrectinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Entrectinib: From Solid Tumours (NTRK/ROS1 Fusion-Positive) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib is a targeted kinase inhibitor (TRK, ROS1 and ALK) that is marketed in Canada as ROZLYTREK. The TxGNN model ranks **multiple endocrine neoplasia** as its top prediction, but the support is thin: **1 terminated clinical trial** (2 patients enrolled) and **1 publication** that gives only indirect context. Among the other predictions, **female breast carcinoma** has the strongest evidence, with a Phase 2 basket trial and several publications, and it applies to the fusion-positive subset only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data compiled for this report (the drug is a TRK/ROS1/ALK inhibitor used for fusion-positive solid tumours) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From known information, entrectinib inhibits TRK, ROS1 and ALK kinases. It is not a primary RET inhibitor.

Multiple endocrine neoplasia type 2 is driven by activating germline RET mutations. The link to entrectinib is therefore indirect and rests on its multikinase activity and possible off-target effects on the RET pathway. The 2024 paper on resistance to selective RET inhibitors in RET-driven cancer provides context, not direct evidence for entrectinib. The model's score is high, but the biological rationale is weak.

**Other predictions worth noting:**
- **Female breast carcinoma** (score 97.76%, L2): This is the best-supported alternative. Breast secretory carcinoma is characterized by ETV6-NTRK3 fusions, which entrectinib targets. The benefit would apply to the fusion-positive subset, not to unselected breast cancer.
- **Thrombocytopenia and pulmonary hypertension:** The literature describes these as possible safety signals during entrectinib therapy, not as therapeutic opportunities.
- **Amenorrhea, cytomegalovirus infection and several rare thrombocytopenia-related conditions:** There are no trials or literature, and no plausible mechanism. These are computational predictions only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision-oncology platform; terminated after 2 patients, so no usable efficacy or safety data for multiple endocrine neoplasia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/Translational | NPJ Precision Oncology | Resistance mechanisms to selective RET inhibitors (selpercatinib, pralsetinib) in RET-driven cancer, including a medullary thyroid carcinoma case; context only, not direct evidence for entrectinib |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02495015 | ROZLYTREK | Not specified | Not specified |
| 02495007 | ROZLYTREK | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug interactions:** The interaction screening returned 100 interacting drugs, 20 of which were included in the data compiled for this report. The main **Major** interactions are:
- Aprepitant
- Dexamethasone
- Clarithromycin
- Dolasetron

Examples of **Moderate** interactions include famotidine, loperamide, cimetidine, budesonide, levofloxacin, naltrexone, saxagliptin, empagliflozin and several bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate). Minor interactions include naloxegol and metronidazole.

**Possible safety signals from the literature:** A 2025 case report describes pulmonary tumor thrombotic microangiopathy (PTTM) progressing during entrectinib therapy in a patient with NTRK fusion-positive colon cancer, despite a marked tumour response. This is a single case report and should be monitored, not over-interpreted.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, multiple endocrine neoplasia, has only an indirect mechanistic link (entrectinib is not a primary RET inhibitor). Its single trial was terminated after 2 patients, so there is no efficacy data.
- Breast carcinoma is a more credible direction (L2, **Proceed with Guardrails**), but only in the NTRK-fusion-positive subset such as breast secretory carcinoma.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- For multiple endocrine neoplasia: preclinical or clinical data on entrectinib activity against RET-driven disease
- For breast carcinoma: the number of breast patients and response data from the STARTRK-2 basket trial (NCT02568267), plus a biomarker-selection strategy for NTRK fusion-positive tumours
- Review of the major drug interactions, particularly with strong CYP3A inhibitors such as clarithromycin, and monitoring for pulmonary vascular events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

