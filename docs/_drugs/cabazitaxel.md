---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a next-generation taxane originally approved for docetaxel-refractory metastatic castration-resistant prostate cancer (mCRPC), where it stabilizes microtubules to trigger cancer cell death while evading the P-glycoprotein drug efflux pump that causes resistance to older taxanes.
The TxGNN model predicts it may be effective for **female breast carcinoma** with a confidence score of **99.92%**,
supported by **0 registered clinical trials** retrieved by automated search and **20 publications** — including one Phase 2 RCT and one Phase I/II dose-escalation study that directly tested cabazitaxel in breast cancer patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), post-docetaxel (inferred from published literature; no Canadian DIN on file) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel is a semi-synthetic taxane derived from the natural precursor 10-deacetylbaccatin III. Like paclitaxel and docetaxel, it binds to β-tubulin within assembled microtubules and stabilizes them against depolymerization. This freezes the dynamic instability that dividing cells require for proper chromosome segregation, causing G2/M arrest and programmed cell death. What distinguishes cabazitaxel from first-generation taxanes is its very low affinity for P-glycoprotein (P-gp/MDR1) — the cell-surface efflux pump that exports taxanes out of resistant tumor cells — which is why it retains activity even after docetaxel or paclitaxel have failed.

Breast cancer cells, particularly triple-negative (TNBC) and luminal B/HER2-negative subtypes, proliferate rapidly and depend on intact microtubule dynamics. Taxanes are already cornerstones of breast cancer chemotherapy, and MDR1-mediated resistance is a well-recognized clinical obstacle after multiple lines of treatment. Cabazitaxel's P-gp evasion makes it mechanistically compelling precisely in this taxane-refractory setting. Notably, overexpression of the βIII-tubulin isotype — common in TNBC and normally associated with taxane resistance — paradoxically *enhances* cabazitaxel's efficacy relative to docetaxel (PMID 28567478), providing an additional molecular rationale that aligns the drug's unique properties with a breast cancer subpopulation that has few remaining options.

A further advantage is cabazitaxel's ability to penetrate the blood-brain barrier, a consequence of its low P-gp substrate affinity. Breast cancer patients who develop CNS metastases have very limited systemic treatment options because most chemotherapeutics are excluded from the brain. A Phase II study (PMID 29678476) specifically exploited this property by combining cabazitaxel with lapatinib in HER2-positive metastatic breast cancer patients with active intracranial metastases, directly demonstrating clinical interest in this CNS-penetrating capability.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in ClinicalTrials.gov or ICTRP for cabazitaxel in female breast carcinoma (search conducted 2026-03-24).

> **Note:** Several clinical trial publications are captured in the Literature Evidence section below (PMID 28768217, PMID 21339064, PMID 29678476), indicating that trials have been conducted; however, they were not retrieved by the automated registry query and may have been registered under broader search terms or different indication labels.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase 2 RCT | European Journal of Cancer | GENEVIEVE study: cabazitaxel vs. weekly paclitaxel as neoadjuvant therapy in HER2-negative breast cancer (TNBC and luminal B); compared pathological complete response rates in operable patients |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/2 | European Journal of Cancer | Multicentre dose-escalation of cabazitaxel + capecitabine in metastatic breast cancer progressing after anthracycline and taxane; determined MTD, safety profile, PK, and anti-tumour activity |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase 2 | Clinical Breast Cancer | Cabazitaxel + lapatinib in HER2+ metastatic breast cancer with active intracranial metastases (NCT01934894); leveraged cabazitaxel's blood-brain barrier penetration for CNS disease |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review (Resistance) | Molecular Cancer Therapeutics | Mechanisms of cabazitaxel resistance characterized using MCF-7 breast cancer cell lines; cabazitaxel showed markedly less MDR cross-resistance (15-fold) than paclitaxel/docetaxel (200-fold) |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | Journal for Immunotherapy of Cancer | Cabazitaxel reprogrammes tumour-associated macrophages (TAMs) to enhance CD47-targeted immunotherapy in TNBC; in vitro and in vivo mouse models |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Preclinical | Cancer Chemotherapy and Pharmacology | βIII-tubulin overexpression (frequent in TNBC) enhances cabazitaxel efficacy relative to docetaxel; mechanistic basis for preferential use in βIII-tubulin-high tumours |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | Cabazitaxel-loaded PACA nanoparticles achieved complete remission in 6/8 patient-derived basal-like breast cancer (TNBC) xenografts vs. 3/8 with free drug |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | Extended preclinical evaluation of poly(2-alkyl cyanoacrylate) NP variants of cabazitaxel in breast cancer models, with evidence of tumour microenvironment modulation (M2 macrophage reduction) |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs of Today | Foundational overview of cabazitaxel: characterizes P-gp bypass, broad activity across taxane-resistant cell lines, Phase I safety profile (neutropenia, neuropathy as primary AEs) |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | Review (Patent) | Expert Opinion on Therapeutic Patents | Taxane patent landscape; documents cabazitaxel's 2010 FDA approval for mCRPC and positions it alongside abraxane for multiple cancer indications including breast cancer |

---

## Canada Market Information

Cabazitaxel currently has **no Drug Identification Numbers (DINs)** registered in Canada. The drug is not approved or commercially available in Canada as of the data cutoff (2026-04-10). Any clinical use would require either a Health Canada authorization (e.g., Special Access Programme) or a Clinical Trial Application (CTA).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (semi-synthetic microtubule stabilizer) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia with fatal outcomes has been reported. G-CSF primary prophylaxis is standard practice |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential before each cycle; liver function tests (ALT, AST, bilirubin); renal function (creatinine); neurological assessment for peripheral neuropathy; diarrhoea severity grading |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in a certified biosafety cabinet, double-glove PPE, closed-system drug transfer devices recommended; spill kits required |

---

## Safety Considerations

Please refer to the package insert (Jevtana® product monograph) for complete safety information, as formal Health Canada-approved warnings and contraindications are not available in this Evidence Pack.

Based on published clinical trial data and the known taxane class profile, clinicians should be aware of the following key risks:

- **Severe myelosuppression**: Grade 3–4 neutropenia is frequent; neutropenic deaths have occurred. Mandatory CBC monitoring before each cycle and G-CSF prophylaxis are required.
- **Severe hypersensitivity**: Serious reactions (including anaphylaxis) can occur; antihistamine and corticosteroid premedication is required prior to each infusion.
- **Peripheral neuropathy**: A class effect of taxanes; cumulative neuropathy may require dose reduction or treatment discontinuation.
- **Gastrointestinal toxicity**: Diarrhoea and mucositis are more prominent with cabazitaxel than with docetaxel; aggressive supportive management is needed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between cabazitaxel and breast cancer is well-grounded — it shares the taxane class mechanism with established breast cancer drugs while specifically overcoming MDR1-mediated resistance, which is clinically relevant for taxane-refractory patients. The GENEVIEVE Phase 2 RCT and the Phase I/II capecitabine combination study provide direct clinical proof-of-concept in breast cancer patients, justifying an L2 evidence rating. However, cabazitaxel is not currently marketed in Canada and carries a high myelosuppression risk that requires robust monitoring infrastructure before any clinical rollout.

**To proceed, the following is needed:**
- Obtain and fully review the Jevtana® (cabazitaxel) product monograph to document Health Canada-recognized contraindications, formal warnings, and drug interactions
- Define the target breast cancer subpopulation (e.g., TNBC post-taxane failure, HER2+ with active CNS metastases) to sharpen the clinical hypothesis and patient selection criteria
- Engage Health Canada for a pre-submission consultation to determine the regulatory pathway for a new breast cancer indication or a clinical trial authorization (CTA)
- Develop a comprehensive safety monitoring plan covering G-CSF prophylaxis protocols, CBC monitoring schedules, and neuropathy assessment
- Conduct additional preclinical or translational studies in βIII-tubulin-high breast cancer models to further validate the mechanistic rationale and support a biomarker-driven patient selection strategy

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

