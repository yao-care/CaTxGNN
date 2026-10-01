---
layout: default
title: Ziprasidone
parent: Model Prediction Only (L5)
nav_order: 987
evidence_level: L5
indication_count: 10
---

# Ziprasidone
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

# Ziprasidone: From Antipsychotic Therapy to Trichotillomania

## One-Sentence Summary

Ziprasidone is an atypical antipsychotic, marketed in Canada under several brand and generic names. The TxGNN model predicts it may be effective for **trichotillomania** (a hair-pulling disorder), but **no clinical trials and no publications** were retrieved to support this prediction. It is a model-only signal at this point.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, ziprasidone blocks dopamine D2 and serotonin 5-HT2A receptors. It also acts as a 5-HT1A partial agonist and inhibits serotonin and norepinephrine reuptake.

Trichotillomania is an impulse-control and habit disorder. Dopamine and serotonin signalling are thought to be involved in this kind of repetitive behaviour, so a drug that modulates both is a plausible candidate. This rationale is theoretical. No retrieved trial or publication supports it, and the original indication has not been compared with the new one in the data provided.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Eight authorizations are on record. The first five are listed below. The records contain no dosage form or approved-indication text.

| DIN | Product Name |
|---------|------|
| 2298597 | ZELDOX |
| 2298619 | ZELDOX |
| 2449544 | AURO-ZIPRASIDONE |
| 2449552 | AURO-ZIPRASIDONE |
| 2449579 | AURO-ZIPRASIDONE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it rests on the graph model alone. There are no trials or publications for trichotillomania, so the evidence level is L5 and the case for moving forward is not yet made.

**To proceed, the following is needed:**
- A targeted literature and trial search for ziprasidone in trichotillomania and related impulse-control or habit disorders
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Approved-indication text for the Canadian DINs, to confirm the original indication

**Note on other predicted indications:** Trichotillomania is the top-ranked prediction, but the Evidence Pack holds stronger evidence for other candidates.
- **Major affective disorder (rank 3):** L1 evidence, with multiple completed Phase 3 trials in bipolar disorder and Phase 2 trials in depression. The pack recommends Proceed with Guardrails: QTc/ECG monitoring, metabolic monitoring, and administration with food. Several of these uses, such as bipolar mania, may already be approved, so this may not be true repurposing.
- **Tourette syndrome (rank 7):** L3 evidence, limited to an early pilot study, a case report and pediatric pharmacokinetic data.

Most other top-ranked predictions, such as the congenital malformations and myopia entries, have no mechanistic link and look like network artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

