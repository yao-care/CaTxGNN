---
layout: default
title: Larotrectinib
parent: Moderate Evidence (L3-L4)
nav_order: 522
evidence_level: L4
indication_count: 10
---

# Larotrectinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Larotrectinib: From NTRK-Fusion Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is a selective TRK (NTRK1/2/3) inhibitor, marketed in Canada as VITRAKVI and used tumor-agnostically for NTRK-fusion solid tumors.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but the support is thin: **1 clinical trial** (a broad basket trial, not MEN-specific) and **2 publications** (neither tests larotrectinib in MEN).

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, larotrectinib is a selective inhibitor of the TRK receptor tyrosine kinases (NTRK1/2/3). Its efficacy is established in solid tumors that carry NTRK gene fusions.

The link to MEN is indirect. MEN syndromes, especially MEN2, are driven mainly by **RET** mutations, not NTRK. The only shared ground is that both are receptor tyrosine kinase pathways in endocrine tumors. The supplied data show no direct RET activity or MEN-specific activity for larotrectinib.

The very high graph score (0.992) therefore reflects proximity in the knowledge graph rather than demonstrated biology. Any benefit would most plausibly be limited to the rare patient whose tumor carries an NTRK fusion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6452 | NCI-MATCH: a single-arm, biomarker-directed basket trial in advanced, refractory solid tumors, lymphomas and myelomas. It is not MEN-specific, and a larotrectinib arm would apply only to NTRK-fusion tumors, so it offers no direct MEN evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Overview of kinase inhibitor therapy for advanced thyroid cancer, including approved multikinase and mutation-specific agents. It is background for endocrine tumors, not evidence for larotrectinib in MEN. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical / case report | NPJ Precision Oncology | Off-target resistance mechanisms to selective RET inhibition (selpercatinib) in RET-driven medullary thyroid carcinoma. It concerns RET inhibitors, not larotrectinib. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2490331 | VITRAKVI |
| 2490315 | VITRAKVI |
| 2490323 | VITRAKVI |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRK kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on graph proximity rather than biology: MEN is RET-driven, and the only trial is a non-specific basket study. No study tests larotrectinib in MEN. The other nine predicted indications are weaker still. Most have no supporting evidence, and several (cytomegalovirus, bovine diseases) look like knowledge-graph artifacts. The one partial exception is PR-negative breast cancer, where the completed Phase 2 NTRK-fusion basket trial (NCT02576431) is relevant only to NTRK-fusion tumors.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and any evidence of larotrectinib activity against RET or MEN-associated tumors
- Health Canada package insert warnings and contraindications
- Data on NTRK-fusion frequency in MEN-associated tumors, or reported cases of larotrectinib response in such patients
- Approved indication text for the three DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

