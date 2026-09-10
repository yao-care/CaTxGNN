---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Clear-Cell Renal Cell Carcinoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor already established as therapy for advanced clear-cell renal cell carcinoma and non-adipocytic soft tissue sarcoma. The TxGNN model predicts it may also be effective for **Unclassified Renal Cell Carcinoma**, with **1 completed Phase 3 trial** and **6 publications** currently supporting this direction — though most of that literature is retrospective/real-world evidence in the broader non-clear-cell RCC population rather than trials specific to the unclassified subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Health Canada licensing data (drug not marketed in Canada); per trial/literature evidence in this pack, pazopanib is an established therapy for advanced clear-cell renal cell carcinoma (ccRCC) and non-adipocytic soft tissue sarcoma |
| Predicted New Indication | Unclassified Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug is not yet in our records (DrugBank MOA lookup pending, DG002). Based on the trial and literature descriptions collected in this evidence pack, pazopanib is consistently characterized as an oral multi-target receptor tyrosine kinase inhibitor acting on VEGFR, PDGFR, and c-KIT, with strong anti-angiogenic activity (e.g., trial NCT01059656 describes it as a "Multi Tyrosine Kinase Inhibitor" acting on PDGF-mediated signaling; literature entry PMID 24041629 describes it as having "strong anti-angiogenetic activity"). It is already a standard first-line treatment for metastatic clear-cell RCC (PMID 28108284).

Unclassified RCC is one of several non-clear-cell RCC (nccRCC) histologic subtypes. Because ccRCC and nccRCC (including unclassified RCC) share a common organ of origin and overlapping VEGF-pathway-driven tumor biology, clinicians have long extrapolated pazopanib's antiangiogenic activity from ccRCC into nccRCC settings — this is explicitly the rationale behind several of the retrospective and single-arm studies in this pack (PMID 28108284, PMID 28546525). PMID 28108284 states directly: "Pazopanib is a standard first-line treatment for metastatic clear-cell renal cell carcinoma (ccRCC). Very few data on its activity in non-clear-cell renal cell carcinoma (nccRCC) are currently available" — indicating an active, ongoing evidence-generation effort in exactly this direction.

The most recent literature item (PMID 41558869, 2026, IMDC registry) explicitly stratifies outcomes by "papillary RCC, unclassified RCC, and chromophobe RCC," confirming that unclassified RCC is being actively studied as a distinct subgroup for first-line targeted/IO therapies. This supports mechanistic plausibility, but no trial in this pack was designed specifically around the unclassified-RCC subtype — the Phase 3 RCT (NCT01613846) enrolled a general advanced/metastatic RCC population, and the supporting publications are predominantly retrospective or real-world analyses rather than subtype-specific RCTs.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Completed | 544 | Randomized, sequential, open-label trial comparing sorafenib→pazopanib vs. pazopanib→sorafenib sequencing in advanced/metastatic RCC. Establishes pazopanib's role in RCC treatment sequencing at the broader-RCC level (not unclassified-RCC-specific). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospective registry (IMDC) | European Urology Oncology | International multicenter database analysis comparing contemporary IO-based/cabozantinib regimens vs. traditional targeted therapy (incl. pazopanib) across nccRCC subtypes, explicitly including unclassified RCC. |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Retrospective/real-world | Ecancermedicalscience | Compared first-line sunitinib vs. pazopanib effectiveness in non-clear cell RCC and sarcomatoid RCC; found the two TKIs may not be interchangeable across these underrepresented subtypes. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospective case series | Clinical genitourinary cancer | Characterized carcinoma-of-unknown-primary patients with RCC histology (CUP-mRCC) treated with VEGF-targeted therapies including pazopanib. |
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase II, single-arm | Cancer Research and Treatment | Single-arm, open-label Phase II study designed specifically to evaluate pazopanib efficacy/safety in non-clear cell RCC. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective multicenter (PANORAMA) | Clinical genitourinary cancer | Italian multicenter retrospective study of pazopanib efficacy and toxicity in non-clear-cell RCC. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clinical genitourinary cancer | Reviewed real-world outcomes of pazopanib in metastatic non-clear-cell RCC, noting limited data outside clear-cell disease. |

---

## Cytotoxicity

Pazopanib is an oncology drug (renal cell carcinoma / sarcoma indications), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — oral multi-target receptor tyrosine kinase inhibitor (VEGFR, PDGFR, c-KIT), anti-angiogenic mechanism (per trial/literature descriptions in this pack) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No drug warning, contraindication, or interaction data is currently available in this evidence pack — Health Canada / TFDA product-monograph retrieval (DG001, Blocking severity) has not yet been completed. Please refer to the official product monograph for safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT establishes pazopanib's clinical activity across advanced RCC broadly, and a growing, increasingly recent body of literature (6 publications, most recently a 2026 IMDC registry analysis) specifically studies non-clear-cell and unclassified RCC subgroups. However, no trial is unclassified-RCC-specific, and the drug's safety labeling data and confirmed MOA remain unresolved (DG001 Blocking, DG002 High) — both must be closed before formal safety pre-assessment (S1) can proceed.

**To proceed, the following is needed:**
- Resolve DG001: retrieve TFDA/Health Canada product monograph (warnings, contraindications) — currently blocking safety pre-assessment
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Seek prospective, unclassified-RCC-specific efficacy data, since current Phase 3 evidence comes from broader advanced-RCC populations
- For portfolio prioritization: this evidence pack's own liposarcoma (L2, Proceed with Guardrails) and dermatofibrosarcoma protuberans (L2, Proceed with Guardrails) candidates already have subtype-specific Phase II trial evidence and may warrant earlier action than unclassified RCC
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

