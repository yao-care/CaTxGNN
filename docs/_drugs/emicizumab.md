---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Congenital Hemophilia A to Acquired Coagulation Factor Deficiency

## One-Sentence Summary

Emicizumab (Hemlibra®) is a bispecific monoclonal antibody originally approved for prophylaxis of bleeding episodes in congenital Hemophilia A, acting as a functional substitute for activated Factor VIII by simultaneously binding FIXa and FX in the intrinsic tenase complex.
Among 10 TxGNN-predicted new indications, **acquired coagulation factor deficiency** (specifically **Acquired Hemophilia A, AHA**) is the highest-priority repurposing candidate, supported by **2 prospective Phase 2/3–3 trials** (AGEHA and GTH-AHA-EMI) and **20+ publications** forming a complete L1 evidence body.
Note: TxGNN's top-scored prediction by model rank is pseudo-von Willebrand disease (Score 99.99%), but this direction has no clinical evidence (L5, Hold); the most actionable finding in this pack is acquired hemophilia A, which already carries international expert consensus and is actively shifting treatment paradigms.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Hemophilia A with FVIII inhibitors — prophylaxis of bleeding episodes (based on FDA/EMA approvals; Health Canada DIN not registered) |
| Predicted New Indication | Acquired Coagulation Factor Deficiency (Acquired Hemophilia A) |
| TxGNN Prediction Score | 99.90% (Model Rank #5; Rank #1 by evidence tier) |
| Evidence Level | L1 — Phase 3 prospective RCT (AGEHA) + Phase 2/3 single-arm trial (GTH-AHA-EMI) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned by the DrugBank API query in this evidence pack. However, emicizumab's mechanism is extensively documented in the clinical literature: it is a humanized bispecific monoclonal antibody that simultaneously binds FIXa and FX, physically bridging these two coagulation factors to reconstitute the cofactor function normally provided by FVIIIa within the intrinsic tenase complex. This action amplifies the intrinsic coagulation cascade and drives thrombin generation entirely independently of FVIII.

The mechanistic connection between congenital and acquired Hemophilia A is direct. In congenital Hemophilia A, FVIII is absent due to a hereditary gene defect. In Acquired Hemophilia A, autoantibodies (inhibitors) neutralize endogenous FVIII — producing the identical functional consequence: loss of FVIIIa cofactor activity. Emicizumab's FVIII-independent FIXa–FX bridge therefore addresses the core hemostatic defect in both settings through the same mechanism, regardless of whether the FVIII deficiency is genetic or immune-mediated.

The clinical evidence has moved well beyond hypothesis: the prospective Phase 3 AGEHA study and Phase 2/3 GTH-AHA-EMI study both demonstrated that emicizumab effectively prevents bleeding in AHA patients while enabling deferral of immunosuppressive therapy (IST), which carries significant infection risk in the typically elderly and frail AHA population. Real-world data from US and European multicenter cohorts corroborate these findings, and the German-Austrian-Swiss (GTH) AHA Working Group has issued formal consensus recommendations for emicizumab use in AHA — marking a paradigm shift from reactive bypassing agent use to prophylactic FVIIIa-mimetic therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A (Registry) | Recruiting | 3,000 | ATHN Transcends: large US natural history registry tracking real-world treatment practice and long-term safety across non-neoplastic hematologic disorders including AHA and rare bleeding conditions; captures emicizumab utilization and outcomes in clinical practice |

> **Note:** The pivotal AGEHA (Phase 3, Japan) and GTH-AHA-EMI (Phase 2/3, Europe) trials are published in peer-reviewed journals (PMIDs 36696195, 37858328, 39134043) and provide the L1 evidence anchor for this indication. Their ClinicalTrials.gov NCT identifiers were not captured by the current evidence query but their published findings are fully referenced in the Literature Evidence section below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 Prospective RCT (AGEHA) | J Thromb Haemost | First prospective multicenter open-label Phase 3 study of emicizumab in AHA; demonstrates favorable benefit-risk profile for bleeding prophylaxis with and without concurrent IST |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2/3 Single-arm (GTH-AHA-EMI) | Lancet Haematology | Emicizumab prevents bleeding in AHA and permits deferral of immunosuppression during the critical first 12 weeks of management, reducing IST-associated morbidity |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 Final Analysis (AGEHA) | Thromb Haemost | AGEHA final analysis confirms sustained emicizumab benefit in both IST-eligible and IST-ineligible AHA patients; supports long-term prophylaxis across the full patient spectrum |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus Recommendation | Hamostaseologie | GTH-AHA Working Group formal consensus: indications, dosing, monitoring, and integration with immunosuppression for emicizumab use in AHA; directly influences clinical practice guidelines |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Multicenter Cohort | Blood Advances | US real-world cohort (N=62, 12 hemophilia treatment centers): off-label emicizumab in AHA reduces bleeding burden with manageable safety profile, supporting guideline-concordant adoption |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Follow-up Cohort | Blood Advances | 2-year GTH-AHA-EMI follow-up: sustained survival benefit confirmed with emicizumab plus postponed immunosuppression; IST-related infection deaths reduced |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Comparative Analysis | J Thromb Haemost | Emicizumab vs. immunosuppressive therapy as primary management for AHA; defines role of FVIIIa-mimetics in reducing early aggressive IST exposure in frail patients |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrative Review | J Thromb Haemost | Comprehensive 2025 review of AHA management in the emicizumab era: epidemiology, diagnosis, hemostatic strategies, and immunosuppression algorithms |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | Review | Haemophilia | Advances in AHA, acquired von Willebrand syndrome, and liver disease coagulopathy; emicizumab prophylaxis benefit in AHA prominently discussed |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review / Commentary | Blood Transfusion | Emicizumab in AHA: balanced pros/cons analysis comparing prophylactic FVIIIa-mimetic strategy vs. on-demand bypassing agent use |

---

## Canada Market Information

Emicizumab is **not registered** with Health Canada. No Drug Identification Numbers (DINs) have been issued.

> Emicizumab (Hemlibra®) holds regulatory approvals from the US FDA (November 2017 for inhibitor patients; October 2018 extended to non-inhibitor patients) and the EMA (February 2018). Health Canada registration status should be independently verified via the Drug Product Database (DPD), as the regulatory data captured in this evidence pack reflects no active Canadian product licenses. Patients in Canada requiring emicizumab for any indication would currently require the Special Access Programme (SAP).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Key clinical safety note from repurposing rationale:** When emicizumab is used concurrently with activated prothrombin complex concentrates (aPCC / FEIBA), cases of thrombotic microangiopathy (TMA) and thromboembolic events have been documented. Co-administration of aPCC with emicizumab is contraindicated. Thromboembolic monitoring is required during transitions between hemostatic agents. Complete warnings and contraindications must be sourced from the Roche/Chugai Hemlibra® product monograph — this information is a flagged blocking data gap in the current evidence pack (DG001).

---

## Prediction Landscape Summary

This evidence pack evaluated 10 TxGNN-predicted indications for emicizumab. The full landscape is summarized below to assist prioritization:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Mechanistic Fit | Decision |
|------|------------------|-------------|---------------|-----------------|---------|
| 1 | Pseudo-von Willebrand Disease | 99.99% | L5 | ✗ GPIbα gain-of-function defect unrelated to FVIII/coagulation cascade | Hold |
| 2 | Primary Release Disorder of Platelets | 99.99% | L5 | ✗ Platelet dense/alpha granule defect upstream of coagulation pathway | Hold |
| 3 | Glanzmann Thrombasthenia | 99.98% | L4 | △ Indirect: enhanced thrombin generation may partially compensate GPIIb/IIIa defect | Research Question |
| 4 | Scott Syndrome | 99.92% | L5 | △ TMEM16F defect impairs phospholipid surface for tenase assembly; emicizumab efficacy uncertain | Hold |
| **5** | **Acquired Coagulation Factor Deficiency (AHA)** | **99.90%** | **L1** | **✓ Direct: FIXa-FX bridge bypasses neutralized FVIII — identical mechanism to approved indication** | **Proceed with Guardrails** |
| 6 | Bleeding Diathesis due to Collagen Receptor Defect | 99.86% | L5 | ✗ GPVI/GPIa-IIa platelet-collagen adhesion defect unrelated to FVIII pathway | Hold |
| 7 | Hemorrhagic Disorder due to Constitutional Thrombocytopenia | 99.85% | L5 | ✗ Primary platelet count deficiency cannot be corrected by coagulation pathway enhancement | Hold |
| 8 | Thrombotic Thrombocytopenic Purpura | 99.61% | L5 | ⚠️ **Contraindication direction**: TTP is thrombotic; emicizumab may worsen microvascular occlusion | Hold |
| 9 | Fetal and Neonatal Alloimmune Thrombocytopenia | 99.52% | L5 | ✗ Immune platelet destruction; neonatal safety data absent | Hold |
| 10 | Flood Factor Deficiency (Prekallikrein) | 99.40% | L5 | ✗ Contact pathway defect; not a clinical bleeding disorder; mechanistic mismatch | Hold |

> ⚠️ **TTP Safety Flag**: Emicizumab's procoagulant mechanism is directly opposed to the pathophysiology of TTP (a microthrombotic disorder driven by ADAMTS13 deficiency). This predicted indication should be considered a contraindication direction and excluded from further research.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Emicizumab's FIXa–FX bridging mechanism directly and precisely addresses the core hemostatic defect in Acquired Hemophilia A — the neutralization of endogenous FVIII by autoantibodies — using the identical mechanistic pathway that underpins its approved indication in congenital Hemophilia A. Two prospective Phase 2/3–3 trials (AGEHA and GTH-AHA-EMI), multiple real-world multicenter cohorts, and formal GTH Working Group consensus recommendations establish a robust L1 evidence foundation, making this one of the most scientifically grounded and clinically ready repurposing opportunities identified in this evidence pack.

**To proceed, the following is needed:**

- **Health Canada access pathway**: No Canadian DIN exists for emicizumab; the Special Access Programme (SAP) or a formal regulatory submission is required before any clinical use in Canada
- **Safety profile completion**: Roche/Chugai Hemlibra® product monograph must be reviewed for complete warnings and contraindications (flagged as Blocking data gap DG001 in this pack)
- **Thrombosis risk protocol**: Establish a formal protocol for monitoring thromboembolic events; aPCC co-administration must be strictly avoided; define bridging rules when transitioning from bypassing agents
- **IST coordination plan**: Define timing criteria and monitoring strategy for concurrent immunosuppressive therapy aimed at eradicating FVIII inhibitors (per GTH consensus, PMID 38049124)
- **MOA documentation**: Complete DrugBank API query for formal mechanism of action record to close data gap DG002 and enable downstream mechanistic analysis for other predicted indications (particularly Glanzmann thrombasthenia at rank 3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

