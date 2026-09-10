---
layout: default
title: Polyethylene Glycol 400
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 2
---

# Polyethylene Glycol 400
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Polyethylene Glycol 400: From Pharmaceutical Excipient to Bronchitis

## One-Sentence Summary

Polyethylene Glycol 400 (PEG 400, DrugBank DB11077) is not marketed in Canada as an independent therapeutic product and has no registered original indication — it is primarily used as a pharmaceutical excipient/solvent. The TxGNN model predicts a possible link to **Bronchitis** with a very high raw score, but on inspection the 5 "supporting" clinical trials are actually studies of a *different* drug (MIRCERA®, methoxy‑polyethylene glycol‑epoetin beta) for renal anemia — a false-positive match caused by the shared substring "polyethylene glycol." **No genuine clinical trial or literature evidence currently supports this prediction.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — PEG 400 has no registered original indication; it is used primarily as a pharmaceutical excipient/solvent |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, MOA: Data Gap). PEG 400 has no known pharmacological mechanism that would plausibly explain an effect on bronchitis — it is a small-molecule polymer used as a solvent, vehicle, or osmotic agent in formulations, not an active therapeutic agent in its own right.

More importantly, the clinical trial "evidence" retrieved for this candidate is a **data-quality artifact, not supporting evidence**. All 5 trials listed under this prediction actually study MIRCERA® (methoxy‑polyethylene glycol‑epoetin beta), a PEGylated erythropoiesis-stimulating biologic used to correct renal anemia in chronic kidney disease patients. This is an entirely different drug entity from PEG 400 (a small-molecule excipient); the two share only the text string "polyethylene glycol," which appears to have caused a false-positive match during evidence retrieval or knowledge-graph embedding. None of the retrieved trials studied bronchitis or any respiratory condition.

Given the absence of a mechanistic rationale and the fact that the only retrieved trials are mismatched to both the drug and the disease, this prediction should currently be treated as a **model-score-only hypothesis (L5)** rather than one with any corroborating clinical evidence.

---

## Clinical Trial Evidence

⚠️ **Note:** The trials below were retrieved by automated search but are **not actually relevant** — they study a different drug (MIRCERA®) for a different condition (renal anemia), not PEG 400 for bronchitis. Listed here for transparency/audit purposes only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00559273](https://clinicaltrials.gov/study/NCT00559273) | Phase 3 | Completed | 307 | **Not relevant** — studies MIRCERA vs. darbepoetin for renal anemia in non-dialysis CKD, not PEG 400/bronchitis |
| [NCT01519947](https://clinicaltrials.gov/study/NCT01519947) | Phase 4 | Completed | 87 | **Not relevant** — studies altitude effect on MIRCERA dosing for renal anemia |
| [NCT01422824](https://clinicaltrials.gov/study/NCT01422824) | N/A (Observational) | Completed | 185 | **Not relevant** — observational safety/efficacy study of MIRCERA in hemodialysis patients |
| [NCT01379963](https://clinicaltrials.gov/study/NCT01379963) | N/A (Observational) | Completed | 780 | **Not relevant** — retrospective hemoglobin-level reporting in MIRCERA-treated renal anemia patients |
| [NCT01309295](https://clinicaltrials.gov/study/NCT01309295) | N/A (Observational) | Completed | 250 | **Not relevant** — prospective efficacy/safety study of MIRCERA in CKD pre-dialysis/dialysis patients |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Polyethylene Glycol 400 is currently **not marketed** in Canada as a standalone licensed product under this evidence pack (0 DINs on file).

---

## Additional Candidate Indication (Rank 2): Congenital Ichthyosiform Erythroderma

The evidence pack also includes a second, lower-confidence candidate:

| Item | Content |
|------|------|
| Predicted Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| Clinical Trials | Currently no related clinical trials registered |
| Literature | Currently no related literature available |
| Recommended Decision | Hold |

**Rationale:** PEG 400 is commonly used as an emollient/humectant excipient in topical formulations, which offers a plausible (but unproven) theoretical basis for symptomatic skin-hydration benefit in ichthyosis. However, there is no direct pharmacological or clinical evidence of therapeutic effect on this condition — the link is model-score only.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/label warnings, contraindications, and DDI data are currently unavailable — DG001, flagged as Blocking for safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (bronchitis) is not supported by genuine evidence — the retrieved clinical trials are a false-positive match to a different drug (MIRCERA®) caused by string overlap in "polyethylene glycol," and no relevant literature exists.
- The second candidate (congenital ichthyosiform erythroderma) has a weak theoretical rationale (topical emollient use) but zero clinical trial or literature support.
- Both candidates remain at Evidence Level L5 (model prediction only) and are correctly staged at S0 by the scoring pipeline.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/Health Canada label warnings and contraindications before any safety screening can begin.
- Resolve DG002: obtain confirmed mechanism-of-action data for PEG 400 as a small molecule (distinct from PEGylated biologics).
- Re-run evidence retrieval with stricter drug-entity disambiguation to exclude PEGylated biologic products (e.g., MIRCERA, pegfilgrastim, PEG-interferon) from matching on the "polyethylene glycol" substring.
- If pursuing the ichthyosis hypothesis, seek dermatology-specific preclinical or case-level evidence on PEG-based emollient formulations before advancing past S0.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

