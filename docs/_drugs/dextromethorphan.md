---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 274
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Dextromethorphan"
predicted_indications: ["acute laryngopharyngitis", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Allergic Rhinitis and Related Upper Respiratory Conditions to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a centrally acting cough suppressant, originally associated with allergic rhinitis, vasomotor rhinitis, pharyngitis, the common cold and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The high score appears to reflect closeness to existing upper respiratory indications rather than a genuine new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Dextromethorphan is generally known as a centrally acting antitussive that works as an NMDA receptor antagonist and sigma-1 receptor agonist. This general pharmacology is not backed by mechanism data in the compiled material.

"Nasal cavity disease" is a broad parent category that overlaps heavily with conditions the drug is already linked to, such as allergic rhinitis, vasomotor rhinitis, rhinitis and the common cold. The very high score is most likely explained by this closeness within the knowledge graph. It is not an independent signal.

No separate mechanistic rationale for nasal cavity disease is supported by the data. This prediction should be read as a broad category overlapping existing indications, not as a true repurposing opportunity.

### Other Predicted Indications (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Acute laryngopharyngitis | 99.98% | L5 | Nearly equivalent to existing pharyngitis/common cold indications; limited novelty. Symptomatic cough relief is plausible but unproven. |
| Faucial diphtheria | 99.36% | L5 | Bacterial toxin-mediated infection; the drug has no antimicrobial or antitoxin activity. Not clinically credible. |
| Trigeminal autonomic cephalalgia | 99.32% | L5 | The most plausible as a research hypothesis (NMDA antagonism and sigma-1 modulation in pain and central sensitization), but no supporting evidence. |
| Cervical disc degenerative disorder | 99.30% | L5 | No clear mechanistic link; at most speculative symptom relief of chronic pain. |
| Allergic urticaria | 99.25% | L5 | Likely driven by proximity to allergic rhinitis; the drug is not an antihistamine or mast-cell stabilizer. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

There are 20 valid single-ingredient licences in Canada. Dosage form and approved indication text are not available for any of them. The main authorizations are:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01944738 | BENYLIN EXTRA STRENGTH DRY COUGH | Not available | Not available |
| 02511320 | BUCKLEY'S DRY COUGH EXTRA STRENGTH | Not available | Not available |
| 02534754 | DRY COUGH RELIEF EXTRA STRENGTH | Not available | Not available |
| 01928775 | BALMINIL DM (3MG/ML SUCROSE FREE) | Not available | Not available |
| 02549360 | DAYQUIL KIDS HONEY | Not available | Not available |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph contraindication edges, not label text)**: The knowledge graph links the drug to a long list of conditions, including:
  - Cardiovascular: hypertension, hypotension, long QT syndrome (including familial), torsades de pointes
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Respiratory: COPD, bronchitis
  - Gastrointestinal: peptic and gastric ulcer, inflammatory bowel disease, pancreatitis
  - Endocrine: diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, hypothyroidism
  - Others: epilepsy, benign prostatic hyperplasia, thrombocytopenia

  These are graph-derived signals and should be verified against the official label.

- **Drug Interactions**: 100 interactions were recorded. The major-level interactions shown are:
  - Serotonergic and anorectic agents: dexfenfluramine, fenfluramine, lorcaserin, sibutramine
  - 5-HT3 antagonists: dolasetron, granisetron, ondansetron, palonosetron

  Moderate-level interactions include:
  - Bupropion and cimetidine
  - Morphine, liposomal morphine and opium
  - Dronabinol and nabilone
  - Eliglustat, glycerol phenylbutyrate, mazindol, metoclopramide and phentermine

  The drug's dependence on CYP2D6 metabolism is also a safety consideration, especially where serotonergic or CYP2D6-inhibiting drugs are co-administered.

Package insert warnings and contraindications for the Canadian products were not available. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model-level support (L5), with no clinical trials or publications. Its high score largely reflects overlap with existing upper respiratory indications rather than new biology. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank to allow a proper mechanistic-link analysis
- Health Canada package insert warnings and contraindications, which are required before safety screening can proceed
- Approved indication text and dosage forms for the Canadian licences, to clarify what is already labelled
- A literature and trial search for the nasal cavity indication specifically, to separate genuine novelty from overlap with existing indications
- If a novel direction is wanted, consider prioritising trigeminal autonomic cephalalgia as a research hypothesis, with careful review of the drug interaction and CYP2D6 considerations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

