---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 280
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Dicyclomine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Irritable bowel syndrome"
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antimuscarinic antispasmodic, originally used for irritable bowel syndrome (IBS) and related gastrointestinal conditions.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome (also listed in the knowledge graph: Clostridium difficile colitis, neurocirculatory asthenia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

*Note: The Canadian licence records compiled for this report contain no approved indication text. The original indications above come from the TxGNN knowledge graph.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dicyclomine is an antimuscarinic/antispasmodic agent that relaxes smooth muscle. Its use in irritable bowel syndrome is established, and mechanistically it may relieve smooth-muscle spasm in other settings.

Cauda equina syndrome often presents with bladder and bowel dysfunction. A theoretical link exists only for symptom management, such as bowel spasm or detrusor overactivity. However, anticholinergic activity could **worsen urinary retention**, which is a core feature of this condition.

Cauda equina syndrome is a surgical emergency caused by nerve root compression. No mechanism is established by which dicyclomine would treat the underlying cause. The high score (0.997) is a computational prediction only.

A second prediction, **neurogenic bladder** (listed under an obsolete ontology term), has a score of 99.50%. Antimuscarinics are an established class for neurogenic detrusor overactivity, so a class-level rationale is plausible. However, there is no dicyclomine-specific evidence, and better-characterized agents such as oxybutynin and tolterodine are used for this purpose. The obsolete term should be mapped to a current ontology term before further assessment.

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
| 02366088 | JAMP-DICYCLOMINE HCL | Not specified | Not specified |
| 02391619 | JAMP-DICYCLOMINE HCL | Not specified | Not specified |
| 00557102 | RIVA-DICYCLOMINE | Not specified | Not specified |

All three licences are valid single-ingredient products. No cancelled licences were found.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease relationships, not package insert text):
  - Eye: angle-closure (closed-angle) glaucoma
  - Urinary and prostate: benign prostatic hyperplasia, pyoureter
  - Liver and kidney: liver disease, liver failure, hepatic coma, hepatic encephalopathy, kidney disease, gallbladder disease
  - Gastrointestinal: gastric ulcer
  - Blood: thrombocytopenia, neutropenia, agranulocytosis, anemia (including macrocytic anemia)
  - Cardiovascular: hypertension, hypertensive disorder, coronary artery disease
  - Metabolic: porphyria (inherited porphyria, porphyrin metabolism disease)
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
  - Sleep and respiratory: obstructive sleep apnea, sleep apnea syndrome, congenital central hypoventilation syndrome (Haddad syndrome)
- **Drug Interactions**: 100 interactions were recorded, and the first 20 reviewed are mostly Moderate, with a few Minor. Main ones include:
  - Other anticholinergics and antimuscarinics: hyoscyamine, aclidinium, amitriptyline
  - Antihistamines: chlorpheniramine, acrivastine, phenyltoloxamine
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Others: ethanol, loperamide, amantadine, galantamine, botulinum toxin type A, acetylcholine, acebutolol
  - Minor: acetaminophen, hydrochlorothiazide
- **Specific concern for the predicted indication**: Anticholinergic effects may worsen urinary retention, and the large interaction burden calls for caution.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or publications behind it. Cauda equina syndrome is a surgical emergency with nerve compression as the cause, and dicyclomine's anticholinergic action may worsen urinary retention, a core feature of the condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently unavailable and blocking safety screening)
- Mechanism of action data for dicyclomine
- Approved indication text and dosage forms for the Canadian licences
- Any clinical or preclinical evidence for dicyclomine in cauda equina syndrome
- If neurogenic bladder is pursued instead, mapping of the obsolete disease term to a current one, plus a comparison against established antimuscarinics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

