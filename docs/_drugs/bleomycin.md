---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Bleomycin: From Hodgkin's Lymphoma / Testicular Cancer to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a cytotoxic glycopeptide antibiotic with long-established use in treating Hodgkin's lymphoma, testicular germ cell tumors, and squamous cell carcinomas, primarily as a backbone component of the ABVD and BEP regimens.
The TxGNN model predicts it may be effective for **Cauda Equina Neoplasm**, achieving the highest prediction score (99.30%) among six modelled new indications.
Currently, **no clinical trials** and only **3 publications** — none directly targeting cauda equina tumors — are available to support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin's Lymphoma / Testicular Germ Cell Tumor (internationally established; not registered in Canada) |
| Predicted New Indication | Cauda Equina Neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not recorded in the Canadian regulatory database. Based on established scientific knowledge, bleomycin is a glycopeptide antitumor antibiotic that generates free radicals upon binding to DNA, causing single- and double-strand DNA breaks. This damage is selective for cells in the G2/M phase of the cell cycle, making bleomycin particularly effective against rapidly proliferating malignancies. It has historically been used in combination regimens (ABVD, BEP, ProMACE-CytaBOM) for lymphomas and germ cell tumors.

Cauda equina neoplasms are a heterogeneous group of tumors arising at or near the terminal spinal cord and nerve roots; histologically, many represent lymphomatous infiltration (e.g., diffuse large B-cell lymphoma or Hodgkin's lymphoma) or metastatic germ cell tumors spreading to the lumbosacral compartment. Given bleomycin's proven activity in both of these tumor types, a theoretical mechanistic rationale exists: if a cauda equina neoplasm shares the histological profile of a bleomycin-sensitive cancer, the drug's DNA-damaging mechanism could plausibly be active at that anatomical site.

However, the TxGNN model's high score most likely reflects **topological proximity** in the knowledge graph between lymphoma/GCT nodes and the cauda equina neoplasm node, rather than direct biological evidence. None of the three supporting publications address cauda equina neoplasm as a primary study endpoint, and no pharmacokinetic data exist on bleomycin's penetration into the spinal compartment. The prediction should therefore be interpreted as a hypothesis-generating signal, not a clinical recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bleomycin in cauda equina neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Retrospective Series | J Clin Oncol | Radiation therapy successfully salvaged CNS germinoma patients who relapsed after PEB (carboplatin + etoposide + **bleomycin**) primary chemotherapy; spinal/cauda equina sites were included in the relapse evaluation |
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Retrospective Cohort | Am J Clin Oncol | CNS involvement (including one documented cauda equina case at autopsy) in aggressive NHL treated with bleomycin-containing regimens; highlights anatomical vulnerability but does not report bleomycin efficacy at the cauda equina |
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case Report | Rinsho Shinkeigaku | Paraneoplastic sensory neuropathy in a 17-year-old with Hodgkin's lymphoma; MRI showed cauda equina enhancement; treated with IVIG, not bleomycin — illustrates cauda equina involvement in lymphoma context |

---

## Canada Market Information

Bleomycin is currently **not marketed in Canada**. No Health Canada–approved products or DINs are registered. Prescribers should refer to internationally recognized product monographs (e.g., FDA label, EMA SmPC) for regulatory and prescribing information.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antitumor glycopeptide antibiotic |
| Myelosuppression Risk | **Low** — Bleomycin is notable for its bone marrow–sparing properties; historical series (PMID 4109401) specifically highlight this as an advantage over other cytotoxics; neutropenia and thrombocytopenia are uncommon at standard doses |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function tests (DLCO, FVC) before each cycle; chest X-ray or CT to detect early bleomycin pulmonary toxicity (BPT); renal function (CrCl-based dose reduction required); cumulative lifetime dose tracking (maximum ~400 IU to limit irreversible pulmonary fibrosis); oxygen supplementation should be used with caution peri-operatively |
| Handling Protection | Must be prepared and administered following cytotoxic drug handling regulations; use certified biological safety cabinet and appropriate personal protective equipment (gloves, gown, mask) |

> **Key Safety Alert:** Bleomycin pulmonary toxicity (BPT) is the most clinically significant adverse effect, occurring in up to 10% of patients and potentially fatal. Risk increases with cumulative dose, age > 70, renal impairment, concurrent G-CSF use, and high inspired oxygen concentrations during anaesthesia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No formal safety data (warnings, contraindications, or drug interactions) were retrievable from Canadian regulatory sources, as bleomycin is not currently approved or marketed in Canada. Clinicians should consult an internationally recognized product monograph and be particularly vigilant regarding **bleomycin pulmonary toxicity**, which represents the primary dose-limiting safety concern.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN knowledge graph assigns bleomycin a top-ranked score for cauda equina neoplasm, but this signal is driven by graph-topological proximity to lymphoma and germ cell tumor nodes — both of which are established bleomycin indications — rather than by direct therapeutic evidence. With zero clinical trials and only three tangentially relevant publications, the current evidence base is insufficient to justify clinical translation without substantial preclinical and pharmacokinetic groundwork.

**To proceed, the following is needed:**

- **Histological clarification**: Characterize which cauda equina neoplasm subtypes (lymphoma, GCT, ependymoma, meningioma, etc.) are theoretically bleomycin-sensitive, as efficacy is highly histology-dependent
- **Pharmacokinetic data**: Investigate bleomycin's penetration into the cerebrospinal fluid and lumbosacral spinal compartment; systemic bleomycin has very limited CNS penetration (paralleling the blood-brain barrier problem documented in astrocytoma literature, PMID 12416544)
- **Preclinical evidence**: In vitro or in vivo studies using cauda equina tumor cell lines or animal models to establish proof-of-concept activity
- **Delivery strategy**: Evaluate intrathecal or convection-enhanced delivery (CED) as alternative routes to bypass CNS penetration barriers, similar to intratumoral bleomycin approaches explored in glioblastoma (PMID 12416544)
- **Full safety profile**: Obtain complete prescribing information from an internationally recognized monograph; evaluate pulmonary toxicity risk-benefit, especially given potential overlap with spinal cord compression symptoms that may complicate monitoring
- **Canada regulatory pathway**: Bleomycin is not marketed in Canada (0 DINs); any clinical development would require a Clinical Trial Application (CTA) with Health Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

