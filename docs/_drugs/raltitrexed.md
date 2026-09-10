---
layout: default
title: Raltitrexed
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed: From Antineoplastic Chemotherapy to Sclerosing Cholangitis

## One-Sentence Summary

Raltitrexed is a thymidylate synthase (TS) inhibitor — a cytotoxic antimetabolite chemotherapy agent — though this evidence pack does not record its specific original indication. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as likely a graph-prediction artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antineoplastic chemotherapy (thymidylate synthase inhibitor); specific historical indication not recorded in this evidence pack |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (drug-level data gap DG002). Based on what is recorded elsewhere in the pack, Raltitrexed is a thymidylate synthase inhibitor — a cytotoxic antimetabolite chemotherapy agent whose principal toxicity is myelosuppression (neutropenia, thrombocytopenia).

Sclerosing cholangitis is an autoimmune/inflammatory biliary disease. There is no established pathophysiological connection between TS inhibition and cholangitis, and the evidence pack's own rationale explicitly states there is "no known mechanistic link, no hypothesis, no clinical trials, and no literature support," describing this as likely knowledge-graph noise rather than a genuine repurposing signal.

Given the absence of a mechanistic bridge and the total lack of corroborating trial or literature evidence, this specific prediction should be treated as low-confidence despite its high raw TxGNN score. Notably, the remaining 9 predicted indications in this pack (largely hematologic conditions such as myelodysplastic syndrome and sickle-cell variants) show the same pattern — high score, zero evidence, and in several cases an outright contradiction between the drug's myelosuppressive toxicity and the target disease's need for intact marrow function. This suggests a systemic scoring artifact for this drug rather than an isolated false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Raltitrexed currently holds no Canadian market authorizations (0 DINs; market status: Not Marketed). No product-level licensing data is available to tabulate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite / thymidylate synthase inhibitor) |
| Myelosuppression Risk | High — documented as the principal toxicity (neutropenia, thrombocytopenia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (neutrophils, platelets), liver and renal function |
| Handling Protection | Cytotoxic drug handling precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a very high TxGNN similarity score but zero supporting clinical trials or literature (Evidence Level L5), and the pack's own rationale identifies the link as biologically implausible — a myelosuppressive cytotoxic agent proposed for a disease with no known connection to its mechanism. The same evidence gap and pattern of mechanistic contradiction recur across all 10 predicted indications for this drug, and Raltitrexed is not currently marketed in Canada.

**To proceed, the following is needed:**
- TFDA/Canadian product label warnings and contraindications (blocking gap DG001)
- Confirmed mechanism of action from DrugBank API (gap DG002)
- An independent mechanistic hypothesis linking TS inhibition to sclerosing cholangitis before any further evaluation stage is initiated
- Preclinical or observational evidence, since no clinical or literature signal currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

