---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

Using the Evidence Pack, here is the drug repurposing evaluation report for Hydroxyurea (predicted_indications[0] = Female Breast Carcinoma, the top-ranked TxGNN prediction in this multi-indication pack).

---

# Hydroxyurea: From Hematologic Malignancies / Sickle Cell Disease to Female Breast Carcinoma

## One-Sentence Summary

> Hydroxyurea is a ribonucleotide reductase (RNR) inhibitor historically used as an antineoplastic and antisickling agent for conditions such as leukemia, sickle cell disease, and thrombocythemia.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> but this specific indication is currently supported only by **0 breast-cancer-specific clinical trials** and **20 publications**, most of which are preclinical, mechanistic, or decades-old combination-regimen studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Canadian licenses on file); internationally recognized uses include chronic myeloid leukemia, sickle cell disease, and essential thrombocythemia |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the literature retrieved in this evidence pack (PMID 26844848), hydroxyurea is described as an antineoplastic drug historically used for leukemia, sickle-cell disease, HIV, psoriasis, thrombocythemia, and various neoplastic diseases — its core pharmacology is inhibition of ribonucleotide reductase (RNR), which blocks DNA synthesis.

Because RNR inhibition blocks DNA synthesis broadly, the mechanistic rationale extends in theory to rapidly dividing breast carcinoma cells, and hydroxyurea has historically been explored as a radiosensitizer within combination chemoradiotherapy regimens for solid tumors. However, the direct clinical evidence for breast cancer specifically is thin: it is limited to early-1990s Phase I combination trials (HALF regimen, high-dose consolidation with autologous stem cell rescue) in which hydroxyurea was a secondary agent rather than the primary therapeutic driver.

More recent literature is predominantly preclinical or computational — in-silico lipid-conjugate design, radiolabeling/imaging studies, and mechanistic work on replication stress and DNA repair (e.g., valproic acid sensitization, ATR inhibition) — rather than modern controlled trials. This pattern is consistent with a plausible but so far unproven mechanistic hypothesis rather than a clinically validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hydroxyurea in female breast carcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I Trial | American Journal of Clinical Oncology | HALF regimen (5-FU/leucovorin + allopurinol, followed by hydroxyurea) tested in 20 patients with advanced GI and breast cancer |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II Trial | Bone Marrow Transplantation | High-dose cyclophosphamide + thiotepa + hydroxyurea with autologous stem cell rescue as consolidation for metastatic breast cancer (n=26) |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | Preclinical/In-silico | Drug Research | In-silico design of hydroxyurea–lipid conjugates targeting PI3K/AKT/mTOR to improve HU lipophilicity and efficacy in breast cancer |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | Preclinical (In Vitro/In Vivo) | Cancer Biotherapy & Radiopharmaceuticals | Radiolabeling of hydroxyurea ([99mTc(CO)3]-HU) for imaging; confirms HU's use across leukemia, sickle-cell disease, and neoplastic disease |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid influences RPA2 hyperphosphorylation as a potential alternative to valproic acid for HU-sensitization in breast carcinoma |
| [33631478](https://pubmed.ncbi.nlm.nih.gov/33631478/) | 2021 | Review | Pathology, Research and Practice | Review of long non-coding RNAs in breast cancer pathogenesis and prognosis |
| [31338966](https://pubmed.ncbi.nlm.nih.gov/31338966/) | 2019 | Preclinical | Journal of Cellular and Molecular Medicine | Berberine attenuates XRCC1-mediated base excision repair, sensitizing breast cancer cells to chemotherapeutic drugs |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | British Journal of Cancer | ATR inhibitor NU6027 evaluated in breast and ovarian cancer cell lines (replication-stress pathway relevant to HU mechanism) |
| [28585003](https://pubmed.ncbi.nlm.nih.gov/28585003/) | 2017 | Case Report | Breast Cancer (Tokyo, Japan) | Secondary breast carcinoma reported in a patient previously treated with hydroxyurea and imatinib for CML |

---

## Canada Market Information

Hydroxyurea is currently **not marketed** in Canada under this evidence pack — no Drug Identification Numbers (DINs) or license records are on file.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Ribonucleotide reductase inhibitor / antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
- There is a Blocking-severity data gap (DG001) on TFDA/Health Canada product monograph warnings and contraindications, which prevents even an initial safety screen (S1). Combined with the absence of any breast-cancer-specific clinical trials and evidence limited to preclinical/in-silico work plus non-specific 1990s Phase I combination regimens, this indication remains at a hypothesis-generation stage rather than one ready for development decisions.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph — warnings, contraindications, and drug interaction data (resolves Blocking gap DG001)
- Detailed mechanism of action (MOA) data from DrugBank (resolves High-severity gap DG002)
- Modern controlled clinical trials evaluating hydroxyurea specifically (not as a secondary combination agent) in breast carcinoma
- Confirmation of hydroxyurea's original approved indications and Canadian regulatory status, since no licenses are currently on file

**Note:** This evidence pack contains 9 additional TxGNN-predicted indications for hydroxyurea. Notably, **Sickle Cell–Hemoglobin C Disease Syndrome** (rank 6) carries a much stronger evidence base — Evidence Level **L1**, supported by multiple Cochrane systematic reviews and a completed Phase 3 RCT (NOHARM, n=187) — and a recommendation of "Proceed with Guardrails." That candidate likely warrants its own dedicated evaluation report separate from this breast carcinoma assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

