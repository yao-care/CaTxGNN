---
layout: default
title: Medroxyprogesterone Acetate
parent: Model Prediction Only (L5)
nav_order: 577
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "MEDROXYPROGESTERONE ACETATE"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "renal hypoplasia (disease)", "apocrine adenosis of breast", "blunt duct adenosis of breast"]
description: "Medroxyprogesterone Acetate: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Medroxyprogesterone Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Medroxyprogesterone Acetate: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Medroxyprogesterone acetate (MPA) is a synthetic progestin originally used for endometriosis, endometrial cancer, and postmenopausal conditions such as osteoporosis and atrophic vaginitis.
The TxGNN model predicts it may be effective for **amenorrhea**, but the data compiled for this report show **0 clinical trials** and **19 publications**, mostly older reviews on injectable contraception, so the evidence rests largely on the model prediction and general pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, MPA is a synthetic progestin that induces secretory transformation of estrogen-primed endometrium and withdrawal bleeding. It is used clinically in progestin challenge tests and in the management of secondary amenorrhea.

The original indications (endometriosis and endometrial disease) are also hormone-driven conditions in which progestin action on the endometrium is central. This overlap makes a role in menstrual disorders such as amenorrhea mechanistically plausible.

Caution is needed in reading the literature. The retrieved publications mainly describe amenorrhea and menstrual disturbance as *effects* of injectable contraception (Depo-Provera), not as a treatment target. They therefore support pharmacology and safety context rather than therapeutic efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Of 19 retrieved publications, the most relevant are listed below. All are low-tier evidence (reviews, a survey, and older narrative articles).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Systematic review | Cochrane Database Syst Rev | Combination injectable contraceptives are highly effective but may be limited by bleeding pattern changes |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic review | Cochrane Database Syst Rev | Update of the review above on combination injectable contraceptives |
| [6230212](https://pubmed.ncbi.nlm.nih.gov/6230212/) | 1983 | Survey | Contraception | Survey of 35 investigators on managing menstrual disturbances during DMPA and NET-EN use; counselling emphasised |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counselling and side-effect management for women using DMPA contraception |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Review | Int J Fertil Menopausal Stud | Long-acting contraceptive options, including depot injectables |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception timing in relation to postpartum amenorrhea |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Drug-induced infertility via effects on the hypothalamic-pituitary-gonadal axis |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monogr | General monograph on MPA carcinogenic risk evaluation |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02267640 | AA-MEDROXY | Not available | Not available |
| 02244726 | AA-MEDROXY | Not available | Not available |
| 02277298 | AA-MEDROXY | Not available | Not available |
| 02221284 | TEVA-MEDROXYPROGESTERONE | Not available | Not available |
| 02523493 | DEPO-PROVERA | Not available | Not available |

Eight valid single-ingredient licences are held in Canada; the five above are the main ones shown.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease associations, not label text):
- Cardiovascular and metabolic: hypertension, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia
- Hepatic and renal: liver failure, liver disease, gallbladder disease, kidney disease
- Hormone-related and malignancy: female breast carcinoma, hypothyroidism
- Bone and mineral: osteoporosis (including postmenopausal), hypercalcemia, nephrocalcinosis, humoral hypercalcemia of malignancy
- Other: epilepsy, asthma, systemic lupus erythematosus, anxiety and dysthymic disorders, substance abuse/dependence

**Drug interactions:** 100 interactions were recorded, all of those listed being Moderate level. The main groups are:
- Antidiabetic agents (acarbose, metformin, glimepiride, chlorpropamide, SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin, DPP-4 inhibitors such as alogliptin and saxagliptin, GLP-1 agonists such as liraglutide, semaglutide and dulaglutide, and insulins): glycaemic control may be affected
- Others: aprepitant, dexamethasone, clarithromycin, pegvaliase

Package insert warnings and contraindications were not available, so please refer to the Health Canada package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is very high, but there are no registered clinical trials and the literature mainly covers menstrual disturbance as a side effect of injectable contraception, not as a therapeutic outcome. MPA's use in secondary amenorrhea is established pharmacology, so this is not a distinct repurposing opportunity, and the repurposing case rests on model prediction alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indication text (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Confirmation of whether amenorrhea management is already covered by an existing Canadian label indication
- Controlled clinical evidence for amenorrhea, or a review of the existing therapeutic guidance
- A review of the metabolic and breast-related contraindication signals, together with the antidiabetic drug interactions, for the target population

**Other predicted indications (for reference):**
- Fibrocystic breast disease (L3, Research Question): two small, dated clinical reports of MPA use, but HRT literature shows mixed breast safety signals, including increased mammographic density.
- Benign mammary dysplasia, cervix endometriosis, endometriosis of the rectovaginal septum and vagina, endometriosis in cutaneous scar, apocrine adenosis, and blunt duct adenosis (Hold): little or no direct evidence. Several are subtypes of the existing endometriosis indication, or are breast lesions where progestin proliferation risk argues for caution.
- Bilateral renal hypoplasia and renal hypoplasia (Hold, L5): no plausible mechanism; the predictions are likely TxGNN model (deep learning) artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

