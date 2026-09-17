---
layout: default
title: Selexipag
parent: High Evidence (L1-L2)
nav_order: 708
evidence_level: L2
indication_count: 10
---

# Selexipag
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Selexipag: From Pulmonary Arterial Hypertension to PAH Associated with Congenital Heart Disease

## One-Sentence Summary

Selexipag is a selective oral prostacyclin (IP) receptor agonist originally developed for Pulmonary Arterial Hypertension (WHO Group 1). TxGNN's top-ranked prediction for this drug is efficacy in **PAH associated with congenital heart disease**, a recognized subtype of the same WHO Group 1 disease family, currently supported by **2 clinical trials** (one terminated, one large ongoing extension study) with **no dedicated literature** yet indexed for this specific subgroup.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (WHO Group 1) — established via global labeling (Uptravi); not independently confirmed in this dataset, as Canadian regulatory records for this candidate are empty |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Selexipag is flagged as a data gap in the source registry (DG002). Based on well-established pharmacology, however, Selexipag is a selective, non-prostanoid small-molecule agonist at the IP (prostacyclin) receptor. Receptor activation raises intracellular cAMP in pulmonary vascular smooth muscle, producing vasodilation and inhibiting vascular remodeling/proliferation — the mechanism underlying its approved global use in Pulmonary Arterial Hypertension.

PAH associated with congenital heart disease (e.g., Eisenmenger syndrome) is itself a recognized **WHO Group 1** subtype, sharing the same underlying pathophysiology — pulmonary vascular smooth muscle proliferation and vasoconstriction — as idiopathic PAH. This prediction therefore does not represent extrapolation to an unrelated disease, but an extension within the same disease family to a specific aetiological subgroup, consistent with the very high TxGNN score.

Worth noting: within this same screening run, **connective tissue disease-associated PAH** (rank 3) shows substantially stronger, more mature evidence (L1, including a GRIPHON pivotal-trial subgroup analysis and multiple real-world registries) than the top-ranked congenital heart disease subgroup. See the "Other Candidate Indications" table below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04435782](https://clinicaltrials.gov/study/NCT04435782) | Phase 4 | Terminated | 9 | Assessed selexipag's effect on right ventricular remodeling in PAH via cardiac MRI; terminated early with only 9 participants enrolled — too small to support a robust conclusion, useful only as a safety signal |
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Open-label long-term follow-up/platform study continuing treatment for participants from six parent PAH trials (NCT03422328, NCT03904693, NCT04565990, NCT02932410, NCT03492177, NCT04175600); designed to assess long-term safety, not efficacy in this subgroup specifically |

---

## Literature Evidence

Currently no related literature available for this specific indication (PAH associated with congenital heart disease).

---

## Canada Market Information

Selexipag currently has **0 DIN records** in the Canadian regulatory dataset reviewed for this analysis, and the product is marked as **not marketed**. No authorization or product-level details are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this dataset (flagged as **Blocking** data gap DG001 — TFDA/Health Canada label warnings and contraindications must be obtained before this candidate can proceed to a formal safety review, S1).

---

## Other Candidate Indications from This Screen

This evidence pack evaluated 10 candidate indications for Selexipag. For context, the full ranking is summarized below:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|---|---|---|---|---|---|---|
| 1 | PAH associated with congenital heart disease | 98.03% | L2 | S2 | Proceed with Guardrails | Primary indication in this report; 2 trials, no dedicated literature |
| 2 | Pulmonary arteriovenous malformation | 98.00% | L5 | S0 | Hold | Structural vascular malformation, mechanistically unrelated; no trials/literature — likely embedding artifact |
| 3 | PAH associated with connective tissue disease (CTD-PAH) | 97.78% | L1 | S3 | Proceed with Guardrails | **Strongest evidence in this screen** — GRIPHON pivotal RCT subgroup + multiple real-world registries (EXPOSURE, SPHERE); recommend prioritizing over the top-ranked candidate |
| 4 | PAH associated with HIV infection | 97.78% | L4 | S1 | Research Question | Same WHO Group 1 mechanism, but no dedicated trial/literature in this dataset |
| 5 | PAH associated with schistosomiasis | 97.78% | L3 | S1 | Research Question | 1 Phase 2 trial (status unknown) + 1 not-yet-recruiting trial; evidence still emerging |
| 6 | PAH associated with chronic haemolytic anaemia | 97.78% | L5 | S0 | Hold | Mechanistically plausible (WHO Group 1) but zero trials/literature |
| 7 | Hypotrichosis simplex of the scalp | 97.11% | L5 | S0 | Hold | Wrong receptor subtype (FP vs IP); no mechanistic basis |
| 8 | Congenital hypotrichosis with milia | 96.30% | L5 | S0 | Hold | Same as above; no mechanistic basis |
| 9 | Diffuse alopecia areata | 95.98% | L5 | S0 | Hold | Autoimmune mechanism unrelated to IP-receptor pharmacology |
| 10 | Malformation syndrome with odontal/periodontal component | 93.77% | L5 | S0 | Hold | 20 literature hits are all generic periodontitis papers with no mention of selexipag — confirmed false-positive text-mining signal |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked indication (PAH-congenital heart disease) is mechanistically sound and within Selexipag's established WHO Group 1 disease family, but current trial evidence is limited to one terminated small study and one non-comparative long-term extension study. Meanwhile, the connective tissue disease-associated PAH candidate (rank 3) in this same screen already has L1-level evidence (pivotal RCT subgroup + real-world data) and should be evaluated in parallel, and likely prioritized, as it presents a materially stronger case for near-term action.

**To proceed, the following is needed:**
- TFDA/Health Canada approved label (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formal drug-drug interaction profile (current query returned no results)
- Detailed mechanism-of-action documentation from DrugBank (DG002)
- Confirmation of Canadian market/regulatory status, as no DIN records currently exist for this product in this dataset
- A dedicated efficacy/safety trial or subgroup analysis specific to the congenital heart disease-PAH population, given the small size and early termination of the only dedicated trial identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

