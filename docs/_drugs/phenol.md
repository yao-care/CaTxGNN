---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 729
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Phenol: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "PHENOL"
predicted_indications: ["acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "dry eye syndrome"]
---

# Phenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Phenol: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Phenol is a chemical agent (antiseptic, neurolytic, caustic) whose original indication in the knowledge graph is dermatitis.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenol is known as a topical or local chemical agent used as an antiseptic, neurolytic and caustic, and its link to dermatitis comes from the knowledge graph.

Acrodermatitis chronica atrophicans is the late skin manifestation of Borrelia infection and is treated with antibiotics. Phenol has no known antimicrobial role in this setting, so no mechanistic link can be established. The high score (99.95%) is most likely a computational association with skin disease, not evidence of benefit.

Other top-ranked predictions show the same pattern. They include neonatal and amyopathic dermatomyositis, pediatric connective-tissue-disease-associated interstitial lung disease, familial hydroa vacciniforme, severe nonproliferative diabetic retinopathy and dry eye syndrome. None has clinical trials, and none has a plausible mechanism. The one partial exception is **acne keloid**, which has indirect evidence from phenol chemical peels (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for acrodermatitis chronica atrophicans.

For context, the other predicted indications have the following literature:

- **Acne keloid (rank 5, L4):** One 2007 publication, [PMID 17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) (J Dermatol), describes a modified phenol peel (Exoderm) for facial wrinkles, acne scars and other skin problems in Asian patients. It is a clinical series and indirect evidence only. It is not specific to acne keloid, and caustic injury could worsen keloid formation.
- **Dry eye syndrome (rank 8, L5):** The 20 retrieved publications concern dry eye biology and other agents (berberine, evodiamine, chrysin, nanoparticles). None evaluates phenol, and phenol is caustic to ocular tissue.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00298409 | PHENOL SALINE INJ | Not specified | Not specified |
| 00298417 | GLYCERINATED PHENOL SALINE | Not specified | Not specified |
| 02157292 | BLISTEX DCT | Not specified | Not specified |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** The knowledge graph links phenol to contraindications in many conditions. The main groups are:
  - Cardiac and vascular: sudden cardiac arrest, heart conduction disease, atrioventricular block, peripheral arterial disease, intermittent claudication.
  - Metabolic and organ: diabetes mellitus, diabetic ketoacidosis, liver disease, gallbladder disease, respiratory failure, active peptic ulcer disease, appendicitis.
  - Haematological and neurological: neutropenia, agranulocytosis, epilepsy.
  - Infections and cancers: herpes simplex, herpes zoster, cytomegalovirus infection, anogenital HPV infection, common wart, progressive multifocal leukoencephalopathy, cancer, lymphoma and related lymphoid tumours.
  - Skin: dermatitis, which is also the original indication and therefore needs clarification.
- **Other safety concerns noted in the evaluation:** Phenol is caustic and irritating, and systemic exposure carries toxicity concerns. Neonatal and ocular use are of particular concern.

No drug interaction data were found. For label warnings, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies only on a model score. It has no clinical trials or publications and no plausible mechanism, since the condition is an antibiotic-treated infectious skin disease. Safety concerns are also substantial.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Any published or registered evidence for phenol in acrodermatitis chronica atrophicans
- Route and formulation compatibility assessment, since the licensed products' dosage forms and indications are not specified
- If a lead is wanted, a separate review of acne keloid, where phenol-peel evidence is indirect, with a safety assessment first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

