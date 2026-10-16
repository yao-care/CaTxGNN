---
layout: default
title: Ribociclib
parent: Moderate Evidence (L3-L4)
nav_order: 804
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-13
description: "Ribociclib: predicted new indication Myeloid leukemia (evidence level L4). Approved use: Hormone receptor-positive, HER2-negative breast cancer"
monitor_inn: "RIBOCICLIB"
predicted_indications: ["myeloid leukemia", "thrombocytopenia", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets"]
---

# Ribociclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Ribociclib: From Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Ribociclib (Kisqali) is a CDK4/6 inhibitor marketed in Canada and, based on the literature compiled for this report, used in hormone receptor-positive, HER2-negative breast cancer.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but this rests on **0 clinical trials** and **1 relevant preclinical publication**.
This is a research question, not a clinical recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormone receptor-positive, HER2-negative breast cancer (inferred from the literature; the Canadian licence text compiled for this report is blank) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ribociclib is a selective CDK4/6 inhibitor. CDK4/6 drives cells through the G1-to-S phase of the cell cycle, and blocking it halts proliferation of cells that depend on this pathway.

This gives a plausible link to myeloid leukemia, where rapidly dividing blasts may rely on the same cell-cycle machinery. A 2020 preclinical study (PMID 32560251) reported that CDK4/6 inhibitors can target pharmacokinetic drug resistance in acute myeloid leukemia cells. This resistance is linked to ABCB1 and ABCG2 transporters and to drug-metabolising enzymes.

The evidence is in vitro only. No clinical efficacy data for ribociclib in myeloid leukemia were identified. The prediction is therefore a hypothesis worth testing in the laboratory, not a proven benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical (in vitro) | Cancers | CDK4/6 inhibitors may target pharmacokinetic drug resistance (ABCB1/ABCG2 transporters, carbonyl reducing enzymes) in AML cells |

A second publication retrieved for this prediction (PMID 41641105) is a case report of vulvar adenocarcinoma and is not relevant to myeloid leukemia, so it is not listed.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02473569 | KISQALI | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | High. Neutropenia, leukopenia, thrombocytopenia and anaemia are widely reported with CDK4/6 inhibitors |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function, ECG/QT interval and electrolytes (standard practice for this class) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Haematological toxicity**: The literature identifies myelosuppression as the most common toxicity of CDK4/6 inhibitors. This includes an umbrella review of meta-analyses (PMID 38288438), pharmacovigilance analyses (PMIDs 39123221, 37895811) and a network meta-analysis (PMID 38753541). This is particularly important in a disease like leukemia, where marrow function is already compromised.
- **Other reported adverse events**: Pneumonitis (case report, PMID 34248473) and visual hallucination (case report, PMID 37306182).
- **Drug Interactions**: 100 interactions were found in the DDI screening, of which 20 are listed in the data compiled for this report. Most are Moderate, and two are **Major**:
  - Clarithromycin (Major)
  - Dolasetron (Major)
  - Moderate examples: famotidine, hydrocortisone, metformin, pioglitazone, loperamide, aprepitant, dexamethasone, cimetidine

Health Canada package insert warnings and contraindications were not available. They must be obtained before any safety screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is supported only by a single in vitro study, with no clinical trials. Ribociclib's marked myelosuppression is a significant safety concern in leukemia. The other top-ranked predictions (thrombocytopenia and related inherited platelet disorders) are likely a reversed signal. Ribociclib causes thrombocytopenia rather than treating it, and no supporting trials or literature exist for them.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication text for DIN 02473569
- Further preclinical work in AML models (cell lines, patient-derived samples), including combinations with standard induction therapy
- A review of myelosuppression risk specific to leukemia patients before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

