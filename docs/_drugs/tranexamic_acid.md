---
layout: default
title: Tranexamic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 930
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Tranexamic Acid: predicted new indication Amenorrhea (evidence level L4). Approved use: Endometriosis"
monitor_inn: "TRANEXAMIC ACID"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Tranexamic Acid: From Endometriosis to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent. The data compiled for this report list endometriosis as its original indication, and it is widely marketed in Canada.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are currently **no registered clinical trials** and only **2 review-type publications**, which support reduction of menstrual bleeding rather than induction of amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (from the knowledge graph; no approved indication text is available from Canadian licences) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge of the drug class, tranexamic acid is an antifibrinolytic that inhibits plasminogen activation and so reduces fibrinolysis-driven bleeding, including endometrial bleeding. Its marketed use in heavy menstrual bleeding provides a plausible link to menstrual suppression.

However, amenorrhea is not a direct pharmacological effect of the drug. The high TxGNN score most likely reflects network proximity to abnormal uterine bleeding and menstrual disorders, rather than a demonstrated ability to stop menstruation. The two retrieved publications support reducing menstrual blood loss, not inducing amenorrhea. The mechanistic link should therefore be treated as a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of pharmacological therapies for abnormal uterine bleeding. Selection depends on the cause and amount of bleeding, contraception needs, fertility preservation and perimenopausal status. Non-hormonal options are included. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Approach to menses prophylaxis and suppression in pre-menopausal women with haematologic cancer, where menstrual bleeding adds to the risk from low blood counts. Comparative data are scarce. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02246365 | Tranexamic Acid Injection BP | Not specified | Not specified |
| 02409097 | GD-Tranexamic Acid | Not specified | Not specified |
| 02466015 | Tranexamic Acid Injection | Not specified | Not specified |
| 02531208 | Tranexamic Acid Injection | Not specified | Not specified |
| 02401231 | Tranexamic Acid Tablets | Not specified | Not specified |

These are 5 of the 12 valid single-ingredient licences. They include the Cyklokapron brand (500 mg and 100 mg/mL).

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
Conditions linked to contraindications include hypertension, thrombophlebitis, stroke and cerebrovascular disorder, coronary artery disease, liver and gallbladder disease, diabetes mellitus and diabetic ketoacidosis, hyperglycemia, hyperlipidemia and hypertriglyceridemia, porphyria, migraine, brain edema, anxiety and neurotic disorders, obesity, female breast carcinoma, and endometrial or uterine corpus cancer. These come from network associations and must be checked against the official label.

**Drug Interactions:** 35 interactions were identified in total. The main ones are:
- **Major:** oestrogens and hormonal contraceptives (ethinylestradiol, estradiol, conjugated and esterified estrogens, estrone, diethylstilbestrol, norethisterone, drospirenone, etonogestrel), as well as estramustine, carfilzomib, anti-inhibitor coagulant complex, and Factor IX complex. The common concern is an additive risk of thrombosis.
- **Moderate:** thrombolytics (alteplase, anistreplase), which have opposing pharmacological effects.

Label warnings and contraindications from the Canadian package insert are not yet available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and two reviews that address reduced menstrual bleeding, not amenorrhea. There are no clinical trials, and the mechanism is not directly linked to the predicted indication. Many hormonal drugs that interact with tranexamic acid are commonly used for menstrual suppression, which raises thrombotic risk for this use.

**To proceed, the following is needed:**
- Canadian package insert data (indications, warnings, contraindications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Clinical evidence showing that tranexamic acid induces or maintains amenorrhea, rather than only reducing blood loss
- A thrombotic risk assessment for combination with hormonal agents
- Clarification of the intended clinical goal, for example menstrual suppression in haematology patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

