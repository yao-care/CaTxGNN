---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Asthma"
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Salbutamol: From Asthma and Bronchial Disease to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting bronchodilator, originally used to treat asthma and bronchial disease.
The TxGNN model predicts it may be effective for **papillary conjunctivitis** with a very high score, but **no clinical trials and no publications** were found to support this specific prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma; bronchial disease |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 15 of 15) |
| Number of DINs | 15 (valid: 15) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, salbutamol is a beta-2 adrenergic agonist. Its efficacy in asthma and bronchial disease is well established, and it acts by relaxing airway smooth muscle.

Papillary conjunctivitis is an allergic or inflammatory eye condition, so it is not obviously related to airway obstruction. The only mechanistic argument is indirect. Beta-2 agonists have shown mast-cell-stabilizing and anti-inflammatory effects in conjunctival tissue in preclinical settings, which could matter in allergic eye disease. The compiled data contains no study that tests this for papillary conjunctivitis, so the link remains speculative.

The strength of the model score should not be read as clinical evidence. The prediction has not been checked against any human data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Salbutamol is widely marketed in Canada, with 15 valid single-ingredient licences and no cancelled ones. Dosage form and approved-indication text were not available in the compiled data. Five main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02208229 | PMS-SALBUTAMOL | Not listed | Not listed |
| 02326450 | TEVA-SALBUTAMOL HFA | Not listed | Not listed |
| 02243115 | VENTOLIN DISKUS | Not listed | Not listed |
| 02241497 | VENTOLIN HFA | Not listed | Not listed |
| 02213486 | VENTOLIN RESPIRATOR SOLUTION | Not listed | Not listed |

Other authorizations include an intravenous infusion solution (Ventolin I.V.) and combination-type inhalation products with ipratropium (Combivent Respimat and others). No ophthalmic salbutamol product appears in the list.

---

## Safety Considerations

- **Contraindications (knowledge-graph disease associations, not label text):** hypertension and hypertensive disorders, long QT syndrome (including familial), epilepsy, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, metabolic acidosis, sudden cardiac arrest, heart conduction disease, myocardial ischemia and coronary artery disease, hyperthyroidism (Graves disease, thyrotoxicosis), angle-closure glaucoma and ocular hypertension, benign prostatic hyperplasia, and bladder neck obstruction.
- **Drug Interactions:** 100 interactions were identified. Examples:
  - **Moderate:** epinephrine, clarithromycin, cisapride, famotidine, isometheptene, diethylpropion, bisacodyl, castor oil.
  - **Moderate (glucose-lowering drugs):** acarbose, alogliptin, albiglutide, acetohexamide, chlorpropamide, canagliflozin, dapagliflozin.
  - **Minor (corticosteroids):** hydrocortisone, dexamethasone, betamethasone, budesonide, beclomethasone dipropionate.
- **Eye-specific caution:** angle-closure glaucoma and ocular hypertension appear among the associated contraindications. This deserves particular attention for any ocular use.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials or publications for papillary conjunctivitis. The only mechanistic support is indirect preclinical data on conjunctival effects of beta-2 agonists. Glaucoma-related contraindications also raise an ocular safety question.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to support the proposed link.
- Preclinical or early human studies of salbutamol in papillary conjunctivitis.
- An ocular formulation and route assessment, since no ophthalmic product exists in the Canadian list.
- Package insert warnings and contraindications from Health Canada, which are currently missing.

**Other predictions in the same analysis have stronger support:**
- **Obstructive lung disease (L1):** Phase 3 evidence exists for ipratropium/salbutamol in COPD (NCT02177253, n=1118). This is largely a label extension rather than true repurposing.
- **Bronchitis/bronchiolitis (L2) and anaphylaxis (L3):** both are research questions. Evidence for bronchiolitis is weak or negative, and the anaphylaxis Phase 3 trial was terminated early with 24 participants.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

