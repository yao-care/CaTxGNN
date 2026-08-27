---
layout: default
title: Histidine
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 2
---

# Histidine
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

# Histidine: From No Established Indication to Two Investigational Candidates (Gastroparesis / Primary Sclerosing Cholangitis)

## One-Sentence Summary

Histidine (DrugBank DB00117) is an essential amino acid with no approved indication on file and no Canadian market presence in this dataset. The TxGNN model independently flagged two candidate indications — **Gastroparesis** (score 99.55%) and **Primary Sclerosing Cholangitis** (score 99.27%) — but neither is supported by any clinical trial, and the eight publications found for sclerosing cholangitis actually describe histamine signaling as **harmful** to bile duct tissue, the opposite of what a repurposing hypothesis would need.

---

## Quick Overview

| Item | Candidate 1: Gastroparesis | Candidate 2: Primary Sclerosing Cholangitis |
|------|------|------|
| Original Indication | Not available (no approved indication on record) | Not available (no approved indication on record) |
| Predicted New Indication | Gastroparesis | Primary Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.55% | 99.27% |
| Evidence Level | L5 | L4 |
| Canada Market Status | ✗ Not marketed | ✗ Not marketed |
| Number of DINs | 0 | 0 |
| Recommended Decision | Hold | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for histidine is not available. Based on known information, histidine is an essential amino acid and the metabolic precursor of histamine (via the enzyme histidine decarboxylase, HDC). No approved indication is on record in this evidence pack, so there is no established clinical use to anchor a mechanistic comparison for either candidate.

**Gastroparesis**: No mechanistic link could be identified. There is no known physiological pathway connecting histidine metabolism to delayed gastric emptying or gut autonomic/smooth-muscle function. The 99.55% score reflects only a knowledge-graph embedding similarity — a purely algorithmic association with zero supporting clinical trials or literature.

**Primary Sclerosing Cholangitis (PSC)**: A biologically plausible pathway exists — histidine is converted to histamine via HDC — but the direction of the evidence runs counter to the repurposing hypothesis. Multiple preclinical studies in the Mdr2⁻/⁻ mouse model of PSC (PMID 27351144, 32054995, 29601088, 35799467) consistently show that mast-cell-derived histamine, acting through H1/H2 receptors, **promotes** biliary hyperplasia and fibrosis, and that blocking this pathway (receptor antagonists or HDC knockout) **reduces** disease severity. This suggests that increasing histidine availability — the substrate for histamine synthesis — could theoretically worsen biliary injury rather than treat it. The remaining literature (biomarker/cohort studies and a genetics review) is only indirectly related and does not evaluate histidine supplementation as a therapy.

---

## Clinical Trial Evidence

**Gastroparesis**: Currently no related clinical trials registered.

**Primary Sclerosing Cholangitis**: Currently no related clinical trials registered.

---

## Literature Evidence

**Gastroparesis**: Currently no related literature available.

**Primary Sclerosing Cholangitis**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8020893](https://pubmed.ncbi.nlm.nih.gov/8020893/) | 1994 | Review | Hepatology | Reviews HLA-linked genetic susceptibility in autoimmune liver disease; only indirectly related to PSC, no histidine/histamine link. |
| [30325540](https://pubmed.ncbi.nlm.nih.gov/30325540/) | 2019 | Cohort/Biomarker | Hepatology | Serum metabolomic profiling distinguishes cholangiocarcinoma, HCC, and PSC; a diagnostic biomarker study, not a treatment study. |
| [23928409](https://pubmed.ncbi.nlm.nih.gov/23928409/) | 2013 | Cohort/Biomarker | Journal of Hepatology | microRNA profiles in graft preservation fluid predict post-transplant ischemic biliary lesions; unrelated to histidine supplementation. |
| [19691661](https://pubmed.ncbi.nlm.nih.gov/19691661/) | 2010 | Cohort (epidemiology) | Transplant International | Risk factor analysis for ischemic-type biliary lesions after liver transplant; PSC patients were explicitly excluded from this cohort. |
| [27351144](https://pubmed.ncbi.nlm.nih.gov/27351144/) | 2016 | Preclinical/Mechanistic | Hepatology | In Mdr2⁻/⁻ mice, blocking mast-cell-derived histamine (cromolyn sodium) **decreased** biliary proliferation and fibrosis — implies histamine is pathogenic, not therapeutic. |
| [32054995](https://pubmed.ncbi.nlm.nih.gov/32054995/) | 2020 | Preclinical/Mechanistic | Laboratory Investigation | HDC-knockout (histamine-deficient) mice showed **ameliorated** biliary damage and fibrosis when crossed with the Mdr2⁻/⁻ PSC model — reducing histamine production is protective. |
| [29601088](https://pubmed.ncbi.nlm.nih.gov/29601088/) | 2018 | Preclinical/Mechanistic | Hepatology | Chronic H1/H2 histamine receptor blockade **inhibited** biliary damage/fibrosis and cholangiocarcinoma tumorigenesis in the same model. |
| [35799467](https://pubmed.ncbi.nlm.nih.gov/35799467/) | 2022 | Preclinical/Mechanistic | Hepatology Communications | Mast cells target large cholangiocytes via H2 receptor/cAMP/pERK signaling during biliary injury, reinforcing histamine's role as a driver of pathology. |

---

## Canada Market Information

Histidine currently has **no marketed drug license** in this dataset (market status: not marketed; total licenses: 0). No DIN records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available in this evidence pack (TFDA label data is flagged as a blocking data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold** (both candidates)

**Rationale:**
- *Gastroparesis*: The prediction is supported only by a knowledge-graph similarity score (L5) with zero clinical trials or literature, and no biologically plausible mechanism could be identified.
- *Primary Sclerosing Cholangitis*: Although mechanistic literature exists (L4), it consistently shows histamine signaling — the pathway histidine feeds into — accelerates biliary fibrosis in the disease model. The directionality of the evidence argues against, not for, histidine as a treatment.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a blocking gap (DG001)
- Confirmed mechanism of action data for histidine (DG002)
- Any direct pharmacological or clinical evidence evaluating histidine supplementation's effect on gastric motility (gastroparesis) or biliary fibrosis (PSC), rather than relying on histamine-pathway-blocking studies that point the opposite direction
- Reassessment of whether the PSC hypothesis should instead be reframed around histamine-pathway *inhibitors* rather than histidine itself, given the current evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

