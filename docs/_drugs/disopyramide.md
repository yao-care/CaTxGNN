---
layout: default
title: Disopyramide
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a Class Ia antiarrhythmic agent historically used for the treatment of ventricular and supraventricular cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Tourette Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction rests entirely on computational inference; no empirical evidence has been identified to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (drug not marketed in Taiwan; no approved indication on record) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, disopyramide is a Class Ia antiarrhythmic agent whose primary action is voltage-gated sodium channel blockade, reducing myocardial excitability and prolonging the effective refractory period. It also carries clinically significant anticholinergic (muscarinic antagonist) activity, which is responsible for many of its side effects (dry mouth, urinary retention, blurred vision).

The speculative mechanistic connection to Tourette Syndrome runs through this anticholinergic component: cholinergic interneurons in the basal ganglia striatum are known to be dysregulated in tic disorders, and anticholinergic agents such as trihexyphenidyl have occasionally been used off-label for tic suppression. On this basis, a pharmacological class analogy can be drawn.

However, this link is highly indirect and faces a critical biological barrier: disopyramide has poor central nervous system penetration, which severely limits its ability to exert meaningful pharmacological effects at basal ganglia cholinergic synapses. There is no published clinical evidence, animal model data, or mechanistic hypothesis in the literature supporting disopyramide's use in Tourette Syndrome. The high TxGNN score most likely reflects a pattern-based signal propagated through the knowledge graph via the anticholinergic class rather than a direct, drug-specific mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Disopyramide is not currently marketed in Taiwan. No approved drug licenses are on record with the Taiwan FDA (TFDA). Package insert warnings and contraindications are therefore not available from the local regulatory source and must be obtained from the originator's labelling or international references (e.g., FDA, EMA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert data (warnings, contraindications) was identified as a blocking data gap (DG001) in this Evidence Pack. Full safety characterisation — including QT-prolongation risk, negative inotropy, and anticholinergic burden — cannot be completed without resolving this gap.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.86%), the Tourette Syndrome indication is not supported by any registered clinical trials, published literature, or a pharmacologically plausible direct mechanism — and disopyramide's poor CNS penetration makes it an unlikely candidate for central tic-circuit modulation without substantial additional evidence.

**Noteworthy alternative within this candidate set:**
Among the 10 TxGNN-predicted indications in this pack, **Idiopathic Neonatal Atrial Flutter** (Rank 7, score 99.42%, Evidence Level L4) carries the strongest mechanistic rationale: disopyramide's Class Ia sodium channel blockade directly addresses the macro-reentry circuit underlying atrial flutter. This candidate may warrant a focused research question evaluation, subject to neonatal pharmacokinetic and safety data review.

**To proceed with any indication, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve and parse the TFDA or originator package insert to obtain warnings, contraindications, and QT-prolongation / negative inotropic risk data before any further safety gating.
- **Resolve DG002 (High):** Query DrugBank API for confirmed MOA, pharmacokinetic parameters, and BBB penetration data to enable mechanistic plausibility scoring.
- **For Tourette Syndrome specifically:** Commission a targeted literature and preclinical landscape review to determine whether any Class Ia agents have demonstrated CNS tic-modulating activity; absence of such data would formally close this candidate.
- **For Idiopathic Neonatal Atrial Flutter:** Conduct a neonatal pharmacokinetic review and consult paediatric cardiology literature (off-label use reports) before advancing to a formal research proposal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

