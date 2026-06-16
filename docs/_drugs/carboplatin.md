---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a second-generation platinum-based chemotherapy agent used across multiple solid tumor types — including ovarian, lung, and head-and-neck cancers — working by forming covalent DNA cross-links that halt cancer cell replication and trigger programmed cell death.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, particularly in triple-negative (TNBC) and BRCA-mutated subtypes, with **50 registered clinical trials** and **20 publications** spanning over two decades of research providing strong support.
Multiple completed Phase 2/3 trials enrolling thousands of patients confirm the highest-tier evidence level (L1), and the recommended decision is to **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Health Canada DINs registered in current dataset (data gap) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs confirmed) |
| Canada Market Status | Not marketed (0 DINs in dataset) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data is not available in this dataset. Based on well-established oncology pharmacology, carboplatin belongs to the platinum-based antineoplastic class and acts by forming bulky platinum-DNA adducts — primarily intrastrand cross-links between adjacent guanine residues and interstrand cross-links between complementary strands. These lesions physically block the DNA polymerase machinery, stalling replication and triggering the DNA damage response. The critical dependency is on the cell's ability to reverse these adducts: effective repair requires a functional homologous recombination (HR) pathway, and tumors deficient in HR — whether through BRCA1/BRCA2 mutations or through epigenetic "BRCAness" — cannot survive platinum-induced damage, leading to a synthetic lethal outcome. This is the mechanistic foundation for carboplatin's predicted activity in breast cancer.

Breast cancer is strongly linked to this vulnerability through two major subtypes. In triple-negative breast cancer (TNBC), approximately 70% of tumors carry some degree of HR deficiency, and 15–20% carry germline BRCA1/2 mutations — making TNBC the breast cancer population most likely to benefit from platinum therapy. The landmark GeparSixto trial demonstrated this directly: adding carboplatin to standard neoadjuvant chemotherapy raised pathologic complete response (pCR) rates from 37% to 53% in TNBC patients. In HER2-positive breast cancer, a separate but complementary rationale applies: HER2 overexpression aberrantly activates the PI3K/AKT pathway, which impairs DNA damage repair machinery and sensitises these tumors to platinum agents. The BCIRG 006 Phase 3 trial (n=3,222) established the carboplatin-containing TCH regimen (docetaxel + carboplatin + trastuzumab) as a standard-of-care option for HER2+ operable breast cancer with equivalent efficacy to anthracycline-based regimens and a significantly better cardiac safety profile.

The TxGNN prediction therefore reflects validated pharmacology rather than speculative graph-based inference alone. Carboplatin is already integrated into breast cancer treatment globally, including in neoadjuvant TNBC protocols, adjuvant HER2+ regimens, BRCA-mutated metastatic settings, and emerging combinations with immune checkpoint inhibitors and PARP inhibitors. The repurposing question is less about whether carboplatin works in breast cancer and more about how to formalise indication-specific dosing, optimise patient selection through HRD biomarkers, and guide rational sequencing with newer targeted agents.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3,222 | BCIRG 006: TCH (docetaxel + carboplatin + trastuzumab) vs. anthracycline-based AC-T and AC-TH in HER2+ operable breast cancer; TCH showed equivalent disease-free survival with significantly lower rates of congestive heart failure, establishing it as the preferred anthracycline-sparing standard |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: dose-dense ETC vs. weekly paclitaxel/liposomal doxorubicin with carboplatin or dual HER2-blockade in high-risk early breast cancer; provides direct pCR and survival data for a carboplatin-containing dose-intensive regimen |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Head-to-head RCT comparing weekly paclitaxel alone vs. weekly paclitaxel + carboplatin as neoadjuvant therapy in large operable or locally advanced TNBC; primary endpoint pCR with long-term follow-up ongoing |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | Randomized evaluation of adding carboplatin to standard neoadjuvant anthracycline + taxane (± trastuzumab) in TNBC and HER2+ early breast cancer; one of the pivotal trials defining the scope of carboplatin's neoadjuvant benefit |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | Completed | 191 | First-line nab-paclitaxel + gemcitabine vs. nab-paclitaxel + carboplatin vs. gemcitabine + carboplatin in triple-negative metastatic breast cancer; three-arm design directly comparing carboplatin-containing doublets |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | Active, not recruiting | 120 | Pembrolizumab (anti-PD-1) + carboplatin + docetaxel as neoadjuvant for stage I–III TNBC; explores whether PD-1 blockade augments the platinum-based backbone to improve pCR and long-term outcomes |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomized comparison of neoadjuvant carboplatin + docetaxel vs. carboplatin + paclitaxel followed by AC in stage I–III TNBC; informs the optimal taxane partner for carboplatin in a sequenced regimen |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | BRCA Trial: carboplatin vs. docetaxel as single agents in metastatic BRCA1/2-mutated breast cancer; provides direct head-to-head evidence for carboplatin monotherapy activity in the genomically selected population |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | NEAT Trial: neoadjuvant bevacizumab + docetaxel + carboplatin in TNBC; evaluates anti-angiogenic augmentation of a platinum-taxane backbone, with pCR as primary endpoint |
| [NCT07074106](https://clinicaltrials.gov/study/NCT07074106) | Phase 2 | Not yet recruiting | 40 | DespaTIL: biomarker-guided de-escalated carboplatin neoadjuvant regimen for stage I–II TNBC stratified by TIL levels and MRI response; represents the next generation of response-adapted precision de-escalation research |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2) | Lancet Oncology | GeparSixto: carboplatin addition to neoadjuvant chemotherapy raised pCR from 37% to 53% in TNBC (statistically significant); landmark trial establishing platinum's clinical role in HR-deficient breast cancer |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT (Phase 3) | JAMA | CamRelief: camrelizumab (anti-PD-1) + anthracycline/cyclophosphamide/taxane/platinum neoadjuvant regimen significantly improved pCR in early and locally advanced TNBC; confirms carboplatin as the essential chemotherapy backbone for current immunotherapy combinations |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clin Cancer Res | NeoSTOP: multisite trial comparing anthracycline-free (carboplatin + taxane) vs. anthracycline-containing carboplatin regimens in TNBC; both achieved favourable pCR rates, supporting a carboplatin-based anthracycline-sparing option |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3, final OS) | Eur J Cancer | BROCADE3 final OS data: veliparib (PARPi) + carboplatin + paclitaxel significantly improved progression-free survival vs. placebo + carboplatin + paclitaxel in germline BRCA1/2-mutated advanced breast cancer; supports PARPi + platinum synthetic lethality in practice |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nature Comm | MUKDEN 06: ARX788 (anti-HER2 ADC) + pyrotinib vs. TCbHP (docetaxel + carboplatin + trastuzumab + pertuzumab) as neoadjuvant in early HER2+ breast cancer; carboplatin-containing TCbHP serves as the gold-standard comparator, affirming its current benchmark role |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Pooled meta-analysis confirming that both carboplatin and bevacizumab independently improve pCR in TNBC neoadjuvant treatment; quantifies the platinum effect across multiple trials |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncology | Comprehensive synthesis of preclinical synergy data and Phase II clinical results for paclitaxel + carboplatin in advanced breast cancer; foundational review establishing the pharmacological rationale for the doublet |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Prospective cohort | Breast Cancer R&T | Phase I trial of carboplatin + gemcitabine + mifepristone (glucocorticoid receptor antagonist) in GR-positive advanced breast and ovarian cancer; demonstrates that GR blockade enhances carboplatin cytotoxicity and provides a novel resistance-reversal strategy |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase II | Breast Cancer Res | Carboplatin + bevacizumab for breast cancer brain metastases; signals CNS penetration activity and manageable toxicity profile in a heavily pre-treated, poor-prognosis population |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Phase II | Semin Oncol | Early foundational evidence for carboplatin single-agent activity and paclitaxel + carboplatin synergy in advanced breast cancer; established the pharmacological and clinical rationale that preceded modern trial development |

---

## Canada Market Information

No Health Canada drug identification numbers (DINs) are registered for carboplatin in the current dataset (total DINs = 0). Carboplatin is, however, a widely available generic chemotherapy agent in Canadian oncology centres with decades of clinical use. This absence most likely reflects a data collection gap rather than true market unavailability. A direct query of the Health Canada Drug Product Database is recommended to identify approved carboplatin formulations, current labelled indications, and associated product monographs before proceeding.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum compound (forms bifunctional platinum-DNA adducts; mechanism functionally analogous to alkylating agents) |
| Myelosuppression Risk | High — Thrombocytopenia is the primary dose-limiting toxicity (more pronounced than cisplatin); neutropenia also common; nadir typically at days 14–21 post-infusion; platelet transfusion or dose modification may be required in heavily pre-treated patients or dose-dense regimens |
| Emetogenicity Classification | Moderate to High — Aggressive prophylaxis required: 5-HT₃ antagonist + NK₁ receptor antagonist + dexamethasone ± olanzapine as per MASCC/ESMO guidelines |
| Monitoring Items | CBC with differential and platelet count before each cycle; serum creatinine and calculated GFR (Calvert formula mandatory for carboplatin dose calculation); serum electrolytes (Mg²⁺, K⁺, Ca²⁺); liver function tests; audiometric testing if high-dose chemotherapy (HDCT) regimen is used |
| Handling Protection | Preparation in a certified biological safety cabinet (BSC) by trained oncology pharmacy personnel; full cytotoxic PPE required (chemotherapy gloves, impermeable gown, eye/face protection) per institutional cytotoxic handling and spill management protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carboplatin for female breast carcinoma carries the highest achievable evidence level (L1), underpinned by multiple completed Phase 3 trials with thousands of participants, a well-characterised mechanistic basis in HR-deficiency/BRCAness, and current real-world use across major oncology centres worldwide. The TxGNN prediction score of 99.86% is fully consistent with this deep empirical evidence base. The primary guardrails are patient selection using HRD/BRCA biomarkers, mandatory renal-function-based dosing via the Calvert formula, and cardiac monitoring when trastuzumab co-administration is planned.

**To proceed, the following is needed:**
- **Resolve the Health Canada DIN data gap**: query the Health Canada Drug Product Database directly to confirm approved carboplatin formulations, labelled indications, and current product monograph content
- **Obtain the package insert/monograph**: review up-to-date contraindications, key warnings, and drug interaction data (currently a Blocking data gap per DG001)
- **Establish BRCA1/2 and HRD testing protocol**: patient selection is essential, particularly for early-stage TNBC where carboplatin addition is not universally standard — HRD score or BRCA status should guide treatment decisions
- **Define the specific regimen and clinical setting**: options include neoadjuvant TCH (HER2+), carboplatin + taxane ± immunotherapy (TNBC), or veliparib + carboplatin + paclitaxel (BRCA-mutated metastatic) — each requires a dedicated dosing and monitoring plan
- **Cardiac safety plan**: baseline ECHO or MUGA scan required before any trastuzumab co-administration; ongoing cardiac monitoring per HER2-targeted therapy protocols
- **Institutional cytotoxic handling SOP review**: confirm compliance with current Canadian safe handling standards and waste disposal requirements for platinum-based agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

