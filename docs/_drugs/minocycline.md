---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 2
---

# Minocycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Minocycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a broad-spectrum tetracycline-class antibiotic traditionally used to treat bacterial infections including acne, respiratory tract infections, and other susceptible organisms.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, a condition characterized by scattered inflammatory erosions of the corneal epithelium.
Currently, **no clinical trials** and **no publications** directly support this repurposing direction — this candidate remains at the earliest exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canadian regulatory data on file (tetracycline antibiotic, class indication: bacterial infections) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published pharmacology, however, Minocycline is recognized for anti-inflammatory properties that extend well beyond its antibacterial activity. These include inhibition of the NF-κB signaling pathway, suppression of matrix metalloproteinases MMP-2 and MMP-9, and anti-apoptotic activity mediated through inhibition of cytochrome C release and caspase-3 activation. These properties are relevant to a range of chronic inflammatory conditions.

Punctate epithelial keratoconjunctivitis involves recurrent superficial corneal epithelial erosions sustained by inflammatory cascades at the ocular surface. The mechanistic hypothesis is that Minocycline's NF-κB inhibition and MMP suppression could dampen these cascades, reducing epithelial damage and limiting the cycle of inflammation that defines PEK. The second-ranked prediction — exposure keratitis — shares a similar pathophysiological basis (corneal epithelial injury followed by neuroinflammatory sequelae), and Minocycline's reported neuroprotective properties add a secondary layer of biological plausibility.

Indirect support comes from the tetracycline class more broadly: doxycycline, a closely related compound, has been investigated in dry eye disease and meibomian gland dysfunction — conditions that frequently co-present with PEK. The TxGNN high score likely reflects the knowledge graph capturing this structural class relationship between tetracyclines and ocular surface inflammation. A direct clinical pathway for Minocycline in PEK has not been established, and the evidence currently does not extend beyond this model-level signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Minocycline has no Drug Identification Numbers (DINs) registered with Health Canada, indicating no authorized marketed product in Canada at time of data cutoff (2026-06-22).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported solely by a TxGNN model score with no corroborating clinical trials or published literature (Evidence Level L5, Decision Stage S0). Although the mechanistic rationale is biologically plausible given Minocycline's known anti-inflammatory profile, the absence of any direct ocular evidence and the lack of Canadian regulatory authorization make this a research hypothesis that requires further development before investment decisions can be considered.

**To proceed, the following is needed:**
- Targeted literature review covering Minocycline and tetracycline-class drugs in ocular surface diseases (PEK, dry eye, conjunctivitis) to assess class-level evidence
- Evaluation of doxycycline's ocular evidence as a pharmacological proxy for Minocycline
- Retrieval of full MOA data from DrugBank to confirm mechanism relevance
- Assessment of feasibility for ophthalmic delivery (topical formulation, ocular bioavailability, local tolerability)
- Safety data retrieval from package insert sources to complete S1 safety screening
- If the above steps yield positive signals, proceed to preclinical proof-of-concept in a PEK animal model before any clinical pathway is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

