---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Cimetidine: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Gastric ulcer, gastroesophageal reflux disease, duodenal ulcer…"
monitor_inn: "CIMETIDINE"
predicted_indications: ["active peptic ulcer disease", "gastrojejunal ulcer", "peptic ulcer perforation", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Cimetidine: From Gastric Ulcer to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist originally used to treat gastric and duodenal ulcers, reflux disease and gastric hypersecretory conditions.
The TxGNN model predicts it may be effective for **Smouldering systemic mastocytosis**,
but **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, gastroesophageal reflux disease, duodenal ulcer, Zollinger-Ellison syndrome and related conditions (the Canadian licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cimetidine is known as a competitive H2-receptor antagonist. It blocks histamine on gastric parietal cells and reduces acid secretion, which is the basis of its ulcer and reflux uses.

Systemic mastocytosis is already listed among cimetidine's original indications in the knowledge graph. In mast cell disease, excess histamine release drives gastric hypersecretion and gastrointestinal symptoms, and H2 blockade can control these. The high score most likely reflects this existing link and the shared mast cell and histamine biology, rather than new evidence specific to the smouldering subtype.

Any benefit would be symptomatic, such as acid and GI symptom control. It would not modify the underlying disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00584215 | CIMETIDINE | Not specified | Not specified |
| 00487872 | CIMETIDINE | Not specified | Not specified |

Both licences are valid single-ingredient products.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are model-graph associations, not label text): liver disease, gallbladder disease, impaired renal function, and gastric cancer or neoplasm (including diffuse gastric adenocarcinoma, linitis plastica and gastric carcinoma).
- **Drug Interactions**: 100 interactions were identified in total. Examples among those listed:
  - Moderate: paclitaxel, fentanyl, acalabrutinib, lidocaine, acebutolol, dihydrocodeine, codeine, tramadol, nifedipine, alfentanil
  - Minor: dolutegravir, zidovudine, acetaminophen, ketorolac, ibuprofen, ethinylestradiol, albendazole, ethanol, alendronic acid, cholecalciferol

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for smouldering systemic mastocytosis has no supporting trials or publications (L5). It most likely echoes the existing systemic mastocytosis indication, and any benefit would be symptomatic only.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Clinical or observational evidence in smouldering systemic mastocytosis specifically
- Review of the interactions with other drugs, and of the knowledge-graph contraindications, in this patient population

---

### Other Predicted Indications (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Active peptic ulcer disease | 99.79% | L3 | Already an approved use, so not a repurposing opportunity. One placebo-controlled study (PMID 7034155) and several reviews. |
| Gastrojejunal ulcer | 99.77% | L3 | Extension of the ulcer indication. Literature is general and not specific to this condition. |
| Peptic ulcer perforation | 99.77% | L4 | Case reports of perforation during cimetidine therapy suggest no protection. Perforation is a surgical emergency. |
| Lymphoadenopathic mastocytosis with eosinophilia | 99.76% | L5 | No evidence supplied. At best symptomatic control. |
| Duodenogastric reflux | 99.49% | L4 | Only physiological studies, with no evidence of clinical benefit. |
| Duodenal obstruction | 99.44% | L4 | A single case-level report (PMID 361048). Mechanical obstruction needs endoscopic or surgical management. |
| Acne | 99.33% | L4 | Plausible anti-androgenic and immunomodulatory link, but only reviews and no controlled data. Classified as a research question. |
| Abnormality of glucagon secretion | 99.14% | L5 | The only record is an unrelated Meckel's diverticulum imaging study. Unsupported. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

