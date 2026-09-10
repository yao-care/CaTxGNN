---
layout: default
title: Propylene Glycol
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
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

# Propylene Glycol: From Excipient Use to Predicted Bronchitis Application

## One-Sentence Summary

Propylene glycol (PG, DB01839) has no formally recorded therapeutic indication of its own — it is used almost exclusively as a pharmaceutical excipient (solvent/co-solvent) in inhaled, oral, and topical formulations. The TxGNN model predicts a possible association with **bronchitis** (score 99.90%), but the supporting evidence retrieved so far is **indirect**: the clinical trials found all test *cyclosporine inhalation solution*, not PG itself, and the literature centers on inhaled PG/glycerin aerosol exposure as a potential airway irritant rather than a treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — PG has no approved indication; it is used as a pharmaceutical excipient/solvent |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for propylene glycol is not currently available. PG is a small-molecule diol widely used as a solvent/humectant in drug formulations, including inhalation solutions, and this formulation role is likely why it co-occurs with respiratory-disease trial data in the knowledge graph — not because PG itself has a demonstrated pharmacological effect on airway disease.

All four clinical trials retrieved for the bronchitis prediction study *Cyclosporine Inhalation Solution (CIS)* for bronchiolitis obliterans syndrome after lung or stem-cell transplantation. In each of these, PG (if present at all) would function only as an inactive excipient in the inhaled formulation, not as the tested active ingredient — the evidence pack's own relevance grading marks all four trials "C" for exactly this reason.

The literature signal points in the opposite direction from a treatment hypothesis: two reviews (PMID 26408554, 28983782) and one preclinical study (PMID 20920189) discuss how inhaled aerosols containing PG/glycerin (as used in e-cigarettes) may be associated with airway irritation and chronic bronchitis/COPD-type pathology. This is a potential **safety signal**, not supporting efficacy evidence. Taken together, the mechanistic case for repurposing PG itself for bronchitis is currently unsupported.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Evaluated Cyclosporine Inhalation Solution (CIS) for improving BOS-free survival after lung transplant, added to standard immunosuppression; PG is not the study drug, at most an inactive excipient |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | CIS for treatment of bronchiolitis obliterans syndrome in lung/stem-cell transplant recipients; same caveat — PG not the tested agent |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access follow-on of CIS in transplant recipients with bronchiolitis obliterans; very small sample, PG role unchanged |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Long-term follow-up extension of a Phase 3 inhaled-cyclosporine study for chronic rejection prevention; trial was terminated |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews chronic e-cigarette use and lung disease risk, including chronic bronchitis as part of COPD; discusses inhaled aerosol constituents (PG/glycerin) as a potential harm pathway, not a therapeutic one |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | Reviews e-cigarette liquid/aerosol constituents (including PG) as airway irritants potentially worsening pre-existing respiratory disease such as asthma |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal model) | Respiratory Research | Elastase/LPS mouse model of COPD (chronic bronchitis, emphysema); tests quercetin, not PG — included in the search results but not directly on-topic |

---

## Canada Market Information

Propylene glycol is currently **not marketed** under this evidence pack's Canadian regulatory search (0 DINs, 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. Note that a **blocking data gap** (DG001) exists: TFDA label warnings/contraindications for PG have not yet been retrieved, which by design prevents this candidate from entering the S1 safety pre-screen stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is not currently supported by direct evidence — all identified clinical trials test cyclosporine inhalation solution rather than PG, and the literature raises a potential airway-irritation safety signal rather than efficacy support. Combined with the absence of an established original indication, missing MOA data, and a blocking gap in TFDA safety labeling, the evidence base does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications for propylene glycol (DG001, blocking)
- Mechanism of action data from DrugBank or primary literature (DG002)
- Evidence specific to PG as an active agent (not merely as a formulation excipient) in respiratory disease
- Clarification of PG's established/approved uses, since no original indication is currently on record
- Note: the other 9 predicted indications for this drug (diabetic retinopathy, cataract subtypes, etc.) are rated L4–L5 with little to no clinical trial or literature support and are also recommended Hold; none currently warrant prioritization over bronchitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

