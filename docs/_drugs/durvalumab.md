---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From NSCLC to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab (Imfinzi®) is an anti-PD-L1 checkpoint inhibitor with established global approvals for NSCLC, small cell lung cancer, and biliary tract cancer, but currently holds no Canadian DINs per this dataset.
The TxGNN model predicts it may be effective across **10 rare urothelial and gynaecological carcinoma subtypes**, led by prostatic urethra urothelial carcinoma (rank 1, score 99.98%); evidence quality ranges from **L2 (endocervical carcinoma)** to **L5 (model prediction only)** depending on the specific indication.
Across all 10 predictions, **3 clinical trials** and **1 publication** were identified; the highest-actionability indication is endocervical carcinoma (rank 6), supported by a completed Phase 1 and an ongoing Phase 2 trial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NSCLC / SCLC / biliary tract cancer (global approvals; no Canadian DIN on record in this dataset) |
| Predicted New Indication (Top Rank) | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (rank 1 top indication); L2 best-in-class (endocervical carcinoma, rank 6) |
| Canada Market Status | ✗ Not Marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold (urothelial subtypes, ranks 1–4); Proceed with Guardrails (endocervical carcinoma, rank 6) |

---

## Why Is This Prediction Reasonable?

Detailed MOA data from DrugBank is not available in this dataset. Based on the published literature and class pharmacology, Durvalumab is a selective, high-affinity human IgG1κ monoclonal antibody that blocks PD-L1 binding to both PD-1 and CD80 (B7.1), thereby restoring T-cell–mediated anti-tumour immune surveillance. Its proven efficacy in NSCLC, SCLC, and biliary tract cancer is underpinned by the widespread expression of PD-L1 across tumour types with high mutational burden (TMB) or carcinogen/virus-driven genomic instability.

The urothelial carcinoma predictions (ranks 1–4) share a common anatomical and histological basis: all arise from PD-L1–expressing urothelial epithelium. Durvalumab has previously been evaluated in broad urothelial carcinoma programmes (DANUBE Phase 3, NCT01693562), establishing proof-of-concept even where primary endpoints were not met. The sarcomatoid variants (ranks 2–3) are particularly compelling because sarcomatoid dedifferentiation is associated with higher TMB and elevated PD-L1 expression, increasing theoretical sensitivity to checkpoint blockade. NCT03912818 targeted the sarcomatoid bladder variant directly (Phase 2), though it was terminated early.

For the gynaecological predictions, endocervical carcinoma (rank 6) stands apart. HPV-driven E5/E7 oncoproteins directly upregulate PD-L1 expression through the JAK/STAT and PI3K pathways, creating an immune-suppressive microenvironment that is mechanistically susceptible to PD-L1 inhibition. This rationale is already being tested clinically in NCT04065269 (ATARI, Phase 2, n=174). The remaining gynaecological predictions (ranks 5, 7–10) are ultra-rare entities with distinct molecular profiles — several are HPV-negative or carry biology antagonistic to checkpoint inhibitors — and the TxGNN scores reflect topological proximity in the knowledge graph rather than direct mechanistic evidence.

---

## Predicted Indications — All-10 Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Evidence Available |
|------|---------|-------------|----------------|----------|------------------------|
| 1 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L4 | Hold | None |
| 2 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.98% | L3 | Hold | 1 trial (Early Phase 1) |
| 3 | Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant | 99.98% | L3 | Hold | 2 trials (Phase 2 terminated; Early Phase 1) |
| 4 | Renal Pelvis Papillary Urothelial Carcinoma | 99.98% | L4 | Hold | None |
| 5 | Uterine Ligament Adenocarcinoma | 99.92% | L5 | Hold | None |
| **6** | **Endocervical Carcinoma** | **99.91%** | **L2** | **Proceed with Guardrails** | **2 trials + 1 publication** |
| 7 | Adenoid Cystic Carcinoma of the Cervix Uteri | 99.91% | L5 | Hold | None |
| 8 | Uterine Ligament Serous Adenocarcinoma | 99.91% | L5 | Hold | None |
| 9 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold | None |
| 10 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold | None |

---

## Clinical Trial Evidence

Trials identified across all relevant predicted indications:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab + neoadjuvant chemotherapy (MVAC/GC) in variant histology bladder cancer including sarcomatoid; terminated early due to low accrual — no efficacy conclusions possible, but design directly targeted this subtype |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Durvalumab + tremelimumab pre-surgical in muscle-invasive high-risk urothelial carcinoma ineligible for cisplatin; safety and immune response assessment; covers upper urinary tract; no efficacy endpoint reached yet |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated SBRT + durvalumab + tremelimumab in recurrent/metastatic cervical, vaginal, or vulvar cancer; completed — safety and dosing established; results applicable to endocervical carcinoma subtype |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Active, Not Recruiting | 174 | ATARI trial: ATR inhibitor ceralasertib ± olaparib or durvalumab in relapsed gynaecological cancers stratified by ARID1A loss; largest ongoing Durvalumab trial in gynaecological cancers; results expected August 2026 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Small cell neuroendocrine carcinoma of the cervix: molecular basis and therapeutic landscape; highlights emerging role of immune checkpoint strategies in aggressive cervical cancer variants; management parallels with neuroendocrine lung cancer noted |

---

## Canada Market Information

No Canadian product authorisations for Durvalumab are registered in this dataset.

> **Note:** Durvalumab (Imfinzi®) holds approvals from the FDA (NSCLC, ES-SCLC, biliary tract cancer, HCC) and EMA in multiple indications. If Health Canada regulatory status has changed after the data cutoff (2026-04-04), the DIN registry should be re-queried to confirm current market standing before proceeding with any repurposing strategy.

---

## Cytotoxicity

Durvalumab is an antineoplastic agent (checkpoint inhibitor immunotherapy) indicated for cancer treatment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-L1 checkpoint inhibitor (IgG1κ monoclonal antibody); not a conventional cytotoxic |
| Myelosuppression Risk | Low (haematological toxicity uncommon; primary toxicities are immune-mediated: pneumonitis, hepatitis, endocrinopathies) |
| Emetogenicity Classification | Low |
| Monitoring Items | LFTs, thyroid function (TSH / free T4), fasting glucose, CBC with differential, serum creatinine; clinical assessment for immune-related adverse events (irAEs) before each cycle |
| Handling Protection | Standard biohazard precautions for IV monoclonal antibody administration; cytotoxic drug handling protocols are not required |

---

## Safety Considerations

Detailed Health Canada package insert warnings and contraindications are not available in this dataset. Please refer to the Imfinzi® product monograph for complete prescribing information.

Based on class pharmacology (anti-PD-L1 checkpoint blockade), clinicians should be aware of the following key safety considerations:

- **Immune-related adverse events (irAEs):** Pneumonitis, immune-mediated hepatitis, colitis, endocrinopathies (thyroiditis, adrenal insufficiency, type 1 diabetes), nephritis, and dermatitis — may be severe or life-threatening; require corticosteroid management and potential permanent discontinuation
- **Infusion-related reactions:** Monitor patients during and for at least 1 hour after each infusion
- **Reproductive toxicity:** Checkpoint inhibitors can cause immune-mediated foetal harm; effective contraception required; breastfeeding not recommended during treatment

---

## Conclusion and Next Steps

### For Urothelial Subtypes (Ranks 1–4)

**Decision: Hold**

**Rationale:**
No direct clinical trial evidence exists for the specific urothelial subtypes predicted (prostatic urethral, renal pelvic sarcomatoid, renal pelvic papillary). Evidence from broader urothelial carcinoma programmes is mechanistically relevant but insufficient to justify dedicated pursuit without subtype-specific data.

**To proceed, the following is needed:**
- Conduct a targeted literature review for subgroup analyses within DANUBE (NCT01693562) and PEARL trials that may report outcomes stratified by tumour location (upper tract vs. bladder) or histological variant
- Monitor NCT02812420 (currently active, n=54) for interim results covering upper urinary tract urothelial carcinoma
- For the sarcomatoid variants (ranks 2–3): assess whether future basket trials in high-TMB urothelial carcinoma could enrol these subtypes; consider partnering with a rare histology consortium

---

### For Endocervical Carcinoma (Rank 6)

**Decision: Proceed with Guardrails**

**Rationale:**
Two clinical trials provide direct support: a completed Phase 1 (NCT03452332, n=20) establishing safety in cervical cancer, and an ongoing Phase 2 (NCT04065269, ATARI, n=174) evaluating durvalumab in relapsed gynaecological cancers with ARID1A stratification. The HPV-mediated PD-L1 upregulation mechanism provides a credible biological rationale for endocervical carcinoma specifically.

**To proceed, the following is needed:**
- Retrieve Health Canada product monograph / TFDA package insert to complete safety evaluation (DG001 — currently blocking S1 safety review)
- Obtain MOA data from DrugBank (DG002) to formalise mechanistic justification
- Monitor NCT04065269 (ATARI) results — expected completion August 2026; endocervical carcinoma subgroup data will be pivotal
- Conduct PD-L1 expression prevalence review specific to endocervical (vs. exocervical) adenocarcinoma to quantify the biomarker-eligible patient population
- Assess whether a Health Canada regulatory filing for a cervical cancer indication is feasible following ATARI results, particularly given the absence of current DINs

---

### For Ultra-Rare Gynaecological Entities (Ranks 5, 7–10)

**Decision: Hold**

These indications (uterine ligament tumours, adenoid cystic carcinoma of cervix, signet ring cell/intestinal mucinous adenocarcinomas) lack any supporting clinical or preclinical data. TxGNN scores reflect knowledge graph topology rather than biological plausibility. Deprioritise unless targeted evidence emerges from dedicated rare tumour programmes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

