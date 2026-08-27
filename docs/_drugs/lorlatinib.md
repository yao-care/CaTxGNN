---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

Using the Evidence Pack as provided — note upfront that `predicted_indications[0]` (the highest TxGNN score) is **Gingival Fibromatosis**, and the pack's own `repurposing_rationale` for this candidate explicitly states there is no mechanistic plausibility and no supporting evidence. I'm reporting this honestly rather than reframing it as a stronger signal than the data supports.

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

> Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor, globally approved for ALK-positive non-small cell lung cancer (NSCLC) — though it currently holds no marketing authorization in Canada.
> The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, with a **99.81%** prediction score,
> but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — derived from literature evidence in this pack; not a Health Canada–registered indication (drug is unmarketed in Canada) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged in this pack as data gap DG002, High severity). Based on the literature evidence collected elsewhere in this pack (e.g., the CROWN trial series and adverse-event management reviews), lorlatinib is known to be a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor, with its established efficacy in ALK-rearranged NSCLC.

Gingival fibromatosis, however, is a benign gingival overgrowth condition primarily associated with genes such as *SOS1* and *REST*, and has no established connection to the ALK signaling pathway that lorlatinib targets. The evidence pack's own mechanistic assessment for this candidate states directly that there is "no known association with the ALK pathway, no mechanistic plausibility, and no clinical or literature evidence of any kind."

Taken together, this suggests the high TxGNN score most likely reflects proximity within the model's embedding space (e.g., shared graph neighbors) rather than a genuine, biologically grounded repurposing signal. This is corroborated by the complete absence of clinical trials or publications for this drug-disease pair (see query log entries #2–#4, all zero results).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Lorlatinib currently holds **no Health Canada market authorization** — `market_status` is recorded as "not marketed" with **0 DINs** on file. No product listing, dosage form, or approved-indication text is available for extraction from `taiwan_regulatory.licenses`.

---

## Cytotoxicity

Lorlatinib is an oncology drug (ALK/ROS1-targeted small-molecule inhibitor used in NSCLC), so this section is included per the antineoplastic-drug criteria, drawing on general lorlatinib safety literature found elsewhere in this evidence pack (not specific to the gingival fibromatosis candidate).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Low — literature in this pack reports lorlatinib's dominant toxicities as metabolic/lipid (hypercholesterolemia, hypertriglyceridemia), weight gain, edema, and CNS/cognitive effects, rather than hematologic suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting lipid panel, weight/BMI, liver function, CNS/cognitive and mood assessment; renal function if nephrotic-range proteinuria is suspected |
| Handling Protection | Standard oral oncology-drug handling; not subject to conventional cytotoxic (hazardous chemotherapy) handling protocols, but formal confirmation should follow the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all unavailable in this evidence pack — DG001, Blocking severity — and a TFDA/Health Canada label review is required before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- This candidate has zero clinical trials, zero literature support, and the evidence pack's own rationale explicitly identifies the mechanistic link as absent — the high TxGNN score alone cannot justify further evaluation. Additionally, a Blocking-severity data gap (missing TFDA/Health Canada label warnings) prevents even a preliminary safety assessment (S1).

**To proceed, the following is needed:**
- Health Canada / package insert data: warnings, contraindications, and drug interactions (resolves DG001, currently Blocking)
- Confirmed mechanism-of-action data for lorlatinib (resolves DG002)
- If repurposing evaluation continues for this drug, consider re-prioritizing toward **lung hilum carcinoma** (rank 4 in this pack), which — while still limited to a single case report (L3) — has a biologically coherent rationale (ALK-positive NSCLC anatomic subtype) not present in the top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

