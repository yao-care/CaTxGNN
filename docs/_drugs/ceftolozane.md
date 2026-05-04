---
layout: default
title: Ceftolozane
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozane: From Complicated Urinary Tract Infections to Ureaplasma urethritis

## One-Sentence Summary

Ceftolozane is a novel cephalosporin antibiotic used internationally (in combination with tazobactam) for complicated urinary tract infections (cUTI) and complicated intra-abdominal infections (cIAI), with FDA and EMA approval since 2014–2015.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, however this is supported by **0 clinical trials** and **0 publications** — representing model-level prediction only.
Critically, the mechanistic rationale actively argues against this prediction: Ureaplasma organisms lack the peptidoglycan cell wall that beta-lactam antibiotics require to exert their effect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Canada; approved internationally for complicated UTI and complicated intra-abdominal infections (ceftolozane/tazobactam combination) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, ceftolozane is a fifth-generation cephalosporin that exerts its antibacterial effect by binding to penicillin-binding proteins (PBPs) on bacterial cell walls, thereby inhibiting peptidoglycan cross-linking and causing cell lysis. It is typically combined with the beta-lactamase inhibitor tazobactam (as Zerbaxa®) to combat drug-resistant Gram-negative organisms such as *Pseudomonas aeruginosa*.

However, the TxGNN prediction of Ureaplasma urethritis presents a fundamental mechanistic mismatch. *Ureaplasma urealyticum* belongs to the class Mollicutes, which entirely lacks a peptidoglycan cell wall — the very target through which beta-lactam antibiotics (including ceftolozane) work. Without PBP targets, ceftolozane has no established mechanism of action against Ureaplasma, and current standard-of-care guidelines recommend macrolides (azithromycin) or tetracyclines (doxycycline) for this pathogen.

This prediction most likely arises from indirect knowledge graph node connections (e.g., ceftolozane → urinary tract infections → urethritis → Ureaplasma urethritis) rather than a genuine mechanistic or clinical relationship. The high TxGNN score (99.89%) reflects graph topology proximity, not biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ceftolozane and Ureaplasma urethritis.

---

## Literature Evidence

Currently no related literature available for ceftolozane and Ureaplasma urethritis.

---

## Canada Market Information

Ceftolozane is currently not approved or marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Appendix: Additional Predicted Indications (Ranks 2–10)

The following table summarizes the remaining TxGNN-predicted indications and their scientific viability, to provide a complete picture of the model's output for this drug.

| Rank | Disease | Score | Evidence Level | Assessment |
|------|---------|-------|---------------|------------|
| 1 | Ureaplasma urethritis | 99.89% | L5 | **Biologically implausible** — Ureaplasma lacks cell wall (no PBP target for beta-lactams) |
| 2 | Gonococcal urethritis | 99.89% | L5 | **Theoretically possible** but no MIC data or clinical trials; not in CDC/WHO STI guidelines |
| 3 | Uterine inflammatory disease | 99.88% | L5 | **Incomplete coverage** — PID requires anaerobic cover; ceftolozane alone is insufficient |
| 4 | Xanthogranulomatous pyelonephritis | 99.88% | L4 | **Indirect support only** — ceftolozane/tazobactam approved for cUTI; XGP usually requires surgery |
| 5 | Polyclonal hyperviscosity syndrome | 99.52% | L5 | **Biologically implausible** — immunoglobulin disorder unrelated to antibacterial mechanism |
| 6 | Hyperamylasemia | 99.52% | L5 | **Biologically implausible** — metabolic marker; beta-lactams may cause this as a side effect, not treat it |
| 7 | Urogenital tuberculosis | 99.50% | L5 | **Biologically implausible** — MTB expresses BlaC beta-lactamase; ceftolozane not active against MTB |
| 8 | Congenital analbuminemia | 99.44% | L5 | **Biologically implausible** — genetic albumin synthesis disorder; graph artifact via protein-binding nodes |
| 9 | Blood group incompatibility | 99.22% | L5 | **Biologically implausible** — ABO/Rh immune reaction; no antibacterial relevance |
| 10 | Premalignant hematological disease | 99.11% | L5 | **Biologically implausible** — clonal stem cell disorder; ceftolozane has no antiproliferative mechanism |

> **Note:** Rank 4 (xanthogranulomatous pyelonephritis) is the only prediction with any indirect mechanistic support, given the established approval of ceftolozane/tazobactam for complicated UTI/acute pyelonephritis. However, XGP is a rare chronic condition typically requiring nephrectomy, and no XGP-specific trials exist. This could be considered a **Research Question** for case-report or retrospective study design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Ureaplasma urethritis) is biologically implausible — ceftolozane's mechanism of action requires a peptidoglycan cell wall target that Ureaplasma organisms do not possess. Across all 10 predicted indications, 9 are rated L5 (model prediction only) with no supporting evidence, and several carry mechanistic arguments actively opposing the prediction. The one indication with marginal support (xanthogranulomatous pyelonephritis, L4) is a rare surgical condition where antibiotics play only an adjunctive role.

**To proceed, the following is needed:**

- **MOA data (DG002):** Obtain complete mechanism of action from DrugBank API to enable proper mechanistic link analysis
- **Canada regulatory data:** Investigate Health Canada DPD for any ceftolozane/tazobactam (Zerbaxa®) submissions or compassionate-use programs
- **Re-rank predictions:** Consider filtering out predictions with explicit mechanistic counter-evidence before investing in further evidence collection
- **Refocus on rank 4 (XGP) if pursuing UTI space:** Conduct a targeted literature search for case reports of ceftolozane use in complex/recurrent pyelonephritis to assess if a retrospective case series is feasible
- **Gonococcal urethritis (rank 2):** If pursuing STI indications, commission in vitro MIC susceptibility testing for *N. gonorrhoeae* as a minimal pre-clinical data requirement before any clinical hypothesis generation

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

