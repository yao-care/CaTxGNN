---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cyclopentolate: From Ophthalmic Cycloplegia/Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a topical antimuscarinic eye drug, used by class to dilate the pupil and temporarily paralyse eye focusing.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records (by class knowledge: ophthalmic cycloplegic/mydriatic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on class knowledge, cyclopentolate is a topical antimuscarinic (anticholinergic) agent. Its use in the eye is well established, but the licence records do not state the approved indication text.

The link to cauda equina syndrome is weak. This condition is a compressive neurosurgical emergency. An antimuscarinic could at most help secondary bladder symptoms and cannot treat the compression. The high score (0.995) is a graph-based signal that probably reflects proximity to neurogenic bladder and related nodes in the knowledge graph.

Two other predictions share this class-level logic:
- **Neurogenic bladder** (score 99.40%; the ontology term is flagged "obsolete" and needs mapping to a current concept). Systemic antimuscarinics such as oxybutynin reduce detrusor overactivity through M2/M3 blockade.
- **Irritable bowel syndrome** (score 99.27%). Antimuscarinic antispasmodics such as dicyclomine and hyoscyamine reduce smooth muscle contractility.

For both, better-studied approved alternatives already exist. Cyclopentolate is formulated only for ophthalmic use, so systemic exposure, dose and safety for these uses have not been characterised.

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
| 626627 | ODAN-CYCLOPENTOLATE | Not listed | Not listed |
| 2148382 | MINIMS CYCLOPENTOLATE HYDROCHLORIDE | Not listed | Not listed |
| 252506 | CYCLOGYL | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

Class-level cautions from the prediction rationale: ophthalmic dosing gives minimal systemic exposure, but systemic anticholinergic effects (urinary retention, CNS effects, constipation, especially in children) could worsen bladder dysfunction. This is particularly relevant in cauda equina syndrome. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score, with no clinical trials, no literature and no supported mechanism. For cauda equina syndrome, an anticholinergic could worsen bladder function. The bladder and IBS predictions are plausible only at class level, and approved antimuscarinics already cover them.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Approved indication text, dosage forms and routes for the three DINs
- Mapping of the "obsolete neurogenic bladder" term to a current disease concept
- A literature and trial search on systemic or non-ophthalmic antimuscarinic use for any of the three predicted indications, plus a systemic exposure and safety assessment, before further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

