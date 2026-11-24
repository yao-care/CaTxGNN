---
layout: default
title: Vasopressin
parent: Model Prediction Only (L5)
nav_order: 968
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Vasopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not specified in the available Health Canada licence data"
monitor_inn: "Vasopressin"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
---

# Vasopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vasopressin: From an Unspecified Original Indication to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vasopressin is a hormone-based injectable marketed in Canada, but the data compiled for this report do not specify its approved indication.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 clinical trials** and only **3 loosely related publications** (one review and two case reports on other clotting-factor deficiencies), so this remains essentially a model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available Health Canada licence data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 (no trials; indirect literature only, none on prothrombin deficiency) |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for vasopressin: "Vasopressin causes vasoconstriction by binding to V 1 receptors on vascular smooth muscle coupled to the Gq/11-phospholipase C-phosphatidyl-inositol-triphosphate pathway, resulting in the release of intracellular calcium. In addition, vasopressin stimulates antidiuresis via stimulation of V 2 receptors which are coupled to adenyl cyclase." ([DailyMed: Vasostrict (vasopressin) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1147beb-743e-4c62-8927-91192447f8b8), label version 2026-04-21; accessed 2026-11-19.) Based on general pharmacology, vasopressin and its analogue desmopressin (DDAVP) act through V2 receptors to release stored factor VIII and von Willebrand factor from endothelial cells.

That mechanism is relevant to factor VIII and combined factor V/VIII deficiencies, **not** to prothrombin (factor II) deficiency. No documented mechanism raises prothrombin levels. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should therefore be treated as a hypothesis with weak mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Overview of acquired hemophilia A (autoantibodies against factor VIII): diagnosis, causes and treatment options. Not specific to prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | DDAVP given to a patient with congenital combined factor V and factor VIII deficiency. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | Cesarean section managed with factor VIII concentrates in a pregnant woman with combined factor V and VIII deficiency. |

None of these papers addresses prothrombin (factor II) deficiency directly.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02139502 | VASOPRESSIN INJECTION, USP | VASOPRESSIN | Marketed |
| 02247938 | VASOPRESSIN INJECTION USP | VASOPRESSIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Both licences are valid single-ingredient products.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 potential interactions. Examples of the main ones, by severity:
  - **Major**: dolasetron, cisapride, papaverine, macimorelin
  - **Moderate**: famotidine, epinephrine, loperamide, chlorpropamide, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, promethazine, cilostazol, heparin, and others
  - **Minor**: metronidazole

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the supporting papers concern other factor deficiencies, and the known mechanism (raising factor VIII and von Willebrand factor) does not apply to prothrombin deficiency.

**To proceed, the following is needed:**
- The approved indications and the package insert warnings and contraindications from Health Canada
- Mechanism of action data, and evidence of any effect on prothrombin levels
- Preclinical or clinical evidence specific to congenital prothrombin deficiency
- A review of the major drug interactions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available for vasopressin in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vasostrict (vasopressin) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1147beb-743e-4c62-8927-91192447f8b8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

