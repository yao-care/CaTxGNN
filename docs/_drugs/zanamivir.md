---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 835
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor (NAI) originally used for the treatment of Influenza A and B. The TxGNN model predicts a high score for **Pyelonephritis** as a new indication, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale explicitly flags the association as an unsupported knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza A and B (neuraminidase inhibitor class; per literature evidence in this pack) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for zanamivir is not available in this evidence pack (MOA: Data Gap). However, literature retrieved for a secondary candidate in this pack confirms that zanamivir is a neuraminidase inhibitor — "the medicines of choice against influenza A or B" — acting on the viral surface glycoprotein neuraminidase to block viral release and spread.

Despite a high TxGNN score (99.84%), the evidence pack's own mechanistic assessment explicitly states that **no pharmacological bridge exists** between a viral neuraminidase inhibitor and pyelonephritis, which is a bacterial infection of the renal pelvis unrelated to viral neuraminidase activity. The high score is judged to most likely reflect an indirect association in the knowledge-graph embedding space (e.g., clustering through generic "infection/inflammation" disease nodes) rather than a genuine pharmacological mechanism.

The second-ranked candidate in this pack, disorder of tyrosine metabolism (TxGNN score 99.02%), shows the same pattern: three retrieved publications were manually reviewed and found to have no substantive relevance to tyrosine metabolism — they instead discuss oseltamivir resistance mutations (H275Y/H274Y) and neuraminidase inhibition assay methodology. This is consistent with a keyword-matching artifact (shared terms like "neuraminidase" and adjacent metabolic language) rather than true supporting evidence. Both candidates in this pack are therefore assessed as low-confidence, model-only signals without biological or clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Zanamivir currently has no authorized Drug Identification Numbers (DINs) and is not marketed in Canada per this evidence pack (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both candidate indications in this pack (pyelonephritis and disorder of tyrosine metabolism) are supported only by a raw TxGNN embedding score (L5, S0) with no corroborating clinical trials or relevant literature, and the mechanistic rationale explicitly identifies the top candidate as biologically implausible. There is no basis to advance either indication at this time.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data for zanamivir (currently a Data Gap)
- TFDA/Health Canada product monograph warnings and contraindications (currently a Data Gap; blocking S1 safety review)
- Independent literature or preclinical search targeted specifically at pyelonephritis and tyrosine metabolism disorder to confirm or rule out the KG-embedding signal
- Canadian regulatory/market status confirmation, since zanamivir currently has zero DINs on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

