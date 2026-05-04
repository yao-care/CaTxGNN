---
layout: default
title: Bismuth Subsalicylate
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Bismuth Subsalicylate
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

# Bismuth Subsalicylate: From Gastrointestinal Disorders to Paratyphoid Fever

## One-Sentence Summary

Bismuth subsalicylate (BSS) is a well-established compound widely used for gastrointestinal disorders including traveler's diarrhea, nausea, and dyspepsia, though no formal Canadian regulatory authorization is currently on record.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**, ranked 836th with a prediction score of **99.98%**.
No clinical trials or publications directly targeting this indication were identified; evidence rests on mechanistic inference from closely related *Salmonella* infections.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal disorders (traveler's diarrhea, dyspepsia) — no Canadian regulatory record available |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured dataset. Based on known information, bismuth subsalicylate is a dual-component compound (bismuth ion + salicylate anion) with well-documented antimicrobial and antisecretory properties. The bismuth ion disrupts bacterial outer membranes and inhibits bacterial adhesion to intestinal epithelial cells, while the salicylate component suppresses prostaglandin E2 (PGE2)-mediated intestinal hypersecretion — reducing fluid loss in secretory diarrhea. Together, these mechanisms underpin BSS's established clinical use against traveler's diarrhea, where *Salmonella* species are among the principal causative organisms.

Paratyphoid fever is caused by *Salmonella enterica* serovars Paratyphi A, B, and C — organisms that are phylogenetically and pathophysiologically close to *S. enteritidis* (implicated in salmonellosis) and *S. typhi* (typhoid fever). In vitro evidence confirms BSS exerts direct bactericidal activity against *Salmonella* species (PMID 2694949), providing a coherent mechanistic bridge. The TxGNN model likely captured this phylogenetic proximity and the shared gastrointestinal infection pathway in its knowledge graph, yielding a high prediction score.

A key clinical limitation applies: *S. paratyphi* frequently causes systemic bacteremia during weeks 1–2 of illness. BSS acts locally in the gastrointestinal lumen and cannot substitute for systemic antibiotics (fluoroquinolones, azithromycin) required to manage invasive disease. Any plausible role for BSS would be adjunctive — reducing intestinal bacterial burden and ameliorating secretory symptoms — rather than curative. No modern clinical studies have evaluated this role specifically for paratyphoid fever.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Bismuth subsalicylate has no authorized products in Canada. No DINs (Drug Identification Numbers) have been issued under Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
TxGNN assigns a high prediction score (99.98%) grounded in the mechanistic and phylogenetic proximity between BSS's demonstrated anti-*Salmonella* activity and the *Salmonella paratyphi* etiology of paratyphoid fever; however, no direct preclinical or clinical evidence for this specific indication exists, and the systemic nature of paratyphoid fever substantially limits the utility of a locally acting agent.

**To proceed, the following is needed:**
- In vitro bactericidal studies of BSS specifically against *Salmonella paratyphi* A, B, and C (distinct from existing *S. enteritidis* / *S. typhi* data)
- Animal model studies (e.g., murine paratyphoid model) to evaluate intestinal burden reduction and adjunctive benefit alongside antibiotics
- Formal MOA documentation from DrugBank API (Data Gap DG002) to support regulatory dossier preparation
- Package insert and warning/contraindication data (Data Gap DG001) to enable safety pre-screening (currently blocking S1 assessment)
- Assessment of appropriate dosage form and route of administration for the target indication
- Health Canada pre-submission consultation if in vitro and in vivo data prove promising
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

