---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 3
---

# Bictegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Bictegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Bictegravir is a second-generation integrase strand transfer inhibitor (INSTI) used as a component of combination therapy (Biktarvy®) for the treatment of HIV-1 infection in adults and pediatric patients. The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**, based on the shared lentiviral architecture between FIV and HIV-1. Currently, **no clinical trials** and **no publications** directly support this repurposing direction, placing the prediction at evidence level **L5** with a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (integrase strand transfer inhibitor) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Bictegravir acts by binding to the catalytic core (DDE motif) of the HIV-1 integrase enzyme, blocking the strand transfer step that inserts viral cDNA into the host cell genome. As a second-generation INSTI, it offers a higher genetic barrier to resistance than first-generation agents such as raltegravir and elvitegravir. Although detailed MOA data is not available in the current evidence pack, its mechanism is well-established in the HIV pharmacology literature and underpins all predictions in this report.

Feline Immunodeficiency Virus (FIV) — the pathogen responsible for feline acquired immunodeficiency syndrome — belongs to the same *Lentivirus* genus as HIV-1 and similarly encodes an integrase enzyme with a conserved DDE catalytic triad. The conceptual basis for TxGNN's prediction is this shared enzymatic target: an integrase inhibitor active against HIV-1 might, in principle, inhibit a homologous lentiviral integrase in another species. The model's high score (99.82%) most likely reflects the tight topological proximity between HIV and FIV nodes in the knowledge graph rather than a validated mechanistic link.

Critically, FIV integrase shares substantially lower amino acid sequence homology with HIV-1 integrase than do primate lentiviruses. No in vitro or in vivo data currently demonstrate that Bictegravir inhibits FIV integrase. By contrast, the second-ranked TxGNN prediction — **Simian Immunodeficiency Virus (SIV) infection** — rests on a firmer mechanistic footing: SIV integrase shares >85% amino acid identity with HIV-1, and a 2017 preclinical study ([PMID 28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/)) directly assayed Bictegravir's antiviral activity against integrase inhibitor-resistant SIVmac239. The FIV prediction therefore represents a **topology-driven hypothesis** and should be treated as a starting point for targeted in vitro validation rather than a translatable clinical candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the prediction carries mechanistic plausibility at the conceptual level (lentiviral integrase conservation), no biochemical, in vitro, animal, or clinical data confirm Bictegravir activity against FIV integrase specifically. An L5 score indicates the prediction is entirely model-generated at this stage and does not yet meet the minimum evidentiary threshold to justify resource commitment.

**To proceed, the following is needed:**
- Amino acid sequence alignment of FIV, SIV, and HIV-1 integrase DDE domains to quantify structural conservation and binding-pocket compatibility
- In vitro FIV integrase strand transfer inhibition assay with Bictegravir to establish biochemical activity
- Feline cell-based antiviral assay (e.g., FL-4 or Crandell-Reese feline kidney cells infected with FIV) if in vitro integrase data is positive
- MOA data for Bictegravir retrieved from DrugBank (DB11799) or peer-reviewed sources to complete the mechanistic rationale
- Package insert safety data to enable a basic S1 safety screen before any in vivo work is initiated
- If the FIV hypothesis is to be deprioritized in favor of the better-supported SIV direction (L4, 3 preclinical publications), re-run this evaluation with `predicted_indications[1]` as the primary target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

