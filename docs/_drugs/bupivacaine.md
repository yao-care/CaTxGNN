---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Bupivacaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "Bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Bupivacaine: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is an amide local anaesthetic whose original indication in the knowledge graph is dermatitis.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
but **no clinical trials and no publications** currently support this direction. The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, bupivacaine is an amide local anaesthetic that blocks voltage-gated sodium channels and so interrupts nerve conduction.

Acrodermatitis chronica atrophicans is the late skin manifestation of Borrelia infection (Lyme disease), and its standard treatment is antibiotic therapy. Sodium channel blockade does not address the infection. The only plausible role for bupivacaine is symptomatic relief of neuropathic pain, which is speculative. The link to the original indication (dermatitis) is weak, so the high score of 0.992 should be read as a graph-based association and not as evidence of a mechanism.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Neonatal dermatomyositis | 99.15% | Immune-mediated disease. Sodium channel blockade does not address its pathology. Bupivacaine is myotoxic at high concentrations, and neonates are at risk of systemic local anaesthetic toxicity. |
| 3 | Secondary childhood interstitial lung disease associated with a connective tissue disease | 99.11% | No credible mechanism. Bupivacaine would only serve procedural analgesia, which is not disease-modifying. |
| 4 | Amyopathic dermatomyositis | 99.03% | Possible symptomatic relief of skin pain or itch only. Standard therapy relies on immunomodulators and photoprotection. |

All four predictions are at evidence level L5 with a recommendation of Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Bupivacaine has 16 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved indication text are not available in the data compiled for this report. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02241917 | MARCAINE |
| 02443694 | BUPIVACAINE INJECTION BP |
| 02460645 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP |
| 02512424 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP |
| 01976168 | SENSORCAINE |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (graph-derived associations, not label text): hypertension and hypertensive disorder, liver failure and liver disease, kidney disease, epilepsy, COPD, respiratory failure, coronary artery disease, myocardial infarction, atrial fibrillation, sudden cardiac arrest, heart conduction disease, diabetes mellitus and diabetic ketoacidosis, hypothyroidism and myxedema, inflammatory bowel disease, benign prostatic hyperplasia, angle-closure glaucoma, hemoglobinopathy, substance abuse/dependence, and others.
- **Drug interactions:** 56 interactions were identified. Those with a known severity level are **Moderate**: aprepitant and liposomal morphine. Others, including pantoprazole, omeprazole, lansoprazole, vancomycin, atropine, corticosteroids (triamcinolone, prednisone, hydrocortisone, prednisolone, dexamethasone), simvastatin, ondansetron, metronidazole and naloxone, have no severity classification.
- **Specific concerns for the predicted indications:** bupivacaine is myotoxic at high concentrations, which matters in inflammatory muscle disease. Neonates carry a higher risk of local anaesthetic systemic toxicity.

Warnings and contraindications from the Canadian package inserts were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest only on a knowledge-graph score, with no trials or publications. The mechanisms are implausible or speculative, and some indications carry specific safety concerns, such as myotoxicity and neonatal toxicity.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- A systematic literature and trial search for bupivacaine in the predicted conditions, especially pain relief in acrodermatitis chronica atrophicans
- Review of route compatibility and approved indication text for the Canadian products
- A clearer link between the original indication (dermatitis) and each predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

