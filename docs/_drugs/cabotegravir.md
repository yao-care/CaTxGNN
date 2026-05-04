---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabotegravir: From HIV Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an integrase strand transfer inhibitor (INSTI) approved internationally for HIV-1 infection treatment and pre-exposure prophylaxis (PrEP), though it holds no Health Canada Drug Identification Number (DIN) at present.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
however, **no clinical trials and no published literature** currently support this direction, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (treatment and PrEP; no Canadian DIN on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only — no supporting studies identified) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Cabotegravir belongs to the integrase strand transfer inhibitor (INSTI) class. It works by blocking HIV-1 integrase, the enzyme responsible for inserting viral DNA into the host cell genome. It is best known as the active component of long-acting injectable HIV regimens (cabotegravir + rilpivirine), administered monthly or bi-monthly.

The proposed mechanistic bridge to rheumatoid arthritis rests on a speculative hypothesis: certain studies have suggested that endogenous retroviruses (ERVs) and retrotransposons may contribute to synovial inflammation in RA. In theory, an integrase inhibitor could suppress ERV integration activity in synovial tissue, potentially dampening inflammatory signalling. However, this hypothesis has not been tested in any RA model, human or animal.

It is important to note that the mechanistic link between Cabotegravir and RA pathophysiology remains entirely unvalidated. Unlike the gastric-cancer-to-colorectal-cancer extrapolation seen in fluoropyrimidine repurposing, RA and HIV infection share no established pharmacological pathway. The high TxGNN score likely reflects broad network connectivity in the knowledge graph rather than a direct biological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cabotegravir in Rheumatoid Arthritis.

---

## Literature Evidence

Currently no related literature available for Cabotegravir in Rheumatoid Arthritis.

---

## Canada Market Information

Cabotegravir currently holds no Drug Identification Numbers (DINs) in Canada. No licensed products are on file.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.45%), but the score alone cannot justify advancement — there is zero clinical, observational, or preclinical evidence linking Cabotegravir to rheumatoid arthritis, and the proposed ERV-mediated mechanistic link is entirely hypothetical and unvalidated.

**To proceed, the following is needed:**

- **Mechanism validation:** Pre-clinical studies (in vitro or animal models) demonstrating that INSTI-class drugs modulate ERV expression or synovial inflammation in RA-relevant models.
- **MOA data:** Retrieve full Cabotegravir pharmacology from DrugBank (DB11751) to confirm or refute the ERV suppression hypothesis.
- **Safety data:** Obtain Health Canada package insert or international prescribing information (GSK/ViiV Healthcare) to assess warnings, contraindications, and drug interactions — currently a blocking data gap (DG001).
- **Literature scoping:** Conduct a broader PubMed search using INSTI class terms (e.g., "integrase inhibitor AND rheumatoid arthritis", "endogenous retrovirus AND synovitis") to determine whether any class-level evidence exists beyond Cabotegravir specifically.
- **Regulatory pathway:** If early evidence emerges, confirm Health Canada DIN pathway requirements and consider whether the long-acting injectable formulation is appropriate for a non-infectious, chronic inflammatory indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

