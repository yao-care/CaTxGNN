---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From COPD/Asthma to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a long-acting β2-adrenergic receptor agonist (LABA) bronchodilator, globally used for COPD and asthma maintenance therapy; it is not currently marketed in Canada. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this ranking is supported by **zero clinical trials** and **zero publications** — the evidence pack itself flags it as having no known mechanistic connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Canada (drug not marketed); globally indicated as a LABA bronchodilator for COPD/asthma |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for indacaterol in this evidence pack. Based on known information, indacaterol is a selective β2-adrenergic receptor agonist (LABA class), and its bronchodilator efficacy in COPD and asthma has been well established (see the "bronchial disease" candidate later in this evidence pack, which reflects this on-label mechanism).

For NSIAD specifically, however, the evidence pack's own rationale is explicit that no such connection exists: NSIAD is a rare disease caused by gain-of-function mutations in the vasopressin V2 receptor, and there is no known pharmacological relationship between V2-receptor-mediated free water retention and β2-adrenergic agonism. The TxGNN score of 99.54% (rank 8745) is therefore a pure knowledge-graph prediction with no clinical or mechanistic corroboration — it should be treated as a hypothesis-generating signal only, not as a plausible repurposing lead at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Indacaterol is not currently marketed in Canada under this evidence pack's regulatory data (0 DINs on file, market status "Not marketed"). No product authorizations are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at decision stage S0 with evidence level L5 — a high TxGNN score unsupported by any clinical trials, literature, or plausible mechanism of action. The repurposing rationale in the evidence pack itself concludes there is no known biological link between indacaterol's β2-agonist activity and NSIAD pathophysiology.

**To proceed, the following is needed:**
- Confirmed drug mechanism of action (MOA) data from DrugBank or product labeling
- A pharmacological plausibility review connecting β2-adrenergic signaling to V2-receptor-driven antidiuresis (currently absent)
- Any preclinical, case-report, or real-world evidence specific to NSIAD
- Canada regulatory/market data, since indacaterol is not currently marketed (0 DINs)

**Note:** This same evidence pack contains a substantially better-supported candidate — "bronchial disease" (rank 7, TxGNN score 99.18%) — with evidence level **L1**, decision stage **S3**, and a "Proceed with Guardrails" recommendation, backed by 37 clinical trials (including multiple completed Phase 3 RCTs with 1,000+ participants) and 20 publications. That candidate aligns directly with indacaterol's established LABA mechanism and may warrant its own separate evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

