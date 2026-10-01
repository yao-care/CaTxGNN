---
layout: default
title: Entrectinib
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib is a kinase inhibitor (TRK, ROS1 and ALK) used in cancer treatment. The Evidence Pack refers to an existing tumour-agnostic indication for NTRK fusion-positive solid tumours, but the Canadian licence records list no indication text.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)** with a high score, but only **2 loosely related clinical trials** and **no publications** support this, and no clear mechanistic link exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; the Evidence Pack refers to a tumour-agnostic indication for NTRK fusion-positive solid tumours |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. From the pack's rationale notes, entrectinib inhibits TRKA/B/C, ROS1 and ALK. It is used in tumours driven by these kinases, such as those carrying NTRK fusions.

The link to multiple endocrine neoplasia is weak. The main driver of MEN2 is RET, which entrectinib does not target. The prediction is most likely driven by shared "neoplasia" or kinase-signalling nodes in the knowledge graph rather than a real pharmacological relationship.

The two trials found for this prediction were probably matched on the word "endocrine". Neither enrolled a MEN population. This prediction should be treated as a model artefact until shown otherwise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, not recruiting | 65 | Neoadjuvant ROS1-targeted therapy plus endocrine therapy in invasive lobular breast carcinoma. Not a MEN population; no results available. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision-oncology platform trial. Not MEN-specific; no interpretable efficacy signal. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2495015 | ROZLYTREK |
| 2495007 | ROZLYTREK |

Dosage form and approved-indication text are not recorded in the licence data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (TRK/ROS1/ALK kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The pack notes kinase inhibitors more often cause cytopenias than treat them. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. Entrectinib does not act on RET, the main MEN2 driver, and the two trials retrieved are not MEN studies and offer no efficacy signal. There is no supporting literature.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Confirmed mechanism-of-action data from DrugBank
- Preclinical or clinical evidence linking TRK/ROS1/ALK inhibition to MEN biology
- Approved-indication text for the two ROZLYTREK DINs, to confirm the original indication

Among the other TxGNN candidates in this pack, **female breast carcinoma** is the only one with clinically relevant trials. These are the ROS1 Phase 2 trial in invasive lobular carcinoma (NCT04551495) and the STARTRK-2 basket study (NCT02568267). Supporting evidence is limited to biomarker-selected subsets, the Phase 2 studies are single-arm with no results in the pack, and NTRK fusion-positive tumours are already covered by the existing indication. It is better framed as a research question than as a repurposing decision.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

