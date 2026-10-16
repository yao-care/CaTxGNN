---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 836
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Scopolamine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Motion sickness, irritable bowel syndrome, peptic ulcer disease…"
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Scopolamine: From Motion Sickness and Gastrointestinal/Ocular Conditions to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is an antimuscarinic drug originally used for conditions such as motion sickness, irritable bowel syndrome, peptic ulcer disease, uveitis and cycloplegia (pupil dilation and eye-focus paralysis for eye examination).
The TxGNN model predicts it may be effective for **cauda equina syndrome**, with a very high model score.
However, **no clinical trials and no publications** currently support this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness, irritable bowel syndrome, peptic ulcer disease, uveitis, cycloplegia, and others (the Canadian licence records list no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, scopolamine is a non-selective muscarinic antagonist. Its established uses (motion sickness, gastrointestinal spasm, ocular cycloplegia) all rely on blocking acetylcholine receptors.

Cauda equina syndrome often causes bladder dysfunction, such as urinary retention or overflow incontinence. Antimuscarinics act on bladder detrusor muscarinic receptors, which is the likely source of the model's association. However, the link is weak. Antimuscarinics would be expected to worsen urinary retention, and they do not address the underlying cause, which is nerve root compression requiring urgent surgical decompression. The prediction is a model score only, with no supporting clinical data.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Neurogenic bladder (obsolete ontology term) | 99.98% | Mechanism plausible (M3 blockade), but scopolamine has strong CNS effects and is a poor choice compared with bladder-selective agents |
| 3 | Papillary conjunctivitis | 99.98% | Driven by mechanical irritation and allergy; muscarinic antagonism does not target these pathways |
| 4 | Atopic conjunctivitis | 99.80% | Standard care is antihistamines, mast cell stabilizers and corticosteroids; anticholinergics may worsen ocular dryness |
| 5 | Rosacea conjunctivitis | 99.40% | Reduced secretion may aggravate dry eye and meibomian gland dysfunction |
| 6 | Vernal conjunctivitis | 99.08% | Only a symptomatic cycloplegic effect is plausible; not disease-modifying |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242811 | Scopolamine Hydrobromide Injection | Injection | Not listed in the data |
| 02242810 | Scopolamine Hydrobromide Injection | Injection | Not listed in the data |

---

## Safety Considerations

- **Disease contraindications (from knowledge-graph associations, not label text):** Associations were found with hypertension, liver failure and liver disease, epilepsy, COPD, gastric ulcer, anxiety and neurotic disorders, porphyria, kidney disease, pancreatitis, gallbladder disease, thrombocytopenia, neutropenia and agranulocytosis, open-angle glaucoma, psychotic and other mental disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, and hepatic coma. Benign prostatic hyperplasia is particularly relevant to the bladder-related predictions, since antimuscarinics can worsen urinary retention.
- **Drug Interactions:** The data compiled for this report show 100 recorded interactions, most rated Moderate. Examples among those reviewed include:
  - Opioids and analgesics: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergics and antihistamines: hyoscyamine, aclidinium, chlorpheniramine, acrivastine, phenyltoloxamine, amitriptyline
  - Other agents: ethanol, loperamide, amantadine, phenylephrine, acebutolol, acetylcholine, botulinum toxin type A
  - Minor interactions: acetaminophen and hydrochlorothiazide

  Additive anticholinergic and central nervous system depressant effects are the main concern.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions rest on model scores alone (Evidence Level L5), with no clinical trials or publications. For the top prediction, cauda equina syndrome, the mechanism is weak and potentially harmful because of the risk of worsening urinary retention. The neurogenic bladder prediction is mechanistically plausible but is outperformed by approved bladder-selective antimuscarinics and carries a relevant CNS adverse-effect burden.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Health Canada package insert warnings and contraindications (parsed from the PDF), which block safety screening
- Indication text and dosage form for the two Canadian licences
- A targeted literature and trial search for scopolamine in neurogenic bladder, the most plausible of the predicted indications
- A review of whether the obsolete ontology term can be mapped to a current disease definition
- Assessment of route compatibility, since only injectable products are authorised in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

