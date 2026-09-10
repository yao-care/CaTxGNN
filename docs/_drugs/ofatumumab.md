---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma to IGHV-Mutated CLL/SLL

## One-Sentence Summary

Ofatumumab is a human anti-CD20 monoclonal antibody historically approved for chronic lymphocytic leukemia (CLL)/small lymphocytic lymphoma (SLL) refractory to fludarabine and alemtuzumab. The TxGNN model's top-ranked prediction points to a molecular subtype of the same disease — **CLL/SLL with immunoglobulin heavy chain variable-region gene somatic hypermutation (IGHV-mutated CLL/SLL)** — with a **99.77%** prediction score, but currently **no clinical trials or literature specific to this molecular subtype** support the prediction; all supporting evidence is indirect extrapolation from the broader CLL/SLL population.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic lymphocytic leukemia (CLL)/small lymphocytic lymphoma (SLL), relapsed/refractory (based on clinical trial descriptions in the evidence pack; no formal Taiwan/Canada license record available) |
| Predicted New Indication | CLL/SLL with IGHV somatic hypermutation |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question (Hold) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded for this candidate. Based on information available elsewhere in the evidence pack, ofatumumab is a fully human IgG1κ anti-CD20 monoclonal antibody that binds a distinct membrane-proximal epitope on CD20 and depletes CD20-positive B cells via complement-dependent cytotoxicity (CDC) and antibody-dependent cellular cytotoxicity (ADCC). Its efficacy in CLL/SLL — including relapsed/refractory disease and combination regimens with chemotherapy — is well established across dozens of completed trials.

The predicted new indication, IGHV-mutated CLL/SLL, is not a distinct disease but a **prognostic molecular subtype of the same CLL/SLL population** ofatumumab was originally developed for. CD20 expression does not differ meaningfully by IGHV mutation status — IGHV mutation is a prognostic marker (mutated status is generally associated with more indolent disease and better response to CD20-directed therapy) rather than a distinct therapeutic target. Mechanistically the extrapolation is plausible, but it remains indirect: no trial or publication in this evidence pack stratifies ofatumumab outcomes specifically by IGHV mutation status, so the prediction should be treated as a research hypothesis rather than an evidence-backed new indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Cytotoxicity

Ofatumumab is an antineoplastic/immuno-oncology agent (anti-CD20 monoclonal antibody used in CD20-positive B-cell malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (targeted anti-CD20 monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; infusion-related reaction monitoring; hepatitis B reactivation screening (standard precaution for anti-CD20 antibody class) |
| Handling Protection | Not subject to conventional cytotoxic drug handling regulations (biologic monoclonal antibody); standard IV infusion precautions and premedication per institutional protocol apply |

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN score is high, but the predicted indication is a molecular subtype of ofatumumab's own original disease rather than a genuinely novel indication, and no clinical trial or literature evidence specific to IGHV-mutated CLL/SLL exists — the mechanistic link is entirely inferred from general CLL/SLL data. This does not yet meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/Canada regulatory label data (currently a Blocking data gap — required before any S1 safety evaluation)
- Formal DrugBank-sourced mechanism of action (MOA) record
- IGHV-mutation-stratified outcome data from existing or future ofatumumab CLL/SLL trials
- A decision on whether to instead prioritize **follicular lymphoma** (rank 3: L2 evidence, multiple completed trials including a Phase 3 RCT, "Proceed with Guardrails") or the drug's original **CLL/SLL** indication (rank 5: L1 evidence, "Proceed with Guardrails"), both of which are substantially better supported than this top-ranked subtype prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

