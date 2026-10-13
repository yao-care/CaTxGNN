---
layout: default
title: Propafenone
parent: Model Prediction Only (L5)
nav_order: 776
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Propafenone: From Atrial Fibrillation and Ventricular Tachycardia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Propafenone is an antiarrhythmic originally used to treat atrial fibrillation and ventricular tachycardia. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials** and only **3 publications** were found. None of those publications shows a benefit, and they instead describe mania and psychiatric adverse events linked to propafenone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; ventricular tachycardia (the Canadian licence records contain no indication text) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propafenone is an established antiarrhythmic with proven use in atrial fibrillation and ventricular tachycardia. No data compiled for this report links that activity to a therapeutic effect in mania.

The retrieved literature points the other way. A 1985 case report describes **mania secondary to propafenone**. The authors speculated that its chemical relationship to bupropion might give it antidepressant-like activity that could trigger affective side effects. A 2001 case report describes an organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar disorder. A 2020 review covers harmful interactions between antipsychotics and cardiovascular drugs in patients with bipolar disorder or schizophrenia.

The high model score is therefore not corroborated by any clinical evidence of benefit. The available signal is a safety concern in the opposite direction of the predicted indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Mania secondary to propafenone, described as a previously unrecognized complication. The authors suggest possible antidepressant-like activity. |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | Organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar affective disorder. |
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacol Rep | Review of adverse interactions between antipsychotics and cardiovascular drugs in patients with bipolar disorder or schizophrenia. It does not show a therapeutic effect of propafenone. |

---

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|------|
| 00603708 | RYTHMOL | Valid |
| 00603716 | RYTHMOL | Valid |
| 02243324 | APO-PROPAFENONE | Valid |
| 02243325 | APO-PROPAFENONE | Valid |
| 02457164 | MYLAN-PROPAFENONE | Valid |
| 02457172 | MYLAN-PROPAFENONE | Valid |

All 6 authorizations are single-ingredient products. Dosage form and approved indication text were not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications and cautions (from a knowledge graph, not label text):** The TxGNN knowledge graph links propafenone to the following conditions:
  - Cardiac rhythm and ischaemia: long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary artery disease and atherosclerosis.
  - Blood pressure and organ function: hypotension, kidney disease, liver disease, gallbladder disease.
  - Electrolytes, blood and nerve–muscle disorders: potassium deficiency, myasthenia gravis, neutropenia and agranulocytosis (including congenital forms), hemoglobinopathy.
- **Drug interactions:** 100 interactions were identified.
  - **Major:** dolasetron and eliglustat.
  - **Moderate (examples):** clarithromycin, levofloxacin, ondansetron, palonosetron, bupropion, cimetidine, famotidine, aprepitant, loperamide, alosetron and lorcaserin.
  - **Minor:** metronidazole.
- **Psychiatric safety signal:** The literature above reports mania and psychosis associated with propafenone or its interactions.

Official package insert warnings were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no supporting trials and no evidence of benefit. The only relevant literature reports mania and psychiatric adverse events with propafenone, which is the opposite of the predicted indication.

**To proceed, the following is needed:**
- A plausible mechanistic rationale for propafenone in mania, with MOA data.
- Any preclinical or clinical evidence showing a benefit rather than harm.
- Review of the Health Canada package insert warnings and contraindications.
- A comparison against other predicted indications for this drug. For example, catecholaminergic polymorphic ventricular tachycardia has mechanistic and case-level support and may be a more promising direction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

