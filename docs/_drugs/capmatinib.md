---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Capmatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Capmatinib: From Non-Small Cell Lung Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib (Tabrecta) is a selective MET/c-Met receptor tyrosine kinase inhibitor, originally approved for metastatic non-small cell lung cancer (NSCLC) harbouring MET exon 14 skipping mutations.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**, with the mechanistic basis centred on pathological HGF/c-Met overactivation in RA synovial tissue.
Currently, **0 clinical trials** and **1 tangentially related publication** support this direction — this remains an early-stage research hypothesis with no clinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-small cell lung cancer (NSCLC) with MET exon 14 skipping mutations |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the retrieved dataset. Based on known pharmacological information, capmatinib is a highly selective small-molecule inhibitor of the MET receptor tyrosine kinase (c-Met). Its approved oncology indication exploits MET exon 14 skipping mutations, which eliminate a regulatory degradation signal and cause sustained MET kinase activation — driving tumour cell proliferation and survival in NSCLC.

In rheumatoid arthritis, the same HGF/c-Met signalling axis is pathologically dysregulated in a non-oncological context. c-Met is overexpressed in synovial fibroblasts (FLS), and HGF-driven MET signalling promotes FLS proliferation, invasion into articular cartilage, and pannus formation — the core tissue-destructive mechanism of RA joint damage. MET activation also upregulates RANKL, amplifying osteoclastogenesis and accelerating periarticular bone erosion.

The conceptual bridge between cancer and RA therefore lies in a shared effector pathway: aberrant c-Met activity drives tissue invasion in both contexts, whether in tumour cells or synovial fibroblasts. This mechanistic rationale is biologically coherent and generates a testable hypothesis, but it remains entirely unvalidated in RA — no preclinical animal model studies or clinical trials with capmatinib have been published for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Capmatinib in Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Narrative Review | Pharmacological Research | Comprehensive compendium of 62 FDA-approved small-molecule protein kinase inhibitors (2021 update); capmatinib is catalogued as a selective MET inhibitor — rheumatoid arthritis is not a focus of this article and no RA-specific data are presented |

---

## Canada Market Information

Capmatinib currently has no Health Canada–issued Drug Identification Numbers (DINs) and is not commercially available in Canada as of the data cutoff (June 2026). No approved product listings are available to display.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective MET receptor tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (peripheral oedema, nausea, fatigue, and dyspnoea are the predominant adverse effects; significant cytopenias are uncommon) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, serum creatinine, liver function tests (ALT/AST/bilirubin), peripheral oedema assessment, pulmonary symptoms (interstitial lung disease monitoring) |
| Handling Protection | Should follow institutional cytotoxic/antineoplastic drug handling procedures for oral targeted agents |

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) was retrieved for this candidate in the current Evidence Pack.

Please refer to the Tabrecta (capmatinib) full prescribing information and Health Canada product monograph for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HGF/c-Met pathway is mechanistically plausible in RA pathobiology, but no clinical trials or RA-directed preclinical studies have been published for capmatinib, the sole supporting literature is a general kinase compendium unrelated to RA, and the drug is not currently marketed in Canada — making further research groundwork a prerequisite before any development decision.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro FLS invasion/proliferation assays and in vivo RA model studies (e.g., collagen-induced arthritis mouse model) to confirm c-Met inhibition reduces synovial pathology at clinically achievable capmatinib concentrations
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank API and the current prescribing information to close data gap DG002
- **Safety data retrieval**: Download and parse the Tabrecta product monograph for key warnings, contraindications, and clinically significant drug interactions (data gap DG001)
- **Pharmacokinetic assessment**: Confirm whether oral capmatinib achieves adequate synovial tissue concentrations sufficient for anti-inflammatory effect in a non-oncology dosing context
- **Competitive landscape review**: Assess differentiation potential against established RA biologics (TNF inhibitors, IL-6 inhibitors, JAK inhibitors) — particularly JAK inhibitors, which already target overlapping downstream kinase signalling and are approved for RA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

