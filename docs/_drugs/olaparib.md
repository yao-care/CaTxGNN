---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 576
evidence_level: L5
indication_count: 1
---

# Olaparib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib (DrugBank ID: DB09074) is a PARP1/2 inhibitor originally developed for BRCA-mutated, platinum-sensitive relapsed ovarian cancer. The TxGNN model predicts it may also be effective for **female breast carcinoma**, and this is not a purely theoretical extrapolation — it is already backed by **multiple completed Phase 3 RCTs** (OlympiAD, OlympiA) plus **20 supporting publications**, making this one of the strongest-evidenced candidates in this pipeline. The drug is currently **not marketed in Canada**, so regulatory data for this jurisdiction is not yet available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (BRCA-mutated, platinum-sensitive relapsed) — per trial-level evidence in this pack; no Canadian license record exists |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Canada Market Status | Not currently marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Olaparib is a PARP1/2 (poly ADP-ribose polymerase) inhibitor. In tumor cells with BRCA1/2 mutations — which impair homologous recombination DNA repair (HRD) — PARP inhibition triggers a "synthetic lethality" effect, selectively killing the cancer cells while sparing normal cells with intact DNA repair. This mechanism is described directly in the evidence pack's repurposing rationale, and it has already been validated in multiple Phase 3 RCTs, not merely predicted.

Ovarian cancer and breast cancer share substantial biological overlap: both are frequently associated with germline BRCA1/2 mutations, and the same DNA-repair deficiency that makes BRCA-mutated ovarian tumors sensitive to PARP inhibition applies equally to BRCA-mutated breast tumors. This is precisely why olaparib (Lynparza) has already received global regulatory approval for BRCA-mutated metastatic and early-stage breast cancer (OlympiAD, OlympiA trials) — the TxGNN prediction here is essentially recapitulating an already-established, guideline-supported indication.

Because efficacy is contingent on the underlying HRD/BRCA1/2 mutation status rather than tissue-of-origin, patient selection (germline BRCA1/2 testing or HRD status) is the critical guardrail for applying this mechanism safely and effectively in breast cancer.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Confirmatory real-world trial in Indian patients with platinum-sensitive relapsed ovarian cancer and germline BRCA1/2-mutated metastatic breast cancer, supporting approved indications |
| [NCT04553926](https://clinicaltrials.gov/study/NCT04553926) | N/A (post-marketing) | Completed | 661 | Lynparza (olaparib) real-world post-marketing surveillance in South Korea, assessing safety and effectiveness per approved indications |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Early dose-finding of olaparib + carboplatin in BRCA1/2-mutated breast/ovarian cancer and sporadic triple-negative breast/ovarian cancer |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Completed | 118 | Olaparib combined with PI3K inhibitors (BKM120/BYL719) in recurrent triple-negative breast cancer or high-grade serous ovarian cancer |
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | Recruiting | 880 | Comparing 1 vs. 2 years of maintenance olaparib ± bevacizumab in BRCA1/2-mutated/HRD-positive ovarian cancer after first-line platinum chemotherapy |
| [NCT06630325](https://clinicaltrials.gov/study/NCT06630325) | Phase 2 | Active, not recruiting | 30 | Precision-medicine adaptive treatment platform (SMMART-ACT) spanning sarcoma, prostate, breast, ovarian, and pancreatic cancer |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC — personalized treatment trial in high-risk breast cancer, directly testing olaparib in a breast cancer population |
| [NCT05700669](https://clinicaltrials.gov/study/NCT05700669) | Phase 1/2 | Completed | 3 | Basket study of AsiDNA™ + olaparib in recurrent ovarian, breast, and prostate cancer progressing after prior PARP inhibitor therapy (small sample size) |
| [NCT05238922](https://clinicaltrials.gov/study/NCT05238922) | Phase 1 | Recruiting | 604 | INCB123667 monotherapy/combination (including olaparib) in advanced solid tumors — early dose-escalation study |
| [NCT03570437](https://clinicaltrials.gov/study/NCT03570437) | Phase 2 | Unknown | 124 | COPELIA — cediranib + paclitaxel or olaparib vs. paclitaxel in advanced/relapsed endometrial carcinoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | New England Journal of Medicine | OlympiA trial: adjuvant olaparib significantly reduces recurrence in BRCA1/2-mutated, high-risk early breast cancer (pivotal Phase 3) |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | New England Journal of Medicine | OlympiAD trial: olaparib monotherapy shows antitumor activity in germline BRCA-mutated metastatic breast cancer (pivotal Phase 3, basis for approval) |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD final overall survival and tolerability results vs. chemotherapy of physician's choice |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | European Journal of Cancer | OlympiAD extended follow-up confirming long-term overall survival and safety profile |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | OlympiA overall survival analysis for adjuvant olaparib in high-risk, early-stage BRCA-mutated breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT | Journal of Clinical Oncology | TBCRC 048: Phase 2 study of olaparib in metastatic breast cancer with non-BRCA homologous recombination-related gene mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel improves pathologic complete response in high-risk HER2-negative breast cancer |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Annals of Laboratory Medicine | Review of BRCA1/2 pathogenic variant breast cancer — treatment and prevention strategies |
| [31218365](https://pubmed.ncbi.nlm.nih.gov/31218365/) | 2019 | Review | Annals of Oncology | A decade of clinical development of PARP inhibitors in perspective |
| [32444794](https://pubmed.ncbi.nlm.nih.gov/32444794/) | 2020 | Mechanistic study | Nature Communications | High-throughput functional evaluation of BRCA2 variants of unknown significance, supporting BRCA–PARP inhibitor synthetic lethality rationale |

---

## Canada Market Information

Olaparib currently has **no market authorization in Canada** (0 DINs on record in this evidence pack). No product listings, dosage forms, or approved indication text are available to summarize.

---

## Cytotoxicity

Olaparib is an antineoplastic agent (targeted PARP inhibitor used in oncology), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Monitoring required — the repurposing rationale explicitly flags a risk of myelodysplastic syndrome/acute myeloid leukemia (MDS/AML) with PARP inhibitor use; specific grading not provided in this pack |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential); germline BRCA1/2 mutation or HRD status confirmation as a patient-selection guardrail |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — flagged as DG001, a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1 — multiple completed Phase 3 RCTs: OlympiAD and OlympiA) and the mechanism is already clinically validated, not just model-predicted. However, olaparib is not currently marketed in Canada, and safety/label data (DG001) is a blocking gap, so real-world application requires biomarker-based patient selection (BRCA1/2/HRD status) and formal safety documentation before use.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph — key warnings, contraindications, and drug interaction data (DG001, blocking)
- Formal mechanism of action (MOA) documentation from DrugBank or the manufacturer label (DG002)
- Canadian market authorization status confirmation and DIN assignment, if/when filed
- BRCA1/2 germline mutation or HRD testing infrastructure to support guardrailed patient selection
- Long-term myelosuppression/MDS-AML monitoring protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

