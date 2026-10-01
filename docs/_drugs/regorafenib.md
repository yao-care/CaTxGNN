---
layout: default
title: Regorafenib
parent: High Evidence (L1-L2)
nav_order: 793
evidence_level: L2
indication_count: 10
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Regorafenib: From Metastatic Colorectal Cancer and GIST to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multikinase inhibitor, approved elsewhere for metastatic colorectal cancer and gastrointestinal stromal tumour (GIST), and marketed in Canada as STIVARGA.
The TxGNN model predicts it may be effective for **liposarcoma**, with **2 clinical trials** and **9 publications** linked to this prediction.
However, the two randomized Phase 2 trials in this evidence set **did not support** benefit in liposarcoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer and GIST (taken from the literature; the Canadian label text is not available in the data) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Regorafenib is an oral diphenylurea multikinase inhibitor. It targets angiogenic kinases (VEGFR1-3, TIE2), stromal kinases (PDGFR-β, FGFR) and oncogenic kinases (KIT, RET, RAF). This profile comes from the literature in the evidence set, because the DrugBank mechanism field was empty. It was the first small-molecule multikinase inhibitor to show a survival benefit in refractory metastatic colorectal cancer, and it is also used in GIST.

Liposarcoma is a soft tissue sarcoma, a tumour type in which angiogenesis and PDGFR/KIT signalling are thought to play a role. Related kinase inhibitors such as pazopanib are used in non-adipocytic soft tissue sarcoma, which is why the model links regorafenib to sarcoma.

The clinical data weaken this link, though. The REGOSARC trial showed activity in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but **not in liposarcoma**. The dedicated liposarcoma cohort of SARC024 reached the same conclusion. A high model score therefore reflects mechanistic and network similarity, not proven efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: randomized, double-blind, placebo-controlled trial in metastatic soft tissue sarcoma after anthracycline. It had a liposarcoma cohort (Cohort A). Published analyses report benefit in non-adipocytic subtypes but not in liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: blanket protocol of regorafenib in selected sarcoma subtypes, including a randomized placebo-controlled liposarcoma cohort. The liposarcoma result was limited (see PMID 32701199). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncol | REGOSARC primary publication: randomized, double-blind, placebo-controlled Phase 2 trial of regorafenib in anthracycline-pretreated metastatic soft tissue sarcoma. |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | Oncologist | SARC024 liposarcoma cohort confirms earlier data and does not support routine use of regorafenib in this population. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (secondary analysis) | Eur J Cancer | Updated REGOSARC analysis including cross-over. Efficacy was shown in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but not in liposarcoma. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Cohort (post hoc analysis of RCT data) | Cancer | Quality-adjusted time without symptoms or toxicity (Q-TWiST) analysis of REGOSARC in doxorubicin-pretreated non-adipocytic sarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocol | BMC Cancer | REGOSARC study protocol, with the rationale for angiogenesis targeting in sarcoma. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targ Oncol | Review of regorafenib's growing role in sarcoma, with efficacy varying by histological subtype. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | Review of maintenance therapy after first-line treatment for advanced soft tissue sarcoma. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug: anlotinib) | Anti-Cancer Drugs | Anlotinib in well-differentiated/dedifferentiated liposarcoma. Included for context only, as it does not evaluate regorafenib. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2403390 | STIVARGA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multikinase inhibitor) |
| Monitoring Items | Liver function, blood pressure and skin (hand-foot skin reaction). The literature in the evidence set reports hepatic toxicity, hypertension and hand-foot skin reaction with this drug class. |

Please refer to the package insert warnings and precautions for myelosuppression risk, emetogenicity and handling protection.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data provided.

The literature in the evidence set reports hand-foot skin reaction, hypertension and hepatic toxicity as notable adverse events of regorafenib and related anti-angiogenic kinase inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two randomized placebo-controlled Phase 2 studies (REGOSARC and SARC024) did not show benefit of regorafenib in liposarcoma, and the SARC024 authors state the results do not support routine use. The high TxGNN score is not supported by the clinical results for this indication.

**To proceed, the following is needed:**
- Health Canada monograph warnings and contraindications, and the approved indication text
- Rationale for any biomarker- or subtype-selected liposarcoma population, or combination approach, that could justify further study
- Confirmation of the liposarcoma-specific results against the primary publications

**Note on other predictions:** Regorafenib's evidence is stronger for renal cell carcinoma than for liposarcoma, but only at single-arm Phase 2 level (PMID 22959186; NCT00664326, n=49). It would need randomized data before any recommendation. The remaining predicted indications have prediction-only support and should stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

