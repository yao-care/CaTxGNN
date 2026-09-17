---
layout: default
title: Thyroid Porcine
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
---

# Thyroid Porcine
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

# Thyroid, Porcine: From Hypothyroidism to Migraine Disorder

## One-Sentence Summary

> Thyroid, porcine (desiccated thyroid extract) is traditionally used as hormone replacement therapy for **hypothyroidism**. The TxGNN model predicts it may be effective for **Migraine Disorder**,
> but currently **no clinical trials** and **no published literature** support this specific prediction — the signal is a pure computational output with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (based on general pharmacological knowledge of desiccated thyroid extract; no drug-level regulatory indication text is available in the evidence pack) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity data gap). Based on general pharmacological knowledge, Thyroid, porcine is a natural desiccated thyroid hormone extract (containing T4/T3), and its efficacy as replacement therapy in hypothyroidism is well established. The proposed link to migraine rests on an indirect physiological hypothesis: epidemiological observations suggest hypothyroidism is associated with an increased incidence of migraine, so thyroid hormone replacement could theoretically reduce migraine burden in hypothyroid patients. However, there is **no direct clinical or preclinical evidence** demonstrating that porcine thyroid extract treats migraine, and no literature or trials were retrieved for this specific disease pairing.

A closer look at the other nine TxGNN-ranked predictions for this drug reinforces the need for caution rather than confirming the migraine signal. Two related migraine subtypes (migraine with brainstem aura, migraine susceptibility) rely on the same unproven hypothesis or on literature that is actually about epilepsy genetics/neuroinflammation — not thyroid pharmacology — and appears to be a knowledge-graph artifact from shared neurological nodes. More critically, rank 10 (**hyperthyroidism**) is flagged in the evidence itself as a likely *false positive in the wrong direction*: administering exogenous thyroid hormone to a hyperthyroid patient would worsen thyrotoxicosis, making this a pharmacological contraindication rather than a treatment indication. The 20 "supporting" citations for that pairing are basic-science studies using porcine thyroid tissue as a laboratory model, not clinical evidence of therapeutic benefit. This pattern across the top-10 list suggests the model is generating associations driven by entity co-occurrence (e.g., "thyroid," "neurological") rather than genuine mechanistic or clinical signal, which should lower confidence in the migraine prediction as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada warnings and contraindications data are marked as a Blocking data gap (DG001) and could not be retrieved for this evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction is supported only by a TxGNN model score (Evidence Level L5) with zero clinical trials and zero literature citations — there is no empirical basis to advance this candidate. Review of the broader prediction set for this drug also surfaces a likely direction-reversed/contraindicated pairing (hyperthyroidism) and mechanistically irrelevant literature (epilepsy genetics), indicating the model's outputs for this drug warrant additional scrutiny before any is prioritized.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank or another authoritative source (DG002)
- TFDA/Health Canada package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Primary literature or preclinical studies directly evaluating thyroid hormone status/replacement in migraine pathophysiology
- Confirmation of Canadian market/DIN status, since none currently exist for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

