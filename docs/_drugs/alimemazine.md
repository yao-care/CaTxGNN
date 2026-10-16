---
layout: default
title: Alimemazine
parent: Moderate Evidence (L3-L4)
nav_order: 34
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Alimemazine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Urticaria, allergic rhinitis, angioedema, pharyngitis, common cold…"
---

# Alimemazine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Alimemazine: From Urticaria and Allergic Conditions to Allergic Urticaria

## One-Sentence Summary

Alimemazine (trimeprazine) is a phenothiazine-class antihistamine, originally used for allergic conditions such as urticaria, allergic rhinitis, angioedema and the common cold.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **no clinical trials and no publications** were found in the data compiled for this report, so support is mechanistic and indirect only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urticaria, allergic rhinitis, angioedema, pharyngitis, common cold, and related allergic conditions (the Canadian licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known pharmacology, alimemazine is a phenothiazine-class H1-receptor antagonist. Blocking H1 receptors on skin blood vessels and sensory nerves can plausibly reduce histamine-driven wheals and itching.

Allergic urticaria is a subtype of urticaria, which alimemazine already covers in general. The prediction is therefore better seen as a refinement of an existing indication than as true repurposing. The very high TxGNN score most likely reflects this existing label.

Other predicted indications are weaker:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Cold urticaria | 99.96% | L4 | H1 blockade is a reasonable approach, but second-generation antihistamines are guideline-preferred over a sedating phenothiazine. |
| IgE responsiveness, atopic | 99.60% | L5 | A predisposition rather than a treatable disease. H1 blockade may ease symptoms but does not change sensitization. |
| Nasal cavity disease | 99.60% | L5 | Too broad. The score likely reflects the existing rhinitis and cold indications. |
| Recalcitrant atopic dermatitis | 99.59% | L5 | Itch is largely non-histaminergic. Sedation may help night-time sleep only. Biologics and JAK inhibitors are the relevant comparators. |
| Acute laryngopharyngitis | 99.54% | L5 | Overlaps with the existing pharyngitis and cold indications. Benefit would be symptomatic and uncertain. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01926306 | PANECTYL | Not listed | Not listed |
| 01926292 | PANECTYL | Not listed | Not listed |

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for these.

- **Disease associations flagged as contraindications (knowledge graph, not label text):** these are drawn from drug-disease contraindication links and should be confirmed against the official label.
  - Cardiac and conduction: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, coronary thrombosis.
  - Blood pressure and autonomic: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - Haematological: neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anaemia (including macrocytic), hemoglobinopathy.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm.
  - Other: liver disease, gallbladder disease, hyperglycaemia, benign prostatic hyperplasia, substance abuse/dependence, female breast carcinoma, obesity disorders (including monogenic obesity).
- **Drug Interactions:** 100 interactions were identified; 20 are shown in the compiled data.
  - **Major:** bupropion, potassium citrate.
  - **Moderate (examples):**
    - Anticholinergics: atropine, hyoscyamine, glycopyrronium.
    - Opioid and GI motility: morphine, loperamide.
    - Antidiabetics: acarbose, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide.
    - Other: epinephrine, famotidine, clarithromycin, lorcaserin, and the laxatives bisacodyl, picosulfuric acid and polyethylene glycol with electrolytes.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria is a subtype of an indication alimemazine already covers, and the score reflects that overlap rather than new evidence. There are no trials or publications for any predicted indication, and the safety profile includes many knowledge-graph contraindications, notably cardiac (QT prolongation) and haematological concerns. Second-generation antihistamines are generally preferred in the closest predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Approved indication text, dosage forms and manufacturer details for the two PANECTYL DINs
- Mechanism of action data from DrugBank
- Clinical or observational evidence for allergic or cold urticaria specifically, and a comparison with second-generation antihistamines
- A cardiac (QT) and haematological safety review, plus a review of the major drug interactions
- Clarification of whether a new indication adds value beyond the existing urticaria label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

