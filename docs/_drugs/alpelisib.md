---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Alpelisib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the Canadian license data"
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
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

## Alpelisib: From an Unspecified Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Alpelisib is a PI3K-alpha inhibitor marketed in Canada as PIQRAY. The approved indication text is not available in the data compiled for this report, but the clinical trials found are in breast and ovarian cancer.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and only **1 publication** (a case report of alpelisib-induced interstitial lung disease, which is a safety signal rather than evidence of benefit).
The prediction currently rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Canadian license data (trials in the evidence set are in HR+/HER2- PIK3CA-mutated advanced breast cancer and ovarian cancer) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 (indirect and mechanistic only; no trials, one case report) |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for alpelisib: "Alpelisib is an inhibitor of phosphatidylinositol-3-kinase (PI3K) with inhibitory activity predominantly against PI3Kα. Gain-of-function mutations in the gene encoding the catalytic α-subunit of PI3K (PIK3CA) lead to activation of PI3Kα and Akt-signaling, cellular transformation and the generation of tumors in in vitro and in vivo models." ([DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b), label version 2026-10-28; accessed 2026-11-19.) Based on known information, alpelisib is a selective PI3K-alpha inhibitor used in oncology, and its efficacy in PIK3CA-mutated breast cancer has been studied in Phase 3 trials.

Mechanistically, PI3K/AKT/mTOR signalling has been implicated in pulmonary vascular remodelling, which is a feature of pulmonary hypertension. This gives a plausible biological rationale, but it is a hypothesis only. No study in the data compiled for this report tests alpelisib in pulmonary hypertension.

The only publication is a case report of alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. This is a pulmonary adverse event, so it raises a safety question for lung-related use rather than supporting benefit. The high TxGNN score (0.9903, rank 15,925) is a model prediction and does not substitute for clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | Journal of Oncology Pharmacy Practice | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer; a pulmonary safety signal, not evidence of therapeutic benefit |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02497069 | PIQRAY | ALPELISIB | Marketed |
| 02497077 | PIQRAY | ALPELISIB | Marketed |
| 02497085 | PIQRAY | ALPELISIB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-alpha inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood glucose is a key parameter (a Phase 2 trial studied metformin to prevent alpelisib-associated hyperglycaemia); also refer to the package insert for haematological, liver and renal monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and the 20 listed in the compiled data are all rated Moderate. Many involve glucose-lowering agents, which fits the hyperglycaemia risk seen with alpelisib. Examples include metformin, pioglitazone, acarbose, alogliptin, albiglutide, dulaglutide, exenatide, glimepiride, glipizide, chlorpropamide, acetohexamide, canagliflozin, dapagliflozin, empagliflozin and ertugliflozin. Others include dexamethasone, bupropion, alosetron, dronabinol and fidaxomicin.
- **Pulmonary signal**: A published case report describes alpelisib-induced interstitial lung disease, which is a relevant concern in a lung-related indication.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials, and the only publication is a case report of a lung adverse event rather than benefit. The mechanistic rationale (PI3K signalling in vascular remodelling) is plausible but untested. The label warnings and contraindications were not available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (a blocking gap)
- Mechanism of action data from DrugBank
- Preclinical evidence (for example, pulmonary hypertension animal models) testing PI3K-alpha inhibition
- Assessment of the interstitial lung disease risk in the context of a pulmonary vascular indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

