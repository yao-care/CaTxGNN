---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine P2Y12 inhibitor whose established use — per the supporting literature in this evidence pack — is antiplatelet therapy for acute coronary syndrome (ACS) patients undergoing percutaneous coronary intervention (PCI); it is not currently marketed in Canada. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but the **2 clinical trials** and **2 publications** currently retrieved for this pairing are keyword co-occurrence hits (anticoagulant/antithrombotic topic overlap) rather than direct evidence of prasugrel treating pulmonary hypertension.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / post-PCI antiplatelet therapy (inferred from supporting literature; no Canadian regulatory record exists) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available for Prasugrel in this evidence pack. Based on known information, Prasugrel is a third-generation thienopyridine and irreversible P2Y12 receptor antagonist, and its efficacy in reducing thrombotic events in ACS/PCI patients is well established in the literature retrieved here (e.g., PMID 21241206 discusses prasugrel alongside clopidogrel as standard post-stent antiplatelet therapy).

The proposed link to pulmonary hypertension rests on a theoretical pathway: antiplatelet agents could plausibly interfere with the thrombotic component seen in chronic thromboembolic pulmonary hypertension (CTEPH), a PH subtype driven partly by unresolved pulmonary thromboemboli. This is a biologically coherent hypothesis in principle.

However, upon review, neither of the two clinical trials nor the two publications returned for this pairing actually studies prasugrel in pulmonary hypertension patients. The trials concern NOAC use in atrial fibrillation and cancer-associated thrombosis eligibility, and the literature covers clopidogrel adherence and COVID-19 comorbidity outcomes — all retrieved through generic "antithrombotic" keyword overlap rather than a PH-specific mechanistic or clinical signal. The mechanistic rationale therefore remains weak and largely unsupported by the available evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational, cross-sectional study describing NOAC use in elderly patients with non-valvular atrial fibrillation in Spain; unrelated to prasugrel or PH, captured via antithrombotic-therapy overlap only |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility of cancer-associated thrombosis patients for trials like CARAVAGGIO; no direct relevance to prasugrel or pulmonary hypertension |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Examines factors associated with clopidogrel (vs. prasugrel) use and adherence in ACS patients post-PCI; supports prasugrel's established antiplatelet role but does not address pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Retrospective | Kardiologiia | Analyzes how pre-existing chronic disease therapy (from the ACTIV COVID-19 registry) affected COVID-19 mortality; comorbidity-background analysis, not a PH-specific or prasugrel-specific study |

---

## Canada Market Information

Prasugrel is currently **not marketed** in Canada — the regulatory data show 0 registered DINs and no active licenses, so no authorization table is available for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trial and literature evidence retrieved for the prasugrel–pulmonary hypertension pairing is indirect (keyword co-occurrence on "antithrombotic" themes) rather than disease-specific, and the candidate has not yet advanced past the initial screening stage (S0) because a blocking data gap — missing TFDA/label safety information — prevents even a preliminary safety assessment (S1).

**To proceed, the following is needed:**
- Drug label warnings and contraindications (currently a **blocking** data gap; required before any safety screening can occur)
- Detailed mechanism of action (MOA) data from DrugBank to properly assess mechanistic plausibility for pulmonary hypertension (specifically CTEPH)
- Pulmonary hypertension–specific clinical trials or case evidence for prasugrel (none currently exist in the retrieved evidence)
- For context: among the other TxGNN-predicted indications for prasugrel in this batch, **migraine disorder** (rank 2, evidence level L3, decision stage S1) has comparatively stronger supporting literature — involving prasugrel's own drug class (thienopyridines) in patients with patent foramen ovale — and may warrant prioritized review ahead of the pulmonary hypertension signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

