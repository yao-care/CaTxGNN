---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 1
---

# Dacarbazine
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

# DACARBAZINE: From Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is a cytotoxic DNA alkylating prodrug with established use in malignant melanoma and Hodgkin's lymphoma (ABVD regimen). The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm (UADT)**, with **1 clinical trial** (conducted with the mechanistically equivalent agent temozolomide) and **20 publications** identified — though direct dacarbazine-specific evidence in this indication is currently absent. The prediction appears mechanistically coherent but is driven primarily by a shared active metabolite with temozolomide rather than by independent clinical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malignant melanoma; Hodgkin's lymphoma (standard clinical use — no Canadian DIN on file) |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dacarbazine (DTIC) is a triazene-class cytotoxic prodrug. It undergoes hepatic bioactivation via CYP1A1/CYP1A2 to MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide), which spontaneously decomposes to methyl diazonium ion — covalently alkylating the N7 and O6 positions of guanine residues in DNA. This triggers mismatch-repair (MMR)-dependent apoptosis. Crucially, temozolomide (TMZ), while structurally distinct, produces the identical MTIC metabolite under physiological pH, making dacarbazine and TMZ functional equivalents at the effector level.

Upper aerodigestive tract (UADT) tumors — encompassing cancers of the oral cavity, pharynx, larynx, sinonasal tract, and esophagus — feature high proliferative activity. In tumours with MGMT promoter methylation (silencing a key DNA repair enzyme), alkylating agents such as TMZ and dacarbazine are theoretically more effective, as unrepaired O6-methylguanine adducts drive apoptosis. The clinical precedent established by NCT00423150 and PMID 23443801 (both Phase 2 studies of TMZ in MGMT-methylated UADT cancers) provides indirect mechanistic validation for dacarbazine in the same disease context.

However, the TxGNN high score (0.9926) most likely reflects a multi-hop knowledge graph connection — dacarbazine → MTIC ← temozolomide → UADT neoplasm — rather than direct trial evidence. Important caveats exist: the available Phase 2 trial was terminated early, suggesting the strategy failed to meet efficacy thresholds or encountered safety/recruitment issues; HPV-positive versus HPV-negative UADT subtypes show divergent responses to alkylating agents; and dacarbazine's oral bioavailability disadvantage relative to TMZ limits practical substitution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Evaluated temozolomide (sharing MTIC active metabolite with dacarbazine) in MGMT promoter-methylated patients with advanced aerodigestive tract cancers (head and neck, esophageal) and colorectal cancer. Trial was terminated — published results (PMID 23443801) indicate modest and tumour-type-dependent activity, with limited efficacy in UADT subgroups. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase II Trial | *Molecular Cancer Therapeutics* | Phase 2 study of TMZ in MGMT-methylated advanced UADT and colorectal cancers; MGMT methylation alone was insufficient to predict response — only modest activity observed in UADT subgroup, providing a cautionary indirect signal for dacarbazine re-purposing |
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase III RCT | *JAMA Oncology* | MELATORCH trial: toripalimab vs. dacarbazine as first-line therapy in advanced acral melanoma; dacarbazine served as the active comparator, providing contemporary data on dacarbazine monotherapy efficacy and tolerability in an Asian population |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Prospective Case Series | *Annals of Oncology* | Pilot study of dacarbazine + 5-FU in advanced medullary thyroid carcinoma (a UADT-adjacent neuroendocrine tumour); modest responses observed, representing one of the few direct dacarbazine datasets in head-and-neck region malignancies |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Retrospective Case Series | *Cancer & Chemotherapy* | Review of CYVADIC chemotherapy (includes DTIC/dacarbazine) in Wilson-Jones angiosarcoma of the head and neck; notes poor prognosis despite multi-agent regimens including dacarbazine |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective Case Series | *Int J Radiation Oncology, Biology, Physics* | Two-centre analysis of radiotherapy for esthesioneuroblastoma (a rare UADT malignancy); provides disease-context data for upper aerodigestive tract neuroectodermal tumours |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Review | *Journal of Clinical Neuroscience* | Review of temozolomide in aggressive pituitary adenomas and carcinomas (skull base/aerodigestive adjacency); supports the mechanistic class concept for MTIC-generating agents in proliferative neuroendocrine UADT-region tumours |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Retrospective Case Series | *Ear, Nose & Throat Journal* | Six-patient institutional series of malignant head and neck paragangliomas; documents disease characteristics and treatment outcomes, underscoring unmet need in rare UADT malignancies |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | *Clinical Oncology* | Comprehensive review of medullary thyroid carcinoma management, including limited chemotherapy data; contextualises the neuroendocrine subtype of UADT-region cancers where dacarbazine has historically been trialled |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Epidemiology | *J Cancer Research & Clinical Oncology* | Global burden of EBV-associated malignancies, including nasopharyngeal carcinoma (a major UADT cancer); provides epidemiological context and highlights EBV-positive UADT subgroups as potentially distinct therapeutic targets |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Retrospective Cohort | *Cancer* | Characteristics and outcomes of Hodgkin's lymphoma involving nodal/extranodal head and neck sites; relevant because dacarbazine is a component of ABVD (standard HL therapy), and HL in the UADT region represents an overlap with dacarbazine's established indication |

---

## Canada Market Information

Dacarbazine currently has **no Drug Identification Numbers (DINs) registered in Canada**. No approved products or active licences are on file.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Triazene/Alkylating agent (DTIC class) |
| Myelosuppression Risk | **High** — Dose-limiting leukopenia and thrombocytopenia are the primary haematological toxicities; nadir typically at 3–4 weeks with 21–28-day cycles |
| Emetogenicity Classification | **High** — Dacarbazine is classified as a highly emetogenic agent (>90% emesis risk without prophylaxis); aggressive 5-HT₃ antagonist + NK₁ antagonist + dexamethasone prophylaxis required |
| Monitoring Items | CBC with differential and platelet count (before each cycle; nadir monitoring); hepatic function (ALT, AST, bilirubin — hepatotoxicity and hepatic vein thrombosis reported); renal function (creatinine); flu-like syndrome (fever, myalgia) — typically peaks 7 days post-infusion |
| Handling Protection | **Required** — Must be handled under cytotoxic drug handling regulations (closed-system transfer devices, class II biological safety cabinet, PPE per institutional policy); photosensitive — protect infusion bags and lines from light |

---

## Safety Considerations

Detailed Canadian product monograph warnings, contraindications, and drug interaction data are not currently available for this assessment. Please refer to the package insert and authoritative drug reference sources (e.g., Lexi-Drugs, Micromedex) for complete safety information prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically coherent — dacarbazine and temozolomide share the same active metabolite (MTIC) — but all identifiable clinical evidence was generated with temozolomide, not dacarbazine directly; furthermore, the single directly relevant Phase 2 trial (NCT00423150) was terminated without demonstrating clear efficacy in UADT cancers. With zero Canadian DINs, absent safety documentation, and no direct dacarbazine evidence in this indication, this candidate does not yet meet the threshold for active clinical development.

**To proceed, the following is needed:**

- **MOA and safety data retrieval:** Obtain the full DrugBank entry and Canadian product monograph (or equivalent reference) to complete the safety profile, including key warnings, contraindications, and clinically significant drug interactions
- **Biomarker stratification plan:** Define UADT subpopulations most likely to respond — specifically, MGMT promoter methylation status, HPV status (HPV+/HPV−), and tumour histology (squamous cell carcinoma vs. neuroendocrine vs. salivary gland) — before designing any exploratory protocol
- **Direct dacarbazine evidence search:** Conduct a targeted literature review for any dacarbazine-specific case series, compassionate use reports, or retrospective data in head and neck cancers beyond medullary thyroid carcinoma (PMID 7826911)
- **Formulation feasibility assessment:** Dacarbazine is IV-only; evaluate whether route-of-administration is compatible with UADT oncology practice settings compared to oral temozolomide, which offers a practical advantage
- **Regulatory pathway clarification:** Since dacarbazine is not marketed in Canada, a New Drug Submission or Special Access Programme application would be required — assess regulatory feasibility before committing to clinical development resources

> ⚠️ **Research use only.** This report is generated for research purposes and does not constitute medical advice. All repurposing candidates require prospective clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

