---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 1
---

# Micafungin
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

The data-report skill governs CLI output fidelity — it doesn't apply to this JSON-to-Markdown report generation task. Proceeding with the report per the Drug Repurposing Evaluation Report Prompt (v5).

---

# Micafungin: From Invasive Candidiasis to Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin antifungal approved globally for invasive candidiasis and esophageal candidiasis, working by disrupting fungal cell wall synthesis.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (Candida)**, with **0 clinical trials** and **13 publications** currently supporting this direction — primarily retrospective cohort studies and case reports involving azole-resistant *Candida* species.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis; esophageal candidiasis (global approvals; no Canada DINs on file) |
| Predicted New Indication | Urinary Tract Infection (Candida) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, micafungin is an echinocandin antifungal that inhibits β-1,3-glucan synthase — the enzyme responsible for synthesising a key structural component of the fungal cell wall. This results in direct fungicidal activity against *Candida* species. Its efficacy in invasive candidiasis is well established, and mechanistically it may be applicable to urinary tract infections caused by *Candida*.

The core pharmacokinetic challenge is that echinocandins are predominantly eliminated via biliary excretion, with renal excretion accounting for only approximately 1–3% of the dose. Urinary concentrations are therefore theoretically subtherapeutic. However, PMID 27424599 (a PK/PD study) provides counter-evidence, reporting that measured urinary micafungin levels in some patients were sufficient to exceed the minimum inhibitory concentration (MIC) for the causative *Candida* species — suggesting a role in selected clinical scenarios.

The strongest rationale for repurposing emerges in the context of **azole-resistant Candida infections**: *C. krusei* (intrinsically fluconazole-resistant), *C. glabrata* (reduced azole susceptibility), and the emerging multidrug-resistant *C. auris* all lack reliable first-line oral options, making echinocandins a practical alternative when standard agents are contraindicated or ineffective. The high TxGNN score of 99.03% reflects strong Candida–drug connectivity in the knowledge graph, though it is worth noting that the model may not fully distinguish between systemic candidiasis indications and urinary tract infection as a distinct clinical entity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Retrospective Cohort (Pediatric) | Pediatrics International | Critically ill children in PICU treated with micafungin for hospital-acquired Candida UTIs; reports treatment success rates by Candida species |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | PK/PD Study | Int J Antimicrobial Agents | 6 patients with Candida UTI (4 fluconazole-resistant) successfully treated; urinary micafungin concentrations via TDM shown to exceed MIC despite low excretion rate |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int Urology and Nephrology | Examined candiduria elimination rates in micafungin-treated inpatients; assessed echinocandins as an alternative where non-albicans Candida limits triazole use |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Multi-institutional Retrospective | Antimicrobial Agents Chemother | 305-patient study on candiduria management; found significant antifungal overuse in asymptomatic candiduria — stewardship context for any micafungin use |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Epidemiology / Susceptibility Survey | Ther Adv Infectious Disease | Vietnamese healthcare survey of Candida species in vulvovaginal candidiasis and UTIs; documents non-albicans species prevalence and varying antifungal susceptibility |
| [24182454](https://pubmed.ncbi.nlm.nih.gov/24182454/) | 2014 | Prospective Surveillance | Int J Antimicrobial Agents | 1218 episodes of Candida bloodstream infections across 52 US hospitals; documents micafungin susceptibility data across species — contextual susceptibility reference |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infectious Disease | *C. krusei* UTI (fluconazole-resistant, reduced amphotericin B susceptibility) in liver/kidney transplant recipient; eradicated with high-dose micafungin |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Medical Mycology Case Reports | 5 patients with candiduria treated with parenteral micafungin (≥6 days); all achieved fungal clearance within 30 days of treatment completion |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report (Neonatal) | Frontiers in Pediatrics | *C. glabrata* UTI in premature neonate in NICU; highlights rising non-albicans Candida in NICUs and use of micafungin in this vulnerable population |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | Multidrug-resistant *C. auris* UTI in a nursing home patient with sepsis; echinocandin selected due to resistance to standard antifungals |

---

## Canada Market Information

Micafungin is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on file. This section cannot be populated until a Health Canada submission is made or a foreign-approved product is identified for cross-reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials for this indication are registered globally, and the available evidence (L3: retrospective cohort studies and case reports) does not yet meet the threshold for a formal repurposing pathway in Canada, particularly given that micafungin has no current market presence (0 DINs). The pharmacokinetic barrier — low renal excretion — remains a fundamental unresolved concern that case-level PK/PD data alone cannot resolve.

**To proceed, the following is needed:**

- **MOA and safety data**: Retrieve full DrugBank record including mechanism of action, key warnings, and contraindications to complete the S1 safety screening (Data Gaps DG001, DG002)
- **Prospective PK/PD study**: A controlled study characterising urinary micafungin concentrations across patient populations (renal function strata, dose levels) to confirm whether therapeutic concentrations are reliably achievable
- **Stratified indication scope**: Define the precise clinical niche — likely limited to azole-resistant Candida UTIs (*C. glabrata*, *C. krusei*, *C. auris*) in immunocompromised or ICU patients — rather than broad UTI repurposing
- **Regulatory pathway review**: Determine whether Health Canada's Special Access Programme (SAP) or a full NDS is the appropriate vehicle, given zero current DINs
- **Antifungal stewardship alignment**: Clarify how a candiduria indication would interact with institutional stewardship guidelines, given evidence (PMID 29109159) of widespread overtreatment of asymptomatic candiduria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

