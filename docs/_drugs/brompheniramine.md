---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 131
evidence_level: L5
indication_count: 2
---

# Brompheniramine
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

# Brompheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation antihistamine originally used for allergic rhinitis, the common cold, allergic conjunctivitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **Allergic Urticaria** (a second prediction, **Cold Urticaria**, is also listed), but **no clinical trials and no publications** currently support this specific direction. The support is indirect, based on drug class and overlap with its existing urticaria use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other listed uses: vasomotor rhinitis, common cold, atopic/vernal/papillary conjunctivitis, familial dermatographia, urticaria, angioedema) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only; no trials or publications. The data compiled for this report assigns L4 on the basis of class-level mechanistic reasoning.) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, brompheniramine is a first-generation H1-receptor antagonist of the alkylamine class. Its efficacy in histamine-driven allergic conditions is established, and mechanistically it may be applicable to allergic urticaria.

Allergic urticaria is mediated by mast cells and histamine, so H1 blockade is a coherent mechanism. The very high TxGNN score most likely reflects the overlap with brompheniramine's existing urticaria and angioedema indications. It probably does not indicate a genuinely new repurposing opportunity.

The second prediction, **cold urticaria** (score 99.55%), is a physical (inducible) urticaria in which mast-cell degranulation follows cold exposure. H1 antihistamines are standard therapy, and first-generation agents have historically been used. However, current guidelines favour second-generation non-sedating antihistamines. This limits the practical value of a first-generation agent that carries sedation and anticholinergic burden.

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
| 02394707 | ROBITUSSIN CHILDREN'S COUGH & COLD BEDTIME | Not specified | Not specified |

---

## Safety Considerations

**Contraindications from the knowledge graph (not label text):** The TxGNN knowledge graph links brompheniramine to contraindications or cautions in the following conditions:

- **Cardiovascular:** hypertension and hypertensive disorder, hypotensive disorder, coronary artery disease, myocardial infarction, coronary thrombosis
- **Hepatic, renal and gastrointestinal:** liver failure, liver disease, kidney disease, pyoureter, pancreatitis, gallbladder disease, gastric ulcer, peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- **Respiratory and neurological:** epilepsy, chronic obstructive pulmonary disease (including severe early-onset COPD)
- **Endocrine and metabolic:** hypothyroidism, myxedema, congenital hypothyroidism, diabetes mellitus, diabetic ketoacidosis
- **Other:** benign prostatic hyperplasia, ocular hypertension, hemoglobinopathy, substance abuse/dependence

**Drug interactions:** 100 interactions were identified. The main ones are:

- **Major:** potassium chloride and potassium citrate
- **Moderate (anticholinergic agents, additive effects):** hyoscyamine, atropine, scopolamine, dicyclomine, clidinium, glycopyrronium, mepenzolate, methscopolamine, propantheline
- **Moderate (CNS or opioid agents, additive sedation):** morphine (including liposomal), opium, loperamide, eluxadoline, dronabinol, nabilone
- **Moderate (other):** metoclopramide

Label warnings and contraindications from the Health Canada package insert were not available. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically coherent, but it largely duplicates an existing labeled use (urticaria and angioedema). No trials or publications support the specific subtypes. For cold urticaria, second-generation non-sedating antihistamines are preferred, and brompheniramine adds sedation and anticholinergic burden.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Brompheniramine-specific clinical or observational evidence for allergic urticaria or cold urticaria
- Comparison against second-generation antihistamines to show a meaningful added value
- Review of the anticholinergic and sedation risks, particularly in older adults and in patients with the conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

