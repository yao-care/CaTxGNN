---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Aprepitant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aprepitant: From Chemotherapy-Induced Nausea & Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a selective neurokinin-1 (NK1) receptor antagonist approved in multiple major markets for prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV).
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, a rare X-linked disorder of constitutive vasopressin V2 receptor activation.
However, **no clinical trials and no supporting publications** currently exist for this direction, placing this prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CINV/PONV prevention (approved in the US, EU, and other markets; not registered in Canada per available data) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, Aprepitant is a selective, high-affinity antagonist of the neurokinin-1 (NK1) receptor — the primary binding target for the neuropeptide Substance P (SP). Its clinical efficacy in CINV/PONV prevention is well-established and stems from blockade of NK1 receptors in the central emetic pathway (area postrema, nucleus tractus solitarius) and in peripheral tissues.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare, X-linked condition caused by constitutively activating mutations in the *AVPR2* gene, which encodes the vasopressin V2 receptor. The result is persistent, inappropriate water reabsorption in the renal collecting duct despite low or undetectable circulating vasopressin. The biological bridge that TxGNN may be exploiting is a proposed cross-talk between the NK1/Substance P signaling axis and the V2 receptor system: NK1 receptors are expressed in the renal collecting duct alongside V2 receptors, and Substance P has been reported in preclinical models to modulate tubular water transport via NO-dependent and cAMP-dependent mechanisms. Blocking NK1 might therefore theoretically reduce aberrant intracellular cAMP signaling downstream of the constitutively active V2 receptor.

However, this mechanistic bridge has not been experimentally validated in the context of NSIAD, and no human data exist. The prediction is hypothesis-generating at best. The rarity of NSIAD (fewer than 60 published cases worldwide as of 2025) further complicates clinical study design. Significant preclinical work — including in vitro studies using cells expressing gain-of-function AVPR2 variants and in vivo animal models — would be required before any human investigation could be ethically justified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Aprepitant is not currently registered in Canada per the regulatory data available for this report (0 DINs found).

> **Note:** Aprepitant is marketed in the United States (EMEND® capsules and CINVANTI® injectable emulsion, Merck) and the European Union (EMEND®/IVEMEND®). If Health Canada's Drug Product Database contains an entry that was not captured in this query, it should be verified directly. This represents a potential data gap that affects the regulatory feasibility assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both key warnings/contraindications and drug interaction data are currently unavailable in this evidence pack (data gaps DG001 and DG002). Retrieval from the Health Canada product monograph and DrugBank API is required before any clinical feasibility assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high algorithmic confidence score (99.97%) to this prediction, but there are zero clinical trials and zero directly relevant publications to support it. The mechanistic hypothesis — NK1 antagonism modulating constitutively active V2 receptor signaling in NSIAD — is biologically plausible at a theoretical level but entirely unvalidated. Combined with no Canadian market presence and two blocking data gaps (safety and MOA data), this candidate cannot move forward without foundational preclinical evidence.

**To proceed, the following is needed:**
- **Resolve DG001 (Blocking):** Retrieve CINV product monograph warnings and contraindications from Health Canada or the US prescribing information to complete the safety profile
- **Resolve DG002 (High):** Confirm full MOA data via DrugBank API to support mechanistic link analysis
- **Verify Canada regulatory status:** Cross-check the Health Canada Drug Product Database directly to determine whether 0 DINs reflects true non-registration or a data retrieval gap
- **Commission preclinical mechanistic study:** Test whether NK1 antagonism reduces cAMP accumulation or aquaporin-2 trafficking in cell lines expressing constitutively active AVPR2 mutants (e.g., R137C, R137L)
- **NSIAD natural history consultation:** Given the extreme rarity of NSIAD, contact rare disease registries (e.g., RareConnect, European Reference Network) to assess patient availability for any future proof-of-concept trial
- **Review broader NK1-renal axis literature:** A systematic search specifically on Substance P / NK1 in renal water handling (independent of the NSIAD query) may reveal foundational preclinical support not captured in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

