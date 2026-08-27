---
layout: default
title: Hypromellose
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Hypromellose
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

This skill is for CLI/DB report pass-through and doesn't apply here — the task is to synthesize a structured Markdown report from the JSON Evidence Pack already provided in full (per the v5 prompt template), not to relay raw CLI output. Proceeding to build the report directly from the given JSON, field by field, without fabricating anything the pack doesn't contain.

---

# Hypromellose: From Pharmaceutical Excipient Use (No Approved Indication) to Hepatic Veno-Occlusive Disease-Immunodeficiency Syndrome

## One-Sentence Summary

Hypromellose (DrugBank DB11075) has no approved therapeutic indication or Canadian market authorization on file — it is a pharmacologically inert cellulose derivative typically used as a viscosity modifier/excipient. The TxGNN model predicts it may be effective for **hepatic veno-occlusive disease-immunodeficiency syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic profile offers no plausible link to this rare, genetically-defined disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file — Canada `taiwan_regulatory.licenses` is empty (0 DINs); Hypromellose is generically used as a pharmaceutical/ophthalmic excipient rather than for a specific disease indication |
| Predicted New Indication | Hepatic veno-occlusive disease-immunodeficiency syndrome |
| TxGNN Prediction Score | 98.30% (raw score 0.9830; candidate rank 25,833 among model outputs) |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the information available, Hypromellose is a pharmacologically inert cellulose derivative used clinically as a viscosity modifier/excipient (e.g., in ophthalmic lubricants and as a coating/binding agent in oral formulations) — it has no established pharmacodynamic activity of its own.

The predicted indication, hepatic veno-occlusive disease-immunodeficiency syndrome, is a rare genetic disorder associated with SP110 gene mutations, involving hepatic sinusoidal endothelial injury and combined immunodeficiency. There is no known biological pathway connecting a cellulose-based excipient to SP110 function, hepatic venous endothelium, or immune reconstitution — the evidence pack's own mechanistic rationale states there is no known pharmacological mechanism explaining this association.

Given the absence of any mechanistic rationale, the complete lack of supporting clinical or literature evidence, and the extremely low prevalence (and correspondingly sparse knowledge-graph representation) of this rare disease, the most plausible explanation is that the high TxGNN score reflects an **embedding artifact from sparse data on this rare-disease node** rather than a genuine pharmacological signal. This assessment is stated directly in the evidence pack's repurposing rationale for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Canadian market authorization (DIN) is currently on file for Hypromellose in this evidence pack — market status is recorded as **Not Marketed**, with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields in the evidence pack — key warnings, contraindications, and drug-drug interactions — are marked as data gaps or returned no results; TFDA/product-label warning data is flagged as a Blocking-severity gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction has no mechanistic plausibility, zero clinical trial evidence, and zero literature support — the evidence level is L5 (model prediction only), and the pack's own rationale flags the score as a likely knowledge-graph sparse-data artifact rather than a real signal.
- The drug has no Canadian market presence (0 DINs, Not Marketed) and a Blocking-severity safety data gap (no TFDA/product-label warnings available), which independently prevents advancement past initial safety screening (S1).

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to properly evaluate mechanistic plausibility (DG002)
- Product label warnings/contraindications from TFDA to clear the Blocking safety gap before any S1 review (DG001)
- Independent validation of the TxGNN score for this candidate, given the rare-disease sparse-embedding concern noted in the rationale — consider deprioritizing in favor of candidates with at least preliminary mechanistic or evidentiary support
- Note: among this drug's top-10 predictions, only rank 8 (psoriasis) has any associated evidence (1 clinical trial, 1 publication), but both concern Hypromellose's use as a topical gel/nanogel *delivery vehicle*, not a direct pharmacological effect on psoriasis pathology — this does not change the Hold recommendation for the top-ranked candidate but may warrant separate, lower-priority tracking.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

