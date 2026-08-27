---
layout: default
title: Pralatrexate
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: From Peripheral T-Cell Lymphoma to Pleural Mesothelioma

## One-Sentence Summary

Pralatrexate (DrugBank DB06813) is an antifolate chemotherapy agent approved for relapsed/refractory peripheral T‑cell lymphoma (PTCL). The TxGNN model's top ten predictions for this drug are dominated by mesothelioma-family indications (8 of 10), and among these the best-supported candidate is **Pleural Mesothelioma**, backed by **1 Phase II clinical trial publication and 2 supporting literature references** — though no clinical trial is currently registered on ClinicalTrials.gov/ICTRP and Health Canada regulatory data is absent.

> **Note on candidate selection:** This evidence pack contains 10 predicted indications. The single highest-scoring candidate (rank 1, "pleural adenomatoid tumor") has no supporting evidence and, per the model's own rationale, is likely a false-positive graph-embedding artifact. This report instead focuses on **rank 10 (Pleural Mesothelioma)**, which is the only candidate with direct evidence — because it is the most decision-relevant signal in the pack, not simply the top-scoring one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral T-cell lymphoma (PTCL), relapsed/refractory *(not present in this evidence pack — `original_indications` is empty; based on established drug information)* |
| Predicted New Indication | Pleural Mesothelioma |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on known pharmacology, pralatrexate is a folate analog / dihydrofolate reductase (DHFR) inhibitor: it is taken up via the reduced folate carrier (RFC-1) and retained intracellularly through high-affinity polyglutamation by folylpolyglutamate synthetase (FPGS), which blocks thymidylate and purine synthesis and halts DNA replication in rapidly dividing cells.

The original indication (PTCL) and the predicted indication (pleural mesothelioma) are biologically distinct tumor types, but they share a pharmacological vulnerability: mesothelioma is a well-documented antifolate-responsive cancer, evidenced by pemetrexed's established regulatory approval for malignant pleural mesothelioma. This creates plausible mechanistic ground for a related antifolate like pralatrexate to show activity in the same tumor type.

Directly supporting this, PMID 17409804 is a completed Phase II single-arm trial that tested pralatrexate specifically in unresectable malignant pleural mesothelioma, preceded by preclinical work from the same research group (PMID 11595715) demonstrating superior in vitro cytotoxic potency versus methotrexate in mesothelioma cell lines. However, this trial was published in 2007 with no identifiable confirmatory or follow-on registered trials since, suggesting the development program did not advance — likely due to efficacy falling short of expectations or a commercial deprioritization rather than a safety failure. The other 7 mesothelioma-subtype predictions in this pack (biphasic, epithelioid, sarcomatoid, peritoneal, lymphohistiocytoid, well-differentiated papillary, pericardium) largely extrapolate this same mechanistic logic from the parent disease category without subtype-specific evidence, and the two non-mesothelioma top predictions (adenomatoid tumor, relapsing-remitting MS) are explicitly flagged by the model's own rationale as biologically implausible and unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase 2 Trial | Journal of Thoracic Oncology | Phase II trial of pralatrexate (PDX) in unresectable malignant pleural mesothelioma; favorable toxicity profile (primarily stomatitis) and demonstrated antitumor activity in mesothelioma cell lines and xenografts |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Management and Research | Review of antifolate chemotherapy mechanisms (DHFR, GARFT, AICARFT, thymidylate synthetase inhibition); contextualizes pralatrexate within the broader antifolate drug class |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclinical | Clinical Cancer Research | Preclinical study showing pralatrexate (PDX) is 25-30-fold more cytotoxic than methotrexate in human mesothelioma cell lines (VAMT-1, JMN), with enhanced activity in combination with platinum agents |

---

## Canada Market Information

Pralatrexate is not currently marketed in Canada — 0 DINs are on record, and no product license data is available for review.

---

## Cytotoxicity

Pralatrexate is an antineoplastic cytotoxic agent (antifolate/DHFR inhibitor class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate / DHFR inhibitor class) |
| Myelosuppression Risk | High — myelosuppression (neutropenia, thrombocytopenia) and mucositis/stomatitis are known dose-limiting toxicities of this drug class; detailed local labeling data is unavailable (see Safety Considerations below) |
| Emetogenicity Classification | Low to moderate (typical for antifolate agents) |
| Monitoring Items | CBC with differential, mucocutaneous/oral exam, renal and hepatic function, folic acid and vitamin B12 status |
| Handling Protection | Standard cytotoxic/hazardous drug handling precautions required (closed-system transfer devices, PPE) per institutional handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data could not be retrieved for this evidence pack — this is flagged as a Blocking data gap, see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pleural mesothelioma signal is mechanistically plausible and backed by a completed Phase II trial plus supporting preclinical/review literature, but that trial is single-arm, nearly two decades old, and shows no subsequent confirmatory development. Combined with the absence of any Taiwan/Canada regulatory safety data (a Blocking-severity data gap) and the drug's non-marketed status in Canada, the evidence is insufficient to proceed beyond a research-question stage.

**To proceed, the following is needed:**
- Local (TFDA or Health Canada) product monograph/package insert to close the Blocking safety data gap (warnings, contraindications, DDIs)
- DrugBank-sourced mechanism of action detail to strengthen the mechanistic rationale
- A search for any post-2007 confirmatory trials or real-world evidence in mesothelioma that may explain why the original Phase II signal was not advanced
- Comparative safety assessment between the drug's approved PTCL population and the proposed mesothelioma patient population (differing baseline organ function, comorbidities)
- Since pralatrexate is not marketed in Canada, an access-pathway evaluation (e.g., Special Access Programme) if further clinical investigation is pursued
- Note: the remaining 8 lower-ranked candidates in this evidence pack (adenomatoid tumor, MS, and unevidenced mesothelioma subtypes) were reviewed and screened out due to absence of evidence and/or biological implausibility per the model's own rationale, and require no further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

