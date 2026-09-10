---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Icatibant (DB06196): From No Approved Indication in Canada to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

Icatibant (DrugBank DB06196) currently holds **no Health Canada market authorization** — it is not marketed and has zero DINs on file in this evidence pack. The TxGNN model predicts efficacy for **C1 inhibitor deficiency** (hereditary angioedema, HAE), which — based on the clinical trial and literature evidence retrieved — is in fact icatibant's globally established primary indication (marketed elsewhere as Firazyr®), supported by **23 clinical trials** (multiple completed Phase 3 RCTs) and **20 publications**. This is best framed as a **market-access gap**, not a novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Health Canada licenses recorded; `original_indications` empty in source data) |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for icatibant is not available in the structured `original_moa` field (flagged as a High-severity data gap). However, the retrieved literature evidence independently corroborates the pharmacology: icatibant is repeatedly described as a **synthetic decapeptide, selective bradykinin B2 receptor antagonist** (e.g., PMID 21284353, PMID 24925394), used to block the bradykinin-mediated vascular permeability that drives angioedema attacks.

The predicted indication — C1 inhibitor deficiency / hereditary angioedema (HAE) — is not a mechanistically distant "new" use. C1-INH deficiency leads to unregulated plasma kallikrein activity and bradykinin accumulation; icatibant directly antagonizes the resulting bradykinin B2 receptor signal. This is consistent with icatibant's known worldwide indication (Firazyr®, approved in the EU, US, Japan, and elsewhere for acute HAE attacks) and with Taiwan's own NHI reimbursement for this use (see NCT07290855 below). In other words, TxGNN has correctly re-identified the drug's own established indication rather than surfacing a genuinely novel mechanistic hypothesis.

The practical significance for this evaluation is therefore different from a typical repurposing case: the open question is **why the product carries no Health Canada authorization / DINs**, not whether the pharmacology supports the indication. That distinction should drive the next steps.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Randomized, double-blind, placebo-controlled study of subcutaneous icatibant for acute cutaneous/abdominal HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Randomized, double-blind, placebo-controlled trial of subcutaneous icatibant vs. placebo for acute HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | Randomized, controlled, parallel-group trial comparing subcutaneous icatibant vs. oral tranexamic acid for HAE attacks; icatibant showed faster time to symptom relief |
| [NCT02584959](https://clinicaltrials.gov/study/NCT02584959) | Phase 3 | Completed | 75 | Randomized, double-blind, placebo-controlled, partial crossover study of prophylactic C1 esterase inhibitor for HAE attack prevention (same disease population) |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large prospective real-world registry documenting long-term safety/effectiveness of Firazyr (icatibant) |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | Open-label, non-randomized study of single-dose subcutaneous icatibant PK, tolerability, and safety in children/adolescents with HAE |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Open-label, non-randomized Japanese pediatric study of icatibant (TAK-667) safety, efficacy, and PK for acute HAE attacks |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Taiwan-based study evaluating icatibant injection for bradykinin-induced angioedema; notes NHI reimbursement for HAE already exists in Taiwan |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label, multicenter study of self-administered subcutaneous icatibant for acute HAE attacks — supports home/self-treatment feasibility |
| [NCT05509569](https://clinicaltrials.gov/study/NCT05509569) | N/A | Completed | 32 | Japan post-marketing all-case surveillance of icatibant 30 mg syringe in pediatric HAE patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Drug Review | Prescrire International | Describes icatibant as a decapeptide bradykinin B2 receptor antagonist authorized in the EU for HAE attacks |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Rev Clin Immunol | Reviews icatibant safety/efficacy in adolescents and children >2 years with C1-INH-HAE |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Review | Chem Immunol Allergy | Describes bradykinin-mediated disease mechanism underlying C1 inhibitor deficiency and ACE-inhibitor angioedema |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonol Alergol Pol | Comparative effectiveness of conestat alfa, C1-INH, and icatibant for acute HAE attacks |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Reviews HAE disease burden and treatment access in the Asia-Pacific region |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Registry Analysis | Allergy Asthma Clin Immunol | Icatibant Outcome Survey (Spain) — real-world treatment outcomes for HAE type 1/2 |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational Study | Allergy | Real-world icatibant use in acquired C1-inhibitor deficiency (off-label use pattern) |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective Study | J Clin Pharmacol | Documents predominance of off-label icatibant/C1-INH prescribing beyond classic HAE |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunol Allergy Clin North Am | Reviews acquired C1 inhibitor deficiency diagnosis and management |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case Series | J Clin Immunol | Icatibant and recombinant C1 inhibitor use for HAE attacks during pregnancy |

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DIN) are on file for icatibant in this evidence pack (`total_licenses: 0`, `market_status: 未上市`). The product is not currently marketed in Canada.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA/product monograph warnings and contraindications), which prevents completion of the initial safety screening (S1) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic and clinical trial evidence for icatibant in C1 inhibitor deficiency (HAE) is strong (L1, multiple completed Phase 3 RCTs, large real-world registries) — but this reflects the drug's already-established global indication rather than a new hypothesis, and it does not resolve the Blocking gap in Canada-specific safety labeling (warnings/contraindications) or the underlying question of why no Health Canada authorization currently exists.

**To proceed, the following is needed:**
- Product monograph / regulatory-agency warnings and contraindications for icatibant (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent primary source (DG002)
- Clarification of Health Canada market-authorization status/history for icatibant (Firazyr®) — this is a market-access question, not a repurposing question
- Drug interaction (DDI) data, currently returning no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

