---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Misoprostol: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Misoprostol: From an Unspecified Original Indication to Amenorrhea

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analogue marketed in Canada, both alone and in combination products. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are **no registered clinical trials**, and the **7 publications** retrieved mostly concern pregnancy termination and related topics rather than amenorrhea treatment.
Evidence is limited to model prediction and indirect literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 (preclinical/mechanistic and indirect literature; no completed RCT for this indication) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, misoprostol is a prostaglandin E1 analogue that causes uterine contraction and cervical ripening.

This supports a plausible effect on pregnancy-related causes of absent menses, such as retained products of conception or missed abortion. It does not address the endocrine or structural causes of primary or secondary amenorrhea, such as hypothalamic, pituitary or ovarian disorders, or Asherman syndrome.

The retrieved literature concerns pregnancy termination, medical management of missed abortion and abnormal uterine bleeding, not the treatment of amenorrhea. The high TxGNN score (0.996) is a model prediction, and the link to this indication is indirect. In most of these studies, "amenorrhea" is used to describe gestational age rather than as the condition being treated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) received low-dose mifepristone with hospital- or self-administered misoprostol for medical abortion |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reprod Sci | 2,500 women with ultra-early pregnancy were randomised to oral mifepristone 50–150 mg followed by misoprostol 200 µg; the primary endpoint was complete abortion without surgery |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Hum Reprod | Low-dose mifepristone plus misoprostol before expected menstruation to prevent unintended pregnancy |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Clinical study | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Clinical study | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation in the management of abnormal uterine bleeding |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy in a patient who presented with amenorrhea; not a misoprostol treatment study |

None of these publications evaluates misoprostol as a treatment for amenorrhea.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244022 | MISOPROSTOL | Not available | Not available |
| 02244023 | MISOPROSTOL | Not available | Not available |
| 02413469 | PMS-DICLOFENAC-MISOPROSTOL | Not available | Not available |
| 02413477 | PMS-DICLOFENAC-MISOPROSTOL | Not available | Not available |
| 02229837 | ARTHROTEC 75 | Not available | Not available |

The data compiled for this report list 10 valid licences in total (all single-entity records, none cancelled). The other products include ARTHROTEC 50, GD-DICLOFENAC/MISOPROSTOL 50 and 75, MIFEGYMISO and FEMYSO.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived disease–drug links, not label text): hypertension, liver disease or failure, drug-induced liver injury, gallbladder disease, congestive heart failure, cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, blood coagulation disease, inflammatory bowel disease, asthma, anaemia and haemoglobinopathy, active peptic ulcer disease, substance abuse/dependence, and non-infectious meningitis.
- **Drug Interactions** (100 records retrieved; main ones listed):
  - **Major:** dinoprostone (topical)
  - **Moderate:** magnesium-containing antacids (magnesium oxide, carbonate, hydroxide, magaldrate) and quinapril
  - **Minor:** sodium citrate, aluminium hydroxide, calcium carbonate, sodium bicarbonate and naproxen
- **Pregnancy-related concern:** misoprostol use in pregnancy has been associated with congenital anomalies (e.g., Möbius sequence, limb defects) after failed abortion. This is a significant safety consideration for any use in women of reproductive age.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (99.64%) with an indirect mechanistic link. There are no registered trials, and the retrieved literature addresses pregnancy termination rather than amenorrhea treatment. Misoprostol would not address the endocrine or structural causes of amenorrhea, and it carries reproductive safety concerns.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational studies that directly evaluate misoprostol in a defined amenorrhea population (e.g., retained products of conception, or intrauterine adhesions)
- A clear definition of which amenorrhea subtype is being targeted, and a reproductive safety risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

