---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is an endothelin receptor antagonist used to treat pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation (AVM)**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (from the supplied literature and rationale; the Canadian licence records list no indication text) |
| Predicted New Indication | Pulmonary arteriovenous malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. The supplied rationale describes ambrisentan as a selective endothelin type A (ETA) receptor antagonist. Its efficacy in PAH is established, and it works by blocking endothelin-mediated vasoconstriction and vascular remodeling.

The link to pulmonary AVM is weak. A pulmonary AVM is a structural malformation of the blood vessels, and the drug's vasodilatory action does not obviously address it. No mechanistic or clinical link was supplied. The high TxGNN score reflects knowledge-graph similarity only, so this prediction should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Worth Noting

The top-ranked prediction has the weakest evidence. Several lower-ranked predictions have much stronger support.

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Support |
|------|------|------|------|------|
| PAH associated with connective tissue disease | 99.30% | L2 | Proceed with Guardrails | 3 trials (2 rated directly relevant: [NCT01042158](https://clinicaltrials.gov/study/NCT01042158), [NCT02290613](https://clinicaltrials.gov/study/NCT02290613)) and 19 publications, including meta-analyses and AMBITION/ARIES-E subgroup analyses |
| PAH associated with congenital heart disease | 99.37% | L2 | Proceed with Guardrails | 9 trials, including a completed Phase 3 single-arm study ([NCT01808313](https://clinicaltrials.gov/study/NCT01808313)). The CHD subgroup is unconfirmed. |
| PAH associated with HIV infection | 99.30% | L4 | Research Question | 1 trial of unverified relevance ([NCT00709956](https://clinicaltrials.gov/study/NCT00709956)) and 4 publications (small case series, a case report, a registry and a referral-centre series) |
| PAH associated with schistosomiasis or chronic hemolytic anemia, and the non-PAH predictions (periodontal malformation syndrome, hypotrichosis, hypertrichosis, Dandy-Walker syndrome) | 99.12–99.30% | L5 | Hold | No supporting evidence. The 20 periodontitis articles retrieved for the periodontal malformation prediction do not mention ambrisentan and appear to be keyword-matching artifacts. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02307065 | VOLIBRIS |
| 02307073 | VOLIBRIS |
| 02475383 | APO-AMBRISENTAN |
| 02475375 | APO-AMBRISENTAN |

Dosage form, manufacturer and approved indication text are not populated in the supplied licence records.

## Safety Considerations

- **Contraindications**: The supplied rationale for another prediction (Dandy-Walker syndrome) notes that ambrisentan is teratogenic and contraindicated in pregnancy. This is not from a package insert.
- **Drug Interactions**: No interaction records were found.

Please refer to the Health Canada package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary AVM prediction rests on model score alone, with no trials, no literature and no plausible mechanistic link. A vasodilator is unlikely to correct a structural vascular malformation. Evidence is far stronger for CTD-associated and CHD-associated PAH, which are subtypes of the drug's core indication.

**To proceed, the following is needed:**
- A mechanistic rationale, or preclinical or case-level evidence, for ETA antagonism in pulmonary AVM
- A targeted literature search for ambrisentan in pulmonary AVM
- Health Canada package insert warnings and contraindications (current safety data is blocking)
- Mechanism of action data from DrugBank
- Consideration of moving the CTD-PAH and CHD-PAH predictions forward. This would need confirmation of the CHD subgroup in the listed trials and a check on whether an existing approved indication already covers them.

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

