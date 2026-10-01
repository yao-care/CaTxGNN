---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Eflornithine
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

# Eflornithine: From Its Marketed Use (Indication Not Recorded) to Esotropia

## One-Sentence Summary

Eflornithine is an irreversible inhibitor of ornithine decarboxylase (ODC) and is marketed in Canada as VANIQA, but the record does not state its approved indication.
The TxGNN model predicts it may be effective for **esotropia**, but there are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eflornithine irreversibly inhibits ODC, the rate-limiting enzyme in polyamine synthesis, and so lowers cellular polyamine levels. The evidence retrieved here also identifies it as an established treatment for late-stage Gambian human African trypanosomiasis. The record does not list its approved indication in Canada.

**No plausible mechanistic link to esotropia was identified.** Esotropia is a disorder of ocular motor alignment, and ODC or polyamine biology has no known role in it. The very high TxGNN score (99.85%, rank 3,522) is therefore a statistical output of the knowledge graph. It has no supporting clinical, preclinical or mechanistic evidence. On this basis the prediction should not be treated as an actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2243837 | VANIQA | Not recorded | Not recorded |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction has L5 evidence only: no trials, no literature and no plausible mechanism. A high model score alone does not justify further investment.

**Other predictions in the same run:**
- **Bovine trypanosomiasis** and **monoclonal gammopathy** reached L4 (preclinical or mechanistic evidence only) and are labelled "Research Question".
- Bovine trypanosomiasis is the more biologically plausible of the two, because eflornithine already treats human African trypanosomiasis. Its supporting papers cover related parasites and parasite enzymes, not bovine Trypanosoma itself.
- The monoclonal gammopathy evidence is old myeloma cell-line work and does not address premalignant states.
- Neither is a clinical-stage candidate.

**To proceed with any indication, the following is needed:**
- The approved indication and dosage form for the Canadian licence (DIN 2243837)
- The Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data confirmed from DrugBank
- For esotropia specifically, a credible mechanistic hypothesis and preclinical support; otherwise, deprioritise it in favour of the L4 candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

