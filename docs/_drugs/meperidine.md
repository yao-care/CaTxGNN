---
layout: default
title: Meperidine
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
---

# Meperidine
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

# Meperidine: From Opioid Analgesia to Tourette Syndrome

## One-Sentence Summary

Meperidine (pethidine) is an opioid analgesic, and one injectable product is marketed in Canada.
The TxGNN model predicts it may be effective for **Tourette syndrome**,
but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (opioid analgesic used for pain) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Meperidine is generally described as a mu-opioid receptor agonist with weak serotonin reuptake inhibition. The endogenous opioid system has been discussed in tic disorders, which is the only mechanistic thread linking the drug to Tourette syndrome.

The direction of effect is unproven. No source in the pack shows that meperidine suppresses tics. The score of 0.9946 is a knowledge-graph prediction only. The similarity between the original and new indication has not been assessed.

The model also ranked **trichotillomania** second (score 99.39%). It has no trial or literature support either. Clinical work on repetitive grooming behaviours points toward opioid *antagonism* (e.g., naltrexone), the opposite of meperidine's action. It is not recommended for pursuit without a new rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 725765 | MEPERIDINE HYDROCHLORIDE INJECTION USP |

Dosage form, manufacturer and approved indication text are not recorded for this authorization.

## Safety Considerations

No package insert warnings, contraindications or drug-interaction records are available in the supplied data. The DDI query returned no results. The following concerns are noted in the repurposing assessment and should be checked against the package insert:

- **Normeperidine neurotoxicity and seizure risk**, especially with repeated dosing
- **Serotonin syndrome risk** with serotonergic drugs or MAOIs
- **Dependence liability**, a major concern for a chronic neuropsychiatric condition such as Tourette syndrome

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature, and no documented mechanism. The safety profile (neurotoxic metabolite, serotonergic interactions, dependence) is unfavourable for chronic use in Tourette syndrome.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank) and an analysis of the link to tic disorders
- A systematic literature and trial search for meperidine or opioid agonists in Tourette syndrome
- A risk-benefit justification against existing tic therapies, including a dependence and neurotoxicity mitigation plan

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

