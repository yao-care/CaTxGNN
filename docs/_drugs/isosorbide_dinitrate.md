---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina to Alopecia

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is an organic nitrate vasodilator, established for angina and other cardiovascular uses (the Canadian license text in the Evidence Pack is empty, so this is not confirmed there).
The TxGNN model predicts it may be effective for **alopecia**, but this is a model-only prediction: **0 clinical trials** and **0 publications** support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina / coronary artery disease (general nitrate use; not stated in the license data) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, ISDN is a nitric oxide (NO) donor. It raises cGMP and dilates blood vessels, and its efficacy in vascular and cardiac conditions is well established. Mechanistically, it could be applicable to alopecia only through a hypothetical improvement in scalp perfusion.

That link is speculative. Nothing in the Evidence Pack shows that a nitrate affects hair growth. The 99.99% score is very high but is not corroborated by any clinical or preclinical signal. It most likely reflects proximity in the knowledge graph to other hair-related phenotypes. The same model output also lists hypertrichosis (the opposite phenotype) and several rare hair disorders. This further suggests the score reflects graph structure rather than real biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 441694 | ISDN |
| 441686 | ISDN |

Dosage form, manufacturer and approved indication text are not available for these two licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

For general context, the Evidence Pack notes nitrate tolerance with chronic use and systemic hypotension as known concerns for this drug class. These have not been assessed for a scalp or hair-loss use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction is model-only (L5) with no trials, no literature and no plausible mechanistic support. A very high TxGNN score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Any preclinical or clinical signal linking nitrates or NO donors to hair growth
- A defined route of administration (the current products are cardiovascular formulations, and route compatibility is still pending)
- Health Canada package insert warnings and contraindications, and MOA data from DrugBank

**Better-supported directions for this drug:**
- **Pulmonary hypertension** (evidence level L3, rank 4): about 20 publications, mostly small human hemodynamic studies from 1979 to 2025 and some animal studies. There are no registered trials and no RCT-level evidence. Risks include nitrate tolerance, V/Q mismatch in lung disease and systemic hypotension.
- **Vascular disease** (evidence level L2, rank 6): the category is broad and overlaps with the established antianginal use, so much of the signal is on-label. The one novel-context signal is a completed Phase 3 trial of ISDN spray with chitosan in diabetic foot ulcers ([NCT02789033](https://clinicaltrials.gov/study/NCT02789033), n=68), and its results are not in the provided data. The target indication should be narrowed before any decision.

Both of these are flagged as "Research Question" in the Evidence Pack. Neither has been reviewed against full texts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

