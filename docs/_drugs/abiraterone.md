---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Abiraterone
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

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone (Zytiga®) is a selective CYP17A1 inhibitor established for castration-resistant prostate cancer (CRPC), where it suppresses androgen biosynthesis to deprive tumours of growth signals.
The TxGNN model predicts it may have activity against **Migraine Disorder** via indirect neurosteroid pathway modulation.
Currently, there are **0 clinical trials** and **0 publications** directly supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Castration-resistant prostate cancer (CRPC) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Abiraterone is a selective irreversible inhibitor of **CYP17A1** (17α-hydroxylase/C17,20-lyase), a bifunctional enzyme that catalyses two key steps in androgen biosynthesis in the testes, adrenal glands, and tumour tissue. By blocking this enzyme, Abiraterone drastically reduces circulating testosterone, DHEA, and related androgens — depriving androgen-dependent prostate cancer cells of their primary growth signal.

The mechanistic link to migraine is indirect and multi-step. CYP17A1 inhibition reduces DHEA, a precursor to neurosteroids such as allopregnanolone. Neurosteroids are endogenous modulators of **GABA-A receptors**, and GABA-A signalling influences **cortical spreading depression (CSD)** — the electrophysiological wave now considered the central mechanism of migraine aura and headache initiation. This chain (CYP17A1 → DHEA ↓ → allopregnanolone ↓ → GABA-A modulation ↓ → CSD threshold changes) involves at least four indirect links and has not been investigated experimentally in any published study.

Critically, the direction of effect is uncertain. Some research indicates DHEA itself has neuroprotective and inhibitory properties on neuronal excitability; reducing DHEA through CYP17A1 inhibition could theoretically *increase* cortical excitability and worsen migraine susceptibility rather than improve it. Until this directional ambiguity is resolved in preclinical models, the TxGNN prediction — while mechanistically conceivable — cannot be confidently translated into a testable clinical hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Abiraterone is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on file with Health Canada. Any future use in Canada would require a New Drug Submission (NDS) or a clinical trial authorisation.

---

## Cytotoxicity

Abiraterone is indicated for prostate cancer and belongs to the androgen biosynthesis inhibitor class (hormonal antineoplastic). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen biosynthesis inhibitor (CYP17A1 inhibitor); **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low — abiraterone does not directly suppress bone marrow; haematological toxicity is not a primary concern |
| Emetogenicity Classification | Low (oral tablet; hormonal mechanism) |
| Monitoring Items | Serum electrolytes (particularly potassium — hypokalemia risk), blood pressure, liver function tests (ALT/AST — hepatotoxicity risk), signs of adrenal insufficiency; must be co-administered with a corticosteroid (prednisone/prednisolone) |
| Handling Protection | Standard oral hormonal/antineoplastic handling precautions; no requirement for full cytotoxic-agent biosafety protocols, but care recommended for women of childbearing potential due to androgen disruption |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.81%), the mechanistic pathway connecting CYP17A1 inhibition to migraine relief is speculative, multi-step, and directionally ambiguous — suppressing DHEA may plausibly worsen, not improve, migraine-related neuronal excitability. There are no clinical trials, observational data, or publications directly investigating Abiraterone in migraine, making this an L5-level prediction with no empirical support to justify advancement.

**To proceed, the following is needed:**
- Preclinical (in vitro or animal) studies examining the effect of CYP17A1 inhibition or DHEA depletion on cortical spreading depression thresholds and migraine-relevant endpoints
- Mechanistic clarification of the DHEA ↓ → allopregnanolone ↓ → GABA-A → CSD directional relationship, distinguishing whether net effect is pro- or anti-migrainous
- Independent literature review on neurosteroid modulation as a migraine therapeutic target (separate from abiraterone)
- Full package insert review to document contraindications and key warnings before any clinical evaluation is considered
- Comparative assessment against established migraine-prevention mechanisms (CGRP antagonism, beta-blockers, topiramate) to determine whether any incremental benefit is pharmacologically plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

