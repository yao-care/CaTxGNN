---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 930
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "TRANEXAMIC ACID"
predicted_indications: ["amenorrhea (disease)"]
description: "Tranexamic Acid: predicted new indication Amenorrhea (disease) (evidence level L5). In Canada: 12 DINs (12 marketed)"
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Tranexamic Acid: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent. The data compiled for this report list endometriosis as its original indication, and it is widely marketed in Canada.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are currently **no registered clinical trials** and only **2 review-type publications**, which support reduction of menstrual bleeding rather than induction of amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9919 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 12 of 12) |
| Number of DINs | 12 (marketed: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tranexamic acid: "Tranexamic acid is a synthetic lysine amino acid derivative, which diminishes the dissolution of hemostatic fibrin by plasmin. In the presence of tranexamic acid, the lysine receptor binding sites of plasmin for fibrin are occupied, preventing binding to fibrin monomers, thus preserving and stabilizing fibrin's matrix structure." ([DailyMed: Cyklokapron (tranexamic acid) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e89a7d9-4da4-42aa-b7f8-c602c24eefe5), label version 2025-09-03; accessed 2026-11-19.) Based on general knowledge of the drug class, tranexamic acid is an antifibrinolytic that inhibits plasminogen activation and so reduces fibrinolysis-driven bleeding, including endometrial bleeding. Its marketed use in heavy menstrual bleeding provides a plausible link to menstrual suppression.

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

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02064405 | CYKLOKAPRON 500 MG | TRANEXAMIC ACID | Marketed |
| 02064413 | CYKLOKAPRON 100 MG/ML | TRANEXAMIC ACID | Marketed |
| 02246365 | TRANEXAMIC ACID INJECTION BP | TRANEXAMIC ACID | Marketed |
| 02392763 | TRANEXAMIC ACID INJECTION | TRANEXAMIC ACID | Marketed |
| 02401231 | TRANEXAMIC ACID TABLETS | TRANEXAMIC ACID | Marketed |
| 02409097 | GD-TRANEXAMIC ACID | TRANEXAMIC ACID | Marketed |
| 02466015 | TRANEXAMIC ACID INJECTION | TRANEXAMIC ACID | Marketed |
| 02496232 | MAR-TRANEXAMIC ACID | TRANEXAMIC ACID | Marketed |
| 02497328 | TRANEXAMIC ACID INJECTION | TRANEXAMIC ACID | Marketed |
| 02519194 | TRANEXAMIC ACID | TRANEXAMIC ACID | Marketed |
| 02531208 | TRANEXAMIC ACID INJECTION | TRANEXAMIC ACID | Marketed |
| 02549395 | M-TRANEXAMIC ACID | TRANEXAMIC ACID | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

They include the Cyklokapron brand (500 mg and 100 mg/mL).

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyklokapron (tranexamic acid) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e89a7d9-4da4-42aa-b7f8-c602c24eefe5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

