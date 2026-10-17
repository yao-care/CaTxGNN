---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 847
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sevoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Health Canada licence data compiled for this report…"
monitor_inn: "SEVOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sevoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Sevoflurane is a volatile (inhaled) anesthetic marketed in Canada under three licences. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but the prediction rests on the model score alone: **no clinical trials** and **no publications** were found for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada licence data compiled for this report (sevoflurane is a general anesthetic) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sevoflurane is a volatile anesthetic used to induce and maintain general anesthesia. Its mechanistic relevance to Prinzmetal angina is theoretical only.

Volatile anesthetics have some vasodilatory and calcium-channel-modulating effects that could relate to coronary vasospasm, the cause of Prinzmetal angina. However, no trials or literature support this link. Sevoflurane is a short-term, inhaled, hospital-administered anesthetic, not a chronic anti-anginal therapy, so its practical fit with this condition is poor.

The high score (0.998) reflects a pattern in the knowledge graph and should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For context, the other predicted indications in the data also have little support. The strongest literature signal was for tendinitis (9 articles) and was limited to perioperative anesthesia studies in which sevoflurane served as the anesthetic or comparator, not as a treatment. Fibromyalgia, migraine disorder and inclusion body myositis each had a single case report or cohort study about anesthetic management. Six other predictions (Tourette syndrome, idiopathic granulomatous myositis, myositis fibrosa, nephrogenic syndrome of inappropriate antidiuresis, trichotillomania and Prinzmetal angina itself) had no evidence at all.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02265974 | SEVOFLURANE | Not specified | Not specified |
| 02307766 | SEVOFLURANE | Not specified | Not specified |
| 02172763 | SEVORANE AF | Not specified | Not specified |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The TxGNN knowledge graph links sevoflurane with contraindication edges for epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, hypotensive disorder, malignant hyperthermia of anesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri, intracranial hypertension, Duchenne muscular dystrophy, Becker muscular dystrophy, muscular dystrophy and proteinuria. Hypotension is relevant to any cardiovascular use.
- **Drug Interactions**: 100 interactions were identified. Major interactions include **epinephrine**, **dolasetron** and **cisapride**. Moderate interactions include famotidine, loperamide, morphine, clarithromycin, levofloxacin, ondansetron, palonosetron, exenatide and several bowel-preparation laxatives (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate, lactitol, lactulose, castor oil). Metronidazole is a minor interaction.

Warnings and contraindications from the Canadian package insert were not available for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications for Prinzmetal angina. Sevoflurane's short-term inhaled use does not fit a chronic anti-anginal role, and the knowledge graph flags hypotension-related cautions.

**To proceed, the following is needed:**
- Mechanism of action data and a specific, testable hypothesis for coronary vasospasm
- Preclinical or early clinical evidence of benefit in Prinzmetal angina
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for each DIN
- A feasibility assessment of whether an inhaled anesthetic could be delivered in a way suited to this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

