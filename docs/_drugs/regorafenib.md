---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 672
evidence_level: L5
indication_count: 10
---

# Regorafenib
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

# Regorafenib: From Metastatic Colorectal Cancer/GIST to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multikinase inhibitor (VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF) originally approved for metastatic colorectal cancer and imatinib/sunitinib-refractory GIST. TxGNN predicts it may be effective for **Liposarcoma**, and two completed Phase 2 randomized controlled trials directly tested this — but both concluded the drug does **not** show clinically meaningful benefit in the liposarcoma subtype specifically. The evidence base is therefore sizeable (2 RCTs, 9 publications) but points against, not toward, this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer; GIST (per literature within evidence pack; not currently marketed in Canada, so no Canada-specific label text is available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 (direct RCT evidence exists, but is negative for this specific subtype) |
| Canada Market Status | 未上市 (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank MOA data was not returned for this candidate (`original_moa: [Data Gap]`). Based on the literature captured in this evidence pack, regorafenib is described as "an oral diphenylurea multi-kinase inhibitor that targets angiogenic (VEGFR1-3, TIE2), stromal (PDGFR-β, FGFR), and oncogenic receptor tyrosine kinases (KIT, RET, and RAF)" (PMID 30069758, 24756792), and was the first small-molecule multikinase inhibitor to show a survival benefit in metastatic colorectal cancer, with subsequent approval in GIST refractory to imatinib/sunitinib (per NCT02048371 summary).

Soft tissue sarcomas, including liposarcoma, are highly vascularized tumors, and angiogenesis is considered a key driver of sarcoma biology (PMID 25884155). This provides a mechanistic rationale for testing anti-angiogenic multikinase inhibitors such as regorafenib, sorafenib, and pazopanib across sarcoma subtypes — and is why liposarcoma was included as a dedicated cohort in two large trials (REGOSARC, SARC024).

However, the direct clinical evidence undercuts the mechanistic rationale for this specific subtype: the REGOSARC trial "demonstrated the efficacy of regorafenib in patients with leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcoma **but not in liposarcoma**" (PMID 29902612), and the SARC024 liposarcoma cohort concluded that results "do not support the routine use of regorafenib in this patient population" (PMID 32701199). Liposarcoma (adipocytic sarcoma) appears biologically distinct from the non-adipocytic sarcoma subtypes where regorafenib does work, which likely explains the discordance between the high TxGNN score and the negative trial outcomes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: international randomized, double-blind, placebo-controlled trial in anthracycline-refractory metastatic soft tissue sarcoma, with a dedicated liposarcoma cohort (Cohort A). Overall trial supported efficacy in non-adipocytic sarcoma subtypes, but not liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: multi-cohort "blanket protocol" testing oral regorafenib in selected sarcoma subtypes including liposarcoma; the liposarcoma cohort's randomized, placebo-controlled results did not support routine use of regorafenib in this population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | Phase 2 randomized, double-blind, placebo-controlled SARC024 liposarcoma cohort; results do not support routine use of regorafenib in treatment-refractory liposarcoma. |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncology | Primary REGOSARC results (NCT01900743): regorafenib efficacy/safety in advanced soft tissue sarcoma after anthracycline failure, across 5 histology cohorts. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (updated analysis) | European Journal of Cancer | Updated REGOSARC analysis including post-cross-over activity; confirms efficacy in leiomyosarcoma/synovial/other non-adipocytic sarcoma but not liposarcoma. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT post-hoc analysis | Cancer | Q-TWiST analysis of REGOSARC (NCT01900743) confirming PFS improvement with regorafenib in doxorubicin-pretreated advanced nonadipocytic sarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol | BMC Cancer | Study protocol for the REGOSARC trial, describing angiogenesis as a key mechanism in sarcoma biology and rationale for regorafenib testing. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Review of regorafenib's growing role in sarcoma treatment across STS histological subtypes including liposarcoma. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Review of maintenance therapy options, including TKIs, after first-line treatment for advanced soft tissue sarcoma. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study | Anti-Cancer Drugs | Retrospective study of anlotinib (a related TKI) in liposarcoma, noting regorafenib and pazopanib are approved for non-adipocytic STS but treatment options for liposarcoma remain limited. |

---

## Canada Market Information

Regorafenib is currently **not marketed in Canada** (`market_status: 未上市`, 0 DINs on file). No Health Canada license records are available for this drug.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multikinase/anti-angiogenic tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low — literature within this evidence pack characterizes regorafenib's dominant toxicities as dermatologic (hand-foot skin reaction, PMID 23700287), hypertension (PMID 36583425), and hepatotoxicity (PMID 23981115) rather than bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests, blood pressure, skin/dermatologic exam (hand-foot skin reaction), CBC |
| Handling Protection | As an oral targeted anticancer agent, follow institutional hazardous/oral-antineoplastic drug handling policy; does not require IV cytotoxic chemotherapy precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA/Health Canada warnings, contraindications, or DDI data were returned for this candidate — `DG001` in the evidence pack flags this as a Blocking data gap for the safety review stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for liposarcoma is high (99.76%) and is backed by an unusually large amount of direct evidence (2 completed Phase 2 RCTs, 9 publications), that evidence specifically and consistently shows regorafenib does **not** provide meaningful benefit in liposarcoma, even though it works in other soft tissue sarcoma subtypes. Combined with the drug's absence from the Canadian market and the missing safety/MOA data (DG001, DG002), there is no basis to proceed with this indication at this time.

**To proceed, the following is needed:**
- Confirmed DrugBank MOA data (DG002) to replace the current data gap
- TFDA/Health Canada label warnings and contraindications (DG001 — currently Blocking)
- If liposarcoma is still of interest, a biomarker- or subtype-stratified reanalysis to explain why non-adipocytic sarcomas respond but liposarcoma does not
- Consider re-evaluating rank 3 (clear cell renal carcinoma), which has a stronger mechanistic fit (VHL/HIF-VEGF pathway) and an unopposed single-arm Phase 2 trial, as a higher-priority alternative candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

