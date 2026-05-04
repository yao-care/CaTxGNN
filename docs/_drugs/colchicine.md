---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
---

# Colchicine
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

# Colchicine: From Gout to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is a classical microtubule-disrupting alkaloid, primarily used in clinical practice for the treatment and prevention of acute gout attacks and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, with **0 clinical trials** and **6 publications** currently supporting this direction — all at the in vitro or preclinical level.
While a mechanistic rationale exists through tubulin inhibition, a fundamental selectivity barrier between parasite and human tubulin remains unresolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout; Familial Mediterranean Fever (established clinical use; no Canadian regulatory records available) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (Preclinical / mechanistic studies only) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Colchicine is a plant-derived alkaloid that exerts its effects primarily by binding to tubulin dimers and blocking their polymerization into microtubules. In the context of inflammation, this disrupts neutrophil chemotaxis, impairs NLRP3 inflammasome assembly, and reduces IL-1β secretion — the basis of its efficacy in gout and FMF.

*Plasmodium falciparum* possesses its own β-tubulin (pfβ-tubulin), which plays essential roles in merozoite formation, red blood cell invasion, and gametocyte development. Because microtubule dynamics are critical to these stages of the parasite life cycle, tubulin-binding compounds like colchicine are theoretically capable of interfering with parasite replication. Supporting this, in vitro studies (PMIDs 2670249 and 2655935) directly demonstrated that multiple tubulin- and cytoskeletal-binding compounds — including structural analogues of colchicine — inhibit intraerythrocytic *P. falciparum* growth, suggesting the parasite's tubulin is a druggable target.

However, a critical and currently unresolved obstacle limits clinical translation: human and *P. falciparum* tubulins share high sequence homology, making selective toxicity against the parasite without harming the host extremely difficult to achieve. Colchicine also carries a narrow therapeutic index in humans, and concentrations likely needed for meaningful antimalarial activity may exceed safe human dosing thresholds. The mechanistic link is biologically plausible, but the selectivity gap represents a fundamental barrier.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro Experimental | Cell Biology International Reports | Nine tubulin-binding compounds (including colchicine analogues) tested against intraerythrocytic *P. falciparum*; parasite tubulins found to be molecularly distinct from mammalian counterparts, suggesting differential druggability |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro Experimental | Cell Biology International Reports | Confirms cytoskeletal-binding compounds have in vitro activity against *P. falciparum*; Tubulozole-T (inactive in mammalian systems) highlighted as a promising selective antimalarial candidate |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro Mechanistic Study | Antimicrobial Agents and Chemotherapy | Tubulozole isomers show protein synthesis inhibition in *P. falciparum* similar to Colcemid (a colchicine derivative), suggesting a shared tubulin-mediated mechanism of action in the parasite |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro Experimental | PLoS ONE | Curcumin disrupts *P. falciparum* microtubule structure via tubulin binding, independently validating tubulin as a druggable target in the parasite |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Molecular Biology / In vitro | Molecular and Cellular Biology | pfmdr1 expression linked to altered chloroquine accumulation — contextual background on *P. falciparum* drug resistance mechanisms relevant to compound penetration strategies |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Clinical Immunology Study | Clinical and Experimental Immunology | Anti-intermediate filament (cytoskeletal) autoantibodies detected in 82% of acute malaria patients, indicating cytoskeletal disruption as part of the host-parasite interaction |

---

## Canada Market Information

Colchicine is not currently marketed in Canada. No Drug Identification Numbers (DINs) are registered. Canadian regulatory records and product monographs are unavailable for this review.

---

## Safety Considerations

Detailed Canadian regulatory safety data (warnings, contraindications, drug interactions) are not available for this review.

> Literature context (PMID 20586571): Colchicine has a **narrow therapeutic index** with no clear distinction between non-toxic, toxic, and potentially lethal doses. Unintentional toxicity is common and associated with serious outcomes. This pharmacokinetic characteristic is a critical safety constraint that must be addressed before any repurposing effort proceeds to clinical stages.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model scores this prediction at 99.60%, all six supporting publications are in vitro preclinical studies (L4), and the fundamental selectivity problem — colchicine's inability to discriminate between *P. falciparum* tubulin and human tubulin at therapeutically safe doses — has not been resolved in any published study. There is no clinical or in vivo animal evidence to support advancement.

**To proceed, the following is needed:**

- **Selectivity profiling**: Comparative binding affinity data for colchicine against pfβ-tubulin vs. human α/β-tubulin to quantify any selectivity margin
- **In vivo efficacy data**: Animal malaria model experiments (e.g., *P. berghei* mouse model) to assess whether anti-parasitic concentrations are achievable below human toxic thresholds
- **Structural optimization**: Evaluation of colchicine analogues (e.g., Tubulozole-T, as suggested in PMID 2655935) that may preferentially bind parasite tubulin over human tubulin
- **Full safety profile**: Package insert warnings, contraindications, and drug interaction data for colchicine before any protocol design
- **MOA data**: Complete DrugBank mechanism-of-action record to support formal mechanistic-link scoring

> **Note on Higher-Ranked Evidence**: The second TxGNN prediction — **Familial Mediterranean Fever (autosomal dominant)** — carries L1 evidence (20 publications, 1 active clinical trial) and a **Proceed with Guardrails** recommendation. The mechanistic link is direct and well-established (colchicine inhibits both neutrophil migration and NLRP3 inflammasome assembly, the core pathophysiology of FMF). This indication warrants a separate, higher-priority evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

