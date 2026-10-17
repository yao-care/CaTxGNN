---
layout: default
title: Warfarin
parent: Moderate Evidence (L3-L4)
nav_order: 985
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Warfarin: predicted new indication Heparin cofactor 2 deficiency (evidence level L4). Approved use: Pulmonary embolism, thrombotic disease, intracranial embolism"
monitor_inn: "Warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Warfarin: From Thrombotic Disease to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Warfarin is an oral anticoagulant originally used to treat and prevent thrombotic disease, including pulmonary embolism and intracranial embolism.
The TxGNN model predicts it may be useful for **heparin cofactor 2 deficiency**, but support is thin: **no clinical trials** and only **3 case reports** (1990-2001) are currently available for this specific condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombotic disease, intracranial embolism (the Canadian licence records contain no indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, warfarin is a vitamin K antagonist. It reduces the production of vitamin K-dependent clotting factors II, VII, IX and X, and its efficacy in thrombotic disease is well established.

Heparin cofactor II deficiency is an inherited condition that predisposes people to blood clots. Because warfarin works as a long-term antithrombotic, it is a plausible option for this kind of inherited thrombophilia. However, this is an extension of warfarin's existing thrombosis use, not an independent repurposing signal.

The other predictions in the list follow a similar pattern. Factor V excess, antithrombin deficiency type 2 and general thrombophilia are all clot-promoting states where anticoagulation makes biological sense. By contrast, rheumatoid arthritis, breast fibrocystic disease and benign mammary dysplasia have no plausible therapeutic link to warfarin. Their high scores appear to reflect co-prescription and drug-interaction associations rather than benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for heparin cofactor 2 deficiency.

For the broader thrombophilia prediction (rank 4), one Phase 3 trial exists:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | D-dimer-guided strategy to decide how long to extend anticoagulation after an unprovoked deep vein thrombosis. Warfarin is part of the strategy, not the isolated test intervention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Right ventricular thrombus in a 14-year-old girl with familial heparin cofactor II deficiency |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Woman with congenital antithrombin deficiency, repeated thrombosis and pulmonary infarction, treated with warfarin for 7 years, then switched to low-dose heparin |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report (family) | Journal of UOEH | Family with multiple thromboses from infancy; a child developed repeat deep vein thrombosis despite warfarin |

None of these provides controlled efficacy data. The first two are listed under heparin cofactor II deficiency, but the second concerns antithrombin deficiency and the third a thrombophilia in which known causes were excluded. They support the clinical context only loosely.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242925 | APO-WARFARIN | Not listed | Not listed |
| 02242928 | APO-WARFARIN | Not listed | Not listed |
| 02242929 | APO-WARFARIN | Not listed | Not listed |
| 02242697 | TARO-WARFARIN | Not listed | Not listed |
| 02242680 | TARO-WARFARIN | Not listed | Not listed |

Sixteen valid single-ingredient licences are held in total (APO-WARFARIN and TARO-WARFARIN products). No cancelled licences were found.

---

## Safety Considerations

**Contraindications from the knowledge graph (not label text):** conditions linked to warfarin as contraindications include liver failure and liver disease, hypertension, congestive heart failure, blood coagulation disease, impaired renal function, nephrotic syndrome, cholestasis, hypothyroidism, anemia, hyperlipidemia, psychotic and other mental disorders, substance abuse or dependence, and chronic diarrheal disease. These should be checked against the official labelling.

**Drug Interactions:** 100 interactions were found in total. Notable ones include:
- **Major:** acetylsalicylic acid (aspirin), metronidazole
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), proton pump inhibitors and H2 blockers (rabeprazole, ranitidine), doxycycline, amoxicillin, metformin, bupropion, aprepitant, mesalazine, balsalazide, chenodeoxycholic acid

**Other considerations from the literature:**
- Warfarin-induced skin necrosis is a rare complication (0.01-0.1%) and is a particular concern in protein C or S deficiency.
- Danazol and leflunomide are reported to increase warfarin's effect, raising bleeding risk or requiring dose reduction.

Product warnings and contraindications from the Canadian package inserts were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For heparin cofactor 2 deficiency, evidence is limited to three old case reports, with no trials and no controlled efficacy data. The TxGNN score is high (99.87%), but it largely reflects the closeness of this condition to warfarin's existing thrombosis indications. The rheumatoid arthritis and breast-related predictions look like artifacts of drug interactions and should not be pursued.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Controlled or registry data on warfarin in inherited thrombophilias such as heparin cofactor II deficiency
- Comparison against current standard anticoagulant options, including direct oral anticoagulants
- A monitoring plan covering INR, bleeding risk and key drug interactions
- Indication text for the Canadian licences, to confirm the approved scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

