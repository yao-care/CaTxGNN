---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 754
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Temozolomide: From Glioblastoma to Adult Astrocytic Tumour

## One-Sentence Summary

> Temozolomide is an oral alkylating agent already documented in this evidence pack as FDA-approved for newly diagnosed glioblastoma. The TxGNN model predicts it may also be effective for **Adult Astrocytic Tumour**, with **2 clinical trials** (including a 500-patient Phase 3 RCT) and **20 publications** — 7 of them Phase 3 RCTs — supporting this direction. Note: since glioblastoma is itself a subtype of astrocytic tumour, this signal largely confirms a mechanism already validated in practice rather than pointing to a genuinely novel disease category.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glioblastoma (stated as FDA-approved in the trial description for NCT00960492; not currently licensed/marketed in Canada per this dataset) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is flagged as a data gap in this evidence pack. Based on the mechanistic description captured alongside the prediction, temozolomide is an oral alkylating (imidazotetrazine) agent that undergoes non-enzymatic hydrolysis to MTIC, which methylates guanine at the O6 position. This causes DNA mismatch-repair failure and apoptosis in dividing cells. Because temozolomide crosses the blood–brain barrier, it has direct antitumor activity against tumours of the glial/astrocytic lineage in the central nervous system.

Glioblastoma — the indication referenced directly in the trial description for NCT00960492 ("approved by the Food and Drug Administration (FDA) for the treatment of newly diagnosed glioblastoma") — is itself classified as a high-grade astrocytic tumour (WHO Grade IV). The predicted indication, "adult astrocytic tumour," therefore sits on the same disease spectrum as temozolomide's established use, rather than representing a mechanistically distant target. NCT00052455 (Phase 3, n=500) directly tested temozolomide against PCV chemotherapy in recurrent WHO Grade III/IV astrocytic tumours, and the Stupp-protocol RCTs (PMID 15758009, 19269895) established temozolomide plus radiotherapy as standard of care for glioblastoma.

**Important caveat:** because astrocytic tumour encompasses glioblastoma, this prediction should be read as the model correctly re-identifying an already well-established, guideline-based use rather than surfacing a genuinely new repurposing opportunity. It is useful primarily as a validation signal for the model and as confirmation that no Canadian market authorization currently exists for this well-established international indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized comparison of temozolomide alone vs. PCV (procarbazine, lomustine, vincristine) in recurrent WHO Grade III/IV astrocytic tumours (recurrent malignant glioma) |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of cabozantinib (XL184) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; temozolomide used as combination partner, not the primary study drug |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark Stupp trial: radiotherapy plus concomitant/adjuvant temozolomide vs. radiotherapy alone improved survival in glioblastoma, establishing the current standard of care |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | 5-year follow-up of the EORTC-NCIC trial confirming sustained survival benefit of temozolomide + radiotherapy in glioblastoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09: lomustine-temozolomide combination superior to temozolomide alone in newly diagnosed, MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumor-treating fields plus temozolomide maintenance vs. temozolomide alone improved survival in glioblastoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Randomized trial of bevacizumab added to temozolomide/radiotherapy in newly diagnosed glioblastoma |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08: temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG Oncology BN007: dual immune checkpoint blockade in MGMT-unmethylated newly diagnosed glioblastoma (temozolomide-based regimen) |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Review of glioblastoma and other primary adult brain malignancies, including temozolomide-based treatment |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Review | J Neurooncol | Radiotherapy and temozolomide outcomes in anaplastic astrocytic gliomas (exploratory cohort) |
| [40725030](https://pubmed.ncbi.nlm.nih.gov/40725030/) | 2025 | Preclinical | Int J Mol Sci | In vivo/in vitro comparison of sodium dichloroacetate + valproic acid vs. temozolomide in glioblastoma models |

---

## Canada Market Information

Temozolomide currently holds no Canadian market authorization (DIN) records in this dataset — **0 licenses, market status "Not Marketed."** No dosage forms, brand names, or approved indication text are available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class — based on the mechanistic rationale captured with this prediction) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a cytotoxic chemotherapy agent, standard cytotoxic drug handling precautions apply; confirm against institutional protocol |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are marked as data gaps in this evidence pack — notably DG001, a **blocking** gap on TFDA-equivalent labeling/contraindication data, which must be resolved before any formal safety review.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical evidence base is strong (L1 — multiple completed Phase 3 RCTs, including the practice-defining Stupp protocol trials), but two structural gaps block full progression: temozolomide has zero market presence in Canada (0 DINs), and safety/labeling data (warnings, contraindications, DDI) are entirely missing (DG001, blocking severity). Guardrails are needed to close these gaps before any regulatory or clinical action is taken.

**To proceed, the following is needed:**
- Resolve DG001: obtain official product labeling (warnings/contraindications) to complete the S1 safety screen
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Clarify Canadian market status: confirm whether temozolomide is available in Canada under a different regulatory pathway (e.g., Special Access Programme) despite showing 0 DINs here
- Treat "adult astrocytic tumour" as a known-indication confirmation rather than a novel repurposing candidate when prioritizing pipeline resources; the lower-ranked candidate (cauda equina neoplasm, Evidence Level L4, currently **Hold**) would be a more genuine novel-repurposing signal if further case-level evidence accumulates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

