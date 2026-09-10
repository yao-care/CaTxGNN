---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is the NS5A-inhibitor component of the fixed-dose combination glecaprevir/pibrentasvir (Mavyret/Maviret), used to treat chronic hepatitis C virus (HCV) genotype 1–6 infection. The TxGNN model predicts it may also be effective for **Hepatitis B Virus (HBV) infection**, with **14 clinical trials** and **20 publications** retrieved — however, essentially all of this evidence concerns HCV treatment rather than direct HBV efficacy, and the drug's own target (HCV NS5A protein) has no known homolog in HBV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (as component of glecaprevir/pibrentasvir combination) |
| Predicted New Indication | Hepatitis B Virus (HBV) infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for pibrentasvir was not available from the DrugBank extraction in this evidence pack. However, the clinical trial and literature evidence consistently describe pibrentasvir as an **NS5A inhibitor**, co-formulated with glecaprevir (an NS3/4A protease inhibitor) as glecaprevir/pibrentasvir (brand names Mavyret/Maviret), approved for chronic HCV genotype 1–6 infection, including in patients with renal impairment, compensated cirrhosis, and HIV co-infection.

On the surface, HCV and HBV are both viral causes of chronic hepatitis and are frequently discussed together in clinical literature (shared elimination goals, co-infection screening, liver disease progression). This topical proximity is likely what drives the TxGNN knowledge-graph prediction.

However, the mechanistic basis is weak: HCV belongs to *Flaviviridae* and NS5A is an HCV-specific non-structural protein, whereas HBV (*Hepadnaviridae*) is a reverse-transcribing DNA virus with no NS5A homolog or analogous drug target. The evidence pack's own mechanistic assessment states explicitly that **pibrentasvir's target does not exist in HBV**, and no cross-viral mechanistic rationale is established. This explains why, despite a high raw prediction score, none of the retrieved trials or literature demonstrate actual antiviral activity against HBV — the score most likely reflects graph-level co-occurrence of "viral hepatitis" concepts rather than pharmacological plausibility.

---

## Clinical Trial Evidence

*Note: All retrieved trials evaluate glecaprevir/pibrentasvir in HCV populations; none test efficacy against HBV specifically. Several are graded "low relevance (C)" for this reason.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | CERTAIN-1: G/P efficacy/safety in Japanese chronic HCV patients; not HBV-specific |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Completed | 136 | CERTAIN-2: G/P vs sofosbuvir+ribavirin in HCV genotype 2; not HBV-specific |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | SURVEYOR-II: G/P efficacy/safety across HCV genotypes 2–6; not HBV-specific |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: G/P vs sofosbuvir+daclatasvir in HCV genotype 3; not HBV-specific |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Completed | 304 | ENDURANCE-2: G/P safety/efficacy in HCV genotype 2; not HBV-specific |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of DAA resistance durability in prior HCV trial participants; not HBV-specific |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | G/P ± ribavirin in HCV genotype 1 patients previously failing NS5A+sofosbuvir; not HBV-specific |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | G/P in treatment-naïve Brazilian adults with HCV genotype 1–6; not HBV-specific |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: G/P ± ribavirin in HCV genotype 1, 4, 5, 6; not HBV-specific |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | G/P ± ribavirin in HCV patients who failed prior DAA therapy; not HBV-specific |

---

## Literature Evidence

*Note: Classification/relevance scoring for most records is still pending in the source data; content below is summarized directly from titles/abstracts. Only one record (PMID 29485084) directly addresses HBV in the context of HCV treatment.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | The Lancet Infectious Diseases | Discusses HBV vaccination strategy for patients after HCV treatment — most topically relevant record, but does not evaluate pibrentasvir against HBV directly |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World Journal of Gastroenterology | Reviews pediatric HBV and HCV management; HCV DAA (incl. G/P) discussed separately from HBV therapy, which "remains far from curative" |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Annals of Hepatology | Compares global drug pricing for HBV and HCV antivirals; not an efficacy study |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | Journal of Viral Hepatitis | Real-world G/P effectiveness/safety in HCV patients with severe renal impairment (Taiwan); not HBV-related |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Reports | G/P-associated acute liver injury in non-cirrhotic HCV patient without HBV co-infection; notes liver injury risk historically associated with HBV co-infection |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report | Journal of Infection and Chemotherapy | G/P used to treat HCV exacerbation during chemotherapy; notes HBV reactivation is far more common than HCV exacerbation in this setting |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | European Journal of General Practice | General primary-care review of chronic HCV diagnosis and treatment; not HBV-related |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clinical Pharmacokinetics | PK/PD review of HCV DAA regimens including G/P; not HBV-related |
| [32296728](https://pubmed.ncbi.nlm.nih.gov/32296728/) | 2020 | Review | Open Forum Infectious Diseases | Review of HCV retreatment after multiple DAA failures; not HBV-related |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | The Lancet Gastroenterology & Hepatology | Review of pediatric/adolescent HCV infection and global elimination strategy; not HBV-related |

---

## Canada Market Information

Pibrentasvir is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) are on file (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured key warnings, contraindications, or drug interaction data were retrievable for this evidence pack; DG001 flags TFDA label warnings/contraindications as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN prediction score (99.84%), the evidence level is L5 (model prediction only) — no retrieved clinical trial or publication demonstrates pibrentasvir efficacy against HBV, and the drug's known target (HCV NS5A) has no counterpart in HBV, undermining mechanistic plausibility. The drug is also not currently marketed in Canada, and core safety/labeling data (DG001, Blocking) is missing.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (DG001 — Blocking gap; required before any S1 safety review)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- A targeted literature/trial search specifically for HBV antiviral outcomes (current searches returned only HCV-focused co-occurrence results)
- An independent virology/mechanistic review to assess whether any indirect pathway (e.g., host-factor modulation) could plausibly justify further investment, given the absence of a direct target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

