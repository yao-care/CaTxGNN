---
layout: default
title: Alteplase
parent: Model Prediction Only (L5)
nav_order: 42
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Alteplase: predicted new indication Posteroinferior myocardial infarction (evidence level L5). Approved use: Pulmonary embolism, stroke, myocardial infarction, coronary thrombosis"
---

# Alteplase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alteplase: From Myocardial Infarction and Stroke to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator, originally used to dissolve blood clots in conditions such as myocardial infarction, pulmonary embolism and ischaemic stroke.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**, but **no clinical trials or publications** are currently linked to this specific prediction.
The more mature signal in this data is for **thrombophilia** (**1 clinical trial** and **20 publications**, mostly case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, stroke, myocardial infarction, coronary thrombosis (approved-indication text for the Canadian licences is not available) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 for this prediction (model prediction only; the closest related literature is indirect) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, alteplase is a recombinant tissue plasminogen activator. It converts plasminogen to plasmin, which breaks down fibrin in clots. Its efficacy in acute myocardial infarction is established.

Posteroinferior myocardial infarction is an anatomical subtype of myocardial infarction, which is already an approved use. The mechanism, dissolving the clot that blocks a coronary artery, applies directly. The high model score likely reflects this close relationship to the parent indication rather than new subtype-specific findings. No trials or literature specific to this subtype were found, so the support is indirect.

Other predictions in the list include posterolateral and septal myocardial infarction, thrombophilia and coronary stenosis. The first two follow the same logic of subtype inclusion. Thrombophilia has the most supporting material, but much of it is case reports of thrombolysis in patients with an underlying clotting disorder. Fibrinolysis treats the acute clot, not the underlying disorder.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for posteroinferior myocardial infarction.

For reference, one trial is linked to the related prediction of thrombophilia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | Recruiting | 70 | Bedside clotting tests used to guide tPA treatment in critically ill patients with a prothrombotic acute respiratory failure (COVID and non-COVID). Safety, dose-finding and efficacy are being assessed. No results yet, and applicability to thrombophilia needs verification. |

---

## Literature Evidence

Currently no related literature is available for posteroinferior myocardial infarction.

For reference, the closest published material comes from the related prediction of septal myocardial infarction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | Clinical study | Rev Port Cardiol | Effect of late alteplase thrombolysis (after 6 hours) on left ventricular function in myocardial infarction |
| [37754803](https://pubmed.ncbi.nlm.nih.gov/37754803/) | 2023 | Case report | J Cardiovasc Dev Dis | Pulmonary embolism mimicking anteroseptal ST-elevation MI after cardiac arrest, treated with thrombectomy and catheter-directed thrombolysis |
| [40281444](https://pubmed.ncbi.nlm.nih.gov/40281444/) | 2025 | Cohort | BMC Cardiovasc Disord | Prospective study of acute coronary syndrome outcomes in a setting with limited PCI access (Bhutan) |

The related prediction of coronary stenosis includes a double-blind randomized alteplase versus placebo trial in chest pain at rest ([8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/), 1993, *Eur Heart J*, 80 patients). It also includes a randomized, placebo-controlled trial in refractory unstable angina ([1782951](https://pubmed.ncbi.nlm.nih.gov/1782951/), 1991, 36 patients). These support the thrombolytic mechanism in acute coronary syndromes but not a subtype-specific claim.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245859 | CATHFLO | Not specified | Not specified |
| 02225689 | ACTIVASE RT-PA | Not specified | Not specified |
| 02147440 | ACTIVASE RT-PA | Not specified | Not specified |

All three licences are valid single-ingredient products.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interactions in total, of which the first 20 are available for review. They include **Major** interactions with several agents that affect clotting or bleeding:
  - Anticoagulants and antithrombotics: fondaparinux, apixaban, anisindione, abciximab
  - Other agents: acalabrutinib, deferasirox, and the radiolabelled antibodies ibritumomab tiuxetan and tositumomab
- **Moderate** interactions include acetylsalicylic acid, ibuprofen, ketorolac, fluvoxamine, fosinopril, aminocaproic acid, aprotinin, and the appetite suppressants fenfluramine, dexfenfluramine and sibutramine.
- Bleeding risk is the main concern when alteplase is combined with these agents.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posteroinferior myocardial infarction is a subtype of an already approved indication, so the mechanism fits. However, no subtype-specific trials or literature exist, and the model score alone is not enough for a new-indication decision. The Health Canada safety label data needed for safety screening is also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved-indication text for the three DINs
- Mechanism-of-action data from DrugBank
- Subtype-specific evidence, or confirmation that posteroinferior MI is already covered under the approved myocardial infarction indication (in which case it may not be a true repurposing)
- For thrombophilia, confirmation of the population and design of NCT05540834, and a bleeding-risk and anticoagulation plan, since current evidence is mostly case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

