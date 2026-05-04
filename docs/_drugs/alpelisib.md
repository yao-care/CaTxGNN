---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Alpelisib
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

# Alpelisib: From Advanced Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray) is a selective PI3Kα inhibitor approved for PIK3CA-mutated HR+/HER2-negative advanced breast cancer, representing a molecularly targeted approach in oncology.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension** (top-ranked predicted indication),
with **0 directly relevant clinical trials** and **2 publications** currently identified — and critically, the available evidence points to potential cardiac safety risks rather than therapeutic benefit in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2-negative advanced breast cancer with PIK3CA mutation (inferred from clinical trial data; original indication field not populated) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed (0 approved products on file) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Alpelisib (BYL719) is a first-in-class, oral, selective inhibitor of PI3Kα (phosphoinositide 3-kinase alpha), the enzyme encoded by the *PIK3CA* gene. In approximately 40% of HR+/HER2-negative breast cancers, activating mutations in *PIK3CA* drive constitutive PI3K/AKT/mTOR signaling, fueling uncontrolled cell proliferation. Alpelisib blocks this driver mutation, and the landmark SOLAR-1 Phase III trial established its efficacy in this population when combined with fulvestrant.

The theoretical connection to pulmonary hypertension (PH) is mechanistically plausible but indirect. PI3K/AKT/mTOR pathway activation is known to drive pulmonary arterial smooth muscle cell (PASMC) proliferation and vascular remodeling — the central pathological process in pulmonary arterial hypertension (PAH). Several other pathway inhibitors (notably mTOR inhibitors like everolimus) have been explored in PAH preclinical models, lending conceptual support to the idea that upstream PI3Kα inhibition could reduce aberrant vascular remodeling. The TxGNN model likely captured this shared pathway biology.

However, this prediction confronts a serious safety counter-signal. PI3Kα signaling is critically cardioprotective in cardiomyocytes — particularly in the right ventricle (RV), which is already under severe pressure overload in PAH patients. A 2019 preclinical study (McLean et al., *Journal of the American Heart Association*) demonstrated that pharmacological PI3Kα inhibition combined with doxorubicin produced **biventricular atrophy and right ventricular dysfunction** in animal models. Since RV failure is the proximate cause of death in advanced PAH, Alpelisib could theoretically accelerate rather than arrest disease progression. Until this safety concern is specifically addressed in PAH-focused preclinical models, the theoretical mechanistic benefit is substantially outweighed by the potential for harm.

---

## Clinical Trial Evidence

No clinical trials directly investigating Alpelisib for pulmonary hypertension were identified. The single trial retrieved during evidence search (NCT06705504, REASSURE study) was a real-world observational cohort study in HR+/HER2-negative breast cancer and has no direct relevance to pulmonary hypertension.

Currently no related clinical trials registered for pulmonary hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease (ILD) in an advanced breast cancer patient — documents a pulmonary adverse event, not therapeutic benefit for PH; highlights alpelisib's potential for pulmonary toxicity |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical Study | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin resulted in distinct biventricular atrophy and right ventricular dysfunction in animal models — a critical safety signal directly relevant to PH, where right heart failure is the primary cause of death |

---

## Canada Market Information

Alpelisib has no approved products on file in the current dataset (0 DINs). No regulatory product information is available for table listing.

---

## Cytotoxicity

Alpelisib is an antineoplastic agent (targeted PI3Kα inhibitor) used in oncology. The cytotoxicity profile differs substantially from conventional chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — PI3Kα-selective kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to moderate (hematological toxicity is not the primary dose-limiting toxicity; anemia and lymphopenia reported at lower rates than cytotoxic chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting plasma glucose and HbA1c (hyperglycemia is the primary dose-limiting toxicity and requires active management), liver function tests, CBC with differential, renal function, skin assessment (rash/severe cutaneous reactions), pulmonary symptoms (ILD monitoring) |
| Handling Protection | Standard oral targeted therapy handling; institutional cytotoxic spill procedures recommended per policy, though lower risk than parenteral cytotoxic agents |

---

## Safety Considerations

Formal prescribing information (TFDA/Health Canada package insert warnings and contraindications) was not available in this evidence pack. Based on the clinical trial literature reviewed, the following class-related safety concerns are known for Alpelisib:

- **Known Adverse Events of Interest (from retrieved literature):** Severe hyperglycemia (class-defining toxicity requiring glucose management protocols), interstitial lung disease/pneumonitis, severe hypersensitivity reactions, severe cutaneous reactions, and diarrhea
- **Cardiac Safety Signal:** Preclinical data (McLean et al. 2019) demonstrates right ventricular dysfunction with PI3Kα inhibition — of direct relevance if repurposing to pulmonary hypertension is considered

Please refer to the official package insert for complete warnings, contraindications, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This indication is supported only by a computational model prediction (L5 evidence), with no directly supportive clinical trials or therapeutic literature; moreover, the available preclinical data raises a specific mechanism-based safety concern — PI3Kα inhibition impairs right ventricular function, which could be acutely harmful in pulmonary hypertension patients where right heart failure is the primary mode of death.

**To proceed, the following is needed:**
- Dedicated PAH-focused preclinical studies evaluating Alpelisib's effects on pulmonary arterial smooth muscle cell proliferation and pulmonary vascular remodeling (without concurrent anthracycline use)
- Right ventricular functional assessment in validated PAH animal models (e.g., monocrotaline or SU5416/hypoxia rat models) to determine whether the observed RV toxicity signal applies to PAH context
- Mechanistic clarification of PI3Kα's differential roles in PASMCs vs. cardiomyocytes vs. right ventricular tissue
- Retrieval and review of the full Health Canada/TFDA prescribing information to complete the safety profile
- Clarification of Canada regulatory status (Alpelisib/Piqray has received approval in multiple jurisdictions for breast cancer; the current dataset showing 0 DINs may reflect a data retrieval gap rather than true non-approval)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

