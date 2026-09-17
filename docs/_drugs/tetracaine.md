---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 766
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is an ester-type local anesthetic used topically/mucosally and via spinal/regional block, based on the clinical trial and literature evidence collected in this pack. TxGNN's top-ranked prediction suggests possible efficacy for **Acrodermatitis Chronica Atrophicans**, a Borrelia-associated chronic dermatologic condition — but this is currently supported by **zero clinical trials** and **zero publications**, and the model's own generated rationale flags the association as a likely knowledge-graph structural artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Health Canada regulatory data (drug currently unlicensed). Known use, per collected evidence, is topical/mucosal and spinal/regional local anesthesia (ester-type) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.93% (rank 1884 of all model predictions) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the evidence collected, tetracaine is an ester-type local anesthetic; its efficacy in topical/mucosal anesthesia (e.g., pre-procedural analgesia for laser and dermatologic procedures) and spinal/regional anesthesia is well established in the literature retrieved for other candidates in this pack. However, sodium-channel blockade — tetracaine's known mechanism as a local anesthetic — has **no established pathophysiological link** to acrodermatitis chronica atrophicans, which is a late-stage cutaneous manifestation of chronic *Borrelia* infection driven by immune-mediated dermal atrophy and fibrosis.

The model's own generated rationale for this candidate explicitly states that the high TxGNN score likely reflects **structural similarity among dermatology-related nodes in the knowledge graph**, rather than a genuine drug-mechanism-to-disease inference. There is no supporting clinical trial, no case report, and no preclinical rationale connecting a local anesthetic to Borrelia-driven dermal pathology. This prediction should be treated as a false-positive candidate typical of L5 (model-only) scores rather than a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Tetracaine currently has **no active marketing authorization in Canada** (0 DINs; market status: Not Marketed). No product licenses were available to extract dosage form or approved-indication information.

---

## Safety Considerations

Please refer to the package insert for safety information (no structured warnings, contraindications, or DDI data are currently available for this drug in this evidence pack).

**⚠️ Notable safety signal identified elsewhere in this evidence pack:** While not part of the top-ranked prediction, a separate candidate indication in this pack (*cauda equina syndrome*, rank 8, TxGNN score 99.55%) is supported by **9 independent publications** — but all of them identify tetracaine (particularly hyperbaric spinal/intrathecal administration at high concentration) as a **causative agent of neurotoxicity and cauda equina syndrome**, not as a treatment. This is a reverse-causality artifact (drug-adverse event co-occurrence misread as a therapeutic association) and should be flagged as a **known risk/contraindication signal** for any future spinal anesthesia use of this drug, rather than pursued as a repurposing opportunity.

---

## Other Candidates Screened in This Evidence Pack

For context, this evidence pack screened 9 TxGNN-predicted indications for tetracaine. Only one reached meaningful clinical evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Note |
|------|---------|------|------|------|------|
| 1 | Acrodermatitis chronica atrophicans | 99.93% | L5 | S0 (Hold) | No mechanistic link; likely graph artifact |
| 2 | Neonatal dermatomyositis | 99.92% | L5 | S0 (Hold) | No mechanistic link |
| 3 | Bronchitis | 99.92% | L4 | S0 (Hold) | Single 1988 non-treatment physiology study |
| 4 | Secondary ILD (childhood, connective tissue disease) | 99.92% | L5 | S0 (Hold) | No mechanistic link |
| **5** | **Acne keloidalis nuchae** | 99.91% | **L3** | **S1 (Research Question)** | Real RCT + literature evidence, but tetracaine used as **procedural topical anesthetic**, not disease-modifying therapy |
| 6 | Hydroa vacciniforme, familial | 99.91% | L5 | S0 (Hold) | No mechanistic link |
| 7 | Amyopathic dermatomyositis | 99.90% | L5 | S0 (Hold) | No mechanistic link |
| 8 | Cauda equina syndrome | 99.55% | L4 | S0 (Hold) | ⚠️ **Safety signal, not opportunity** — 9 papers show tetracaine as causative agent |
| 9 | Irritable bowel syndrome | 99.41% | L5 | S0 (Hold) | Speculative mechanism only, no evidence |

None of the nine candidates in this pack currently meets the evidentiary bar for a "Go" or "Proceed with Guardrails" decision; rank 5 is the only one worth a formal research question, and it concerns tetracaine's existing role as a procedural anesthetic rather than a novel indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acrodermatitis chronica atrophicans) has L5 evidence — a TxGNN score with zero supporting clinical trials or literature — and the model's own rationale contradicts mechanistic plausibility. No candidate in this pack currently justifies advancing tetracaine into a formal repurposing pathway; the most credible candidate (acne keloidalis nuchae, L3/S1) reflects tetracaine's established anesthetic-adjunct role rather than a disease-modifying use.

**To proceed, the following is needed:**
- Drug mechanism of action (MOA) data from DrugBank (currently marked Blocking data gap, DG002)
- TFDA/Health Canada product monograph warnings and contraindications (currently marked Blocking, DG001) — particularly given the cauda equina syndrome safety signal identified in the literature
- Confirmation of Canadian licensing/import status, since the drug currently has 0 DINs
- If pursuing rank 5 (acne keloidalis nuchae) as a research question: clarification of whether the "indication" being evaluated is procedural analgesia rather than disease treatment, since this changes the regulatory pathway entirely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

