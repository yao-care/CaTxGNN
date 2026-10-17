---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Docusate: predicted new indication Plummer-Vinson syndrome (evidence level L5). Approved use: Constipation disorder"
monitor_inn: "Docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
---

# Docusate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Docusate: From Constipation and Anemia-Related Conditions to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is a stool softener (surfactant laxative), originally used for constipation. It is also linked to several deficiency anemias in the knowledge graph used by the model.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder (the Canadian licence records contain no approved indication text; this indication comes from the knowledge graph, which also lists folic acid deficiency anemia, iron deficiency anemia, hypochromic anemia, deficiency anemia and microcytic anemia) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, docusate is a surfactant stool softener. Its efficacy in constipation is established, and it has no recognised effect on the core problems of Plummer-Vinson syndrome.

Plummer-Vinson syndrome features iron deficiency anemia, dysphagia and esophageal webs. Iron deficiency anemia is among the indications linked to docusate in the knowledge graph. The high score most likely reflects these shared anemia-related nodes rather than a biological mechanism.

Docusate does not treat iron deficiency, dysphagia or esophageal webs. The standard of care is iron repletion, with endoscopic dilation of webs when needed. Both are unrelated to docusate's pharmacology. The prediction should therefore be treated as a computational hypothesis only.

A second predicted indication, vitamin B12- and folate-independent constitutional megaloblastic anemia (score 99.15%), has the same limitation. It has no supporting trials or literature and no plausible mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Docusate has 20 valid single-ingredient licences in Canada. The compiled data contain no dosage form or approved indication text for any of them. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02530538 | NRA-DOCUSATE SODIUM | Not specified | Not specified |
| 01994344 | SOFLAX CAPSULES 100MG | Capsule (per product name) | Not specified |
| 02484226 | COLACE CLEAR | Not specified | Not specified |
| 02526492 | ENEMEEZ | Not specified | Not specified |
| 00870226 | RATIO-DOCUSATE SODIUM | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (graph associations, not label text): peptic ulcer disease, potassium deficiency disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, hemolytic anemia, appendicitis, chronic atrophic gastritis, Leber hereditary optic neuropathy, gastroenteritis.
- **Drug Interactions** (4 found):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor

Please refer to the package insert for label-based warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical or literature evidence (L5). Docusate's pharmacology has no plausible link to Plummer-Vinson syndrome, and the standard of care is unrelated to it.

**To proceed, the following is needed:**
- Mechanism of action data for docusate, to allow a proper mechanistic assessment
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Any preclinical or clinical evidence linking docusate to Plummer-Vinson syndrome, or confirmation that the association is only a knowledge-graph artefact
- Route and dosage form data for the Canadian licences, to assess route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

