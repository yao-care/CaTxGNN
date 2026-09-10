---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 616
evidence_level: L5
indication_count: 2
---

# Phenylalanine
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

# Phenylalanine: From No Established Indication to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine (DB00120) has no approved indication on record and is currently **not marketed in Canada** (0 DINs). The TxGNN model assigns a **99.43%** score linking it to **sclerosing cholangitis**, but the 4 supporting publications do not actually study free phenylalanine as a therapeutic agent — closer review suggests the signal is likely a **knowledge-graph entity confusion** (with tyrosine and with the unrelated peptide FMLP) rather than a genuine pharmacological finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no approved indication or licensed product on record |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only, no supportive clinical/mechanistic studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for phenylalanine is not available, and the drug has no recorded original indication or Canadian market authorization. Without a baseline MOA or approved-use context, there is no established pharmacological rationale to connect it to sclerosing cholangitis.

Reviewing the underlying literature raises further doubt rather than support. Of the 4 publications retrieved, none actually test free phenylalanine as a treatment: one studies plasma **tyrosine** (a related but distinct amino acid) and fatigue in PBC/PSC; two study **FMLP** (N-formyl-methionyl-leucyl-phenylalanine), a synthetic bacterial chemotactic peptide with entirely different pharmacology, used in one case to *induce* cholangitis in rats rather than treat it; and one is a metabolomics panel in which phenylalanine appears only as one of many measured serum analytes in cholangiocarcinoma, not as an intervention. This pattern is consistent with the TxGNN knowledge graph conflating "phenylalanine" nodes with related but pharmacologically distinct entities (tyrosine metabolism, FMLP peptide fragments), producing a high score without genuine biological support.

A second predicted indication in this evidence pack, congenital prothrombin deficiency (score 99.26%), shows the same pattern: its only linked trial (NCT06227429) studies Nitisinone — an unrelated drug for hereditary tyrosinemia type 1 — and was withdrawn with zero enrollment. Both candidates in this pack are therefore best interpreted as likely false positives requiring entity-mapping verification before any further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma **tyrosine** (not phenylalanine) levels and their relation to fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; not a phenylalanine intervention study |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | Journal of Clinical and Experimental Hepatology | Serum metabolomic profiling in cholangiocarcinoma vs. benign hepatobiliary disease; phenylalanine appears only as one of many measured biomarkers, not as a treatment |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal study | Journal of Gastroenterology | The peptide FMLP (formyl-methionyl-leucyl-phenylalanine) was used to **induce** small duct cholangitis in rats — a disease model, not therapeutic evidence, and pharmacologically distinct from free phenylalanine |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Other (assay method) | Journal of Gastroenterology and Hepatology | Describes a radioimmunoassay method for bacterial chemotactic peptides (F-met-oligopeptides) and their enterohepatic circulation; a methodology paper, not related to phenylalanine treatment |

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/Health Canada labeling data (warnings, contraindications) has not yet been obtained — this is flagged as a **blocking gap** that prevents any initial safety assessment (S1 stage) for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only), the retrieved literature does not actually study phenylalanine as a therapeutic agent for the predicted indication, and the pattern strongly suggests knowledge-graph entity confusion rather than a real pharmacological signal. The drug is also unmarketed in Canada with no available label or safety data.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings and contraindications) — currently a blocking gap preventing safety review
- Verified mechanism of action data from DrugBank
- Confirmation/correction of the TxGNN entity mapping (rule out confusion between phenylalanine, tyrosine, and the FMLP peptide)
- Genuine clinical or preclinical evidence directly testing free phenylalanine — not confounded surrogate compounds — in sclerosing cholangitis or congenital prothrombin deficiency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

