---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 913
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ticagrelor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ticagrelor: Intracranial arteriosclerosis
{: .text-alpha }

## One-Sentence Summary

Ticagrelor is an oral antiplatelet drug originally used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**,
with **2 clinical trials** (one large Phase 3 trial still ongoing) and **2 publications** currently supporting this direction. Direct evidence is still early, since no results are available yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (see note below) |
| Canada Market Status | Marketed (valid licenses: 12 of 12) |
| Number of DINs | 12 (valid: 12) |
| Recommended Decision | Hold (research question stage) |

*Note on evidence level:* The only Phase 3 trial for this indication (CAPTIVA) is still active with no results, so there is no completed randomised trial. The L2 grade reflects the strongest available signal rather than a completed trial. Strictly applying the grading rules, the level is closer to L4 to L5 for this specific indication.

*Note on the original indication:* The Health Canada records compiled for this report contain no approved-indication text. The original indications listed here do not come from product labels.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible, direct-acting P2Y12 receptor antagonist. It blocks ADP-mediated platelet activation and aggregation, which reduces clot formation on ruptured or diseased arterial plaque.

Acute coronary syndrome and intracranial arteriosclerosis share the same underlying process: atherosclerotic plaque with platelet-driven thrombosis. Ticagrelor acts faster and more consistently than clopidogrel, particularly in people who carry CYP2C19 loss-of-function variants and respond poorly to clopidogrel. This gives a biologically sound reason to test it in symptomatic intracranial atherosclerotic stenosis and stroke prevention.

The current evidence is mainly mechanistic and design-stage. The large Phase 3 CAPTIVA trial compares anticoagulation against antiplatelet strategies, so ticagrelor is not the only variable being tested. Related stroke and TIA evidence (the CYP2C19 carrier trial) supports the biological plausibility but is not specific to intracranial disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1683 | CAPTIVA: tests whether rivaroxaban, ticagrelor or both are superior to clopidogrel for lowering 1-year ischaemic stroke, intracerebral haemorrhage or vascular death in intracranial atherostenosis. No results yet. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot trial of genotype-guided P2Y12 inhibitor selection versus conventional clopidogrel in symptomatic intracranial atherosclerotic disease. Exploratory, not specific to ticagrelor. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Experience with ticagrelor 60 mg twice daily plus aspirin 81 mg versus standard aspirin and clopidogrel for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design/protocol | Int J Stroke | Design and early progress of CAPTIVA, testing whether other dual antithrombotic combinations beat clopidogrel plus aspirin in symptomatic intracranial stenosis. |

Broader supporting evidence for ticagrelor in related ischaemic settings includes the following trials. These are not specific to intracranial arteriosclerosis.
- [34708996](https://pubmed.ncbi.nlm.nih.gov/34708996/) (NEJM 2021): ticagrelor versus clopidogrel in CYP2C19 loss-of-function carriers with stroke or TIA.
- [35727586](https://pubmed.ncbi.nlm.nih.gov/35727586/) (JAMA Neurol 2022): time course of benefit and risk of ticagrelor plus aspirin in CYP2C19 loss-of-function carriers after minor stroke or TIA.

---

## Canada Market Information

Twelve single-ingredient licences are currently valid. The data compiled for this report has no dosage form or approved-indication text for any of them. Main authorisations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02368544 | BRILINTA | Not available | Not available |
| 02455005 | BRILINTA | Not available | Not available |
| 02482630 | APO-TICAGRELOR | Not available | Not available |
| 02492598 | TARO-TICAGRELOR | Not available | Not available |
| 02531798 | JAMP TICAGRELOR | Not available | Not available |

Other valid generics include AG-TICAGRELOR, M-TICAGRELOR and additional JAMP, TARO and APO strengths.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** liver failure, liver disease, gallbladder disease, intracranial haemorrhage. The last one matters in a stroke-related indication, where haemorrhagic transformation is a real concern.
- **Drug Interactions:** 100 interactions were identified in total. Notable examples:
  - **Major:** clarithromycin (a strong CYP3A inhibitor that can raise ticagrelor exposure).
  - **Moderate:** acetylsalicylic acid, morphine (can delay oral ticagrelor absorption), simvastatin, dexamethasone, aprepitant, saxagliptin, miconazole and others.
- **Bleeding risk:** Ticagrelor with aspirin or other antithrombotics raises bleeding risk. Bleeding-reduction strategies such as lower-dose ticagrelor or P2Y12 monotherapy are being studied in other settings.

Product-label warnings and contraindications for Canada were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold (research question stage)**

**Rationale:**
Ticagrelor has a plausible mechanism and a very high model score for intracranial arteriosclerosis. The only large, directly relevant trial (CAPTIVA) has no results and does not isolate ticagrelor. Ticagrelor's strong evidence in coronary disease and CYP2C19-carrier stroke/TIA does not directly transfer to intracranial atherosclerosis, and the added intracranial haemorrhage risk calls for caution. The decision can be revisited when CAPTIVA reports (estimated completion January 2027).

**To proceed, the following is needed:**
- CAPTIVA results, specifically the ticagrelor arm versus clopidogrel
- Mechanism of action data to complete the mechanistic analysis
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening), plus dosage forms and approved indications for the DINs
- Bleeding-risk and patient-selection plan, including CYP2C19 status, intracranial haemorrhage history and interacting drugs
- Larger ticagrelor-specific trials in intracranial atherosclerosis

---

*Other predicted indications (Monckeberg arteriosclerosis, priapism, May-Thurner syndrome, livedo reticularis, mesenteric vascular occlusion, vascular ectasia, angiodysplasia, fibrocartilaginous embolism) have little or no supporting evidence and are on Hold. Angiodysplasia is better treated as a bleeding-safety concern than as a therapeutic indication. "Ischemic disease" (rank 4) is largely an extension of the already approved coronary indication, supported by multiple large randomised trials, and is a candidate for Proceed with Guardrails (bleeding risk, patient selection, regimen duration).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

