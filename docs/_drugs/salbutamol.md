---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: From Obstructive Airway Disease to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol is a beta-2 agonist bronchodilator marketed in Canada; the Evidence Pack lists no approved indication text, so asthma/COPD use is inferred from the drug class.
The TxGNN model predicts it may be effective for **papillary conjunctivitis** with a very high score, but **0 clinical trials** and **0 publications** were retrieved for this indication.
This is a model-only prediction (evidence level L5), and the Evidence Pack itself suggests it may be a graph-propagation artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obstructive airway disease (asthma/COPD), inferred; Canadian licence indication texts are empty |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.996% (rank 160) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, salbutamol is a beta-2 adrenoceptor agonist, its efficacy in airway obstruction is well established, and mechanistically it may be applicable to allergic ocular inflammation.

The proposed link is that beta-2 agonism may stabilize mast cells and reduce allergic inflammation in the eye. A related preclinical finding supports this indirectly: topical salbutamol strongly suppressed immediate allergic conjunctivitis in a guinea pig model (PMID 3666475, 1987). That study concerned allergic conjunctivitis in general, not papillary conjunctivitis, and no human efficacy data exist.

The TxGNN score is extremely high, yet no trial or publication was found. The Evidence Pack assessment is that this pattern more likely reflects propagation through allergic/atopic disease neighbours in the knowledge graph than a real therapeutic signal. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Salbutamol has 15 Canadian authorizations. Five are listed below; dosage form and approved indication text were not provided for any of them.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02208229 | PMS-SALBUTAMOL | — | — |
| 02326450 | TEVA-SALBUTAMOL HFA | — | — |
| 01926934 | TEVA-SALBUTAMOL STERINEBS P.F. | — | — |
| 02173360 | TEVA-SALBUTAMOL STERINEBS P.F. | — | — |
| 02243115 | VENTOLIN DISKUS | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no human data for papillary conjunctivitis. Only indirect preclinical data in allergic conjunctivitis exist, and the score may be a graph artifact. There is no basis to advance this indication.

**To proceed, the following is needed:**
- A targeted search for human studies of topical beta-2 agonists in papillary or allergic conjunctivitis
- Route compatibility assessment: an ophthalmic formulation would be needed, and the listed Canadian products appear to be inhalation products
- Health Canada product monograph (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank, and correction of the empty original-indication field upstream

**Other candidates in this pack (for reference):**
- **Obstructive lung disease** (rank 10) is the only indication at L1 (Proceed with Guardrails). It is almost certainly an existing labelled use rather than true repurposing. Before relying on the Phase 3 trials, confirm that salbutamol was the study drug and not a rescue comparator.
- **Bronchitis, anaphylaxis and atopic conjunctivitis** are flagged as research questions. For anaphylaxis, epinephrine remains first-line, and anaphylaxis to salbutamol itself has been reported.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

