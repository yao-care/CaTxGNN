---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 1
---

# Fexofenadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Fexofenadine is a peripheral histamine H1 antihistamine, originally used for allergic rhinitis, allergic conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis, idiopathic urticaria |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, fexofenadine is a selective peripheral histamine H1 receptor antagonist. Blocking this receptor can reduce histamine-mediated itching, vasodilation and surface inflammation of the eye.

Fexofenadine already has established use in allergic eye conditions (atopic, papillary and vernal conjunctivitis). This gives a plausible bridge to another inflammatory conjunctival condition such as rosacea conjunctivitis, which is the likely basis for the model's high score.

There are important limits to this link. Ocular rosacea is driven mainly by meibomian gland dysfunction, tear film instability, microbial and Demodex factors, and innate immune and neurovascular dysregulation, rather than mainly by histamine. An antihistamine would therefore likely give only partial symptom relief at best. The TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02521245 | ALLEGRA HIVES | Not specified | Not specified |
| 02231462 | ALLEGRA 12 HOUR | Not specified | Not specified |
| 02242819 | ALLEGRA 24 HOUR | Not specified | Not specified |
| 02239853 | ALLEGRA-D | Not specified | Not specified |

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (these come from knowledge-graph relationships, not package insert text): hypertension/hypertensive disorder, kidney disease, pyoureter, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease, coronary atherosclerosis, arteriosclerosis/atherosclerosis, angle-closure glaucoma, hyperthyroidism, Graves disease and thyrotoxicosis. Some of these may relate to combination products such as ALLEGRA-D, which contains a decongestant; this should be verified against the label.
- **Drug Interactions**: 100 interactions were found in total, and 20 are listed in the data compiled for this report.
  - Moderate: eliglustat, eluxadoline, rolapitant, and the antacids magnesium hydroxide, aluminum hydroxide, magaldrate and magnesium carbonate.
  - Minor: clarithromycin, miconazole, clotrimazole.
  - Unclassified: calcitriol, doxycycline, cimetidine, levocarnitine, epinephrine, dolasetron, dicyclomine, chlorhexidine, famotidine, acetylsalicylic acid.

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.85%), but there are no clinical trials or publications for this indication (Evidence Level L5). The disease mechanism of ocular rosacea is mostly not histamine-driven, so benefit is likely limited to symptom relief.

**To proceed, the following is needed:**
- A systematic search of clinical trials and literature on antihistamines in ocular rosacea or blepharoconjunctivitis
- Mechanism of action data for fexofenadine
- Health Canada package insert warnings and contraindications, plus dosage form and approved indication text for each DIN
- Assessment of whether an oral antihistamine is appropriate or a topical ocular route is needed, since route compatibility is still pending
- Comparison against current standard care for ocular rosacea (eyelid hygiene, tear supplements, topical or oral antibiotics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

