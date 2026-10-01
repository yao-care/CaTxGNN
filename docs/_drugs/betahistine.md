---
layout: default
title: Betahistine
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Betahistine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Betahistine: From Vertigo (Ménière-type) to Restless Legs Syndrome

## One-Sentence Summary

Betahistine is a histamine-analogue drug that is marketed for vertigo of inner-ear origin, and the Canadian label text was not included in the data provided.
The TxGNN model ranks **restless legs syndrome** as its top new indication, but this prediction has **0 clinical trials** and **0 publications** behind it.
Better-supported predictions exist for other vestibular conditions (see the table below the literature section).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vertigo of the Ménière type (from the pack's rationale text; Canadian label wording not provided) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 98.51% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Betahistine is described as a weak histamine H1 agonist and a stronger H3 antagonist. Blocking H3 receptors raises histamine turnover, which is thought to improve inner-ear blood flow and help the brain compensate after vestibular damage.

The link to restless legs syndrome is weak. Histamine signalling is loosely tied to sleep-wake regulation, but nothing in the provided data supports an RLS-specific mechanism or clinical signal. The prediction is a statistical output of the knowledge graph. It should be treated as a hypothesis, not a finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for restless legs syndrome.

---

## Literature Evidence

Currently no related literature available for restless legs syndrome.

### Other Predicted Indications for Betahistine (for context)

The pack ranks several other indications with real evidence. This is where most of the supporting data sits.

| Predicted Indication | Score | Evidence Level | Trials | Publications | Pack Recommendation |
|------|------|------|------|------|------|
| Peripheral vertigo | 98.07% | L2 | 4 | 20 | Proceed with Guardrails |
| Active vestibular Ménière disease | 98.34% | L3 | 0 | 19 | Proceed with Guardrails |
| Vertigo, benign recurrent, 2 | 97.78% | L3 | 4 | 20 | Research Question |
| Otosclerosis | 98.19% | L4 | 0 | 2 | Research Question |
| Active cochleovestibular and active cochlear Ménière disease | 98.34% | L4 | 0 | 0 | Research Question |
| Age-related hearing impairment | 97.93% | L5 | 0 | 0 | Hold |
| Kir6.2-deficiency hyperinsulinism and familial hyperinsulinemic hypoglycemia | 97.78% / 97.32% | L5 | 0 | 0 | Hold |

Key points from this evidence:
- **Peripheral vertigo** has a completed Phase 2 RCT (NCT03908567, n=124) of AM-125, an intranasal betahistine formulation. It also has RCT, Cochrane and meta-analysis literature, including the BEMED trial (PMID 26797774) and a 2016 Cochrane review (PMID 27327415). The pack notes the evidence is mixed, so efficacy is not established.
- **Ménière disease** evidence is mostly reviews, observational studies and one cat PK/PD study, with no RCT under that node.
- **"Vertigo, benign recurrent, 2"** is matched to BPPV trials and papers, not the genetically defined entity, so this mapping needs curation.
- The two hyperinsulinism predictions look like knowledge-graph artifacts with no plausible mechanism.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02538121 | MINT-BETAHISTINE |
| 02243878 | SERC |
| 02538148 | MINT-BETAHISTINE |
| 02519682 | M-BETAHISTINE |
| 02544938 | NRA-BETAHISTINE |

Only 5 of the 19 authorizations are listed in the data. Dosage form and approved-indication text were not provided for any of them.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold** (for restless legs syndrome)

**Rationale:**
The RLS prediction rests on model output alone, with no trials, no literature and no supported mechanism. Any repurposing effort should focus on the vestibular indications, where peripheral vertigo is the strongest candidate at L2 with guardrails.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Canadian label indication text for each DIN, to confirm the original indication
- For RLS: any primary evidence, such as a literature search or preclinical rationale
- For peripheral vertigo: full-text review of the RCTs and the Cochrane review, to decide whether the evidence level can be upgraded, and curation of the disease-label mapping
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

