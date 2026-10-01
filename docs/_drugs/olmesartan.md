---
layout: default
title: Olmesartan
parent: Model Prediction Only (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
---

# Olmesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Olmesartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker (ARB). The Canadian license records in the Evidence Pack carry no indication text, so hypertension is assumed from the drug class.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (coronary vasospasm), but **no clinical trials and no publications** were retrieved for this indication.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records (hypertension assumed from the ARB drug class) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olmesartan is an AT1 receptor blocker. Its efficacy in blood pressure control is established, and mechanistically it may be applicable to coronary vasospasm.

Angiotensin II is a strong vasoconstrictor and can impair endothelial function. Blocking the AT1 receptor could reduce these effects, which may matter in coronary vasospasm.

This link is plausible but unsupported. Calcium channel blockers and nitrates are the established therapy for Prinzmetal angina. The high TxGNN score (0.998) is a model prediction only and should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorizations are listed below. Dosage form and approved indication text are not included in the records.

| DIN | Product Name |
|---------|------|
| 2461315 | PMS-OLMESARTAN |
| 2481057 | OLMESARTAN |
| 2469820 | GLN-OLMESARTAN |
| 2499258 | NRA-OLMESARTAN |
| 2442205 | TEVA-OLMESARTAN |

---

## Safety Considerations

Please refer to the package insert for safety information.

Drug interaction queries returned no results.

Literature retrieved for other predicted indications documents ARB-associated fetal toxicity (fetopathy, oligohydramnios), which is a class concern for any new use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Prinzmetal angina has only a model prediction behind it (L5). No trials or publications were found, and effective standard therapies already exist.

Other predicted indications for olmesartan have more supporting material and could be reviewed first:
- **Migraine disorder (L3):** small prospective study and a class-level systematic review.
- **Pulmonary hypertension (L4):** three animal studies.

**To proceed, the following is needed:**
- A literature and trial search specific to olmesartan and coronary vasospasm
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications
- Indication text and dosage forms for the Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

