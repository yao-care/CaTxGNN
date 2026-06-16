---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Invasive Fungal Infections to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is a first-in-class echinocandin antifungal agent, globally approved for the treatment of invasive candidiasis, invasive aspergillosis, and empirical antifungal therapy in febrile neutropenic patients, though no market authorization is currently on file with Health Canada.
The TxGNN model assigns its highest prediction score to **Gastrin Secretion Abnormality** (99.44%), yet **no clinical trials** and **no published literature** exist to support this repurposing direction.
This prediction is most likely a knowledge graph artifact rather than a true pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Health Canada authorization on file; globally approved for invasive candidiasis and invasive aspergillosis |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on publicly known pharmacology, Caspofungin belongs to the echinocandin class and works by non-competitively inhibiting **β-1,3-D-glucan synthase** — an enzyme critical for fungal cell wall biosynthesis that has no human equivalent. This makes Caspofungin highly fungal-selective, with no established activity on mammalian endocrine or hormonal pathways.

Gastrin secretion abnormality involves dysregulation of G-cells in the gastric antrum, affecting gastric acid production through a neuroendocrine mechanism entirely unrelated to fungal cell wall biology. There is no published pharmacological rationale connecting β-1,3-D-glucan synthase inhibition to gastrin regulation.

The TxGNN high score (99.44%, ranked 10,074th out of all evaluated drug-disease pairs) most likely reflects an **indirect associative signal** in the knowledge graph: critically ill patients with severe fungal infections frequently develop gastrointestinal complications — including stress-related gastrin dysregulation — as a co-morbid phenomenon. This is a co-occurrence signal, not a causal mechanistic link, and this prediction should be treated as a likely false positive pending any contrary biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Caspofungin currently has no Drug Identification Numbers (DINs) on file with Health Canada and is not marketed in Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction for Caspofungin — gastrin secretion abnormality — lacks biological plausibility, clinical trial evidence, and supporting literature; the high confidence score is most likely driven by indirect comorbidity associations in the knowledge graph rather than any direct pharmacological mechanism.

**To proceed, the following would be needed:**
- A pre-clinical hypothesis demonstrating any pharmacological effect of echinocandin-class compounds on G-cell function or gastrin signalling pathways
- In vitro or animal model data showing caspofungin activity in gastric tissue
- Clarification of whether the knowledge graph signal reflects true drug-disease biology or a confound from critical illness comorbidities

---

### ⚑ Other Predicted Indications With Actionable Evidence

While the top-ranked TxGNN prediction is not currently actionable, this evidence pack identified several clinically grounded repurposing candidates with meaningful supporting evidence. These warrant separate, full evaluation reports:

| Rank | Indication | Evidence Level | Trials | Publications | Decision |
|------|-----------|---------------|--------|-------------|----------|
| 9 | **Neonatal Candidiasis** | L2 | 2 (incl. 1 published RCT) | 20 | Proceed with Guardrails |
| 8 | **Congenital Candidiasis** | L2 | 1 Phase 3 completed | 11 | Proceed with Guardrails |
| 10 | **Candida glabrata Infection** | L2 | 3 (incl. Phase 4) | 0 | Proceed with Guardrails |
| 4 | **HIV-Associated Opportunistic Fungal Infections** | L3 | 3 | 20 | Research Question |

**Key highlights:**

- **Neonatal Candidiasis (Rank 9)** — Supported by a published Phase 2 double-blind RCT (*J Antimicrob Chemother* 2020, PMID [31586424](https://pubmed.ncbi.nlm.nih.gov/31586424/)), a paediatric meta-analysis (PMID [29596219](https://pubmed.ncbi.nlm.nih.gov/29596219/)), and dedicated neonatal PK data. Caspofungin has FDA approval for children ≥3 months; the sub-3-month gap is exactly what these trials address. This is the strongest repurposing signal in the pack.

- **Congenital Candidiasis (Rank 8)** — Supported by a completed Phase 3 multi-centre trial in Chinese adults (NCT00635648, n=63) and multiple case reports of successful treatment in extremely low birth weight neonates with drug-resistant *Candida*.

- **Candida glabrata (Rank 10)** — *C. glabrata* (now reclassified as *Nakaseomyces glabrata*) has intrinsic reduced azole susceptibility; echinocandins including Caspofungin are already the **IDSA first-line treatment**. A completed Phase 4 PK/PD comparative trial (NCT00839540) and active resistance surveillance (NCT03652194) directly support this indication. FKS gene mutation monitoring for acquired echinocandin resistance is essential.

- **HIV-Associated Opportunistic Fungal Infections (Rank 4)** — This prediction reflects Caspofungin's established role in treating opportunistic infections (*Candida* oesophagitis, PCP salvage, histoplasmosis) in immunocompromised HIV/AIDS patients, **not** as an antiretroviral agent. Evidence includes an ongoing observational study in PCP/HIV patients (NCT06691321) and a systematic review on drug-resistant oral candidiasis in HIV (PMID [38822256](https://pubmed.ncbi.nlm.nih.gov/38822256/)).

> **Overall interpretation:** Caspofungin's genuine repurposing potential centres on expanding its established antifungal mechanism to underserved high-risk populations — neonates, immunocompromised infants, and patients with azole-resistant *Candida* — rather than crossing into novel disease biology. The TxGNN rank-1 prediction should be deprioritized in favour of these evidence-supported directions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

