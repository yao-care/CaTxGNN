---
layout: default
title: Selpercatinib
parent: Model Prediction Only (L5)
nav_order: 710
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Selpercatinib: From RET Fusion-Positive NSCLC to Predicted Pulmonary Hypertension

## One-Sentence Summary

> Selpercatinib is a selective RET kinase inhibitor whose established use — based on the literature returned in this evidence pack — is in RET fusion-positive non-small-cell lung cancer (NSCLC).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of **99.18%**,
> but **no clinical trials** and only **2 indirectly relevant publications** (neither of which studies pulmonary hypertension as a therapeutic endpoint) currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RET fusion-positive non-small-cell lung cancer (NSCLC) — inferred from literature evidence in this pack; not yet confirmed by Canadian regulatory data |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity gap, DG002). Based on the literature retrieved, selpercatinib is a selective RET kinase inhibitor with established clinical activity in RET fusion-positive NSCLC.

However, the mechanistic case for pulmonary hypertension is weak and possibly built on a term-matching artifact rather than real biology. The two literature hits returned by the search both discuss **systemic hypertension** as an adverse event of selpercatinib in oncology patients — not pulmonary arterial/pulmonary hypertension as a treatment target. This looks like a disease-vocabulary collision ("hypertension" vs. "pulmonary hypertension") rather than genuine mechanistic evidence.

More importantly, the direction is inconsistent with the drug's known pharmacology: selpercatinib is clinically associated with **inducing** hypertension as a toxicity, which is the opposite of what would be required for a therapeutic effect in pulmonary hypertension. While RET/GDNF signaling does have a described role in vascular remodeling and pulmonary endothelial biology, no evidence in this pack connects that biology to a beneficial effect of RET inhibition in pulmonary hypertension. The high TxGNN score should be interpreted as an artifact of embedding similarity, not as validated pharmacological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Cohort (Adverse Event Study) | Frontiers in Pharmacology | FAERS-based comparison of adverse events between pralsetinib and selpercatinib in RET-altered cancer patients — discusses hypertension as an **adverse event**, not a treatment indication |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective Cohort (Oncology) | Therapeutic Advances in Medical Oncology | SIREN study: real-world efficacy of selpercatinib in RET fusion-positive NSCLC via an access program; confirms the drug's oncology indication but does not address pulmonary hypertension |

---

## Canada Market Information

Selpercatinib is not currently marketed in Canada — no DIN registrations exist in this evidence pack (total_licenses = 0).

---

## Cytotoxicity

Selpercatinib's oncology use (RET fusion-positive NSCLC) is confirmed by the literature evidence in this pack, so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; literature suggests blood pressure monitoring given reported hypertension as an adverse event |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Key warnings, contraindications, and drug interaction data (TFDA label) are flagged as a Blocking data gap (DG001) and could not be retrieved for this evidence pack.*

---

## Other TxGNN-Predicted Candidates (Lower Priority)

| Rank | Disease | TxGNN Score | Evidence | Recommendation |
|------|---------|-------------|----------|-----------------|
| 2 | Migraine disorder | 99.17% | No trials, no literature | Hold |
| 3 | Migraine with brainstem aura | 99.05% | No trials, no literature | Hold |

Both are pure model-score predictions with a purely theoretical RET/GDNF–nociception rationale and zero supporting trials or literature.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted link to pulmonary hypertension is not supported by real evidence — the only literature returned describes systemic hypertension as an **adverse effect** of the drug in oncology use, which is mechanistically opposite to a therapeutic benefit in pulmonary hypertension. Combined with the absence of any clinical trials, this is a pure model artifact (Evidence Level L5) likely driven by disease-term ambiguity.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed MOA and original indication from DrugBank (DG002)
- Literature/expert review to rule out the "hypertension vs. pulmonary hypertension" term-confusion hypothesis before any further evaluation
- If pursued despite the above, targeted preclinical or mechanistic studies on RET signaling in pulmonary vascular remodeling would be required before this candidate could advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

